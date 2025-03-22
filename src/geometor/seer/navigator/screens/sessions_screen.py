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

    def __init__(self) -> None:
        super().__init__()
        self.sessions = self.app.sessions

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
        for session_key, session in self.sessions.items():
            num_tasks = Text(str(len(session)), style="", justify="right")
            self.table.add_row(session_key, num_tasks)

        self.table.focus()

        self.update_summary()

    def update_summary(self):
        summary = self.query_one("#summary", Static)
        num_sessions = len(self.sessions)  # Use the length of the sessions list
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
        session_key = row[0]
        self.app.push_screen(SessionScreen(session_key))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        session_key = row[0]
        self.app.push_screen(SessionScreen(session_key))
