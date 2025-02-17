# SEER Process Workflow Overview

This document outlines the process workflow for SEER, an agent designed to solve ARC-like tasks.

**Objectives (from README.md):**

-   Understand the nature of the problem based on the context or requirements.
-   Be able to describe the problem and the process through it in natural language.
-   Convert natural language program to executable code.
-   Facilitation and coaching.

SEER uses multi-modal models capable of reasoning and code execution (specifically mentioning Gemini).

## I. Initialization and Setup

1.  **Configuration Loading:**
    *   Reads `config.yaml` to set up parameters for:
        *   Output directory (`output_dir`).
        *   "Dreamer" model (natural language processing):
            *   Model name (`model_name`).
            *   Generation configuration (temperature, `top_p`, `top_k`, `max_output_tokens`, `response_mime_type`).
            *   System context file (`system_context_file`).
        *   "Builder" model (code generation):
            *   Same parameters as "Dreamer".
        *   Task context file (`task_context_file`).
        *   Maximum iterations (`max_iterations` - currently unused).

2.  **Task Loading:**
    *   Creates a `Tasks` object, loading all `.json` task files from the specified folder (default is the current directory).  Each task file represents an ARC-like problem.
    *   Each `Task` object contains:
        *   An ID (`id`).
        *   A list of training `TaskPair` objects (`train`).
        *   A list of testing `TaskPair` objects (`test`).
    *   Each `TaskPair` contains:
        *   An input `Grid` object.
        *   An output `Grid` object (may be `None` for test pairs).
    *   `Grid` objects represent the input/output grids as NumPy arrays and store metadata.

3.  **Seer Instance Creation:**
    *   Creates a `Seer` object, passing in the loaded configuration.
    *   Initializes:
        *   Start time tracking.
        *   Gemini API clients (`dreamer_client` and `builder_client`):
            *   Loads system context from files specified in `config.yaml`.
            *   Sets up generation configuration based on `config.yaml`.
        *   Loads instructions from `nlp_instructions.md` and `code_instructions.md`.
        *   Sets `max_iterations` (currently not used in the provided code).
        *   Initializes counters for tokens and extracted files.

4.  **Session Initialization:**
    *   Creates a `Session` object.
    *   Creates a timestamped session directory within the configured `output_dir`.
    *   Creates subdirectories for each task within the session directory.
    *   Writes the loaded `config.yaml` to the session directory.
    *   Displays the configuration.

## II. Task Solving Loop (Outer Loop - `Seer.run`)

1.  **Iterate through Tasks:**
    *   The `Seer.run` method iterates through each loaded `Task` object in the `Tasks` list.

2.  **Task Setup:**
    *   For each task:
        *   Sets the `Session.task_dir` to the appropriate task subdirectory.
        *   Initializes prompt counter.

3.  **Solve Task (Call to `Seer.solve`)**
    *   Calls the `Seer.solve` method, passing in the current `Task` object.

## III. Task Solving Process (Inner Loop - `Seer.solve`)

1.  **Investigate Examples (`_investigate_examples`):**
    *   Iterates through the training `TaskPair` objects in the current `Task`.
    *   For each `TaskPair`:
        *   **Natural Language Description (Dreamer):**
            *   Constructs a prompt for the "dreamer" model, including:
                *   The input grid as text.
                *   The input grid as an image (optional, controlled by `include_images`).
                *   The output grid as text.
                *   The output grid as an image (optional).
                *   Instructions from `nlp_instructions.md`.
            *   Calls `_generate` to send the prompt to the `dreamer_client`.
            *   Logs the prompt and response.
            *   Processes the response (`_process_response`):
                *   Extracts text parts.
                *   Identifies and extracts content within triple backticks (code, YAML, etc.) and saves them to files.
        *   **Code Generation (Builder):**
            *   Constructs a prompt for the "builder" model, including:
                *   Instructions from `code_instructions.md`, formatted with the input and expected output grids as Python lists.
            *   Calls `_generate` to send the prompt to the `builder_client`, specifying `tools="code_execution"`.
            *   Logs the prompt and response.
            *   Processes the response (`_process_response`):
                *   Extracts text parts.
                *   Identifies and extracts executable code.
                *   Saves the code to a `.py` file.
                *   Executes the code (`_test_code`):
                    *   Runs the `transform` function (if present) on the training input grids.
                    *   Compares the generated output with the expected output.
                    *   Logs the results (input, expected output, transformed output, pass/fail).
                    *   Captures any output printed by the code.
                    *   Handles `SyntaxError` and other exceptions during code execution.
                *   Extracts code execution results (outcome and output).
                *   Saves the code execution output to a `.txt` file.
                *   Extracts function calls (currently not used).

2.  **Review Programs (`_review_programs` - Currently Placeholder):**
    *   This method is intended to summarize observations across all training pairs, but it's currently a placeholder.

## IV. Generation and Response Handling (`_generate`)

1.  **Prompt Construction:**
    *   Combines the history, current prompt, and instructions.
    *   Logs the prompt and total prompt.

2.  **Model Interaction:**
    *   Calls the appropriate Gemini client's `generate_content` method:
        *   Passes the prompt.
        *   Specifies `tools` (e.g., "code_execution") if needed.
        *   Uses retries for robustness.

3.  **Response Processing (`_process_response`):**
    *   Handles different parts of the response:
        *   Text parts.
        *   Executable code (executes and validates).
        *   Code execution results.
        *   Function calls (currently not used).
    *   Extracts content within triple backticks and saves to files.
    *   Logs the response and extracted content.

## V. Code Execution and Validation (`_test_code`)

1.  **Code Execution:**
    *   Parses the generated code using `ast.parse`.
    *   Executes the code in a separate namespace.
    *   Captures standard output.

2.  **Validation:**
    *   Finds the `transform` function within the parsed code.
    *   Iterates through the training examples:
        *   Calls the `transform` function with the input grid.
        *   Compares the result to the expected output grid using `np.array_equal`.
        *   Logs the input, expected output, transformed output, and whether the test passed or failed.

3.  **Error Handling:**
    *   Catches `SyntaxError` and other exceptions during code execution.
    *   Logs error messages.

4.  **Output Capture:**
    *   Captures any output printed by the executed code.
    *   Logs the captured output.

5.  **Result Logging:**
    *   Writes detailed test results to a `.md` file.

## VI. Session Management (`Session` class)

1.  **Initialization:**
    *   Creates output directories.
    *   Writes configuration to file.
    *   Displays configuration.

2.  **Logging:**
    *   `log_prompt`: Logs the prompt and instructions to a file.
    *   `log_total_prompt`: Logs the complete prompt (including history) to a file.
    *   `log_response`: Logs the model's response, token counts, and timing information.
    *   `log_error`: Logs errors to a file.

3.  **Display:**
    *   `display_prompt`: Displays the prompt and instructions using rich Markdown.
    *   `display_response`: Displays the response, usage metadata, and test results using rich Markdown.
    *   `display_config`: Displays the configuration.
    *   `display_test_results`: Displays detailed test results.

## VII. Helper Functions

*   `_write_extracted_content`: Extracts content within triple backticks and saves it to files, handling different file types.
*   `_write_to_file`: Writes content to a specified file.
*   `_call_function`: (Currently not used) Handles function calls made by the model.
*   `_format_banner`: Formats a banner for logging output.

## Key Improvements and Considerations:

*   **Clear Separation of Concerns:** The code is well-structured, with separate classes for tasks, grids, the Seer, and session management.
*   **Detailed Logging:** Extensive logging to files and the console (using `rich`) makes it easy to track the process and debug issues.
*   **Error Handling:** Includes error handling for file operations, code execution, and function calls.
*   **Code Execution and Validation:** The `_test_code` method provides a robust way to execute and validate generated code.
*   **Use of Gemini API:** Leverages the Gemini API for both natural language processing and code generation.
*   **Configuration-Driven:** Uses a YAML configuration file for easy customization.
*   **Extensible:** The design allows for future extensions, such as adding support for different models or tools.
*   **Iteration (Currently Limited):** Although `max_iterations` is defined, the current code doesn't implement an iterative refinement loop. This is a key area for future development.
*   **Function Calls (Unused):** The code includes infrastructure for handling function calls, but this feature is not currently used.
*   **Review/Summarization:** The `_review_programs` method is a placeholder, indicating an intention to summarize findings across examples. This is another area for future development.
*   **Test Set Evaluation:** The code focuses on the training set. Evaluating the generated code on the test set would be a crucial addition.
