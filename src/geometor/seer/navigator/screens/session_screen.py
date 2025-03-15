import os
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

from geometor.seer.navigator.screens.task_screen import TaskScreen  


class SessionScreen(Screen):
    CSS = """
    DataTable {height: 1fr;}
    Static {padding: 1; height: 3}
    Vertical {height: 100%;}
    """
    BINDINGS = [
        Binding("l", "select_row", "Select", show=False),
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
    ]

    def __init__(self, session_key: str) -> None:
        super().__init__()
        self.session_key = session_key
        self.session = self.app.sessions[session_key]

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("TASKS", "MATCH", "STEPS")
        yield Header()
        with Vertical():
            yield self.table
            yield Static(id="summary")
        yield Footer()

    def on_mount(self) -> None:
        self.title = self.session_key
        self.table.cursor_type = "row"
        self.table.focus()
        self.update_tasks_list()

    def update_tasks_list(self):
        if not self.session:
            print(f"Error: Session directory not found: {self.session_path}")
            self.update_summary()  # Update summary with 0 tasks
            return

        for task_key, task in self.session.items():
            #TODO: determine if there is match in task
            num_steps = Text(
                str(len(task)), justify="right"
            )
            self.table.add_row(task_key, 0, num_steps)

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#summary", Static)
        num_tasks = len(self.session)
        summary.update(f"count: {num_tasks}")

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        task_key = row[0]
        self.app.push_screen(TaskScreen(self.session_key, task_key))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        task_key = row[0]
        self.app.push_screen(TaskScreen(self.session_key, task_key))

