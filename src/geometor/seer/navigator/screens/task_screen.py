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

from geometor.seer.session.level import Level  # Import Level


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
        # Add columns, setting justify="right" for "BEST SCORE"
        self.table.add_columns(
            "STEP", "FILES", "DURATION", "TRAIN", "TEST", "BEST SCORE", 
        )
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
            summary_path = step_dir / "index.json"
            try:
                with open(summary_path, "r") as f:
                    summary = json.load(f)
                num_files = sum(1 for _ in step_dir.iterdir())

                duration_str = (
                    Level._format_duration(summary.get("duration_seconds"))
                    if summary.get("duration_seconds") is not None
                    else "-"
                )

                if "train_passed" in summary and summary["train_passed"] is not None:
                    train_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["train_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    train_passed = Text("-", style="", justify="center")

                if "test_passed" in summary and summary["test_passed"] is not None:
                    test_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["test_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    test_passed = Text("-", style="", justify="center")


                #  matches = f"{summary.get('trials', {}).get('train', {}).get('passed', 0)}/{summary.get('trials', {}).get('train', {}).get('total', 0)}"

                best_score_text = (
                    f"{summary.get('best_score'):.2f}"
                    if summary.get("best_score") is not None
                    else "-"
                )
                best_score_text = Text(best_score_text, justify="right")
                # Add the row, with best_score_text already a string
                self.table.add_row(step_dir.name, num_files, duration_str, train_passed, test_passed, best_score_text)

            except FileNotFoundError:
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-")  # Use "-"
            except json.JSONDecodeError:
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-")  # Use "-"
        if self.step_dirs:
            self.select_step_by_index(self.step_index)

    def update_summary(self):
        summary = self.query_one("#summary")
        num_steps = len(self.step_dirs)  # Use len(self.step_dirs)
        train_passed_count = 0
        test_passed_count = 0

        for step_dir in self.step_dirs:
            summary_path = step_dir / "index.json"
            try:
                with open(summary_path, "r") as f:
                    step_summary = json.load(f)
                if step_summary.get("train_passed"):
                    train_passed_count += 1
                if step_summary.get("test_passed"):
                    test_passed_count += 1
            except (FileNotFoundError, json.JSONDecodeError):
                pass

        summary.update(
            f"steps: {num_steps}, train ✔: {train_passed_count}, test ✔: {test_passed_count}"
        )

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
