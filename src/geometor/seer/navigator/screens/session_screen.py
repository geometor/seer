import os
from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem, DataTable
from textual import log  
from textual.containers import Horizontal, Vertical, Grid, ScrollableContainer # Import Grid
from textual.binding import Binding

from geometor.seer.navigator.screens.task_screen import TaskScreen  # Import TaskScreen


class SessionScreen(Screen):
    BINDINGS = [
        Binding("l", "select_row", "Select", show=False),
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
    ]

    def __init__(self, session_path: Path) -> None:
        super().__init__()
        self.session_path = session_path  # Now directly a Path object
        #  self.navigator = navigator

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("tasks", "match", "prompts")
        with Vertical():
            yield self.table
            yield Static(id="session_summary")

    def on_mount(self) -> None:
        self.update_tasks_list()

    
    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        selected_session = row[0]
        session_path = self.app.sessions_root / selected_session
        self.app.push_screen(Task(session_path))

    def update_tasks_list(self):

        self.table.cursor_type = "row"
        self.table.focus()

        self.update_summary()

        if not self.session_path.exists():
            print(f"Error: Session directory not found: {self.session_path}")
            self.update_summary()  # Update summary with 0 tasks
            return

        try:
            for task_dir in self.session_path.iterdir():
                if task_dir.is_dir():
                    self.table.add_row(task_dir.name)

        except FileNotFoundError:
            print(f"Error: Session directory not found during iteration: {self.session_path}")
            #  You could also display a Textual notification here.

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#session_summary", Static)
        num_tasks = self.table.rows
        summary.update(f"Tasks in {self.session_path.name}: {num_tasks}")

    def on_list_view_selected(self, event) -> None:
        """Handles task selection."""
        selected_task_id = event.item.id.removeprefix("task-")
        selected_task_path = self.session_path / selected_task_id
        self.navigator.push_screen(TaskScreen(selected_task_path, self.navigator))
