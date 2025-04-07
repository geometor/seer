# Report: Parallel Processing Strategies for Seer Task Solving

## 1. Introduction

The current `Seer` implementation processes tasks sequentially using the `Seer.run` method, which iterates through a list of tasks and calls `Seer.solve` for each one. Each `solve` call involves multiple API calls to the Gemini model via `Seer._generate`. As the number of tasks increases, this sequential processing becomes a bottleneck.

The goal is to parallelize the task solving process to improve throughput while respecting the API rate limits imposed by the Gemini service (e.g., requests per minute, tokens per minute).

This report outlines three potential strategies to achieve this.

## 2. Problem Context: Rate Limiting

Any parallel execution strategy must incorporate a mechanism to control the rate of API requests. Simply executing many tasks concurrently will lead to exceeding API quotas, resulting in errors and potentially temporary blocks. The rate-limiting logic needs to be applied just before the actual API call (`client.generate_content` within `Seer._generate`).

## 3. Strategy 1: ThreadPoolExecutor + Shared Rate Limiter (Recommended Starting Point)

### 3.1. Explanation

This approach uses Python's built-in `concurrent.futures.ThreadPoolExecutor` to manage a pool of worker threads. The `Seer.run` method would be modified to submit each `self.solve(session, task)` call to the executor instead of running it directly in the loop.

A shared, thread-safe rate-limiting mechanism (e.g., implementing the Token Bucket algorithm) would be introduced. Before making an API call in `_generate`, the thread would acquire a "token" or permission from the rate limiter. If unavailable, the thread waits until the limiter allows it.

### 3.2. Conceptual Code Snippets

**a) Rate Limiter (Token Bucket Example):**

```python
# research/conceptual_rate_limiter.py
import time
import threading
from collections import deque

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initializes a thread-safe token bucket rate limiter.
        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Tokens added per second.
        """
        self.capacity = capacity
        self._tokens = deque(maxlen=capacity)
        self.refill_rate = refill_rate
        self.last_refill_time = time.monotonic()
        self._lock = threading.Lock()
        # Initial fill
        for _ in range(capacity):
            self._tokens.append(1)

    def _refill(self):
        """Adds tokens based on elapsed time."""
        now = time.monotonic()
        elapsed = now - self.last_refill_time
        tokens_to_add = int(elapsed * self.refill_rate)

        if tokens_to_add > 0:
            # Only add up to the capacity, avoiding overflow if maxlen wasn't used
            current_len = len(self._tokens)
            add_count = min(tokens_to_add, self.capacity - current_len)
            for _ in range(add_count):
                 self._tokens.append(1) # Add tokens
            self.last_refill_time = now # Reset refill time only when tokens are added

    def acquire(self, timeout: float | None = None) -> bool:
        """
        Acquires a token, blocking if necessary until one is available or timeout occurs.
        Returns True if acquired, False on timeout.
        """
        start_time = time.monotonic()
        while True:
            with self._lock:
                self._refill() # Refill before checking
                if self._tokens:
                    self._tokens.popleft() # Consume a token
                    return True

            # If no token, check timeout
            if timeout is not None and (time.monotonic() - start_time) >= timeout:
                return False

            # Wait a short interval before retrying to avoid busy-waiting
            # Adjust sleep time based on refill rate and desired responsiveness
            sleep_time = max(0.01, 1.0 / (self.refill_rate * 2)) if self.refill_rate > 0 else 0.1
            time.sleep(sleep_time)

# --- Usage within Seer ---
# In Seer.__init__ or Seer.run:
# self.rate_limiter = TokenBucketRateLimiter(capacity=10, refill_rate=1) # e.g., 10 tokens, 1 per sec

# In Seer._generate, before client.generate_content:
# print("Waiting for rate limiter...")
# if not self.rate_limiter.acquire(timeout=300): # Wait up to 5 mins
#     raise TimeoutError("Rate limiter timeout waiting for token")
# print("Acquired token, making API call.")
# response = client.generate_content(...)
```

**b) ThreadPoolExecutor in `Seer.run`:**

```python
# research/conceptual_seer_run_threadpool.py
from concurrent.futures import ThreadPoolExecutor, as_completed
# ... other imports ...

class Seer:
    # ... __init__ ...

    def run(self, tasks: Tasks, output_dir: Path, description: str):
        session = Session(self.config, output_dir, description)
        # Make max_workers configurable
        max_workers = self.config.get("parallel_workers", 4)
        # Initialize rate limiter if not done in __init__
        # self.rate_limiter = TokenBucketRateLimiter(...)

        futures = []
        # Use ThreadPoolExecutor for parallel execution
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            print(f"Submitting {len(tasks)} tasks to {max_workers} workers...")
            for task in tasks:
                # Submit the solve method for each task
                # Pass necessary arguments that are thread-safe or copied
                # Note: Session object needs careful handling for thread-safety
                future = executor.submit(self.solve, session, task)
                futures.append(future)

            print("Waiting for tasks to complete...")
            # Process results as they complete (optional, good for logging progress)
            for future in as_completed(futures):
                try:
                    # result() will re-raise exceptions from the worker thread
                    future.result()
                    # Optionally log task completion based on future or task mapping
                    print(f"Task completed.") # Needs more context to know *which* task
                except Exception as e:
                    # Log the error associated with the failed task
                    # Need a way to map future back to task_id if possible
                    print(f"A task failed: {e}")
                    # Consider logging this error to the main session log as well

        print("All tasks processed. Summarizing session...")
        session.summarize()
        self._generate_submission_file(session)

    def solve(self, session: Session, task: Task):
        # Ensure Session methods used here (add_task, logging) are thread-safe
        # Potential lock needed in Session.add_task if dictionary access isn't atomic
        # File logging within SessionTask/TaskStep might need locks if writing to shared logs,
        # but typically they write to task-specific directories, reducing conflicts.
        session_task = session.add_task(task)
        try:
            self._investigate(task, session_task)
        except Exception as e:
            session_task.log_error(e, "Investigation failed")
        session_task.summarize()

    def _generate(self, session_task: SessionTask, role_name: str, ...):
        # ... setup ...
        client = self.roles.get(role_name)
        # ...
        task_step = session_task.add_step(...)

        # --- Rate Limiting ---
        if hasattr(self, 'rate_limiter') and self.rate_limiter:
             print(f"    Task {session_task.name}: Waiting for rate limiter...")
             # Use a reasonable timeout
             if not self.rate_limiter.acquire(timeout=self.config.get("rate_limit_timeout", 300)):
                 error_msg = f"Rate limiter timeout waiting for token for task {session_task.name}"
                 print(f"            {error_msg}")
                 exc = TimeoutError(error_msg)
                 task_step.log_error(exc, "Rate Limiter Timeout")
                 raise exc # Fail the step if timeout occurs
             print(f"    Task {session_task.name}: Acquired token.")
        # --- End Rate Limiting ---

        # ... rest of _generate logic (API call, retries, etc.) ...
        response = client.generate_content(total_prompt, tools=tools)
        # ...

```

**c) Thread Safety Considerations:**

*   **Session Object:** Methods like `Session.add_task` modify the shared `session.tasks` dictionary. Dictionary access *might* be thread-safe in CPython due to the GIL for simple operations, but it's safer to add a `threading.Lock` around modifications (`self.tasks[task.id] = session_task`) and potentially reads if iteration occurs concurrently with modification.
*   **Logging:** If multiple threads write to the *same* log file concurrently, locking is needed. However, the current structure seems to log to task-specific directories (`session_task.dir`), minimizing this risk. Console printing (`print`) is generally thread-safe.
*   **Rate Limiter:** The `TokenBucketRateLimiter` example uses `threading.Lock` to ensure atomic updates to the token count and refill time.

### 3.3. Pros

*   Relatively straightforward to implement using standard Python libraries.
*   Good fit for I/O-bound operations like API calls.
*   Parallelism logic is mostly contained within `Seer.run`.
*   Rate limiting logic is centralized before the API call.

### 3.4. Cons

*   Requires careful attention to thread safety for shared objects (`Session`, `RateLimiter`). Debugging race conditions can be tricky.
*   The Global Interpreter Lock (GIL) in CPython means threads won't achieve true parallelism for CPU-bound tasks, but this is less relevant for I/O-bound API calls.
*   Resource management (e.g., number of threads) needs configuration.

## 4. Strategy 2: Asyncio + Semaphore/Rate Limiter

### 4.1. Explanation

This approach involves refactoring the relevant parts of the codebase to use Python's `asyncio` library. Methods involved in the task-solving flow (`run`, `solve`, `_investigate`, `refine`, `_generate`, and the underlying API call in `GeminiClient`) would become `async def` functions using `await` for I/O operations.

Parallelism is achieved using `asyncio.gather` or `asyncio.TaskGroup` in `Seer.run` to launch multiple `solve` coroutines concurrently.

Rate limiting can be implemented using `asyncio.Semaphore` to limit the number of *concurrent* API calls or by integrating an async-compatible token bucket library.

### 4.2. Conceptual Code Snippets

```python
# research/conceptual_seer_async.py
import asyncio
# Assume GeminiClient uses an async-compatible HTTP library (e.g., aiohttp)
# from .async_gemini_client import AsyncGeminiClient

class AsyncTokenBucketRateLimiter:
    # Similar logic to TokenBucketRateLimiter but using asyncio.Lock and asyncio.sleep
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self._tokens = asyncio.Queue(maxsize=capacity) # Use a queue for tokens
        self.refill_rate = refill_rate
        self.refill_interval = 1.0 / refill_rate if refill_rate > 0 else float('inf')
        self._lock = asyncio.Lock()
        self._refill_task = None
        # Initial fill
        for _ in range(capacity):
            self._tokens.put_nowait(1)

    async def _refiller(self):
        """Periodically adds tokens to the bucket."""
        while True:
            await asyncio.sleep(self.refill_interval)
            async with self._lock:
                if not self._tokens.full():
                    self._tokens.put_nowait(1)

    async def start(self):
        """Starts the background refiller task."""
        if self.refill_rate > 0 and self._refill_task is None:
             self._refill_task = asyncio.create_task(self._refiller())

    async def stop(self):
        """Stops the background refiller task."""
        if self._refill_task:
            self._refill_task.cancel()
            try:
                await self._refill_task
            except asyncio.CancelledError:
                pass
            self._refill_task = None

    async def acquire(self):
        """Acquires a token, waiting if necessary."""
        # Queue.get() waits if the queue is empty
        await self._tokens.get()
        self._tokens.task_done() # Mark task as done for queue management

# --- Usage within Seer ---
class Seer:
    # ... async def __init__? Or initialize limiter separately ...

    async def run(self, tasks: Tasks, output_dir: Path, description: str):
        session = Session(self.config, output_dir, description) # Session needs async file I/O?
        # Rate Limiter setup
        limiter = AsyncTokenBucketRateLimiter(capacity=10, refill_rate=1)
        await limiter.start()

        solve_tasks = []
        for task in tasks:
            # Create coroutine objects
            solve_tasks.append(self.solve(session, task, limiter))

        # Run tasks concurrently
        print(f"Running {len(tasks)} tasks concurrently...")
        results = await asyncio.gather(*solve_tasks, return_exceptions=True)

        # Process results/exceptions
        for i, result in enumerate(results):
             if isinstance(result, Exception):
                 print(f"Task {tasks[i].id} failed: {result}")
                 # Log error appropriately

        await limiter.stop()
        print("All tasks processed. Summarizing session...")
        # Session summary/submission might need async file I/O if Session was made async
        session.summarize()
        self._generate_submission_file(session) # Needs async file I/O?

    async def solve(self, session: Session, task: Task, limiter):
        # Session methods would need to be async if they perform I/O
        session_task = session.add_task(task) # Assuming add_task is sync or made async
        try:
            # Pass limiter down
            await self._investigate(task, session_task, limiter)
        except Exception as e:
            session_task.log_error(e, "Investigation failed") # log_error needs async file I/O?
        session_task.summarize() # summarize needs async file I/O?

    async def _investigate(self, task: Task, session_task: SessionTask, limiter):
         # ... history setup ...
         # Calls to _generate must be awaited
         task_step = await self._generate(session_task, "dreamer", ..., limiter=limiter)
         # ... handle results ...
         if not task_step.any_trials_successful("train"):
              task_step = await self._generate(session_task, "coder", ..., limiter=limiter)
         # ... refinement loop with awaited _generate calls ...

    async def _generate(self, session_task: SessionTask, role_name: str, ..., limiter):
        # ... setup ...
        client = self.roles.get(role_name) # Assume client is async
        task_step = session_task.add_step(...) # Needs async file I/O?

        # --- Rate Limiting ---
        print(f"    Task {session_task.name}: Waiting for rate limiter...")
        await limiter.acquire()
        print(f"    Task {session_task.name}: Acquired token.")
        # --- End Rate Limiting ---

        # ... retry logic using asyncio.sleep ...
        while task_step.attempts < max_retries:
            # ... prepare prompt ...
            if task_step.attempts > 0:
                await asyncio.sleep(retry_delay)
            task_step.attempts += 1
            try:
                # Await the async API call
                response = await client.generate_content(total_prompt, tools=tools)
                # ... process response ...
                valid_response_received = True
                break
            except Exception as e:
                # ... handle error ...
                await asyncio.sleep(0.1) # Small sleep on error before retry

        # ... handle final success/failure ...
        # Log response/errors (needs async file I/O?)
        task_step.log_response(...)
        # ...
        return task_step

```

### 4.3. Pros

*   Potentially more efficient for high I/O concurrency due to lower overhead compared to threads.
*   Rate limiting primitives (`Semaphore`, async queues) integrate naturally with the `asyncio` model.
*   Clearer control flow for asynchronous operations compared to callbacks.

### 4.4. Cons

*   Requires significant refactoring of the existing synchronous codebase to use `async`/`await`.
*   All I/O operations down the call stack (including file access in `Session`, `TaskStep`, etc., and the HTTP client in `GeminiClient`) must be replaced with async equivalents. This can be invasive.
*   Debugging async code can have its own challenges.

## 5. Strategy 3: External Task Queue (Celery, RQ, Dramatiq)

### 5.1. Explanation

This approach decouples task execution from the main application flow using a dedicated task queue system.

1.  **Task Definition:** A function (e.g., `solve_task`) is defined, decorated by the task queue library (like Celery or RQ). This function encapsulates the logic currently in `Seer.solve`, taking necessary data (like task details, config path, session ID) as arguments.
2.  **Enqueuing:** The `Seer.run` method iterates through tasks and, instead of executing `solve` directly, it *enqueues* a `solve_task` job for each task, passing the required arguments. These jobs are sent to a message broker (e.g., Redis, RabbitMQ).
3.  **Workers:** Separate worker processes, managed by the task queue system, run independently. They listen to the broker, pick up tasks from the queue, and execute the `solve_task` function. Multiple workers can run concurrently, potentially across different machines.
4.  **Rate Limiting:** Can be implemented within the `solve_task` function (similar to Strategy 1, but needing process-safe locking if multiple workers share a limiter instance, or each worker having its own limiter) or potentially using rate-limiting features provided by the task queue library itself.

### 5.2. Conceptual Code Snippets (using Celery as an example)

```python
# research/conceptual_celery_tasks.py
import celery
import time
from pathlib import Path
# Assume Seer, Task, Session etc. can be initialized/loaded within the task
# Need to handle serialization carefully

# Configure Celery (e.g., using Redis as broker)
app = celery.Celery('seer_tasks', broker='redis://localhost:6379/0')

# Potentially configure rate limiting at the task level
# @app.task(rate_limit='10/m') # Example: 10 tasks per minute allowed *for this task type*
@app.task
def solve_task(config_data: dict, task_data: dict, output_dir_str: str, session_desc: str, task_id: str):
    """
    Celery task to solve a single ARC task.
    Args need to be serializable (dicts, strings, numbers).
    """
    # Re-initialize necessary components within the worker process
    # This avoids sharing complex objects directly
    config = Config.from_dict(config_data) # Assuming a way to load config from dict/path
    task = Task(task_id, task_data) # Recreate Task object
    output_dir = Path(output_dir_str)

    # Session might need to be "re-attached" or managed differently.
    # For simplicity, maybe each task creates a mini-session or logs independently?
    # Or use a shared session ID to coordinate logging if needed.
    # Let's assume Seer can be initialized for a single task run:
    seer_instance = Seer(config) # Rate limiting might be part of Seer init or passed

    # Create a SessionTask structure manually or adapt Session
    # This part needs careful design depending on how results are aggregated.
    # For simplicity, let's assume Seer.solve can be called directly if adapted.
    # This example bypasses Session/SessionTask for clarity, focusing on Seer logic.

    # --- Rate Limiting (if not handled by Celery directly) ---
    # limiter = TokenBucketRateLimiter(...) # Needs process-safe implementation or per-worker instance
    # Pass limiter to relevant methods or make it accessible globally/contextually
    # ---

    try:
        # Adapt Seer's logic or call a simplified solve method
        # This is highly dependent on how Seer/Session are structured for worker use
        print(f"Worker processing task {task.id}...")
        # Placeholder for actual solving logic, potentially calling parts of Seer
        # seer_instance.solve_single_task_for_worker(task, output_dir / task.id)
        time.sleep(5) # Simulate work
        result = f"Success for {task.id}"
        print(f"Worker finished task {task.id}.")
        # Worker needs to save results somewhere (e.g., task-specific files, database)
        # Aggregation happens later.
        return result # Celery task return value
    except Exception as e:
        print(f"Worker failed task {task.id}: {e}")
        # Log error appropriately within the worker context
        raise # Re-raise for Celery to mark task as failed

# --- Usage in Seer.run ---
# research/conceptual_seer_run_celery.py
class Seer:
    # ... __init__ ...

    def run(self, tasks: Tasks, output_dir: Path, description: str):
        # Session setup might primarily be for the main process orchestration now
        session = Session(self.config, output_dir, description)

        print(f"Enqueuing {len(tasks)} tasks...")
        async_results = []
        for task in tasks:
            # Serialize necessary data
            config_data = self.config.data # Assuming config data is serializable
            task_data = task.data # Assuming task data is serializable
            output_dir_str = str(output_dir)

            # Enqueue the task
            # Pass serializable data
            result = solve_task.delay(
                config_data, task_data, output_dir_str, description, task.id
            )
            async_results.append(result)

        print("All tasks enqueued. Workers will process them.")
        # Optionally wait for results (can be complex to track)
        # successful_results = []
        # for ar in async_results:
        #     try:
        #         # This blocks until the specific task completes
        #         res = ar.get(timeout=3600) # Wait up to 1 hour
        #         successful_results.append(res)
        #         print(f"Result received: {res}")
        #     except Exception as e:
        #         print(f"Failed to get result for a task: {e}")

        # Aggregation/Summarization needs to happen *after* workers finish.
        # This might involve reading results from files workers wrote,
        # or using Celery result backend.
        print("Session summary and submission file generation would require results aggregation.")
        # session.summarize_from_worker_outputs() # Needs custom implementation
        # self._generate_submission_file_from_worker_outputs(session) # Needs custom implementation

```

### 5.3. Pros

*   Highly scalable and robust; workers can run on multiple machines.
*   Excellent decoupling of task submission and execution.
*   Mature libraries (Celery, RQ) provide features like retries, monitoring, result backends.
*   Well-suited for long-running tasks.

### 5.4. Cons

*   Introduces significant infrastructure complexity (message broker setup, worker deployment and management).
*   Requires careful consideration of task function design, argument serialization, and state management (workers are typically stateless).
*   Sharing complex Python objects between the main process and workers is difficult; rely on passing serializable data.
*   Result aggregation requires a separate mechanism (reading files, database, result backend).
*   Can be overkill for moderate workloads or simpler deployment scenarios.

## 6. Recommendation

For the current stage of the `geometor-seer` project, **Strategy 1 (ThreadPoolExecutor + Shared Rate Limiter)** is the recommended starting point.

*   It offers a good balance between performance improvement and implementation complexity.
*   It leverages standard Python libraries, minimizing external dependencies.
*   It keeps the core logic within the existing application structure, requiring less invasive refactoring than `asyncio`.
*   It directly addresses the primary bottleneck (sequential task processing) and the rate-limiting constraint.

**Implementation Steps:**

1.  **Implement/Integrate Rate Limiter:** Add a thread-safe `TokenBucketRateLimiter` (or use a library). Configure its capacity and refill rate based on Gemini API limits via the `Config` object.
2.  **Integrate Limiter:** Modify `Seer._generate` to acquire from the limiter before calling `client.generate_content`.
3.  **Modify `Seer.run`:** Use `ThreadPoolExecutor` to submit `self.solve` calls. Make the number of workers configurable.
4.  **Ensure Thread Safety:** Add locks (`threading.Lock`) around critical sections modifying shared resources, particularly in the `Session` object (e.g., `add_task`) and potentially file/console logging if contention is possible.
5.  **Testing:** Thoroughly test concurrent execution with varying numbers of workers and tasks, monitoring for race conditions and ensuring the rate limiter behaves as expected.

If future scalability requirements demand distributed processing or significantly higher I/O concurrency proves `ThreadPoolExecutor` insufficient, migrating to `asyncio` (Strategy 2) or a Task Queue (Strategy 3) can be considered later.
