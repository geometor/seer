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
import json

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

    def __init__(self, session_path: Path) -> None:  # Accept Path
        super().__init__()
        self.session_path = session_path  # Store Path

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("TASKS", "STEPS", "TRAIN", "TEST")
        yield Header()
        with Vertical():
            yield self.table
            yield Static(id="summary")
        yield Footer()

    def on_mount(self) -> None:
        self.title = self.session_path.name
        self.table.cursor_type = "row"
        self.table.focus()
        self.update_tasks_list()

    def update_tasks_list(self):
        for task_dir in sorted(self.session_path.iterdir()):
            if task_dir.is_dir():
                summary_path = task_dir / "task_summary.json"
                try:
                    with open(summary_path, "r") as f:
                        summary = json.load(f)

                    num_steps = Text(str(summary.get("num_steps", 0)), justify="right")
                    train_passed = (
                        Text("✔", style="green", justify="center")
                        if summary.get("train_passed")
                        else Text("✘", style="red", justify="center")
                    )
                    test_passed = (
                        Text("✔", style="green", justify="center")
                        if summary.get("test_passed")
                        else Text("✘", style="red", justify="center")
                    )
                    self.table.add_row(task_dir.name, num_steps, train_passed, test_passed)

                except FileNotFoundError:
                    self.table.add_row(task_dir.name, "Error: No summary", "-", "-")
                except json.JSONDecodeError:
                    self.table.add_row(task_dir.name, "Error: Invalid JSON", "-", "-")

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#summary", Static)
        num_tasks = sum(1 for _ in self.session_path.iterdir() if _.is_dir())
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
        task_name = row[0]
        task_path = self.session_path / task_name
        self.app.push_screen(TaskScreen(self.session_path, task_path))  # Pass Paths

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        task_name = row[0]
        task_path = self.session_path / task_name
        self.app.push_screen(TaskScreen(self.session_path, task_path))  # Pass Paths
