# Task: Refactor Seer for Swappable Workflow Engine

**Goal:** Refactor the `Seer` class to decouple the core orchestration logic from the specific workflow/strategy being executed. This will allow different workflow engines (implementing different strategies or scenarios) to be plugged into the `Seer`.

**Details:**
- Define an abstract base class or interface for a "Workflow Engine".
- Modify the `Seer` class to accept an instance of a Workflow Engine during initialization or via a setter method.
- Delegate the step-by-step execution logic (currently within `Seer.run`) to the provided Workflow Engine instance.
- Ensure the existing workflow logic is encapsulated within a default Workflow Engine implementation.
- Refer to the write-up in the `research/` folder regarding alternate workflow designs.

**Status:** To Do
