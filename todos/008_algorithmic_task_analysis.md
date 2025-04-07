# Task: Algorithmic Task Analysis for Initial Prompting

**Goal:** Develop methods to algorithmically analyze task input/output pairs during the initial investigation phase to extract structural information and relationships.

**Details:**
- Analyze the `train` pairs of a task to identify inherent properties and transformations *before* attempting code generation.
- Look for features such as:
    - Symmetries (rotational, reflectional) within grids or between input/output.
    - Repeating patterns or motifs.
    - Evidence of subdivisions or tiling.
    - Proportional relationships between input and output dimensions or content.
    - Consistent color transformations or mappings.
    - Object identification, counting, or tracking.
- The goal is to extract objective "facts" about the task's transformation rules.
- This extracted information should be incorporated into the initial prompts given to the LLM to provide a better starting point for code generation.
- This differs from Task 007 (Enhance LLM Feedback) which focuses on analyzing the *results* of a code trial for refinement, whereas this task focuses on analyzing the *problem definition* itself.

**Status:** To Do
