# Standard library imports
from __future__ import annotations
from pathlib import Path
import json
from datetime import datetime
import traceback # Import traceback for detailed error logging

# Local application/library specific imports
from geometor.seer.config import Config # Import the new Config class
from geometor.seer.session.level import Level
# Avoid circular import if SessionTask imports Session
# from geometor.seer.session.session_task import SessionTask


class Session(Level):
    # Change type hint from dict to Config
    def __init__(self, config: Config, output_dir: Path, description: str):
        """
        Initializes a new session.

        Args:
            config: The loaded Config object.
            output_dir: The root directory where session data will be saved.
            description: A user-provided description for this session.
        """
        self.config = config # Store the Config object
        self.description = description
        self.tasks = {} # Dictionary to hold SessionTask objects, keyed by task ID
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%y.%j.%H%M")
        super().__init__(None, output_dir / timestamp)

        try:
            self._write_context_files()
        except Exception as e:
            # Log error during context file writing but continue session initialization
            error_context = "Error during initial context file writing"
            print(f"ERROR ({self.name}): {error_context} - {e}")
            # Use traceback for detailed logging if available
            detailed_error = f"{error_context}\n{traceback.format_exc()}"
            # Assuming Level has log_error or similar
            # self.log_error(e, detailed_error) # Log the detailed error

        print(f"Session started: {timestamp}") # More informative message

    def summarize(self):
        """Generates and saves a summary of the session."""
        summary = super().summarize() # Get base summary (errors, duration)
        summary["description"] = self.description
        summary["task_count"] = len(self.tasks)
        summary["train_passed_count"] = self.train_passed_count  # Use count property
        summary["test_passed_count"] = self.test_passed_count    # Use count property
        summary["test_passed"] = self.test_passed_count    # Use count property

        # Aggregate trial counts and tokens from each SessionTask
        # task_trials = {} # REMOVED
        total_steps = 0  # Initialize total steps
        # --- START ADDED TOKEN COUNTERS ---
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        # --- END ADDED TOKEN COUNTERS ---
        total_error_count = summary["errors"]["count"] # Start with session's own errors

        for task_id, session_task in self.tasks.items():
            # Access summary information directly from session_task
            total_steps += len(session_task.steps)  # Use len(steps)
            # REMOVED task_trials aggregation
            # task_trials[task_id] = {
            #     "train": session_task.trials.get("train", {}).get("total", 0),
            #     "test": session_task.trials.get("test", {}).get("total", 0),
            # }

            # --- START ADDED TOKEN AGGREGATION ---
            # Read from the task's index.json for robustness
            task_summary_path = session_task.dir / "index.json"
            try:
                # Ensure the task summary exists before trying to read it
                # This assumes task.summarize() is called before session.summarize()
                if task_summary_path.exists():
                    with open(task_summary_path, "r") as f:
                        task_summary = json.load(f)

                    tokens_data = task_summary.get("tokens", {}) # Get tokens dict
                    prompt_tokens = tokens_data.get("prompt_tokens")
                    candidates_tokens = tokens_data.get("candidates_tokens")
                    total_tokens = tokens_data.get("total_tokens")

                    if prompt_tokens is not None:
                        total_prompt_tokens += prompt_tokens
                    if candidates_tokens is not None:
                        total_candidates_tokens += candidates_tokens
                    if total_tokens is not None:
                        total_tokens_all_tasks += total_tokens
                else:
                    # Log a warning if the task summary is missing
                    # TODO: Implement self.log_warning or use a proper logger
                    print(f"    WARNING (Session {self.name}): Task summary file not found for token aggregation: {task_summary_path}")

                # --- START ADDED ERROR AGGREGATION ---
                task_errors_data = task_summary.get("errors", {}) # Get errors dict, default empty
                total_error_count += task_errors_data.get("count", 0) # Add task's error count
                # --- END ADDED ERROR AGGREGATION ---

            except (json.JSONDecodeError, TypeError) as e:
                 # Log or handle error if task summary isn't valid JSON or structure is wrong
                 # TODO: Implement self.log_error or use a proper logger
                 print(f"    ERROR (Session {self.name}): Error reading task summary for token aggregation: {session_task.name} - {e}")
            except Exception as e:
                 # Catch any other unexpected errors during file reading
                 # TODO: Implement self.log_error or use a proper logger
                 print(f"    ERROR (Session {self.name}): Unexpected error reading task summary for token aggregation: {session_task.name} - {e}")
            # --- END ADDED TOKEN AGGREGATION ---


        # summary["task_trials"] = task_trials # REMOVED
        summary["total_steps"] = total_steps  # Add total_steps to the summary

        # --- START ADDED TOKENS TO SUMMARY ---
        summary["tokens"] = {
            "prompt_tokens": total_prompt_tokens,
            "candidates_tokens": total_candidates_tokens,
            "total_tokens": total_tokens_all_tasks,
        }
        # --- END ADDED TOKENS TO SUMMARY ---
        summary["errors"]["count"] = total_error_count # Update with aggregated count

        # Save the summary
        self._write_to_json("index.json", summary)
        print(f"Session summary generated: {self.dir / 'index.json'}") # Confirmation message

    def add_task(self, task):
        """Adds a new task to the session."""
        # Import locally to prevent circular dependency issues at module level
        from geometor.seer.session.session_task import SessionTask

        session_task = SessionTask(self, task) # Pass self (Session instance) and task
        self.tasks[task.id] = session_task
        return session_task

    def _write_context_files(self):
        """
        Writes copies of the configuration and context files used for this session
        into the session directory for reference.
        """
        # Write system context for each role
        try:
            # Access roles and their pre-loaded content via the Config object
            for role_name, role_config in self.config.roles.items():
                system_context_content = role_config.get("system_context_content")
                if system_context_content is not None:
                    file_path = self.dir / f"{role_name}_system_context.md"
                    file_path.write_text(system_context_content, encoding='utf-8')
                else:
                    # Log warning if content is missing but expected
                    print(f"Warning (Session {self.name}): No system context content found for role '{role_name}' to write.")
        except (IOError, PermissionError, Exception) as e:
            # Log error more robustly
            error_context = "Error writing system context files"
            print(f"ERROR ({self.name}): {error_context} - {e}")
            # self.log_error(e, f"{error_context}\n{traceback.format_exc()}")


        # Write the original config data (or a filtered version) as JSON
        try:
            config_data_to_write = self.config.data # Get the dictionary representation
            file_path = self.dir / "config.json"
            with open(file_path, "w", encoding='utf-8') as f:
                # Use default=str to handle non-serializable types like Path
                json.dump(config_data_to_write, f, indent=2, default=str)
        except (IOError, PermissionError, TypeError, Exception) as e:
            error_context = "Error writing config.json"
            print(f"ERROR ({self.name}): {error_context} - {e}")
            # self.log_error(e, f"{error_context}\n{traceback.format_exc()}")


        # Write the task context content
        try:
            # Access pre-loaded task context content
            task_context_content = self.config.task_context
            if task_context_content: # Only write if not empty
                file_path = self.dir / "task_context.md"
                file_path.write_text(task_context_content, encoding='utf-8')
            else:
                print(f"Warning (Session {self.name}): No task context content found to write.")
        except (IOError, PermissionError, Exception) as e:
            error_context = "Error writing task_context.md"
            print(f"ERROR ({self.name}): {error_context} - {e}")
            # self.log_error(e, f"{error_context}\n{traceback.format_exc()}")


    @property
    def train_passed(self):
        """Checks if any task in the session passed the training set."""
        return any(task.train_passed for task in self.tasks.values())

    @property
    def test_passed(self):
        return any(task.test_passed for task in self.tasks.values())

    @property
    def train_passed_count(self):
        return sum(1 for task in self.tasks.values() if task.train_passed)

    @property
    def test_passed_count(self):
        return sum(1 for task in self.tasks.values() if task.test_passed)
