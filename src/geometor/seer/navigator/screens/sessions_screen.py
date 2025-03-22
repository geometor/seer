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
    ]

    def __init__(self, sessions_root: Path) -> None: # Accept Path
        super().__init__()
        self.sessions_root = sessions_root  # Store Path

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
        for session_dir in sorted(self.sessions_root.iterdir()):
            if session_dir.is_dir():
                summary_path = session_dir / "session_summary.json"
                try:
                    with open(summary_path, 'r') as f:
                        summary = json.load(f)
                    num_tasks = Text(str(summary.get("num_tasks", 0)), style="", justify="right")
                    train_passed = Text(str(summary.get("train_passed", 0)), style="", justify="right")
                    test_passed = Text(str(summary.get("test_passed", 0)), style="", justify="right")
                    self.table.add_row(session_dir.name, num_tasks, train_passed, test_passed)
                except FileNotFoundError:
                    self.table.add_row(session_dir.name, "Error: No summary", "-", "-")
                except json.JSONDecodeError:
                    self.table.add_row(session_dir.name, "Error: Invalid JSON", "-", "-")


    def update_summary(self):
        summary = self.query_one("#summary", Static)
        num_sessions = sum(1 for _ in self.sessions_root.iterdir() if _.is_dir())
        summary.update(f"count: {num_sessions}")

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        session_name = row[0]
        session_path = self.sessions_root / session_name
        self.app.push_screen(SessionScreen(session_path)) # Pass Path

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        session_name = row[0]
        session_path = self.sessions_root / session_name
        self.app.push_screen(SessionScreen(session_path)) # Pass Path
