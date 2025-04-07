# Report: Parallel Generation of Transform and Validate Functions

## 1. Introduction

Building upon the goal of improving the Seer's task-solving capabilities, this report explores an advanced strategy: generating not only a `transform` function but also a corresponding `validate` function within each task-solving cycle. This approach aims to enhance the system's understanding of task rules, improve verification, and provide richer signals for refinement.

The core idea is to run two parallel code-generation processes within the investigation and refinement phases, one focused on transformation logic (`transform`) and the other on rule validation logic (`validate`), using the existing "coder" role but with specialized instructions.

## 2. Rationale: Why Generate a `validate` Function?

Generating an explicit `validate(input_grid, output_grid) -> bool` function alongside `transform(input_grid)` offers several advantages:

*   **Explicit Rule Extraction:** Forces the AI to articulate its understanding of the task's underlying rules into a testable function, rather than solely embedding them implicitly within the transformation logic.
*   **Independent Verification:** Allows for checking:
    *   Whether the provided training examples conform to the AI's extracted rules (`validate(train_input, train_output)` should be `True`).
    *   Whether the `transform` function's output adheres to the extracted rules (`validate(input, transform(input))`), providing a check separate from direct output comparison.
*   **Enhanced Refinement Signal:** Failures in the `validate` function (on training data or transformed outputs) provide a strong, specific signal about flaws in the AI's rule understanding, potentially guiding the refinement process more effectively than pixel differences alone.

## 3. Proposed Workflow: Parallel Generation and Cross-Refinement

This strategy modifies the `_investigate` and `refine` methods within the `Seer` class.

### 3.1. `_investigate` Phase

1.  **Dreamer Step:**
    *   Runs first, analyzing training pairs.
    *   Generates initial insights, plans, or pseudocode.
    *   Its output is added to the history.
2.  **Parallel Coder Step (Transform + Validate):**
    *   Two concurrent `_generate` calls are initiated using the "coder" role, sharing the same history (including dreamer output):
        *   **Thread 1 (Generate Transform):** Uses instructions specifically asking for the `transform` function (e.g., `investigate_coder_transform`).
        *   **Thread 2 (Generate Validate):** Uses instructions specifically asking for the `validate` function (e.g., `investigate_coder_validate`).
    *   These run in parallel, potentially using a dedicated `ThreadPoolExecutor(max_workers=2)` or `threading.Thread` within the `_investigate` method. The global rate limiter (if implemented) manages API call frequency.
    *   Wait for both threads to complete. Handle potential errors in each thread (e.g., if one fails after retries).
3.  **Combine & Test Step:**
    *   Parse the responses from both threads to extract `transform_code` and `validate_code`.
    *   Create a `CodeTrial` instance storing both code snippets.
    *   Execute `code_trial.test_code_with_timeout()` using `transform_code` against train/test pairs.
    *   Execute a new method `code_trial.test_validation_function()` using `validate_code` against:
        *   Training pairs: `validate(train_input, train_output)`
        *   Transformed outputs: `validate(input, transform(input))`
    *   Store results from both tests within the `CodeTrial`.
4.  **Summarize:** The `TaskStep` summary now reflects the success/failure and metrics for both the transformation and the validation.

### 3.2. `refine` Phase (Iteration `N`)

1.  **Input:** Receives `transform_code`, `validate_code`, and the combined test/validation results from the previous iteration (`N-1`).
2.  **Refine Dreamer Step:**
    *   Runs first.
    *   The prompt includes the code and results for *both* `transform` and `validate` from iteration `N-1`.
    *   Instructions ask the dreamer to analyze failures/discrepancies in both functions and suggest improvements for both.
    *   Its output is added to the history for this refinement cycle.
3.  **Parallel Refine Coder Step (Transform + Validate):**
    *   Two concurrent `_generate` calls are initiated using the "coder" role, sharing the same history (including refine dreamer output):
        *   **Thread 1 (Refine Transform):** Uses instructions like `refine_coder_transform`. The prompt context includes the dreamer's analysis and potentially relevant details (code snippets, failure examples) from the *previous `validate` function*.
        *   **Thread 2 (Refine Validate):** Uses instructions like `refine_coder_validate`. The prompt context includes the dreamer's analysis and potentially relevant details from the *previous `transform` function*.
    *   This **cross-sharing** of context is key, aiming to make the refinement of each function aware of the other.
    *   Wait for both threads to complete.
4.  **Combine & Test Step:** Same procedure as in the `_investigate` phase: parse results, create `CodeTrial`, run `transform` tests, run `validate` tests, store combined results.
5.  **Summarize:** Update the `TaskStep` summary.

## 4. Implementation Considerations

*   **Parallel Execution:** Use `concurrent.futures.ThreadPoolExecutor` or `threading.Thread` within `_investigate` and `refine` to manage the parallel coder calls. A shared `RateLimiter` (as discussed in the parallel processing report) is essential.
*   **State Management:**
    *   `TaskStep`: Needs logic to handle receiving and parsing results from two concurrent generation calls before creating/populating the `CodeTrial`. Error handling for partial success (one call fails, one succeeds) is needed.
    *   `CodeTrial`: Requires new attributes (e.g., `validate_code: str`, `validation_results: dict`). Its `__init__` or subsequent methods will store both code strings and both sets of test results. A new method like `test_validation_function` is needed.
    *   `Seer`: Needs to manage the slightly more complex flow within `_investigate` and `refine`.
*   **Configuration (`config.yaml`):** Requires new instruction keys/files (e.g., `investigate_coder_transform`, `investigate_coder_validate`, `refine_dreamer_dual`, `refine_coder_transform`, `refine_coder_validate`).
*   **History Management:** Ensure history correctly incorporates outputs from both parallel coder steps before proceeding to the next cycle or refinement iteration.
*   **Prompt Engineering:** Crafting effective prompts for the dreamer (analyzing both functions) and the coders (generating/refining one function while being aware of the other) is critical.

## 5. Benefits

*   **Deeper Rule Understanding:** Encourages the AI to explicitly model and test task rules.
*   **More Robust Solutions:** Cross-refinement based on both transformation and validation results could lead to more accurate and generalizable `transform` functions.
*   **Improved Debugging:** Validation failures provide clearer insights into *why* a task might be failing beyond simple output mismatches.
*   **Potential for Faster Cycles:** Parallel generation within steps might reduce the wall-clock time per investigation/refinement cycle (at the cost of more simultaneous API calls).

## 6. Drawbacks

*   **Increased Complexity:** Managing parallel execution within steps, coordinating results, and handling partial failures significantly increases the complexity of the `Seer`'s core logic.
*   **Increased API Costs & Usage:** Doubles the number of "coder" API calls per cycle, impacting cost and potentially hitting rate limits more easily if the limiter isn't configured correctly.
*   **Challenging Prompt Engineering:** Designing prompts that effectively leverage the cross-sharing context during refinement requires careful experimentation.
*   **Error Handling:** Defining the desired behavior when one of the parallel generation calls fails (e.g., does the whole step fail? Can refinement proceed with only one updated function?) adds complexity.

## 7. Conclusion

Generating `transform` and `validate` functions in parallel with cross-refinement represents a sophisticated evolution of the Seer's strategy. While significantly more complex to implement and requiring more API resources than the baseline or simple task-level parallelism, it holds the potential to produce more robust and well-understood solutions by forcing the AI to explicitly validate its own logic against the perceived task rules.

This strategy is best considered *after* implementing basic task-level parallelism and rate limiting. It requires careful design, implementation, and tuning, particularly around prompt engineering and error handling for the parallel generation steps.
