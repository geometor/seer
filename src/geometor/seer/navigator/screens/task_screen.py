from rich.text import Text

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
import json


class TaskScreen(Screen):
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

    def __init__(self, session_path: Path, task_path: Path) -> None:  # Accept Paths
        super().__init__()
        self.session_path = session_path  # Store Paths
        self.task_path = task_path

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("STEP", "FILES", "MATCHES")
        yield Header()
        with Vertical():
            yield self.table
            yield Static(id="summary")
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"{self.session_path.name} • {self.task_path.name}"
        self.load_steps()
        self.table.cursor_type = "row"
        self.table.focus()
        self.update_summary()

    def load_steps(self):
        self.app.step_dirs = sorted(
            [d for d in self.task_path.iterdir() if d.is_dir()]
        )
        self.app.step_index = 0
        for step_dir in sorted(self.task_path.iterdir()):
            if step_dir.is_dir():
                num_files = sum(1 for _ in step_dir.iterdir())
                # TODO: check for matches
                self.table.add_row(step_dir.name, num_files, "-")
        if self.app.step_dirs:
            self.select_step_by_index(self.app.step_index)

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#summary")
        num_steps = sum(1 for _ in self.task_path.iterdir() if _.is_dir())
        summary.update(f"steps: {num_steps}")

    def select_step_by_index(self, index: int) -> None:
        """Selects a step by its index in the sorted list."""
        if self.app.step_dirs:
            self.table.move_cursor(row=index)


    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)
        self.app.step_index = self.table.cursor_row

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)
        self.app.step_index = self.table.cursor_row

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        key = row[0]
        # TODO: implement StepScreen
        # self.app.push_screen(StepScreen(key))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        selected_file = row[0]
        #  self.app.push_screen(SessionScreen(session_path))
