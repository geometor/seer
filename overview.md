# SEER Process Workflow Overview (Updated)

This document outlines the process workflow for SEER, an agent designed to solve ARC-like tasks. This version reflects the codebase as of the latest update and incorporates significant changes from previous versions.

**Objectives (from README.md):**

-   Understand the nature of the problem based on the context or requirements.
-   Be able to describe the problem and the process through it in natural language.
-   Convert natural language program to executable code.
-   Facilitation and coaching.

SEER uses multi-modal models capable of reasoning and code execution (specifically mentioning Gemini).

## I. Initialization and Setup

1.  **Configuration Loading:**
    *   Reads a configuration dictionary (passed to `Seer` and `Session` constructors) to set up parameters. This dictionary includes:
        *   Output directory (`output_dir`).
        *   Multiple "roles" (e.g., "dreamer", "coder"), each with:
            *   Model name (`model_name`).
            *   Generation configuration (a dictionary with `temperature`, `top_p`, `top_k`, `max_output_tokens`, `response_mime_type`).
            *   System context file (`system_context_file`).
        *   Task context file (`task_context_file`).
        *   Maximum iterations (`max_iterations`).
        *   Instructions (mapping keys to filenames, e.g., `{"investigate_dreamer": "instructions_dreamer.md"}`).
        *   Whether to use images (`use_images`, defaults to `False`).

2.  **Task Loading:**
    *   Tasks are loaded externally (e.g., using the `Tasks` class) and passed to the `Seer.run()` method. Each `Task` object contains:
        *   An ID (`id`).
        *   A list of training `TaskPair` objects (`train`).
        *   A list of testing `TaskPair` objects (`test`).
    *   Each `TaskPair` contains:
        *   An input `Grid` object.
        *   An output `Grid` object (may be `None` for test pairs).
    *   `Grid` objects represent the input/output grids as NumPy arrays and store metadata.

3.  **Seer Instance Creation:**
    *   A `Seer` object is created, taking the configuration dictionary as input.
    *   Initializes:
        *   `roles`: A dictionary of `GeminiClient` instances, one for each role defined in the configuration. Each client is initialized with the role's specific configuration.
        *   `instructions`: Loads instructions from files specified in the configuration.
        *   `max_iterations`: Stores the maximum number of refinement iterations.
        *   `use_images`: Boolean flag indicating whether to include images in prompts.

4.  **Session Initialization:**
    *   A `Session` object is created, taking the configuration dictionary as input.
    *   Creates a timestamped session directory within the configured `output_dir`.
    *   Writes the configuration to `config.json` in the session directory.
    *   Writes system context files for each role and the task context to the session directory.

## II. Task Solving Loop (Outer Loop - `Seer.run`)

1.  **Iterate through Tasks:**
    *   The `Seer.run` method iterates through each `Task` object.

2.  **SessionTask Creation:**
    *   For each task, a `SessionTask` object is created within the `Session`. This manages the task-specific directory and data.
    *   Saves the task as an image (`task.png`) and JSON (`task.json`) in the task directory.

3.  **Solve Task (Call to `Seer.solve`)**
    *   Calls the `Seer.solve` method, passing in the `Session` object and the current `Task` object.

## III. Task Solving Process (Inner Loop - `Seer.solve`)

1.  **Investigate Examples (`_investigate`):**
    *   This method now handles the entire investigation and refinement process in a structured way.
    *   **Initial "dreamer" Step (All Training Examples):**
        *   A prompt is constructed including *all* training examples (input and output grids, text, and optionally images).
        *   The "dreamer" role is called with the `investigate_dreamer` instructions and `tools="code_execution"`.
        *   The response and any extracted code are processed and logged within a `TaskStep` object.
        *   Code trials are run using `task_step.run_trials()`. This creates `CodeTrial` objects, executes the code, and stores the results.
        *   The `TaskStep` is summarized, including trial results.
        *   If all training examples pass, and optionally if all test examples pass, the process moves to the next task.

    *   **"coder" Step (All Training Examples):**
        *   If the "dreamer" step doesn't solve the task, a "coder" step follows.
        *   The "coder" role is called with the `investigate_coder` instructions, the history from the "dreamer" step, and an empty prompt.
        *   The response, code extraction, trials, and summarization are handled similarly to the "dreamer" step.
        *   If all training (and optionally test) examples pass, the process moves to the next task.

    *   **Refinement Loop:**
        *   If the task is still not solved, a refinement loop begins (up to `max_iterations`).
        *   The `refine` method is called.
        *   Inside `refine`:
            *   **"refine_dreamer" Step:**
                *   A prompt is constructed for the "dreamer", including the *previous code* and the *results* of the previous code trial (using `code_trial.generate_report()`, which includes input, expected output, transformed output, match status, and error metrics).
                *   The "dreamer" is called with `refine_dreamer` instructions.
                *   Trials are run, and the step is summarized.  If successful, the function returns.
            *   **"refine_coder" Step:**
                *   A prompt (currently empty) is constructed for the "coder".
                *   The "coder" is called with `refine_coder` instructions and the history from the "dreamer".
                *   Trials are run, and the step is summarized.
        *   The loop continues until the task is solved or the maximum number of iterations is reached.

2.  **`_generate`:**
    *   This method is now responsible for interacting with the `GeminiClient`, handling logging, and creating `TaskStep` objects.
    *   **TaskStep Creation:**  A `TaskStep` object is created at the beginning of each interaction with the model.  This object manages a subdirectory for the step and stores all related data (prompt, response, extracted code, trial results, etc.).
    *   **Prompt Construction:** Combines the `history`, `prompt`, and `instructions`.
    *   **Model Interaction:** Calls the `GeminiClient.generate_content` method, handling retries.
    *   **Response Logging:** Logs the raw JSON response and response time within the `TaskStep`.
    *   **Response Processing:** Calls `task_step.process_response` to handle different parts of the response (text, executable code, function calls).  This method also extracts code blocks.
    *   **Markdown Logging:** Logs the processed response as Markdown within the `TaskStep`.

## IV. Code Execution and Validation (within `CodeTrial`)

1.  **`CodeTrial` Class:**
    *   Represents a single trial of a piece of code against a `Task`.
    *   Stores the code, filename, and associated `Task`.
    *   `train_results` and `test_results` store the results of executing the code against the training and test sets, respectively.
    *   `train_passed` and `test_passed` properties indicate whether all examples in the respective sets passed.
    *   `generate_report()` creates a detailed report of the trial results, including input/output grids and error metrics.
    *   `average_score` calculates a score representing the difference between transformed and expected output.

2.  **`test_code_with_timeout`:**
    *   Uses `multiprocessing` to run `test_code` in a separate process with a timeout.
    *   Returns the results from the queue or an error if a timeout occurs.

3.  **`test_code`:**
    *   **Parsing and Function Extraction:** Uses `ast.parse` to parse the code and extract the `transform` function.
    *   **Execution and Comparison:**
        *   Iterates through the provided `task_pairs`.
        *   Calls the `transform` function with the input grid.
        *   Creates a `TaskPairTrial` object to store the results of each individual example.
        *   `TaskPairTrial` calculates and stores:
            *   `match`: Whether the transformed output exactly matches the expected output.
            *   `size_correct`: Whether the dimensions match.
            *   `color_palette_correct`: Whether the colors in the transformed output are a subset of the expected output's colors.
            *   `color_count_correct`: Whether the counts of each color are the same.
            *   `pixels_off`: The number of differing pixels (if sizes match).
            *   `percent_correct`: Percentage of correct pixels (if sizes match).
            *   `score`: A score representing the difference between transformed and expected output.
        *   Captures any output printed by the code.
    *   **Error Handling:** Catches exceptions during code execution.
    *   **Return Value:** Returns a dictionary containing a list of `TaskPairTrial` objects (converted to dictionaries).

## V. Session Management (`Session`, `SessionTask`, `TaskStep`, `Level`)

1.  **`Level` (Base Class):**
    *   Provides common functionality for managing directories, logging errors, and writing files.
    *   `log_error`: Logs exceptions with context, datetime, stack trace, and exception message.
    *   `_write_to_file`: Writes content to a file.
    *   `_write_to_json`: Writes JSON data to a file.
    *   `log_markdown`:  Writes Markdown content to a file, handling embedded images.
    *   `summarize`: Provides a base implementation for generating summaries (to be overridden by subclasses).

2.  **`Session`:**
    *   Manages the overall session directory and top-level logging.
    *   `add_task`: Creates a `SessionTask` for each task.
    *   `summarize`: Generates a session-level summary, including aggregated trial counts from each `SessionTask`.

3.  **`SessionTask`:**
    *   Manages the directory for a specific task.
    *   `add_step`: Creates a `TaskStep` for each interaction with the model.
    *   `summarize`: Generates a task-level summary, aggregating results from all `TaskStep` objects within the task.  Calculates `best_score`.
    *   `train_passed` and `test_passed` properties indicate whether any steps within the task passed all training/test examples.

4.  **`TaskStep`:**
    *   Manages the directory for a single step (interaction with the model).
    *   Stores the prompt, response, extracted code, and trial results.
    *   `log_response`: Logs the raw response and response time.
    *   `process_response`: Parses the response, extracts code blocks, and handles function calls (currently not used).
    *   `run_trials`: Creates and runs `CodeTrial` objects for all extracted code.
    *   `summarize`: Generates a step-level summary, including trial results and code information.
    *   `get_first_code_trial()`: Returns the first `CodeTrial` object, if any.
    *   `any_trials_successful()`: Checks if any trials were successful.
    *   `train_passed` and `test_passed` properties.
    *   `get_python`: Returns the extracted Python code.

5. **`StepCodeTrials`:**
    *   Manages a collection of `CodeTrial` instances for a `TaskStep`.
    *   `run_trials`: Creates and runs `CodeTrial` objects for all extracted code in the associated `TaskStep`.
    *   `get_code_trial`: Retrieves a specific `CodeTrial` by filename.
    *   `get_first_code_trial`: Retrieves the first `CodeTrial`.
    *   `any_train_passed` and `any_test_passed` properties.
    *   `count_trials`: Returns the number of `CodeTrial` objects.
    *   `get_all_trials`: Returns a list of all `CodeTrial` objects.
    *   `get_best_trial`: Returns the `CodeTrial` with the lowest average score.
    *   `best_score`: Returns the best score.

## VI. Helper Functions and Classes

*   **`get_pair_prompt` (in `prompts.py`):** Formats prompts for individual task pairs, optionally including images.
*   **`string_to_grid` (in `grid.py`):** Converts a string representation of a grid back into a `Grid` object.
*   **`Task.to_image` (in `tasks.py`):** Creates a combined image of the task's train/test pairs, optionally including transformed outputs from trial results.
*   **`Grid.to_image` (in `grid.py`):** Creates an image of a single grid.

## Key Improvements and Changes:

*   **Structured Step-by-Step Approach:** The code now uses a clear "dreamer" -> "coder" -> "refine_dreamer" -> "refine_coder" pattern, with each step managed by a `TaskStep` object.
*   **`TaskStep` for Logging and Organization:**  The `TaskStep` class significantly improves organization and logging by creating a dedicated directory for each step and storing all relevant information.
*   **`CodeTrial` and `TaskPairTrial`:** These classes encapsulate the execution and evaluation of code, providing detailed results and metrics.
*   **`StepCodeTrials` Class:** Manages multiple `CodeTrial` objects within a `TaskStep`.
*   **Unified `_investigate`:** The `_investigate` method now handles the entire task-solving process, including the initial investigation and the refinement loop.
*   **Simplified `_generate`:**  This method focuses on interacting with the model and creating `TaskStep` objects.
*   **Comprehensive Summarization:**  The `Session`, `SessionTask`, and `TaskStep` classes all have `summarize` methods that generate detailed reports at different levels.
*   **Improved Error Handling:**  Error logging is handled consistently using the `log_error` method in the `Level` class.
*   **Image Handling:** Image generation is integrated into the `Task` and `Grid` classes, and the `use_images` flag controls whether images are included in prompts.
*   **No More Global Variables:** The code avoids using global variables, improving modularity and maintainability.
*   **Function Calls (Still Unused):** The infrastructure for function calls remains present but is not actively used.
*   **Clearer Naming:**  Variable and method names have been improved for clarity (e.g., `extracted_file_counts` is now managed within `TaskStep`).
*   **Removal of Unused Code:**  Several unused functions and code blocks have been removed.
*   **Refactored Code Extraction:** Code extraction is now handled within the `TaskStep.process_response` method, using regular expressions.
*   **Multiprocessing for Timeouts:** The `test_code_with_timeout` function in `CodeTrial` uses multiprocessing to enforce timeouts on code execution.
