from pathlib import Path

from rich.text import Text

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem, DataTable, Header, Footer
from textual import log
from textual.containers import (
    Horizontal,
    Vertical,
    Grid,
    ScrollableContainer,
)
from textual.binding import Binding

from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.session.level import Level  # Import Level

import json  # Import the json module


class SessionsScreen(Screen):
    CSS = """
    DataTable {height: 1fr;}
    Static {padding: 1; height: 3}
    Vertical {height: 100%;}
    """
    BINDINGS = [
        Binding("j", "move_down", "Cursor down", show=True),
        Binding("k", "move_up", "Cursor up", show=True),
        Binding("l", "select_row", "Select", show=True),
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, sessions_root: Path) -> None:
        super().__init__()
        self.sessions_root = sessions_root
        self.session_dirs = []  # Store sibling dirs here
        self.session_index = 0

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        # Add columns in the new requested order, changing DURATION to TIME
        self.table.add_columns(
            "SESSION",
            "TEST",                 # MOVED
            "TRAIN",                # MOVED
            "TASKS",                # MOVED
            "STEPS",
            "TIME",                 # CHANGED from DURATION
            Text("IN", justify="right"),
            Text("OUT", justify="right"),
            Text("TOTAL", justify="right"),
        )
        self.table.cursor_type = "row"
        yield Header()
        with Vertical():
            yield self.table
            yield Static("count:", id="summary")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Session Navigator"
        self.load_sessions()
        self.table.focus()
        self.update_summary()

    def load_sessions(self):
        self.session_dirs = sorted(
            [d for d in self.sessions_root.iterdir() if d.is_dir()]
        )
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

                train_passed = (
                    Text(str(summary.get("train_passed")), style="bold green", justify="center")
                    if summary.get("train_passed")
                    else Text("0", style="red", justify="center")
                )
                test_passed = (
                    Text(str(summary.get("test_passed")), style="bold green", justify="center")
                    if summary.get("test_passed")
                    else Text("0", style="red", justify="center")
                )

                # Add the row with arguments in the new order, using time_str
                self.table.add_row(
                    session_dir.name,    # SESSION
                    test_passed,         # TEST
                    train_passed,        # TRAIN
                    num_tasks,           # TASKS
                    num_steps,           # STEPS
                    time_str,            # TIME (CHANGED from duration_str)
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
        summary_widget = self.query_one("#summary", Static) # Corrected query_one usage
        num_sessions = 0
        train_passed_count = 0
        test_passed_count = 0
        total_steps = 0  # Add total_steps for summary
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
                    if session_summary.get("train_passed"):
                        train_passed_count += 1
                    if session_summary.get("test_passed"):
                        test_passed_count += 1
                    total_steps += session_summary.get("total_steps", 0)  # Accumulate steps

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
                    pass

        # Update summary string to include token totals
        summary_widget.update(
            f"sessions: {num_sessions}, train ✔: {train_passed_count}, test ✔: {test_passed_count}, steps: {total_steps} | "
            f"Tokens: IN={grand_total_prompt_tokens}, OUT={grand_total_candidates_tokens}, TOTAL={grand_total_tokens_all_sessions}"
        )


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
        row = self.table.get_row_at(row_id)
        session_name = row[0] # Session name is still the first column
        session_path = self.sessions_root / session_name

        # Get task directories for the selected session
        task_dirs = sorted([d for d in session_path.iterdir() if d.is_dir()])

        self.app.push_screen(SessionScreen(session_path, task_dirs))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
