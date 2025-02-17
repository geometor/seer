# Configuration Guide for `config.yaml`

This document explains the settings in `config.yaml`, which controls the behavior of the Seer application. It focuses on the parameters for the Gemini models ("dreamer" and "builder") and how they affect performance, particularly for ARC tasks.

## Overview

The `config.yaml` file is structured into several sections:

*   `output_dir`: Specifies the directory where session logs and outputs will be saved.
*   `dreamer`: Configuration for the "dreamer" model (used for natural language processing).
*   `builder`: Configuration for the "builder" model (used for code generation).
*   `task_context_file`: Path to a Markdown file containing the overall task description.
*   `max_iterations`: Maximum number of iterations for the solution refinement loop (currently not used).

## Model Configuration (`dreamer` and `builder`)

Both `dreamer` and `builder` sections have the same structure:

```yaml
dreamer:
  model_name: gemini-2.0-pro-exp-02-05  # Example model name
  generation_config:
    temperature: 1.0
    top_p: 0.95
    top_k: 64
    max_output_tokens: 8192
    response_mime_type: "text/plain"
  system_context_file: "./system_context_dreamer.md"

builder:
  # ... (same structure as dreamer)
```

### `model_name`

This specifies which Gemini model to use.  Different models have different capabilities and performance characteristics.  `gemini-2.0-pro-exp-02-05` is an example; you might use `gemini-1.5-pro-002` or other available models.  The choice of model significantly impacts the quality of both natural language understanding and code generation.  Larger, more advanced models generally perform better on complex reasoning tasks but may be slower and consume more resources.

### `generation_config`

This section contains parameters that fine-tune the model's generation process.  These parameters are crucial for balancing creativity, coherence, and correctness.

*   **`temperature`**:  Controls the randomness of the output.
    *   *Lower values* (e.g., 0.1-0.4) make the output more deterministic and focused, favoring the most likely tokens.  This is generally good for code generation where precision is essential.
    *   *Higher values* (e.g., 0.7-1.0) increase randomness, leading to more creative and diverse outputs.  This can be useful for the "dreamer" model to explore different interpretations of the task, but can also lead to nonsensical or incorrect results.
    *   *For ARC tasks*:  Start with a lower temperature (e.g., 0.2) for the `builder` to ensure code correctness.  For the `dreamer`, you might experiment with slightly higher values (e.g., 0.4-0.7) to encourage diverse descriptions, but be prepared to iterate and refine.

*   **`top_p`**:  Controls nucleus sampling.  It limits the model's choices to a subset of the most likely tokens whose cumulative probability mass does *not* exceed `top_p`.
    *   *Lower values* (e.g., 0.5) restrict the model to a smaller set of highly probable tokens, leading to more focused output.
    *   *Higher values* (e.g., 0.9-1.0) allow the model to consider a wider range of tokens, increasing diversity.
    *   *For ARC tasks*:  A value between 0.7 and 0.95 is generally a good starting point.  Lower `top_p` can improve code quality, while higher `top_p` might help the "dreamer" explore different perspectives.

*   **`top_k`**:  Limits the model's choices to the `k` most likely tokens at each step.
    *   *Lower values* (e.g., 10-20) make the output more deterministic.
    *   *Higher values* (e.g., 40-64) allow for more diversity.
    *   *For ARC tasks*:  A value between 32 and 64 is often a good compromise.  Too low a value can make the output repetitive; too high a value can lead to irrelevant tokens.

*   **`max_output_tokens`**:  Sets the maximum length of the generated text.  Ensure this is large enough to accommodate the expected responses, including both natural language descriptions and code.  8192 is a large value and should be sufficient for most ARC tasks.  If you find responses being truncated, increase this value.

*   **`response_mime_type`**: Specifies the desired format of the response.  `text/plain` is appropriate for both natural language and code.

### `system_context_file`

This points to a Markdown file containing the system instructions for the model.  These instructions provide the overall context and guide the model's behavior.  Separate system context files are used for the "dreamer" and "builder" to tailor their roles.

## Recommendations for ARC Tasks

*   **Start Conservative**: Begin with lower temperatures and `top_p` values, especially for the `builder`.  Prioritize correctness over creativity initially.
*   **Iterate and Experiment**:  Adjust the parameters and observe the effects on the model's output.  There's no one-size-fits-all solution; experimentation is key.
*   **Separate Concerns**:  Use the `dreamer` for exploration and brainstorming (potentially with higher temperature/`top_p`) and the `builder` for precise code generation (with lower temperature/`top_p`).
*   **Monitor Output Length**:  Ensure `max_output_tokens` is sufficient to prevent truncation.
* **Model Choice**: If available, experiment with different `model_name` options. More powerful models may yield better results, but may also have higher latency or resource requirements.

By carefully tuning these parameters, you can optimize the Seer's performance on ARC tasks, balancing the need for creative exploration with the requirement for accurate and executable code.
