from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem, DataTable, Header, Footer
from textual.containers import (
    Horizontal,
    Vertical,
    Grid,
    ScrollableContainer,
)
from textual.binding import Binding

from pathlib import Path


class TaskScreen(Screen):
    BINDINGS = [
        Binding("l", "select_row", "Select", show=False),
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
    ]

    def __init__(self, session_key: str, task_key: str) -> None:
        super().__init__()
        self.session_key = session_key
        self.task_key = task_key
        self.current_task = self.app.sessions[session_key][task_key]

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("prompt", "response", "matches")
        yield Header()
        with Vertical():
            yield self.table
            yield Static(id="summary")
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"{self.session_key } • {self.task_key}"
        for file in self.current_task:
            self.table.add_row(file.name)

        self.table.cursor_type = "row"
        self.table.focus()

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#summary")
        num_files = len(self.current_task)
        summary.update(f"Files in {self.task_key}: {num_files}")

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        selected_file = row[0]
        #  self.app.push_screen(SessionScreen(session_path))

