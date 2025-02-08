
# Refactoring and Logging/Reporting Guidelines

Introduce a Session Object as a Single Source of Truth
- Implement a Session class or structure that holds all state, puzzle references, timestamps, and incremental results. The Session object will be the authoritative runtime record and can serialize its current state to disk at any point.

Incremental, Structured Logging
- After each interaction (prompt-response cycle or code execution), immediately write out a structured JSON file capturing:

Prompt text and metadata
- Response text and metadata
- Timing and token usage information
- Any intermediate grid states or images
- This ensures that even if an error interrupts the process, partial, structured logs remain.

Defer Index Generation
- Move index and summary generation (RST reports, aggregated metrics) to a separate pass that runs after all puzzle steps or after the session concludes. If a catastrophic failure occurs mid-session, you still have raw JSON logs from which you can generate a partial report.
- 
Structured Data Over Parsing
- Store key metrics—such as size correctness, pixel accuracy, and color differences—directly in JSON right after evaluation. Avoid reliance on regex or parsing RST files for metrics. This makes indexing scripts simpler and more robust.

Leverage Python’s Logging and Exception Handling
- Use Python’s built-in logging module for developer-facing runtime logs (info, warnings, errors) and structured JSON files for puzzle-solving details. On catastrophic errors, a top-level exception handler should:

Log the error.
- Force a session.save() call to ensure all current data is preserved.
- Flexible, Post-hoc Report Generation
By separating the raw data capture from report generation, you can:

Easily regenerate summaries and indexes from existing JSON logs without re-running the solver.
- Experiment with new reporting templates or metrics as needed without changing the puzzle-solving code.
- Validation and Testing
- Periodically test and validate JSON logs to ensure integrity. Keeping data well-structured and validated helps ensure that the indexing scripts can reliably produce final reports, even if a run was interrupted.
