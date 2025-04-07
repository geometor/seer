# Report: Modular Workflow Design for Seer

## 1. Introduction

As the Seer system evolves, the need arises to support diverse task-solving approaches beyond the initial "investigate all pairs, then refine" logic. Hardcoding numerous variations (e.g., single-pair analysis, data augmentation, parallel validation) directly into the `Seer` class leads to complexity and maintenance challenges.

This report proposes a modular design using Python classes to represent distinct task-solving workflows. This approach allows for flexibility and extensibility while keeping the core `Seer` orchestrator clean and focused. The specific workflow to be used for a session can be selected via configuration.

## 2. Core Concept: Workflow Classes

The central idea is to encapsulate the logic for a specific end-to-end task-solving process within a dedicated Python class, referred to as a "Workflow".

*   **Interface:** An Abstract Base Class (ABC), `WorkflowBase`, defines the common interface that all concrete workflow classes must adhere to. The primary method is `execute`, which takes the necessary context (session task, task data, Seer instance) and performs the steps defined by that specific workflow.
*   **Implementations:** Concrete classes inherit from `WorkflowBase` and implement the `execute` method. Each class represents a distinct strategy, such as:
    *   `DefaultWorkflow`: Implements the original dreamer -> coder -> refine loop using all training pairs.
    *   `SinglePairWorkflow`: Iterates through training pairs individually, applying analysis steps to each.
    *   `AugmentedDataWorkflow`: Performs data augmentation (e.g., rotations) before potentially delegating to another workflow.
    *   `ParallelValidateWorkflow`: Implements the parallel generation of `transform` and `validate` functions.
*   **Location:** These classes would reside in a dedicated package, e.g., `src/geometor/seer/workflows/`.

## 3. Proposed Implementation Structure

### 3.1. Workflow Interface (`WorkflowBase`)

```python
# src/geometor/seer/workflows/base.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task

class WorkflowBase(ABC):
    """Abstract base class for different task-solving workflows."""

    @abstractmethod
    def execute(self, session_task: 'SessionTask', task: 'Task', seer_instance: 'Seer') -> None:
        """
        Executes the specific workflow to solve the given task.

        Args:
            session_task: The session task object for logging and context.
            task: The task data.
            seer_instance: The main Seer instance to access shared resources
                           (e.g., _generate, config, roles, instructions).
        """
        pass
```

### 3.2. Concrete Workflow Example (`DefaultWorkflow`)

```python
# src/geometor/seer/workflows/default.py
from .base import WorkflowBase
from typing import TYPE_CHECKING
# ... other necessary imports (TaskStep, CodeTrial, exceptions, etc.)

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task

class DefaultWorkflow(WorkflowBase):
    """Implements the standard investigate-all-pairs then refine workflow."""

    def execute(self, session_task: 'SessionTask', task: 'Task', seer_instance: 'Seer') -> None:
        """Orchestrates the default dreamer -> coder -> refine process."""
        print(f"      Executing DefaultWorkflow for task {task.id}")
        history = []
        task_step = None # Keep track of the last successful/attempted step

        try:
            # --- Investigation Phase ---
            # Step 1: Dreamer (All Pairs)
            task_step = self._investigate_dreamer(session_task, task, seer_instance, history)
            history.extend(task_step.response_parts) # Update history after successful step
            if self._check_success_and_log(task_step, "investigate_dreamer"):
                return # Task solved

            # Step 2: Coder (All Pairs) - Only if Dreamer didn't solve
            task_step = self._investigate_coder(session_task, task, seer_instance, history)
            history.extend(task_step.response_parts)
            if self._check_success_and_log(task_step, "investigate_coder"):
                return # Task solved

            # --- Refinement Phase ---
            current_iteration = 0
            max_iterations = seer_instance.config.max_iterations

            while current_iteration < max_iterations:
                if not task_step: # Safety check
                     raise Exception("task_step became None unexpectedly before refinement loop.")

                code_trial = task_step.get_first_code_trial()
                if not code_trial:
                    raise Exception(f"No code trial found to start refinement iteration {current_iteration}.")

                # Refine returns the *last* step performed within it (usually coder)
                task_step = self._refine_iteration(
                    session_task, task, seer_instance, history, code_trial, current_iteration
                )
                # History is updated *within* _refine_iteration before returning task_step
                # No need to extend history here, but the reference is updated

                if self._check_success_and_log(task_step, f"refine_iteration_{current_iteration}"):
                    return # Task solved

                current_iteration += 1

            print(f"            INFO: Reached max iterations ({max_iterations}) without solving task {task.id}.")

        except Exception as e:
            # Catch errors from _investigate_*, _refine_iteration, or _check_success_and_log
            # Error should ideally be logged within the failing sub-method first
            print(f"      ERROR during DefaultWorkflow execution for task {task.id}: {e}")
            # Log a general workflow execution error if not already logged more specifically
            if not session_task.errors or str(e) not in str(session_task.errors):
                 session_task.log_error(e, f"DefaultWorkflow execution failed for task {task.id}")
            # Allow execution to proceed to session_task.summarize() in Seer.solve

    def _investigate_dreamer(self, session_task, task, seer_instance, history):
        """Handles the 'investigate dreamer' step."""
        title = "investigate • dreamer • all training"
        # --- Logic moved from Seer._investigate (dreamer part) ---
        # ... prepare content, instructions ...
        instruction_key = "investigate_dreamer"
        instruction_content = seer_instance.instructions.get(instruction_key)
        if not instruction_content:
            raise ValueError(f"Missing instruction: '{instruction_key}'")
        instructions = [instruction_content]
        content = [] # Build content list (prompts, images)
        for i, pair in enumerate(task.train, 1):
            content.extend(get_pair_prompt(f"train_{i}", pair, seer_instance.use_images))
        if seer_instance.use_images:
            content.append(task.to_image(show_test=False))

        try:
            task_step = seer_instance._generate(
                session_task, "dreamer", title, history, content, instructions, tools="code_execution"
            )
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            session_task.log_error(e, f"Step '{title}' failed.")
            raise # Re-raise to be caught by the main execute block

    def _investigate_coder(self, session_task, task, seer_instance, history):
        """Handles the 'investigate coder' step."""
        title = "investigate • coder • all training"
        # --- Logic moved from Seer._investigate (coder part) ---
        instruction_key = "investigate_coder"
        instruction_content = seer_instance.instructions.get(instruction_key)
        if not instruction_content:
            raise ValueError(f"Missing instruction: '{instruction_key}'")
        instructions = [instruction_content]
        content = [""] # Minimal content, relies on history

        try:
            task_step = seer_instance._generate(
                session_task, "coder", title, history, content, instructions #, tools=...
            )
            task_step.run_trials()
            task_step.summarize()
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            session_task.log_error(e, f"Step '{title}' failed.")
            raise

    def _refine_iteration(self, session_task, task, seer_instance, history, code_trial, iteration):
        """Handles one iteration of the refinement loop (dreamer and coder)."""
        # --- Logic moved from Seer.refine ---
        # Note: History is passed in and modified *within* this method

        # Refine Dreamer
        title = f"refine • {iteration} • dreamer"
        try:
            instruction_key = "refine_dreamer"
            instruction_content = seer_instance.instructions.get(instruction_key)
            if not instruction_content:
                raise ValueError(f"Missing instruction: '{instruction_key}'")
            instructions = [instruction_content]
            content = []
            content.append("\nPrevious Code:\n")
            content.append(f"```python\n{code_trial.code}\n```\n")
            content.append(code_trial.generate_report())

            task_step = seer_instance._generate(
                session_task, "dreamer", title, history, content, instructions, tools="code_execution"
            )
            # Update history *after* successful generation
            history.extend(content)
            history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()
            if self._check_success_and_log(task_step, title):
                return task_step # Solved by dreamer refinement

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            session_task.log_error(e, f"Step '{title}' failed.")
            raise # Re-raise to stop this iteration/workflow

        # Refine Coder (only if dreamer didn't solve)
        title = f"refine • {iteration} • coder"
        try:
            instruction_key = "refine_coder"
            instruction_content = seer_instance.instructions.get(instruction_key)
            if not instruction_content:
                raise ValueError(f"Missing instruction: '{instruction_key}'")
            instructions = [instruction_content]
            content = [""] # Minimal content

            # Use the history updated by the dreamer step above
            task_step = seer_instance._generate(
                session_task, "coder", title, history, content, instructions #, tools=...
            )
            # Update history *after* successful generation
            # history.extend(content) # Usually no new input content here
            history.extend(task_step.response_parts)

            task_step.run_trials()
            task_step.summarize()
            # Return the coder step regardless of success; outer loop checks
            return task_step

        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            session_task.log_error(e, f"Step '{title}' failed.")
            raise # Re-raise to stop this iteration/workflow


    def _check_success_and_log(self, task_step, step_name: str) -> bool:
        """Checks if a step was successful and logs appropriately."""
        if task_step.any_trials_successful("train"):
            print(f"            Step '{step_name}': train passed")
            if task_step.any_trials_successful("test"):
                print(f"            Step '{step_name}': test passed")
            return True
        # print(f"            Step '{step_name}': train failed") # Optional: log failure
        return False

```

### 3.3. `Seer` Class Modifications

*   **Workflow Factory/Map:** Include a mechanism (e.g., dictionary mapping names to classes) to instantiate the correct workflow based on a name.
    ```python
    # Inside Seer class
    from geometor.seer.workflows.default import DefaultWorkflow
    from geometor.seer.workflows.single_pair import SinglePairWorkflow # Example
    # ... import other workflows ...

    WORKFLOW_MAP = {
        "default": DefaultWorkflow,
        "single_pair": SinglePairWorkflow,
        # ... add other workflow classes ...
    }

    def _get_workflow(self, workflow_name: str) -> WorkflowBase:
        workflow_class = self.WORKFLOW_MAP.get(workflow_name)
        if not workflow_class:
            # Fallback or error
            print(f"Warning: Unknown workflow '{workflow_name}', falling back to 'default'.")
            workflow_class = DefaultWorkflow
            # Alternatively: raise ValueError(f"Unknown workflow: {workflow_name}")
        return workflow_class() # Instantiate the workflow
    ```
*   **Simplified `Seer.solve`:** This method becomes a dispatcher.
    ```python
    # Inside Seer class
    def solve(self, session: Session, task: Task):
        """Sets up the SessionTask and delegates solving to the configured workflow."""
        session_task = session.add_task(task)
        # Get workflow name from config, providing a default
        workflow_name = self.config.get("workflow", "default") # Changed key to 'workflow'

        try:
            workflow = self._get_workflow(workflow_name)
            print(f"    Using workflow: {workflow_name} for task {task.id}")
            # Pass self (Seer instance) to the workflow's execute method
            workflow.execute(session_task, task, self)
        except Exception as e:
            # Catch top-level errors during workflow instantiation or execution
            error_msg = f"Workflow '{workflow_name}' failed for task {task.id}: {e}"
            print(f"      ERROR: {error_msg}")
            session_task.log_error(e, error_msg)
            # Potentially log traceback for detailed debugging
            # import traceback
            # session_task.log_error(traceback.format_exc(), f"Traceback for {error_msg}")

        # Summarization always happens after the workflow attempts execution
        session_task.summarize()
    ```
*   **Remove Core Logic:** The original `_investigate` and `refine` methods are removed from `Seer` as their logic now resides within the `DefaultWorkflow` class (or other workflow classes). The `_generate` method remains in `Seer` as a utility used by workflows.

### 3.4. Configuration (`config.yaml`)

*   A top-level key, e.g., `workflow`, specifies which workflow to use:
    ```yaml
    # Example config.yaml snippet
    workflow: default # Or "single_pair", "parallel_validate", etc.

    # Other existing config...
    roles:
      # ...
    instructions:
      # ...
    max_iterations: 5
    # ...
    ```

## 4. Benefits

*   **Modularity:** Encapsulates distinct solving processes, making the system easier to understand and manage.
*   **Flexibility:** Allows easy switching between different solving approaches via configuration.
*   **Extensibility:** Adding new workflows involves creating a new class inheriting from `WorkflowBase` without major changes to the `Seer` core.
*   **Testability:** Individual workflow classes can be tested more easily in isolation.
*   **Code Reusability:** Common steps or utilities (like `_generate`) remain in `Seer` or helper modules, accessible to all workflows. Workflows can potentially call or compose each other.
*   **Adaptability to Diverse Task Types:** This architecture is not limited to grid-based tasks. By creating specialized workflow classes, the system can be extended to handle various problem domains:
    *   **Workflow Specialization:** Create classes like `TextProcessingWorkflow`, `DataAnalysisWorkflow`, or `ImageGenerationWorkflow`, each implementing domain-specific logic and steps.
    *   **Configuration-Driven:** The `config.yaml` can select the appropriate workflow (`workflow:` key), define domain-specific roles/models (`roles:`), load tailored instructions (`instructions:`), and potentially specify required tools.
    *   **Flexible Task Representation:** While the current `Task` class is ARC-specific, a `BaseTask` interface with subclasses (e.g., `ArcTask`, `TextTask`) can be introduced to handle different input data structures. Workflows would operate on their expected task type.
    *   **Varied Evaluation:** Evaluation logic, currently in `CodeTrial`, can be adapted or replaced within each workflow to suit the task type (e.g., LLM-based evaluation, standard metrics like ROUGE, human feedback).

## 5. Conclusion

Adopting a modular design based on Workflow classes provides a robust and scalable way to manage different task-solving strategies within the Seer system. It leverages Python's object-oriented features for clear encapsulation while using configuration (`config.yaml`) to select the desired behavior for a given session. This approach balances the need for structured design with the flexibility required for experimenting with diverse problem-solving techniques and adapting the system to various task types beyond the initial ARC challenge. It is the recommended path forward for incorporating alternative solving processes.
