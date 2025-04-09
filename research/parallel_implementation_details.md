# Report: Implementation Details for Parallel Task Execution

## 1. Introduction

This document provides detailed implementation steps and code snippets for parallelizing Seer task execution using the **ThreadPoolExecutor + Shared Rate Limiter** strategy, as outlined in `research/parallel_execution_plan.md`.

## 2. New Component: Rate Limiter Class

Create a new file `src/geometor/seer/utils/rate_limiter.py` with the following thread-safe `TokenBucketRateLimiter` class:

```python
# src/geometor/seer/utils/rate_limiter.py
# Standard library imports
import time
import threading
from typing import Optional

class TokenBucketRateLimiter:
    """
    A thread-safe token bucket rate limiter.

    Allows controlling the rate of operations by requiring a token to be acquired
    before proceeding. Tokens are refilled at a specified rate. Uses float values
    for finer-grained control.
    """
    def __init__(self, capacity: float, refill_rate: float, name: str = "RateLimiter"):
        """
        Initializes the rate limiter.

        Args:
            capacity: Maximum number of tokens the bucket can hold (float).
            refill_rate: Tokens added per second (float).
            name: An optional name for the limiter (used in logging/debugging).
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        if refill_rate < 0:
            raise ValueError("Refill rate cannot be negative.")

        self.capacity = float(capacity)
        self._tokens = float(capacity) # Start full
        self.refill_rate = float(refill_rate)
        self.last_refill_time = time.monotonic()
        self._lock = threading.Lock() # Ensures thread safety
        self.name = name
        print(f"Initialized {self.name}: Capacity={self.capacity:.2f}, Refill Rate={self.refill_rate:.2f}/sec")

    def _refill(self):
        """Adds tokens based on elapsed time. Must be called within the lock."""
        now = time.monotonic()
        elapsed = now - self.last_refill_time
        if elapsed > 0:
            tokens_to_add = elapsed * self.refill_rate
            self.last_refill_time = now
            self._tokens = min(self.capacity, self._tokens + tokens_to_add)

    def acquire(self, amount: float = 1.0, timeout: Optional[float] = None) -> bool:
        """
        Acquires the specified amount of tokens, blocking if necessary.

        Args:
            amount: The number of tokens required (float, default: 1.0).
            timeout: Maximum time in seconds to wait. None waits indefinitely.

        Returns:
            True if acquired, False if timeout occurred.
        """
        if amount <= 0:
            raise ValueError("Acquire amount must be positive.")
        amount = float(amount)
        start_time = time.monotonic()
        deadline = (start_time + timeout) if timeout is not None else None

        while True:
            with self._lock:
                self._refill()
                if self._tokens >= amount:
                    self._tokens -= amount
                    return True # Acquired

            # Check timeout outside lock
            now = time.monotonic()
            if deadline is not None and now >= deadline:
                return False # Timeout

            # Calculate wait time intelligently
            with self._lock:
                needed = max(0, amount - self._tokens)

            if self.refill_rate > 0:
                wait_time = needed / self.refill_rate
            elif needed > 0: # Need tokens but no refill
                wait_time = float('inf')
            else: # No tokens needed or refill rate is 0
                wait_time = 0.001 # Small wait before re-check

            wait_time += 0.001 # Buffer

            if deadline is not None:
                remaining_time = max(0, deadline - now)
                if wait_time > remaining_time:
                    wait_time = remaining_time
                    if wait_time <= 0.001:
                         time.sleep(0.001) # Sleep briefly before final check
                         continue # Re-check timeout condition

            if wait_time == float('inf'):
                 # If waiting indefinitely and no timeout, sleep for a reasonable interval
                 time.sleep(0.5)
            elif wait_time > 0:
                 time.sleep(wait_time)
            # else loop continues immediately
```

## 3. Configuration Changes

### 3.1. Add Parameters to `run/config/index.yaml`

Add the following section to your main configuration file:

```yaml
# run/config/index.yaml (snippet)

# ... existing config ...

# --- Parallel Processing & Rate Limiting ---
parallel_workers: 4       # Number of tasks to process concurrently (e.g., 4)
rate_limit_rpm: 15        # Max requests/minute (Adjust based on your Gemini tier/model, e.g., 15 for Flash Free)
rate_limit_tpm: 1000000   # Max tokens/minute (Adjust based on your Gemini tier/model, e.g., 1,000,000 for Flash Free)
rate_limit_timeout: 300   # Max seconds to wait for rate limit permit (e.g., 300 = 5 mins, 0 means no timeout)
token_estimation_factor: 1.5 # Estimate total_tokens = input_tokens * factor for TPM limit (e.g., 1.5)

# ... rest of config ...
```
*__Note:__ Adjust `rate_limit_rpm` and `rate_limit_tpm` based on the specific Gemini model and tier you are using.*

### 3.2. Add Properties to `src/geometor/seer/config.py`

Add the following properties to the `Config` class to access the new values safely:

```python
# src/geometor/seer/config.py (within Config class)

    @property
    def parallel_workers(self) -> int:
        """Returns the number of parallel workers for task processing."""
        value = self._data.get("parallel_workers", 1)
        try:
            num_workers = int(value)
            if num_workers <= 0:
                print(f"Warning: 'parallel_workers' must be positive ({value}), using 1.")
                return 1
            return num_workers
        except (ValueError, TypeError):
            print(f"Warning: Invalid 'parallel_workers' value ({value}), using 1.")
            return 1

    @property
    def rate_limit_rpm(self) -> int:
        """Returns the Requests Per Minute limit for the API."""
        value = self._data.get("rate_limit_rpm", 15) # Default matching yaml
        try:
            rpm = int(value)
            if rpm <= 0:
                print(f"Warning: 'rate_limit_rpm' must be positive ({value}), using default 15.")
                return 15
            return rpm
        except (ValueError, TypeError):
            print(f"Warning: Invalid 'rate_limit_rpm' value ({value}), using default 15.")
            return 15

    @property
    def rate_limit_tpm(self) -> int:
        """Returns the Tokens Per Minute limit for the API."""
        value = self._data.get("rate_limit_tpm", 1_000_000) # Default matching yaml
        try:
            tpm = int(value)
            if tpm <= 0:
                print(f"Warning: 'rate_limit_tpm' must be positive ({value}), using default 1,000,000.")
                return 1_000_000
            return tpm
        except (ValueError, TypeError):
             print(f"Warning: Invalid 'rate_limit_tpm' value ({value}), using default 1,000,000.")
             return 1_000_000

    @property
    def rate_limit_timeout(self) -> int:
        """Returns the max seconds to wait for the rate limiter permit."""
        value = self._data.get("rate_limit_timeout", 300) # Default matching yaml
        try:
            timeout = int(value)
            if timeout < 0: # Allow 0 for no timeout? Let's treat 0 as no timeout (None internally)
                print(f"Warning: 'rate_limit_timeout' cannot be negative ({value}), using 300.")
                return 300
            # Return 0 if configured as 0, Seer init will convert to None for limiter
            return timeout
        except (ValueError, TypeError):
            print(f"Warning: Invalid 'rate_limit_timeout' value ({value}), using 300.")
            return 300

    @property
    def token_estimation_factor(self) -> float:
        """Returns factor to estimate total tokens = input_tokens * factor."""
        value = self._data.get("token_estimation_factor", 1.5) # Default matching yaml
        try:
            factor = float(value)
            if factor <= 0:
                 print(f"Warning: 'token_estimation_factor' must be positive ({value}), using 1.5.")
                 return 1.5
            return factor
        except (ValueError, TypeError):
            print(f"Warning: Invalid 'token_estimation_factor' ({value}), using 1.5.")
            return 1.5

    # Also ensure use_images property handles boolean conversion robustly
    @property
    def use_images(self) -> bool:
        """Returns the use_images flag."""
        value = self._data.get("use_images", False)
        return str(value).lower() in ['true', '1', 't', 'y', 'yes']

```

## 4. Thread Safety Modifications

### 4.1. Add Locks to `src/geometor/seer/session/session.py`

Modify the `Session` class to include locks for thread-safe access to shared resources.

```python
# src/geometor/seer/session/session.py

# Add import
import threading

class Session(Level):
    # Change type hint from dict to Config
    def __init__(self, config: Config, output_dir: Path, description: str):
        # ... existing init ...
        self.tasks = {} # Dictionary to hold SessionTask objects, keyed by task ID
        self._tasks_lock = threading.Lock() # Lock for accessing self.tasks
        self._summary_lock = threading.Lock() # Lock for generating summary
        # ... rest of init ...

    def add_task(self, task):
        """Adds a new task to the session. Thread-safe."""
        from geometor.seer.session.session_task import SessionTask
        session_task = SessionTask(self, task)
        # Acquire lock before modifying the shared tasks dictionary
        with self._tasks_lock:
            if task.id in self.tasks:
                 print(f"Warning (Session {self.name}): Task {task.id} already exists. Overwriting.")
            self.tasks[task.id] = session_task
        return session_task

    def summarize(self):
        """Generates and saves a summary of the session. Thread-safe."""
        acquired = self._summary_lock.acquire(blocking=True)
        if not acquired:
             print(f"ERROR (Session {self.name}): Failed to acquire summary lock. Skipping.")
             return
        try:
            print(f"\nGenerating session summary for {self.name}...")
            summary = super().summarize()
            # ... existing summary logic ...

            # Access self.tasks within the summary lock for consistency.
            with self._tasks_lock: # Also lock tasks access while copying
                tasks_to_summarize = list(self.tasks.values())

            for session_task in tasks_to_summarize:
                # ... aggregate data ...

            # ... finish summary logic ...
            self._write_to_json("index.json", summary)
            print(f"Session summary generated: {self.dir / 'index.json'}")
        finally:
            self._summary_lock.release() # Ensure lock is released
```

## 5. Seer Class Modifications (`src/geometor/seer/seer.py`)

### 5.1. Imports and Initialization

Add necessary imports and initialize the shared rate limiters in `Seer.__init__`.

```python
# src/geometor/seer/seer.py

# Standard library imports
from __future__ import annotations
from typing import TYPE_CHECKING, List, Any, Dict, Union, Callable, Optional
from datetime import datetime
import time
from pathlib import Path
import json
from concurrent.futures import ThreadPoolExecutor, as_completed # Added
import traceback # Added
import threading # Added

# Local application/library specific imports
from geometor.seer.config import Config
from geometor.seer.session import Session, SessionTask
from geometor.seer.utils.rate_limiter import TokenBucketRateLimiter # Added
# ... other imports ...

class Seer:
    def __init__(self, config: Config):
        # ... existing init ...

        # Initialize Rate Limiters (shared across threads)
        self.rpm_limiter = TokenBucketRateLimiter(
            capacity=config.rate_limit_rpm,
            refill_rate=config.rate_limit_rpm / 60.0, # Refill per second
            name="RPM Limiter"
        )
        self.tpm_limiter = TokenBucketRateLimiter(
            capacity=config.rate_limit_tpm,
            refill_rate=config.rate_limit_tpm / 60.0, # Refill per second
            name="TPM Limiter"
        )
        # Store config values for easy access in _generate
        # Convert 0 timeout from config to None for limiter's acquire method
        self.rate_limit_timeout = config.rate_limit_timeout if config.rate_limit_timeout > 0 else None
        self.token_estimation_factor = config.token_estimation_factor

        # ... rest of init ...
```

### 5.2. Modify `Seer.run` for Parallel Execution

Replace the sequential loop with `ThreadPoolExecutor`.

```python
# src/geometor/seer/seer.py (within Seer class)

    def run(self, tasks: Tasks, output_dir: Path, description: str):
        """
        Runs the task-solving process concurrently for a collection of tasks.
        """
        session = Session(self.config, output_dir, description)
        max_workers = self.config.parallel_workers

        if max_workers <= 0:
             print("Warning: parallel_workers set to 0 or less, running sequentially.")
             max_workers = 1

        futures = {} # Map future to task_id for better error reporting
        # Use try-finally to ensure session summary runs even if errors occur
        try:
            with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix='SeerWorker') as executor:
                print(f"\nSubmitting {len(tasks)} tasks to {max_workers} workers...")
                for task in tasks:
                    # Submit the solve method for each task
                    # Session object is passed; its methods are now thread-safe
                    future = executor.submit(self.solve, session, task)
                    futures[future] = task.id # Store mapping

                print("Waiting for tasks to complete...")
                # Process results as they complete for progress feedback and error handling
                tasks_completed = 0
                tasks_failed = 0
                total_tasks = len(futures)
                for future in as_completed(futures):
                    task_id = futures[future]
                    try:
                        # result() will re-raise exceptions from the worker thread
                        future.result() # We don't expect a return value from solve
                        tasks_completed += 1
                        print(f"  Task {task_id} completed successfully. ({tasks_completed}/{total_tasks})")
                    except Exception as exc:
                        tasks_failed += 1
                        # Log the error - traceback helps pinpoint the failure location
                        error_details = traceback.format_exc()
                        print(f"  ERROR: Task {task_id} failed: {exc}\n{error_details}")
                        # Log error to the session as well (SessionTask might have already logged specifics)
                        # Check if task exists in session before logging general failure
                        with session._tasks_lock:
                            session_task = session.tasks.get(task_id)
                        if session_task:
                             # Check if the specific error is already logged to avoid duplicates
                             if not any(str(exc) in str(err_entry) for err_entry in session_task.errors.values()):
                                 session_task.log_error(exc, f"Task failed during parallel execution.\n{error_details}")
                        else:
                             # Log at session level if task object wasn't even created successfully
                             session.log_error(exc, f"Task {task_id} failed early in parallel execution.\n{error_details}")

                print(f"\nTask processing finished. Completed: {tasks_completed}, Failed: {tasks_failed}")

        finally:
            # Summarization and submission file generation happen after all threads finish or errors occur
            print("\nFinalizing session...")
            session.summarize()
            self._generate_submission_file(session) # Assumes this reads from completed SessionTask data
```

### 5.3. Modify `Seer.solve` (Minor Change)

The `solve` method itself doesn't need major changes, as the parallelism is handled in `run`. Ensure it catches exceptions appropriately so they are propagated to the future.

```python
# src/geometor/seer/seer.py (within Seer class)

    def solve(self, session: Session, task: Task):
        """Solves a single task. Called by the ThreadPoolExecutor."""
        # Get current thread name for logging context
        thread_name = threading.current_thread().name
        print(f"    [{thread_name}] Starting task {task.id}...")
        session_task = session.add_task(task) # Thread-safe add_task

        try:
            # --- DELEGATE TO WORKFLOW ---
            # Get workflow name from config, providing a default
            # Assuming 'workflow' key exists in config, else defaults to 'default'
            workflow_name = self.config.get("workflow", "default")

            # Import workflows inside the method if needed, or ensure they are imported at module level
            # This assumes a WORKFLOW_MAP exists as proposed in modular_workflow_design.md
            from geometor.seer.workflows import WORKFLOW_MAP, DefaultWorkflow # Example import

            workflow_class = WORKFLOW_MAP.get(workflow_name)
            if not workflow_class:
                print(f"    [{thread_name}] Warning: Unknown workflow '{workflow_name}' for task {task.id}, falling back to 'default'.")
                workflow_class = DefaultWorkflow
            workflow = workflow_class() # Instantiate the workflow

            print(f"    [{thread_name}] Using workflow: {workflow_name} for task {task.id}")
            # Pass self (Seer instance) to the workflow's execute method
            # The workflow's execute method will call self._generate, which handles rate limiting
            workflow.execute(session_task, task, self)
            print(f"    [{thread_name}] Finished workflow for task {task.id}.")

        except Exception as e:
            # Catch top-level errors during workflow execution
            error_msg = f"Workflow execution failed for task {task.id} in thread {thread_name}: {e}"
            print(f"      ERROR: {error_msg}")
            # Log error within the specific session_task
            error_details = traceback.format_exc()
            session_task.log_error(e, f"{error_msg}\n{error_details}")
            # Re-raise the exception so the future in 'run' catches it
            raise
        finally:
            # Summarization happens within the task's own thread context
            # This ensures task summary is written before the thread finishes
            try:
                 print(f"    [{thread_name}] Summarizing task {task.id}...")
                 session_task.summarize()
                 print(f"    [{thread_name}] Finished summarizing task {task.id}.")
            except Exception as e_sum:
                 # Log error during summarization
                 error_msg = f"Failed to summarize task {task.id} in thread {thread_name}: {e_sum}"
                 print(f"      ERROR: {error_msg}")
                 error_details = traceback.format_exc()
                 session_task.log_error(e_sum, f"{error_msg}\n{error_details}")
                 # Do not re-raise here, allow the original exception (if any) to propagate
```
*__Note:__ This assumes the modular workflow design from `research/modular_workflow_design.md` is implemented, where `solve` delegates to a workflow's `execute` method.*

### 5.4. Modify `Seer._generate` for Rate Limiting

This is the core of the rate limiting integration.

```python
# src/geometor/seer/seer.py (within Seer class)

    def _estimate_input_tokens(self, prompt_parts: List[Any]) -> int:
        """
        Estimates the number of input tokens based on prompt content.
        Placeholder implementation - refine as needed.
        """
        # Simple estimation: count characters in strings, add fixed cost for images
        # This is a very rough heuristic. Using client.count_tokens would be more accurate
        # but adds an extra API call per _generate. Consider making this configurable.
        token_count = 0
        chars_per_token = 4 # General approximation for English text
        image_token_cost = 258 # Example fixed cost per image (check Gemini docs for specifics)

        for part in prompt_parts:
            if isinstance(part, str):
                # Estimate tokens based on character count
                token_count += (len(part) + chars_per_token - 1) // chars_per_token # Ceiling division
            elif hasattr(part, 'format') and hasattr(part, 'width'): # Basic check for PIL Image
                # Add fixed token cost for images
                token_count += image_token_cost
            # Add handling for other potential types (e.g., FunctionResponse) if necessary
            # FunctionResponse token counting might be complex and depend on API specifics
        return token_count

    def _generate(
        self,
        session_task: SessionTask,
        role_name: str,
        title: str,
        history: List[Any],
        content: List[Any],
        instructions: List[str],
        tools: Union[List[Callable], str, None] = None,
    ):
        """
        Generate content from the model, handling rate limiting, logging, and retries.
        """
        thread_name = threading.current_thread().name # Get thread name for logging

        client = self.roles.get(role_name)
        if not client:
            raise ValueError(f"[{thread_name}] Invalid role name '{role_name}' provided to _generate for task {session_task.name}.")

        task_step = session_task.add_step(
            title, history, content, instructions, client.model_name
        )

        max_retries = self.config.get("max_retries", 2) # Use config or default
        response = None
        start_time_generate = time.monotonic() # Timer for the whole generate process including waits
        valid_response_received = False

        # Combine all parts for token estimation and the actual prompt
        total_prompt: List[Any] = history + content + instructions

        # --- Rate Limiting Acquisition ---
        # This block attempts to acquire permits before starting the API call retry loop.
        # If it fails (timeout), the entire _generate call fails for this step.
        try:
            # 1. Estimate Tokens for TPM Limiter
            input_tokens = self._estimate_input_tokens(total_prompt)
            # Ensure estimated tokens is at least 1.0 for acquire amount
            estimated_total_tokens = max(1.0, float(input_tokens * self.token_estimation_factor))

            # 2. Acquire RPM Permit (1 request)
            rpm_acquire_start = time.monotonic()
            print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Waiting for RPM permit (1 req)...")
            if not self.rpm_limiter.acquire(amount=1.0, timeout=self.rate_limit_timeout):
                raise TimeoutError(f"RPM Rate Limiter timeout after {self.rate_limit_timeout}s")
            rpm_wait_time = time.monotonic() - rpm_acquire_start
            print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Acquired RPM permit. (Waited {rpm_wait_time:.2f}s)")

            # 3. Acquire TPM Permit (estimated tokens)
            tpm_acquire_start = time.monotonic()
            print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Waiting for TPM permit ({estimated_total_tokens:.0f} tokens)...")
            if not self.tpm_limiter.acquire(amount=estimated_total_tokens, timeout=self.rate_limit_timeout):
                # Note: If TPM times out, the RPM token is already consumed for this attempt.
                raise TimeoutError(f"TPM Rate Limiter timeout after {self.rate_limit_timeout}s (estimated {estimated_total_tokens:.0f} tokens)")
            tpm_wait_time = time.monotonic() - tpm_acquire_start
            print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Acquired TPM permit. (Waited {tpm_wait_time:.2f}s)")

        except TimeoutError as te:
            # Handle rate limiter timeout specifically
            error_msg = f"Rate limiter timeout during permit acquisition for step '{title}': {te}"
            print(f"      ERROR ({thread_name} Task {session_task.name}): {error_msg}")
            task_step.log_error(te, f"Rate Limiter Timeout: {te}")
            # Log response time as 0 or duration until timeout? Let's log duration.
            total_wait_time = time.monotonic() - start_time_generate
            task_step.log_response(None, total_wait_time, retries=0) # Log before raising
            raise te # Re-raise to fail the step/task

        # --- API Call and Retry Logic (after acquiring permits) ---
        # Note: Permits (RPM=1, TPM=estimated) are acquired *once* before this loop.
        # Retries within this loop handle API errors, not rate limit waits.
        while task_step.attempts < max_retries:
            # If not the first attempt, wait before retrying
            if task_step.attempts > 0:
                retry_delay = self.config.get("retry_delay_seconds", 10)
                print(f"            [{thread_name} Task {session_task.name}] ...waiting {retry_delay}s before API retry ({task_step.attempts + 1}/{max_retries}) for step '{title}'")
                time.sleep(retry_delay)

            task_step.attempts += 1
            current_attempt = task_step.attempts
            api_call_start_time = time.monotonic()

            try:
                print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Making API call (Attempt {current_attempt}/{max_retries})...")
                response = client.generate_content(total_prompt, tools=tools)
                api_call_duration = time.monotonic() - api_call_start_time
                print(f"    [{thread_name} Task {session_task.name} Step '{title}'] API call attempt {current_attempt} finished in {api_call_duration:.2f}s.")

                # Check for valid response (e.g., has candidates, text accessible)
                if response.candidates:
                    try:
                        _ = response.text # Attempt access to check for errors like safety blocks
                        valid_response_received = True
                        break # Exit the retry loop successfully
                    except ValueError as ve: # Catches issues getting .text
                        finish_reason_str = getattr(response.candidates[0].finish_reason, "name", "STOP")
                        print(f"            [{thread_name} Task {session_task.name}] Retry {current_attempt}/{max_retries} - Response finished ({finish_reason_str}), but text not accessible: {ve} for step '{title}'")
                        task_step.log_error(ve, f"Response STOP but text inaccessible on attempt {current_attempt}/{max_retries}")
                        # Continue retry loop if attempts remain
                else:
                    # Handle cases with no candidates or non-STOP finish reasons if needed
                    finish_reason = response.candidates[0].finish_reason if response.candidates else "NO_CANDIDATES"
                    finish_reason_str = getattr(finish_reason, "name", str(finish_reason))
                    print(f"            [{thread_name} Task {session_task.name}] RETRY: {current_attempt}/{max_retries} - Invalid response or finish reason: {finish_reason_str} for step '{title}'")
                    task_step.log_error(Exception(f"Invalid response/finish reason ({finish_reason_str})"), f"Attempt {current_attempt}/{max_retries}")
                    # Continue retry loop if attempts remain

            except Exception as e:
                # Catch errors during the API call itself (network, API errors not caught by client's internal retry)
                api_call_duration = time.monotonic() - api_call_start_time
                print(f"            [{thread_name} Task {session_task.name}] RETRY: {current_attempt}/{max_retries} - API Call ERROR after {api_call_duration:.2f}s: {e} for step '{title}'")
                task_step.log_error(e, f"API call failed on attempt {current_attempt}/{max_retries}")
                response = None # Ensure response is None if API call failed
                # Continue retry loop if attempts remain

        # --- After the while loop ---
        end_time_generate = time.monotonic()
        total_duration_generate = end_time_generate - start_time_generate # Includes wait + API calls + delays

        if not valid_response_received:
            error_msg = f"ERROR: Failed to get a valid response after {task_step.attempts} retries for step '{title}'."
            print(f"            ({thread_name} Task {session_task.name}) {error_msg}")
            # Log the final response (even if invalid/None) and total duration
            task_step.log_response(response, total_duration_generate, retries=task_step.attempts)
            exc = Exception(error_msg)
            task_step.log_error(exc, "Final Generate Failure after all retries")
            raise exc # Raise exception to be caught by the caller (workflow/solve)

        # --- Success ---
        print(f"    [{thread_name} Task {session_task.name} Step '{title}'] Valid response received after {task_step.attempts} attempts.")
        # Log successful response and total duration
        task_step.log_response(response, total_duration_generate, retries=task_step.attempts)
        task_step.process_response(response) # Process the valid response
        return task_step

```

## 6. Conclusion

These changes implement the `ThreadPoolExecutor` for parallel task execution and integrate shared `TokenBucketRateLimiter` instances to control API access based on configured RPM and TPM limits. Thread safety is addressed by adding locks to the `Session` class. This provides a robust foundation for improving Seer's throughput. Remember to adjust the configuration values in `index.yaml` based on your specific Gemini API tier and expected workload.
