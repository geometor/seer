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
from geometor.seer.session.level import Level  # Import Level


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
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, session_path: Path, task_dirs: list[Path]) -> None:
        super().__init__()
        self.session_path = session_path
        self.task_dirs = task_dirs  # Receive task_dirs
        self.task_index = 0

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        # Add columns, setting justify="right" for "BEST SCORE"
        self.table.add_columns(
            "TASKS", "STEPS", "DURATION", "TRAIN", "TEST", ("BEST SCORE", {"justify": "right"})
        )
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
        self.table.clear()  # Clear table before adding
        for task_dir in self.task_dirs:  # Use self.task_dirs
            summary_path = task_dir / "index.json"
            try:
                with open(summary_path, "r") as f:
                    summary = json.load(f)

                num_steps = Text(str(summary.get("steps", 0)), justify="right")

                duration_str = (
                    Level._format_duration(summary.get("duration_seconds"))
                    if summary.get("duration_seconds") is not None
                    else "-"
                )

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
                best_score_text = (  # Handle potential None
                    f"{summary.get('best_score'):.2f}"
                    if summary.get("best_score") is not None
                    else "-"
                )
                # Add the row, with best_score_text already a string
                self.table.add_row(task_dir.name, num_steps, duration_str, train_passed, test_passed, best_score_text)

            except FileNotFoundError:
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-")  # Use "-"
            except json.JSONDecodeError:
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-")  # Use "-"
        if self.task_dirs:
            self.select_task_by_index(self.task_index)

        self.update_summary()

    def update_summary(self):
        summary_widget = self.query_one("#summary", Static)
        num_tasks = len(self.task_dirs)
        train_passed_count = 0
        test_passed_count = 0
        best_scores = []

        for task_dir in self.task_dirs:
            summary_path = task_dir / "index.json"
            try:
                with open(summary_path, "r") as f:
                    task_summary = json.load(f)
                if task_summary.get("train_passed"):
                    train_passed_count += 1
                if task_summary.get("test_passed"):
                    test_passed_count += 1
                score = task_summary.get("best_score")
                if score is not None:
                    best_scores.append(score)
            except (FileNotFoundError, json.JSONDecodeError):
                pass

        best_score_summary = (
            f"Best: {min(best_scores):.2f}" if best_scores else "Best: -"
        )  # Handle empty list

        summary_widget.update(
            f"Tasks: {num_tasks}, Train ✔: {train_passed_count}, Test ✔: {test_passed_count}, {best_score_summary}"
        )

    def select_task_by_index(self, index: int) -> None:
        if self.task_dirs:
            self.task_index = index
            self.table.move_cursor(row=index)

    def previous_sibling(self):
        if self.task_dirs:
            self.select_task_by_index((self.task_index - 1) % len(self.task_dirs))

    def next_sibling(self):
        if self.task_dirs:
            self.select_task_by_index((self.task_index + 1) % len(self.task_dirs))

    def action_move_up(self):
        row = self.table.cursor_row - 1
        self.table.move_cursor(row=row)
        self.task_index = self.table.cursor_row  # Update index

    def action_move_down(self):
        row = self.table.cursor_row + 1
        self.table.move_cursor(row=row)
        self.task_index = self.table.cursor_row  # Update index

    def action_select_row(self):
        row_id = self.table.cursor_row
        row = self.table.get_row_at(row_id)
        task_name = row[0]
        task_path = self.session_path / task_name

        # Get step directories for the selected task
        step_dirs = sorted([d for d in task_path.iterdir() if d.is_dir()])
        self.app.push_screen(TaskScreen(self.session_path, task_path, step_dirs))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
