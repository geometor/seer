# SEER Process Workflow Overview (Updated)

This document outlines the process workflow for SEER, an agent designed to solve ARC-like tasks.  This version reflects the codebase as of the last update.

**Objectives (from README.md):**

-   Understand the nature of the problem based on the context or requirements.
-   Be able to describe the problem and the process through it in natural language.
-   Convert natural language program to executable code.
-   Facilitation and coaching.

SEER uses multi-modal models capable of reasoning and code execution (specifically mentioning Gemini).

## I. Initialization and Setup

1.  **Configuration Loading:**
    *   Reads a configuration dictionary (passed to `Seer` and `Session` constructors) to set up parameters.  This dictionary includes:
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
    *   Tasks are loaded externally (e.g., using the `Tasks` class) and passed to the `Seer.run()` method.  Each `Task` object contains:
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
        *   `roles`: A dictionary of `GeminiClient` instances, one for each role defined in the configuration.  Each client is initialized with the role's specific configuration.
        *   `instructions`: Loads instructions from files specified in the configuration.
        *   `max_iterations`: Stores the maximum number of refinement iterations.
        *   `current_iteration`: Tracks the current iteration (used in the `refine` loop).
        *   `use_images`: Boolean flag indicating whether to include images in prompts.
        *   `token_counts`: Dictionary to track token usage.
        *   `extracted_file_counts`: Dictionary to track the number of extracted files of each type.
        *   `task_solved`: A boolean flag to indicate if the current task has been solved.

4.  **Session Initialization:**
    *   A `Session` object is created, taking the configuration dictionary and the list of `Task` objects.
    *   Creates a timestamped session directory within the configured `output_dir`.
    *   Creates subdirectories for each task within the session directory.
    *   Writes the configuration to `config.json` in the session directory.
    *   Writes system context files for each role and the task context to the session directory.
    *   Displays the configuration.

## II. Task Solving Loop (Outer Loop - `Seer.run`)

1.  **Iterate through Tasks:**
    *   The `Seer.run` method iterates through each `Task` object.

2.  **Task Setup:**
    *   For each task:
        *   Calls `session.set_task_dir(task.id)` to create/set the task-specific output directory.
        *   Resets `prompt_count` to 0.
        *   Stores the current `Task` object in `self.task`.
        *   Resets `extracted_file_counts`.
        *   Saves the task as an image (`task.png`) and JSON (`task.json`) in the task directory.

3.  **Solve Task (Call to `Seer.solve`)**
    *   Calls the `Seer.solve` method, passing in the `Session` object and the current `Task` object.

## III. Task Solving Process (Inner Loop - `Seer.solve`)

1.  **Investigate Examples (`_investigate`):**
    *   Resets the `task_solved` flag to `False`.
    *   Defines a nested function `get_pair_prompt` to format prompts for individual task pairs, optionally including images.
    *   **Combined Training Prompt:** Creates a single prompt that includes *all* training examples (input and output grids, both as text and optionally as images).  This is sent to the "dreamer" role with the `investigate_dreamer` instructions.
    *   **Code Testing:**  The response from the "dreamer" is processed, and any extracted code blocks are tested using `_test_extracted_codelist`.
    *   **Coder Prompt:**  After the "dreamer" step, a prompt is sent to the "coder" role with the `investigate_coder` instructions. The history from the "dreamer" interaction is included.
    *   **Code Testing (Again):** The response from the "coder" is processed, and any extracted code blocks are tested.
    *   **Individual Training Pair Loop:**  If the task is not solved after the combined prompt, the code iterates through each training pair *individually*.  For each pair:
        *   The "dreamer" is called with the `investigate_dreamer` instructions and the specific training pair.
        *   Extracted code is tested.
        *   The "coder" is called with the `investigate_coder` instructions, including the history from the "dreamer".
        *   Extracted code is tested again.
        *   The loop breaks if `task_solved` becomes `True`.

2.  **`_test_extracted_codelist`:**
    *   Iterates through all extracted code blocks (identified by type, content, and a base filename).
    *   For each Python (`.py`) code block:
        *   Calls `verifier.test_code_with_timeout` to execute the code against the training examples.  This function uses `multiprocessing` to enforce a timeout.
        *   Writes the test results to a JSON file (`<base_filename>-train.json`) and a Markdown file (`<base_filename>-train.md`).
        *   If all training examples pass, it runs the code against the *test* examples.
        *   Writes the test results to JSON and Markdown files (`<base_filename>-test.json` and `<base_filename>-test.md`).
        *   Generates images showing the input, expected output, and transformed output for both training and test sets (if applicable).
        *   If all *test* examples pass, sets `self.task_solved = True` and breaks the inner loop.
        *   If not all training examples pass, and the maximum number of iterations has not been reached, calls the `refine` method.

3.  **Refinement (`refine`):**
    *   Increments `current_iteration`.
    *   Constructs a prompt for the "dreamer" role, including:
        *   The previous code.
        *   The results of the training set execution (input, expected output, transformed output, match status, and various error metrics).
        *   The results of the test set execution (if applicable), with the same level of detail as the training results.
        *   Images of the transformed outputs.
    *   Calls `_generate` with the "dreamer" role and `refine_dreamer` instructions.
    *   Tests any code extracted from the "dreamer" response (although code is not generally expected here).
    *   Constructs a prompt for the "coder" role (currently empty).
    *   Calls `_generate` with the "coder" role, `refine_coder` instructions, and the history from the "dreamer" interaction.
    *   Tests any code extracted from the "coder" response.

## IV. Generation and Response Handling (`_generate`)

1.  **Prompt Construction:**
    *   Combines the `history`, current `prompt`, and `instructions`.
    *   Logs the prompt and the total prompt using `session.log_prompt` and `session.log_total_prompt`.

2.  **Model Interaction:**
    *   Gets the appropriate `GeminiClient` instance from `self.roles`.
    *   Calls the client's `generate_content` method:
        *   Passes the total prompt.
        *   Specifies `tools` if provided (e.g., "code_execution").  If `tools` is not "code_execution", sets `tool_config` to allow function calling.
        *   Uses retries for robustness.

3.  **Response Logging:**
    *   Logs the raw JSON response using `session.log_response_json`.

4.  **Response Processing (`_process_response`):**
    *   Handles different parts of the response:
        *   Text parts: Appends the text to `response_parts`.  Also calls `_parse_code_text` to extract any code blocks within the text.
        *   Executable code (deprecated):  If present, appends a marker and the code to `response_parts`.
        *   Code execution result (deprecated): If present, appends a marker, outcome, and output to `response_parts`, and writes the output to a file.
        *   Function calls (currently not used):  If present, appends a marker and the function name to `response_parts`, then calls `_call_function` (which currently raises an error).
    *   Returns `response_parts` (a list of strings) and `extracted_code_list` (a list of tuples: `(file_type, code, base_filename)`).

5.  **Markdown Logging:**
    *   Logs the processed response (including extracted code) as Markdown using `session.log_response_md`.

## V. Code Extraction (`_parse_code_text`)

1.  **Extraction:**
    *   Uses regular expressions (`re.findall`) to find code blocks enclosed in triple backticks.
    *   Handles optional language specifiers (e.g., ```python).  Defaults to "txt" if no language is specified.  Converts "python" to "py".

2.  **File Writing:**
    *   Calls `session._write_code_text` to write the extracted code to a file.  This function:
        *   Determines the filename based on the prompt count, file type, and an internal counter (`extracted_file_counts`).
        *   Writes the content to the file using `session._write_to_file`.
        *   Returns the full path to the created file.

3.  **Return Value:**
    *   Returns a list of tuples: `(file_type, code, base_filename)`.  `base_filename` is the filename *without* the extension.

## VI. Code Execution and Validation (in `verifier.py`)

1.  **`test_code_with_timeout`:**
    *   Uses `multiprocessing` to run `test_code` in a separate process with a timeout.
    *   If the process times out, terminates it and returns an error result.
    *   If the process completes within the timeout, returns the result from the queue.

2.  **`test_code`:**
    *   **Parsing and Function Extraction:**
        *   Uses `ast.parse` to parse the code.
        *   Finds the `transform` function using `ast.walk`.
        *   If `transform` is not found or a `SyntaxError` occurs, returns an error result.
    *   **Execution and Comparison:**
        *   Iterates through the provided `task_pairs` (either training or testing).
        *   Calls the `transform` function with the input grid.
        *   Converts the result to a NumPy array.
        *   Compares the transformed output to the expected output using `np.array_equal`.
        *   Calculates and stores:
            *   `match`: Whether the transformed output exactly matches the expected output.
            *   `size_correct`: Whether the dimensions match.
            *   `color_palette_correct`: Whether the set of colors in the transformed output is a subset of the colors in the expected output.
            *   `correct_pixel_counts`: Whether the counts of each color are the same.
            *   `pixels_off`: The number of pixels that differ (if the size is correct).
            *   `percent_correct`: The percentage of correct pixels (if the size is correct).
        *   Captures any output printed by the code using `contextlib.redirect_stdout`.
    *   **Error Handling:**  Catches exceptions during code execution and stores error messages.
    *   **Return Value:** Returns a dictionary containing the results for each example, including input, expected output, transformed output, match status, error messages, and calculated statistics.

3.  **`write_test_results`:**
    *   Writes the test results to both JSON and Markdown files.
    *   Generates and saves images of the transformed output grids.
    *   Formats the output to include input, expected output, transformed output, and various metrics.

4.  **`string_to_grid`:**
    *   Converts a string representation of a grid back into a `Grid` object.  Handles potential errors during conversion.

## VII. Session Management (`Session` class)

1.  **Initialization:**
    *   Creates output directories (session and task-specific).
    *   Writes configuration to `config.json`.
    *   Writes system context files and the task context file.
    *   Displays configuration using `display_config`.

2.  **Logging:**
    *   `log_prompt`: Logs the prompt and instructions to `<prompt_count>-prompt.md`.
    *   `log_total_prompt`: Logs the complete prompt (including history) to `<prompt_count>-total_prompt.md`.
    *   `log_response_json`: Logs the raw model response, response time, and filename to `<prompt_count>-response.json`.
    *   `log_response_md`: Logs the processed response parts to `<prompt_count>-response.md`.
    *   `log_prompt_image`: Saves an image and returns the filename.
    *   `log_error`: Logs errors to `error_log.txt`.

3.  **Display:**
    *   `display_prompt`: Displays the prompt and instructions using rich Markdown.
    *   `display_response`: Displays the response, usage metadata, and timing information using rich Markdown.
    *   `display_config`: Displays the configuration using rich Markdown.
    *   `display_test_results`: Displays test results (currently unused).

4.  **File Writing:**
    *   `_write_code_text`:  Writes extracted code blocks to files, handling file type counters.
    *   `_write_to_file`: Writes content to a specified file within the *task* directory.

5. **Summary:**
    * `summarize_session`: Generates a session level summary
    * `summarize_task`: Generates a task level summary

## VIII. Helper Functions

*   `_format_banner`: Formats a banner for logging output.
*   `_call_function`: (Currently raises an error) Intended to handle function calls made by the model.

## Key Improvements and Considerations:

*   **Combined Training Prompt:**  Sending all training examples in a single prompt at the beginning of the investigation phase is a significant change.
*   **Refinement Loop:** The `refine` method implements an iterative process to improve the generated code based on test results.
*   **Timeout for Code Execution:** The `verifier.test_code_with_timeout` function uses `multiprocessing` to prevent infinite loops or excessively long execution times.
*   **Detailed Test Results:** The `verifier.test_code` function calculates and logs various metrics to assess the quality of the generated code.
*   **Image Generation:**  The code generates images of the input, expected output, and transformed output grids, making it easier to visualize the results.
*   **JSON and Markdown Logging:**  Detailed logs are written in both JSON and Markdown formats.
*   **Session and Task Summaries:** The `summary.py` module generates summary reports at both the session and task levels.
*   **Error Handling:** The code includes more comprehensive error handling, particularly for file operations and code execution.
*   **Clearer Separation of Concerns:** The code is better organized, with separate modules for tasks, grids, the Seer, session management, the Gemini client, and code verification.
*   **No More `_write_extracted_content`:** This function has been replaced by `_parse_code_text` and `_write_code_text`, which provide a cleaner separation of concerns.
*   **Function Calls (Unused):** The infrastructure for handling function calls is still present but not actively used.
*   **Test Set Evaluation:** The code now evaluates the generated code on the test set *after* all training examples pass.
