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
        # Add columns, including token counts, setting justify="right" for numeric columns
        self.table.add_columns(
            "STEP",
            "FILES",
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

                # --- START ADDED TOKEN HANDLING ---
                prompt_tokens = summary.get("response", {}).get("prompt_tokens")
                candidates_tokens = summary.get("response", {}).get("candidates_tokens")
                total_tokens = summary.get("response", {}).get("total_tokens")

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
                # Add the row, including new token columns
                self.table.add_row(
                    step_dir.name,
                    num_files,
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
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")  # Use "-"
            except json.JSONDecodeError:
                # Update exception handling to include placeholders for new columns
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-", "-", "-", "-")  # Use "-"
        if self.step_dirs:
            self.select_step_by_index(self.step_index)

    def update_summary(self):
        summary_widget = self.query_one("#summary") # Corrected query_one usage
        num_steps = len(self.step_dirs)  # Use len(self.step_dirs)
        train_passed_count = 0
        test_passed_count = 0
        # --- START ADDED TOKEN COUNTERS ---
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_steps = 0
        # --- END ADDED TOKEN COUNTERS ---


        for step_dir in self.step_dirs:
            summary_path = step_dir / "index.json"
            try:
                with open(summary_path, "r") as f:
                    step_summary = json.load(f)
                if step_summary.get("train_passed"):
                    train_passed_count += 1
                if step_summary.get("test_passed"):
                    test_passed_count += 1

                # --- START ADDED TOKEN ACCUMULATION ---
                prompt_tokens = step_summary.get("response", {}).get("prompt_tokens")
                candidates_tokens = step_summary.get("response", {}).get("candidates_tokens")
                total_tokens = step_summary.get("response", {}).get("total_tokens")

                if prompt_tokens is not None:
                    total_prompt_tokens += prompt_tokens
                if candidates_tokens is not None:
                    total_candidates_tokens += candidates_tokens
                if total_tokens is not None:
                    total_tokens_all_steps += total_tokens
                # --- END ADDED TOKEN ACCUMULATION ---

            except (FileNotFoundError, json.JSONDecodeError):
                pass

        # Update summary string to include token totals
        summary_widget.update(
            f"steps: {num_steps}, train ✔: {train_passed_count}, test ✔: {test_passed_count} | "
            f"Tokens: IN={total_prompt_tokens}, OUT={total_candidates_tokens}, TOTAL={total_tokens_all_steps}"
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
