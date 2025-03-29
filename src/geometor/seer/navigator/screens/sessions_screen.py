from pathlib import Path
from datetime import timedelta # Import timedelta for duration calculation

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
# REMOVED subprocess import
# REMOVED shutil import

from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.session.level import Level  # Import Level
from geometor.seer.tasks.tasks import Task # ADDED Task import for weight calculation

import json  # Import the json module


class SessionsScreen(Screen):
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
    DataTable { /* Style for the main sessions table */
        height: 1fr;
    }
    /* Keep old Static style for reference or remove if not needed */
    /* Static {padding: 1; height: 3} */
    Vertical {height: 100%;}
    """
    BINDINGS = [
        Binding("j", "move_down", "Cursor down", show=True),
        Binding("k", "move_up", "Cursor up", show=True),
        Binding("l,enter", "select_row", "Select", show=True), # ADDED enter key
        # REMOVED Binding("i", "view_images", "View Images", show=True),
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, sessions_root: Path) -> None:
        super().__init__()
        self.sessions_root = sessions_root
        self.session_dirs = []  # Store sibling dirs here
        self.session_index = 0
        # REMOVED sxiv check state attributes

    # REMOVED _check_sxiv method

    def compose(self) -> ComposeResult:
        self.table = DataTable() # Main sessions table
        # Add columns in the new requested order, changing DURATION to TIME
        # Right-align TEST, TRAIN, TIME, ERROR headers
        self.table.add_columns(
            "SESSION",
            Text("ERROR", justify="center"),               # ADDED & ALIGNED
            Text("TEST", justify="right"),                 # MOVED & ALIGNED
            Text("TRAIN", justify="right"),                # MOVED & ALIGNED
            "TASKS",                                       # MOVED
            "STEPS",
            Text("TIME", justify="right"),                 # CHANGED from DURATION & ALIGNED
            Text("IN", justify="right"),
            Text("OUT", justify="right"),
            Text("TOTAL", justify="right"),
            Text("WEIGHT", justify="right"), # ADDED WEIGHT column
            "DESC",                          # ADDED DESC column
        )
        self.table.cursor_type = "row"

        yield Header()
        with Vertical():
            # Summary Grid with three DataTables
            with Grid(id="summary-grid"):
                yield DataTable(id="summary-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="trials-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="tokens-table", show_header=False, cursor_type=None, classes="summary-table")
            # Main sessions table
            yield self.table
        yield Footer()

    def on_mount(self) -> None:
        self.title = "SEER Navigator"
        self.sub_title = str(self.sessions_root)

        # Add columns to summary tables
        summary_table = self.query_one("#summary-table", DataTable)
        summary_table.add_columns("Metric", "Value", "Avg") # ADDED "Avg" column
        trials_table = self.query_one("#trials-table", DataTable)
        trials_table.add_columns("Metric", "Value", "±") # Changed % to ±
        tokens_table = self.query_one("#tokens-table", DataTable)
        tokens_table.add_columns("Metric", "Value")

        self.load_sessions() # Load main table data
        self.table.focus()
        self.update_summary() # Populate summary tables

    def load_sessions(self):
        """Loads data into the main sessions DataTable."""
        self.session_dirs = [d for d in self.sessions_root.iterdir() if d.is_dir()]
        # Sort sessions by name (directory name)
        self.session_dirs = sorted(self.session_dirs, key=lambda d: d.name)
        self.session_index = 0
        self.table.clear() # Clear existing rows
        for session_dir in self.session_dirs:
            summary_path = session_dir / "index.json"
            try:
                with open(summary_path, 'r') as f:
                    summary = json.load(f)
                num_tasks = Text(str(summary.get("count", 0)), style="", justify="right")
                num_steps = Text(str(summary.get("total_steps", 0)), style="", justify="right") # Get total_steps

                # Use the updated _format_duration method
                time_str = (
                    Level._format_duration(summary.get("duration_seconds"))
                    if summary.get("duration_seconds") is not None
                    else "-"
                )

                # --- START ADDED ERROR HANDLING ---
                errors_data = summary.get("errors", {})
                error_count = errors_data.get("count", 0)
                error_text = (
                    Text(str(error_count), style="bold yellow", justify="center")
                    if error_count > 0
                    else Text("-", justify="center")
                )
                # --- END ADDED ERROR HANDLING ---

                # --- START ADDED TOKEN HANDLING ---
                tokens_data = summary.get("tokens", {}) # Get the tokens dict, default to empty
                prompt_tokens = tokens_data.get("prompt_tokens")
                candidates_tokens = tokens_data.get("candidates_tokens")
                total_tokens = tokens_data.get("total_tokens")

                in_tokens_text = Text(str(prompt_tokens) if prompt_tokens is not None else "-", justify="right")
                out_tokens_text = Text(str(candidates_tokens) if candidates_tokens is not None else "-", justify="right")
                total_tokens_text = Text(str(total_tokens) if total_tokens is not None else "-", justify="right")
                # --- END ADDED TOKEN HANDLING ---

                # Right-align TEST and TRAIN counts
                train_passed = (
                    Text(str(summary.get("train_passed")), style="bold green", justify="right") # ALIGNED right
                    if summary.get("train_passed")
                    else Text("0", style="red", justify="right") # ALIGNED right
                )
                test_passed = (
                    Text(str(summary.get("test_passed")), style="bold green", justify="right") # ALIGNED right
                    if summary.get("test_passed")
                    else Text("0", style="red", justify="right") # ALIGNED right
                )

                # --- START ADDED WEIGHT CALCULATION ---
                session_total_weight = 0
                try:
                    for item in session_dir.iterdir():
                        if item.is_dir(): # Check if it's a task directory
                            task_json_path = item / "task.json"
                            if task_json_path.exists():
                                try:
                                    with open(task_json_path, "r") as f_task:
                                        task_data = json.load(f_task)
                                    task_obj = Task(item.name, task_data)
                                    session_total_weight += task_obj.weight
                                except (json.JSONDecodeError, Exception) as e_task:
                                    log.error(f"Error loading/processing task {item.name} for weight: {e_task}")
                                    # Optionally mark weight as error? For now, just skip adding its weight.
                except Exception as e_session:
                    log.error(f"Error iterating tasks for weight in session {session_dir.name}: {e_session}")
                    # Indicate error in the weight column?
                    session_weight_text = Text("ERR", style="bold red", justify="right")
                else:
                    session_weight_text = Text(f"{session_total_weight:,}", justify="right") # Format with comma
                # --- END ADDED WEIGHT CALCULATION ---

                # --- START ADDED DESCRIPTION HANDLING ---
                description = summary.get("description", "-") # Get description or default
                # --- END ADDED DESCRIPTION HANDLING ---

                # Add the row with arguments in the new order, using time_str
                self.table.add_row(
                    session_dir.name,    # SESSION
                    error_text,          # ERROR (ADDED)
                    test_passed,         # TEST
                    train_passed,        # TRAIN
                    num_tasks,           # TASKS
                    num_steps,           # STEPS
                    time_str,            # TIME (column definition handles alignment)
                    in_tokens_text,      # IN
                    out_tokens_text,     # OUT
                    total_tokens_text,   # TOTAL
                    session_weight_text, # WEIGHT (ADDED)
                    description          # DESC (ADDED)
                )
            except FileNotFoundError:
                # Update exception handling for 12 columns
                self.table.add_row(session_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
            except json.JSONDecodeError:
                # Update exception handling for 12 columns
                self.table.add_row(session_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
        if self.session_dirs:
            self.select_session_by_index(self.session_index)

    def update_summary(self):
        """Updates the three summary DataTables."""
        summary_table = self.query_one("#summary-table", DataTable)
        trials_table = self.query_one("#trials-table", DataTable)
        tokens_table = self.query_one("#tokens-table", DataTable)

        num_sessions = 0
        total_tasks_count = 0 # New counter for total tasks
        train_passed_count = 0
        test_passed_count = 0
        total_steps = 0
        total_duration_seconds = 0.0 # New counter for total duration
        total_error_count = 0 # Initialize error counter
        # --- START ADDED TOKEN COUNTERS ---
        grand_total_prompt_tokens = 0
        grand_total_candidates_tokens = 0
        grand_total_tokens_all_sessions = 0
        # --- END ADDED TOKEN COUNTERS ---
        grand_total_weight = 0 # ADDED grand total weight counter

        for session_dir in self.sessions_root.iterdir():  # Iterate over sessions_root
            if session_dir.is_dir():
                num_sessions += 1
                summary_path = session_dir / "index.json"
                try:
                    with open(summary_path, "r") as f:
                        session_summary = json.load(f)

                    total_tasks_count += session_summary.get("count", 0) # Sum tasks
                    train_passed_count += session_summary.get("train_passed", 0)
                    test_passed_count += session_summary.get("test_passed", 0)
                    total_steps += session_summary.get("total_steps", 0)
                    total_error_count += session_summary.get("errors", {}).get("count", 0) # Accumulate errors

                    # Sum duration
                    duration = session_summary.get("duration_seconds")
                    if duration is not None:
                        total_duration_seconds += duration

                    # --- START ADDED TOKEN ACCUMULATION ---
                    tokens_data = session_summary.get("tokens", {})
                    prompt_tokens = tokens_data.get("prompt_tokens")
                    candidates_tokens = tokens_data.get("candidates_tokens")
                    total_tokens = tokens_data.get("total_tokens")

                    if prompt_tokens is not None:
                        grand_total_prompt_tokens += prompt_tokens
                    if candidates_tokens is not None:
                        grand_total_candidates_tokens += candidates_tokens
                    if total_tokens is not None:
                        grand_total_tokens_all_sessions += total_tokens
                    # --- END ADDED TOKEN ACCUMULATION ---

                    # --- START ADDED WEIGHT ACCUMULATION ---
                    try:
                        session_weight = 0
                        for item in session_dir.iterdir():
                            if item.is_dir():
                                task_json_path = item / "task.json"
                                if task_json_path.exists():
                                    try:
                                        with open(task_json_path, "r") as f_task:
                                            task_data = json.load(f_task)
                                        task_obj = Task(item.name, task_data)
                                        session_weight += task_obj.weight
                                    except (json.JSONDecodeError, Exception):
                                        # Error logged during row creation, ignore here for summary
                                        pass
                        grand_total_weight += session_weight
                    except Exception as e_weight_sum:
                        log.error(f"Error summing weight for session {session_dir.name} in summary: {e_weight_sum}")
                    # --- END ADDED WEIGHT ACCUMULATION ---


                except (FileNotFoundError, json.JSONDecodeError):
                    pass # Skip sessions with missing/invalid index.json

        # Format total duration
        formatted_total_duration = Level._format_duration(total_duration_seconds)

        # Calculate test percentage
        test_percent = (test_passed_count / total_tasks_count * 100) if total_tasks_count > 0 else 0.0 # Use total_tasks_count
        test_percent_str = f"{test_percent:.1f}%"

        # --- START Calculate difference ---
        diff = test_passed_count - train_passed_count
        diff_str = f"{diff:+}" # Format with sign (+/-)
        # --- END Calculate difference ---

        # --- START Calculate average steps per task ---
        avg_steps_per_task = (total_steps / total_tasks_count) if total_tasks_count > 0 else 0.0
        avg_steps_str = f"{avg_steps_per_task:.1f} avg"
        # --- END Calculate average steps per task ---

        # Clear and update summary table (right-align keys and values)
        summary_table.clear()
        summary_table.add_row(
            Text("sessions:", justify="right"),
            Text(str(num_sessions), justify="right"),
            Text("") # Empty third column
        )
        summary_table.add_row(
            Text("steps:", justify="right"),
            Text(str(total_steps), justify="right"),
            Text(avg_steps_str, justify="right") # ADDED average steps
        )
        summary_table.add_row(
            Text("time:", justify="right"),
            Text(formatted_total_duration, justify="right"),
            Text("") # Empty third column
        )
        summary_table.add_row( # ADDED total weight row
            Text("weight:", justify="right"),
            Text(f"{grand_total_weight:,}", justify="right"),
            Text("") # Empty third column
        )

        # Clear and update trials table (right-align keys and values)
        trials_table.clear()
        trials_table.add_row(
            Text("tasks:", justify="right"),
            Text(str(total_tasks_count), justify="right"),
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
            Text(str(total_error_count), justify="right"),
            Text("") # Empty third column for errors
        )

        # Clear and update tokens table (right-align keys and values, format with commas)
        tokens_table.clear()
        tokens_table.add_row(Text("in:", justify="right"), Text(f"{grand_total_prompt_tokens:,}", justify="right"))
        tokens_table.add_row(Text("out:", justify="right"), Text(f"{grand_total_candidates_tokens:,}", justify="right"))
        tokens_table.add_row(Text("total:", justify="right"), Text(f"{grand_total_tokens_all_sessions:,}", justify="right"))


    def select_session_by_index(self, index: int) -> None:
        if self.session_dirs:
            self.session_index = index
            self.table.move_cursor(row=index)

    def previous_sibling(self):
        if self.session_dirs:
            self.select_session_by_index((self.session_index - 1) % len(self.session_dirs))

    def next_sibling(self):
        if self.session_dirs:
            self.select_session_by_index((self.session_index + 1) % len(self.session_dirs))

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)
        self.session_index = self.table.cursor_row  # Update index

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)
        self.session_index = self.table.cursor_row  # Update index

    def action_select_row(self):
        row_id = self.table.cursor_row
        if row_id is None or not (0 <= row_id < len(self.session_dirs)): # Check index validity
            return
        row = self.table.get_row_at(row_id)
        session_name = row[0] # Session name is still the first column
        session_path = self.sessions_root / session_name

        # Get task directories for the selected session
        task_dirs = sorted([d for d in session_path.iterdir() if d.is_dir()]) # Sort tasks

        self.app.push_screen(SessionScreen(session_path, task_dirs))

    # REMOVED action_view_images method

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()

    def refresh_content(self) -> None:
        """Reloads session data and updates the screen."""
        log.info("Refreshing SessionsScreen content...")
        # Store current cursor position
        current_cursor_row = self.table.cursor_row

        self.load_sessions() # Reloads table data
        self.update_summary() # Reloads summary data

        # Restore cursor position if possible
        if current_cursor_row is not None and 0 <= current_cursor_row < self.table.row_count:
            self.table.move_cursor(row=current_cursor_row, animate=False)
        elif self.table.row_count > 0:
            self.table.move_cursor(row=0, animate=False) # Move to top if previous row is gone

        self.table.focus() # Ensure table has focus
