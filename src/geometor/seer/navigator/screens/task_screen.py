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
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, session_path: Path, task_path: Path, step_dirs: list[Path]) -> None:
        super().__init__()
        self.session_path = session_path
        self.task_path = task_path
        self.step_dirs = step_dirs  # Receive step_dirs
        self.step_index = 0

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
        self.table.clear()  # Clear before adding
        for step_dir in self.step_dirs:  # Use self.step_dirs
            if step_dir.is_dir():
                num_files = sum(1 for _ in step_dir.iterdir())
                self.table.add_row(step_dir.name, num_files, "-")
        if self.step_dirs:
            self.select_step_by_index(self.step_index)

    def update_summary(self):
        summary = self.query_one("#summary")
        num_steps = len(self.step_dirs)  # Use len(self.step_dirs)
        summary.update(f"steps: {num_steps}")

    def select_step_by_index(self, index: int) -> None:
        if self.step_dirs:
            self.step_index = index
            self.table.move_cursor(row=index)

    def previous_sibling(self):
        if self.step_dirs:
            self.select_step_by_index((self.step_index - 1) % len(self.step_dirs))

    def next_sibling(self):
        if self.step_dirs:
            self.select_step_by_index((self.step_index + 1) % len(self.step_dirs))

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)
        self.step_index = self.table.cursor_row  # Update index

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)
        self.step_index = self.table.cursor_row  # Update index

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        key = row[0]
        # TODO: implement StepScreen
        # self.app.push_screen(StepScreen(key))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # kept for compatibility
        self.action_select_row()
