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
        # Add columns, including token counts, setting justify="right" for numeric columns
        self.table.add_columns(
            "TASKS",
            "STEPS",
            "DURATION",
            Text("IN", justify="right"),    # ADDED
            Text("OUT", justify="right"),   # ADDED
            Text("TOTAL", justify="right"), # ADDED
            "TRAIN",
            "TEST",
            Text("BEST SCORE", justify="right"),
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

                # --- START ADDED TOKEN HANDLING ---
                tokens_data = summary.get("tokens", {}) # Get the tokens dict, default to empty
                prompt_tokens = tokens_data.get("prompt_tokens")
                candidates_tokens = tokens_data.get("candidates_tokens")
                total_tokens = tokens_data.get("total_tokens")

                in_tokens_text = Text(str(prompt_tokens) if prompt_tokens is not None else "-", justify="right")
                out_tokens_text = Text(str(candidates_tokens) if candidates_tokens is not None else "-", justify="right")
                total_tokens_text = Text(str(total_tokens) if total_tokens is not None else "-", justify="right")
                # --- END ADDED TOKEN HANDLING ---

                if "train_passed" in summary and summary["train_passed"] is not None:
                    train_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["train_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    # Default if key is missing or None (adjust style as needed)
                    train_passed = Text("-", style="", justify="center") # Changed default from ✔ to -

                if "test_passed" in summary and summary["test_passed"] is not None:
                    test_passed = (
                        Text("✔", style="green", justify="center")
                        if summary["test_passed"]
                        else Text("✘", style="red", justify="center")
                    )
                else:
                    # Default if key is missing or None (adjust style as needed)
                    test_passed = Text("-", style="", justify="center") # Changed default from ✔ to -

                best_score_text = (
                    f"{summary.get('best_score'):.2f}"
                    if summary.get("best_score") is not None
                    else "-"
                )
                best_score_text = Text(best_score_text, justify="right")
                # Add the row, including new token columns
                self.table.add_row(
                    task_dir.name,
                    num_steps,
                    duration_str,
                    in_tokens_text,      # ADDED
                    out_tokens_text,     # ADDED
                    total_tokens_text,   # ADDED
                    train_passed,
                    test_passed,
                    best_score_text
                )

            except FileNotFoundError:
                # Update exception handling to include placeholders for new columns
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")  # Use "-"
            except json.JSONDecodeError:
                # Update exception handling to include placeholders for new columns
                self.table.add_row(task_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")  # Use "-"
        if self.task_dirs:
            self.select_task_by_index(self.task_index)

        self.update_summary()

    def update_summary(self):
        summary_widget = self.query_one("#summary", Static)
        num_tasks = len(self.task_dirs)
        train_passed_count = 0
        test_passed_count = 0
        best_scores = []
        # --- START ADDED TOKEN COUNTERS ---
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        # --- END ADDED TOKEN COUNTERS ---

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

                # --- START ADDED TOKEN ACCUMULATION ---
                tokens_data = task_summary.get("tokens", {})
                prompt_tokens = tokens_data.get("prompt_tokens")
                candidates_tokens = tokens_data.get("candidates_tokens")
                total_tokens = tokens_data.get("total_tokens")

                if prompt_tokens is not None:
                    total_prompt_tokens += prompt_tokens
                if candidates_tokens is not None:
                    total_candidates_tokens += candidates_tokens
                if total_tokens is not None:
                    total_tokens_all_tasks += total_tokens
                # --- END ADDED TOKEN ACCUMULATION ---

            except (FileNotFoundError, json.JSONDecodeError):
                pass

        best_score_summary = (
            f"Best: {min(best_scores):.2f}" if best_scores else "Best: -"
        )  # Handle empty list

        # Update summary string to include token totals
        summary_widget.update(
            f"Tasks: {num_tasks}, Train ✔: {train_passed_count}, Test ✔: {test_passed_count}, {best_score_summary} | "
            f"Tokens: IN={total_prompt_tokens}, OUT={total_candidates_tokens}, TOTAL={total_tokens_all_tasks}"
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
        task_name = row[0] # Get task name from the first column
        task_path = self.session_path / task_name

        # Get step directories for the selected task
        step_dirs = sorted([d for d in task_path.iterdir() if d.is_dir()])
        self.app.push_screen(TaskScreen(self.session_path, task_path, step_dirs))

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # This method is kept for compatibility, but the core logic is in action_select_row
        self.action_select_row()
