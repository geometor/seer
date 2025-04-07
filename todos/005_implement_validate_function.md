# Task: Implement Generation of a `validate` Function

**Goal:** Investigate and potentially implement the generation of a `validate` function alongside the `transform` function during the LLM prompting process.

**Details:**
- Explore how the analysis phase could identify properties or rules that the output grid must satisfy.
- Modify the prompting strategy to request the LLM generate a `validate(input_grid, output_grid)` function based on these identified rules.
- Determine how this `validate` function would be used within the workflow (e.g., during trials, as a self-correction mechanism).
- Integrate the execution and results of the `validate` function into the trial reporting and scoring.
- Refer to existing write-ups and research on this concept.

**Status:** To Do
