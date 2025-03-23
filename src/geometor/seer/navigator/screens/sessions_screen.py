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
        self.table.add_column("SESSION")
        self.table.add_column("TASKS")
        self.table.add_column("TRAIN")
        self.table.add_column("TEST")
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

                self.table.add_row(session_dir.name, num_tasks, train_passed, test_passed)
            except FileNotFoundError:
                self.table.add_row(session_dir.name, "-", "-", "-")  # Use "-" for missing summary
            except json.JSONDecodeError:
                self.table.add_row(session_dir.name, "-", "-", "-")  # Use "-" for invalid JSON
        if self.session_dirs:
            self.select_session_by_index(self.session_index)

    def update_summary(self):
        summary = self.query_one("#summary", Static)
        num_sessions = 0
        train_passed_count = 0
        test_passed_count = 0

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
                except (FileNotFoundError, json.JSONDecodeError):
                    pass

        summary.update(
            f"sessions: {num_sessions}, train ✔: {train_passed_count}, test ✔: {test_passed_count}"
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
        session_name = row[0]
        session_path = self.sessions_root / session_name

        # Get task directories for the selected session
        task_dirs = sorted([d for d in session_path.iterdir() if d.is_dir()])

        self.app.push_screen(SessionScreen(session_path, task_dirs))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
