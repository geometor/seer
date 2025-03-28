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
import subprocess # ADDED import
import shutil # ADDED import

from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.session.level import Level  # Import Level

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
        Binding("i", "view_images", "View Images", show=True), # ADDED binding
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, sessions_root: Path) -> None:
        super().__init__()
        self.sessions_root = sessions_root
        self.session_dirs = []  # Store sibling dirs here
        self.session_index = 0
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
        self.table = DataTable() # Main sessions table
        # Add columns in the new requested order, changing DURATION to TIME
        # Right-align TEST, TRAIN, TIME headers
        self.table.add_columns(
            "SESSION",
            Text("TEST", justify="right"),                 # MOVED & ALIGNED
            Text("TRAIN", justify="right"),                # MOVED & ALIGNED
            "TASKS",                                       # MOVED
            "STEPS",
            Text("TIME", justify="right"),                 # CHANGED from DURATION & ALIGNED
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
            # Main sessions table
            yield self.table
        yield Footer()

    def on_mount(self) -> None:
        self.title = "SEER Navigator"
        self.sub_title = str(self.sessions_root)

        # Add columns to summary tables
        summary_table = self.query_one("#summary-table", DataTable)
        summary_table.add_columns("Metric", "Value")
        trials_table = self.query_one("#trials-table", DataTable)
        trials_table.add_columns("Metric", "Value")
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

                # Add the row with arguments in the new order, using time_str
                self.table.add_row(
                    session_dir.name,    # SESSION
                    test_passed,         # TEST
                    train_passed,        # TRAIN
                    num_tasks,           # TASKS
                    num_steps,           # STEPS
                    time_str,            # TIME (column definition handles alignment)
                    in_tokens_text,      # IN
                    out_tokens_text,     # OUT
                    total_tokens_text    # TOTAL
                )
            except FileNotFoundError:
                # Update exception handling for 9 columns
                self.table.add_row(session_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")
            except json.JSONDecodeError:
                # Update exception handling for 9 columns
                self.table.add_row(session_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")
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
        total_error_count = 0 # New counter for errors
        # --- START ADDED TOKEN COUNTERS ---
        grand_total_prompt_tokens = 0
        grand_total_candidates_tokens = 0
        grand_total_tokens_all_sessions = 0
        # --- END ADDED TOKEN COUNTERS ---

        for session_dir in self.sessions_root.iterdir():  # Iterate over sessions_root
            if session_dir.is_dir():
                num_sessions += 1
                summary_path = session_dir / "index.json"
                try:
                    with open(summary_path, "r") as f:
                        session_summary = json.load(f)

                    total_tasks_count += session_summary.get("count", 0) # Sum tasks
                    train_passed_count += session_summary.get("train_passed", 0) # Sum train passed
                    test_passed_count += session_summary.get("test_passed", 0) # Sum test passed
                    total_steps += session_summary.get("total_steps", 0)  # Accumulate steps
                    total_error_count += session_summary.get("errors", {}).get("count", 0) # Sum errors

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

                except (FileNotFoundError, json.JSONDecodeError):
                    pass # Skip sessions with missing/invalid index.json

        # Format total duration
        formatted_total_duration = Level._format_duration(total_duration_seconds)

        # Clear and update summary table (right-align keys and values)
        summary_table.clear()
        summary_table.add_row(Text("sessions:", justify="right"), Text(str(num_sessions), justify="right"))
        summary_table.add_row(Text("tasks:", justify="right"), Text(str(total_tasks_count), justify="right"))
        summary_table.add_row(Text("steps:", justify="right"), Text(str(total_steps), justify="right"))
        summary_table.add_row(Text("time:", justify="right"), Text(formatted_total_duration, justify="right"))

        # Clear and update trials table (right-align keys and values)
        trials_table.clear()
        trials_table.add_row(Text("test:", justify="right"), Text(str(test_passed_count), justify="right"))
        trials_table.add_row(Text("train:", justify="right"), Text(str(train_passed_count), justify="right"))
        trials_table.add_row(Text("errors:", justify="right"), Text(str(total_error_count), justify="right"))

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

    # ADDED action
    def action_view_images(self) -> None:
        """Find and open all PNG images in the sessions root directory using sxiv."""
        sxiv_cmd = self._check_sxiv()
        if not sxiv_cmd:
            return # sxiv not found, notification already shown

        try:
            # Find all .png files recursively within the sessions root directory
            image_files = sorted(list(self.sessions_root.rglob("*.png")))

            if not image_files:
                self.app.notify("No PNG images found in sessions root.", severity="information")
                return

            # Prepare the command list
            command = [sxiv_cmd] + [str(img_path) for img_path in image_files]

            log.info(f"Opening {len(image_files)} images with sxiv from {self.sessions_root}")
            subprocess.Popen(command)

        except FileNotFoundError:
            log.error(f"'sxiv' command not found when trying to execute.")
            self.app.notify("sxiv not found. Cannot open images.", severity="error")
        except Exception as e:
            log.error(f"Error finding or opening images with sxiv from {self.sessions_root}: {e}")
            self.app.notify(f"Error viewing images: {e}", severity="error")

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
