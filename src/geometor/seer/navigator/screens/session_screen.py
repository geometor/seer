import os
from pathlib import Path
from datetime import timedelta # Import timedelta

from rich.text import Text

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem, DataTable, Header, Footer
from textual import log # ADDED import
from textual.containers import (
    Horizontal,
    Vertical,
    Grid, # Import Grid
    ScrollableContainer,
)
from textual.binding import Binding
import json
import subprocess # ADDED import
import shutil # ADDED import

# Import Task to calculate weight
from geometor.seer.tasks.tasks import Task
from geometor.seer.navigator.screens.task_screen import TaskScreen
from geometor.seer.session.level import Level  # Import Level


class SessionScreen(Screen):
    CSS = """
    Screen > Vertical {
        grid-size: 2;
        grid-rows: auto 1fr; /* Summary auto height, table takes rest */
    }
    #summary-grid {
        grid-size: 3; /* Three columns for the summary tables */
        grid-gutter: 1 2;
        height: auto; /* Let the grid determine its height */
        padding: 0 1; /* Add some horizontal padding */
        margin-bottom: 1; /* Space below summary */
    }
    .summary-table {
        height: auto; /* Fit content height */
        border: none; /* No border for summary tables */
    }
    /* Ensure no focus border on summary tables */
    .summary-table:focus {
        border: none;
    }
    DataTable { /* Style for the main tasks table */
        height: 1fr;
    }
    Vertical {height: 100%;}
    """
    BINDINGS = [
        Binding("l,enter", "select_row", "Select", show=False), # ADDED enter key
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
        Binding("i", "view_images", "View Images", show=True), # ADDED binding
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, session_path: Path, task_dirs: list[Path]) -> None:
        super().__init__()
        self.session_path = session_path
        self.task_dirs = task_dirs  # Receive task_dirs
        self.task_index = 0
        self._sxiv_checked = False # ADDED sxiv check state
        self._sxiv_path = None     # ADDED sxiv path cache

    # ADDED sxiv check method
    def _check_sxiv(self) -> str | None:
        """Check if sxiv exists and cache the path."""
        if not self._sxiv_checked:
            self._sxiv_path = shutil.which("sxiv")
            self._sxiv_checked = True
            if not self._sxiv_path:
                log.warning("'sxiv' command not found in PATH. Cannot open images externally.")
                self.app.notify("sxiv not found. Cannot open images.", severity="warning", timeout=5)
        return self._sxiv_path

    def compose(self) -> ComposeResult:
        self.table = DataTable() # Main tasks table
        # Add columns in the new requested order, including ERROR
        self.table.add_columns(
            "TASKS",
            Text("ERROR", justify="center"), # ADDED ERROR column
            "TEST",
            "TRAIN",
            Text("SCORE", justify="right"), # Renamed from BEST SCORE
            Text("WEIGHT", justify="right"), # ADDED WEIGHT column
            "STEPS",
            "TIME",                 # CHANGED from DURATION
            Text("IN", justify="right"),
            Text("OUT", justify="right"),
            Text("TOTAL", justify="right"),
        )
        self.table.cursor_type = "row"

        yield Header()
        with Vertical():
            # Summary Grid with three DataTables
            with Grid(id="summary-grid"):
                yield DataTable(id="summary-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="trials-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="tokens-table", show_header=False, cursor_type=None, classes="summary-table")
            # Main tasks table
            yield self.table
        yield Footer()

    def on_mount(self) -> None:
        self.title = self.session_path.name
        self.table.cursor_type = "row"

        # Add columns to summary tables
        summary_table = self.query_one("#summary-table", DataTable)
        summary_table.add_columns("Metric", "Value", "Avg") # ADDED "Avg" column
        trials_table = self.query_one("#trials-table", DataTable)
        trials_table.add_columns("Metric", "Value", "±") # Changed % to ±
        tokens_table = self.query_one("#tokens-table", DataTable)
        tokens_table.add_columns("Metric", "Value")

        self.table.focus()
        self.update_tasks_list() # Load main table data
        self.update_summary() # Populate summary tables

    def update_tasks_list(self):
        """Loads data into the main tasks DataTable."""
        self.table.clear()  # Clear table before adding
        for task_dir in self.task_dirs:  # Use self.task_dirs
            summary_path = task_dir / "index.json"
            task_json_path = task_dir / "task.json" # Path to task.json
            try:
                # Load task summary
                with open(summary_path, "r") as f:
                    summary = json.load(f)

                # Load task data to calculate weight
                task_weight = "-" # Default weight
                if task_json_path.exists():
                    try:
                        with open(task_json_path, "r") as f_task:
                            task_data = json.load(f_task)
                        task_obj = Task(task_dir.name, task_data)
                        task_weight = Text(str(task_obj.weight), justify="right")
                    except (json.JSONDecodeError, Exception) as e_task:
                        log.error(f"Error loading or processing {task_json_path}: {e_task}")
                        task_weight = Text("ERR", justify="right", style="bold red") # Indicate error loading task data

                num_steps = Text(str(summary.get("steps", 0)), justify="right")

                # Use the updated _format_duration method
                time_str = (
                    Level._format_duration(summary.get("duration_seconds"))
                    if summary.get("duration_seconds") is not None
                    else "-"
                )

                # --- START ERROR HANDLING ---
                # Check if the task itself had errors during its processing/summarization
                task_errors = summary.get("errors", {})
                has_errors = task_errors.get("count", 0) > 0 # Check if error count > 0
                error_text = (
                    Text("⚠", style="bold yellow", justify="center")
                    if has_errors
                    else Text("-", justify="center")
                )
                # --- END ERROR HANDLING ---


                # --- START TOKEN HANDLING ---
                tokens_data = summary.get("tokens", {}) # Get the tokens dict, default to empty
                prompt_tokens = tokens_data.get("prompt_tokens")
                candidates_tokens = tokens_data.get("candidates_tokens")
                total_tokens = tokens_data.get("total_tokens")

                in_tokens_text = Text(str(prompt_tokens) if prompt_tokens is not None else "-", justify="right")
                out_tokens_text = Text(str(candidates_tokens) if candidates_tokens is not None else "-", justify="right")
                total_tokens_text = Text(str(total_tokens) if total_tokens is not None else "-", justify="right")
                # --- END TOKEN HANDLING ---

                # --- START PASS/FAIL HANDLING ---
                if "train_passed" in summary and summary["train_passed"] is not None:
                    train_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["train_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    # Default if key is missing or None (adjust style as needed)
                    train_passed = Text("-", style="", justify="center") # Changed default from ✔ to -

                if "test_passed" in summary and summary["test_passed"] is not None:
                    test_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["test_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    # Default if key is missing or None (adjust style as needed)
                    test_passed = Text("-", style="", justify="center") # Changed default from ✔ to -
                # --- END PASS/FAIL HANDLING ---

                # --- START SCORE HANDLING ---
                best_score_text = (
                    f"{summary.get('best_score'):.2f}"
                    if summary.get("best_score") is not None
                    else "-"
                )
                best_score_text = Text(best_score_text, justify="right")
                # --- END SCORE HANDLING ---

                # Add the row with arguments in the new order (10 columns total), using time_str
                self.table.add_row(
                    task_dir.name,       # TASKS
                    error_text,          # ERROR (ADDED)
                    test_passed,         # TEST
                    train_passed,        # TRAIN
                    best_score_text,     # SCORE
                    task_weight,         # WEIGHT (ADDED)
                    num_steps,           # STEPS
                    time_str,            # TIME (CHANGED from duration_str)
                    in_tokens_text,      # IN
                    out_tokens_text,     # OUT
                    total_tokens_text    # TOTAL
                )

            except FileNotFoundError:
                # Update exception handling for 11 columns (added WEIGHT)
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
            except json.JSONDecodeError:
                # Update exception handling for 11 columns (added WEIGHT)
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
            except Exception as e: # Catch other potential errors during loading
                log.error(f"Error processing task row for {task_dir.name}: {e}")
                # Update exception handling for 11 columns (added WEIGHT)
                self.table.add_row(task_dir.name, Text("ERR", style="bold red"), "-", "-", "-", "-", "-", "-", "-", "-", "-")

        if self.task_dirs:
            self.select_task_by_index(self.task_index)

    def update_summary(self):
        """Updates the three summary DataTables for the current session."""
        summary_table = self.query_one("#summary-table", DataTable)
        trials_table = self.query_one("#trials-table", DataTable)
        tokens_table = self.query_one("#tokens-table", DataTable)

        num_tasks = len(self.task_dirs)
        total_steps_count = 0
        train_passed_count = 0
        test_passed_count = 0
        error_count = 0
        total_duration_seconds = 0.0
        best_scores = []
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        total_weight = 0 # ADDED total weight counter

        for task_dir in self.task_dirs:
            summary_path = task_dir / "index.json"
            task_json_path = task_dir / "task.json" # Path to task.json
            try:
                with open(summary_path, "r") as f:
                    task_summary = json.load(f)

                total_steps_count += task_summary.get("steps", 0)
                if task_summary.get("train_passed"):
                    train_passed_count += 1
                if task_summary.get("test_passed"):
                    test_passed_count += 1
                if task_summary.get("errors", {}).get("count", 0) > 0:
                    error_count += 1

                duration = task_summary.get("duration_seconds")
                if duration is not None:
                    total_duration_seconds += duration

                score = task_summary.get("best_score")
                if score is not None:
                    best_scores.append(score)

                tokens_data = task_summary.get("tokens", {})
                prompt_tokens = tokens_data.get("prompt_tokens")
                candidates_tokens = tokens_data.get("candidates_tokens")
                total_tokens = tokens_data.get("total_tokens")

                if prompt_tokens is not None:
                    total_prompt_tokens += prompt_tokens
                if candidates_tokens is not None:
                    total_candidates_tokens += candidates_tokens
                if total_tokens is not None:
                    total_tokens_all_tasks += total_tokens

            except (FileNotFoundError, json.JSONDecodeError):
                pass # Skip tasks with missing/invalid index.json

        best_score_summary = (
            f"{min(best_scores):.2f}" if best_scores else "-"
        )
        formatted_total_duration = Level._format_duration(total_duration_seconds)

        # Calculate test percentage
        test_percent = (test_passed_count / num_tasks * 100) if num_tasks > 0 else 0.0
        test_percent_str = f"{test_percent:.1f}%"

        # --- START Calculate difference ---
        diff = test_passed_count - train_passed_count
        diff_str = f"{diff:+}" # Format with sign (+/-)
        # --- END Calculate difference ---

        # --- START Calculate average steps per task ---
        avg_steps_per_task = (total_steps_count / num_tasks) if num_tasks > 0 else 0.0
        avg_steps_str = f"{avg_steps_per_task:.1f} avg"
        # --- END Calculate average steps per task ---

        # Clear and update summary table (right-align keys and values)
        summary_table.clear()
        summary_table.add_row(
            Text("steps:", justify="right"),
            Text(str(total_steps_count), justify="right"),
            Text(avg_steps_str, justify="right") # ADDED average steps
        )
        summary_table.add_row(
            Text("time:", justify="right"),
            Text(formatted_total_duration, justify="right"),
            Text("") # Empty third column
        )
        summary_table.add_row(
            Text("best:", justify="right"),
            Text(best_score_summary, justify="right"),
            Text("") # Empty third column
        )
        summary_table.add_row( # ADDED total weight row
            Text("weight:", justify="right"),
            Text(f"{total_weight:,}", justify="right"),
            Text("") # Empty third column
        )

        # Clear and update trials table (right-align keys and values)
        trials_table.clear()
        summary_table.add_row(
            Text("tasks:", justify="right"),
            Text(str(num_tasks), justify="right"),
            Text("") # Empty third column
        )
        trials_table.add_row(
            Text("test:", justify="right"),
            Text(str(test_passed_count), justify="right"),
            Text(test_percent_str, justify="right") # Add percentage
        )
        trials_table.add_row(
            Text("train:", justify="right"),
            Text(str(train_passed_count), justify="right"),
            Text(diff_str, justify="right") # ADDED difference
        )
        trials_table.add_row(
            Text("errors:", justify="right"),
            Text(str(error_count), justify="right"),
            Text("") # Empty third column for errors
        )

        # Clear and update tokens table (right-align keys and values, format with commas)
        tokens_table.clear()
        tokens_table.add_row(Text("in:", justify="right"), Text(f"{total_prompt_tokens:,}", justify="right"))
        tokens_table.add_row(Text("out:", justify="right"), Text(f"{total_candidates_tokens:,}", justify="right"))
        tokens_table.add_row(Text("total:", justify="right"), Text(f"{total_tokens_all_tasks:,}", justify="right"))


    def select_task_by_index(self, index: int) -> None:
        if self.task_dirs:
            self.task_index = index
            self.table.move_cursor(row=index)

    def previous_sibling(self):
        if self.task_dirs:
            self.select_task_by_index((self.task_index - 1) % len(self.task_dirs))

    def next_sibling(self):
        if self.task_dirs:
            self.select_task_by_index((self.task_index + 1) % len(self.task_dirs))

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)
        self.task_index = self.table.cursor_row  # Update index

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)
        self.task_index = self.table.cursor_row  # Update index

    def action_select_row(self):
        row_id = self.table.cursor_row
        if row_id is None or not (0 <= row_id < len(self.task_dirs)): # Check index validity
            return
        row = self.table.get_row_at(row_id)
        task_name = row[0] # Get task name from the first column
        task_path = self.session_path / task_name

        # Get step directories for the selected task
        step_dirs = sorted([d for d in task_path.iterdir() if d.is_dir()])
        self.app.push_screen(TaskScreen(self.session_path, task_path, step_dirs))

    # ADDED action
    def action_view_images(self) -> None:
        """Find and open all PNG images in the current session directory using sxiv."""
        sxiv_cmd = self._check_sxiv()
        if not sxiv_cmd:
            return # sxiv not found, notification already shown

        try:
            # Find all .png files recursively within the session directory
            image_files = sorted(list(self.session_path.rglob("*.png")))

            if not image_files:
                self.app.notify("No PNG images found in this session.", severity="information")
                return

            # Prepare the command list
            command = [sxiv_cmd] + [str(img_path) for img_path in image_files]

            log.info(f"Opening {len(image_files)} images with sxiv from {self.session_path}")
            subprocess.Popen(command)

        except FileNotFoundError:
            log.error(f"'sxiv' command not found when trying to execute.")
            self.app.notify("sxiv not found. Cannot open images.", severity="error")
        except Exception as e:
            log.error(f"Error finding or opening images with sxiv from {self.session_path}: {e}")
            self.app.notify(f"Error viewing images: {e}", severity="error")

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
