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
from textual import log # ADDED import
import subprocess # ADDED import
import shutil # ADDED import

from pathlib import Path
import json

from geometor.seer.session.level import Level  # Import Level
from geometor.seer.navigator.screens.step_screen import StepScreen # IMPORT THE NEW SCREEN


class TaskScreen(Screen):
    CSS = """
    DataTable {height: 1fr;}
    Static {padding: 1; height: 3}
    Vertical {height: 100%;}
    """
    BINDINGS = [
        Binding("l,enter", "select_row", "Select", show=False), # Added enter key
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
        Binding("i", "view_images", "View Images", show=True), # ADDED binding
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    def __init__(self, session_path: Path, task_path: Path, step_dirs: list[Path]) -> None:
        super().__init__()
        self.session_path = session_path
        self.task_path = task_path
        self.step_dirs = step_dirs  # Receive step_dirs
        self.step_index = 0
        self._sxiv_checked = False # ADDED sxiv check state
        self._sxiv_path = None     # ADDED sxiv path cache

    # ADDED sxiv check method
    def _check_sxiv(self) -> str | None:
        """Check if sxiv exists and cache the path."""
        if not self._sxiv_checked:
            self._sxiv_path = shutil.which("sxiv")
            self._sxiv_checked = True
            if not self._sxiv_path:
                log.warning("'sxiv' command not found in PATH. Cannot open images externally.")
                self.app.notify("sxiv not found. Cannot open images.", severity="warning", timeout=5)
        return self._sxiv_path

    def compose(self) -> ComposeResult:
        self.table = DataTable()
        # Add columns in the new requested order, including ERROR
        self.table.add_columns(
            "STEP",
            Text("ERROR", justify="center"),     # ADDED
            "TEST",
            "TRAIN",
            Text("SCORE", justify="right"),
            Text("SIZE", justify="center"),
            Text("PALETTE", justify="center"),
            Text("COLORS", justify="center"),
            Text("PIXELS", justify="right"),
            Text("%", justify="right"),
            "TIME",
            Text("ATTEMPTS", justify="right"),
            Text("IN", justify="right"),
            Text("OUT", justify="right"),
            Text("TOTAL", justify="right"),
            "FILES",
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
                num_files = sum(1 for item in step_dir.iterdir() if item.is_file()) # Count only files

                # Use the updated _format_duration method
                time_str = (
                    Level._format_duration(summary.get("duration_seconds"))
                    if summary.get("duration_seconds") is not None
                    else "-"
                )

                # --- START ERROR HANDLING ---
                has_errors = summary.get("has_errors", False) # Default to False if missing
                error_text = (
                    Text("⚠", style="bold yellow", justify="center") # CHANGED character and style
                    if has_errors
                    else Text("-", justify="center")
                )
                # --- END ERROR HANDLING ---

                # --- START RETRIES HANDLING ---
                attempts = summary.get("attempts")
                attempts_text = Text(str(attempts) if attempts is not None else "-", justify="right")
                # --- END RETRIES HANDLING ---

                # --- START TOKEN HANDLING ---
                prompt_tokens = summary.get("response", {}).get("prompt_tokens")
                candidates_tokens = summary.get("response", {}).get("candidates_tokens")
                total_tokens = summary.get("response", {}).get("total_tokens")

                in_tokens_text = Text(str(prompt_tokens) if prompt_tokens is not None else "-", justify="right")
                out_tokens_text = Text(str(candidates_tokens) if candidates_tokens is not None else "-", justify="right")
                total_tokens_text = Text(str(total_tokens) if total_tokens is not None else "-", justify="right")
                # --- END TOKEN HANDLING ---

                # --- START PASS/FAIL HANDLING ---
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
                # --- END PASS/FAIL HANDLING ---

                # --- START BEST SCORE HANDLING ---
                best_score_text = (
                    f"{summary.get('best_score'):.2f}"
                    if summary.get("best_score") is not None
                    else "-"
                )
                best_score_text = Text(best_score_text, justify="right")
                # --- END BEST SCORE HANDLING ---

                # --- START BEST TRIAL METRICS HANDLING ---
                metrics = summary.get("best_trial_metrics", {})

                def format_bool_metric(value):
                    if value is True:
                        return Text("✔", style="green", justify="center")
                    elif value is False:
                        return Text("✘", style="red", justify="center")
                    else:
                        return Text("-", justify="center")

                size_correct_text = format_bool_metric(metrics.get("all_size_correct"))
                palette_correct_text = format_bool_metric(metrics.get("all_palette_correct"))
                color_count_correct_text = format_bool_metric(metrics.get("all_color_count_correct"))

                # Get TOTAL pixels off count
                pixels_off_val = metrics.get("pixels_off")
                # Format as integer string
                pixels_off_text = Text(str(pixels_off_val) if pixels_off_val is not None else "-", justify="right")

                percent_correct_val = metrics.get("avg_percent_correct")
                percent_correct_text = Text(f"{percent_correct_val:.1f}" if percent_correct_val is not None else "-", justify="right")
                # --- END BEST TRIAL METRICS HANDLING ---


                # Add the row with arguments in the new order (16 columns total)
                self.table.add_row(
                    step_dir.name,             # STEP
                    error_text,                # ERROR
                    test_passed,               # TEST
                    train_passed,              # TRAIN
                    best_score_text,           # SCORE
                    size_correct_text,         # SIZE
                    palette_correct_text,      # PALETTE
                    color_count_correct_text,  # COLORS
                    pixels_off_text,           # PIXELS
                    percent_correct_text,      # %
                    time_str,                  # TIME
                    attempts_text,             # ATTEMPTS
                    in_tokens_text,            # IN
                    out_tokens_text,           # OUT
                    total_tokens_text,         # TOTAL
                    num_files                  # FILES
                )

            except FileNotFoundError:
                # Update exception handling for 16 columns
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
            except json.JSONDecodeError:
                # Update exception handling for 16 columns
                self.table.add_row(step_dir.name, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-")
        if self.step_dirs:
            self.select_step_by_index(self.step_index)

    def update_summary(self):
        summary_widget = self.query_one("#summary") # Corrected query_one usage
        num_steps = len(self.step_dirs)  # Use len(self.step_dirs)
        train_passed_count = 0
        test_passed_count = 0
        error_count = 0 # ADDED error counter
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
                if step_summary.get("has_errors"): # ADDED check for errors
                    error_count += 1

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

        # Update summary string to include error count and token totals
        summary_widget.update(
            f"steps: {num_steps}, train ✔: {train_passed_count}, test ✔: {test_passed_count}, errors ⚠: {error_count} | " # CHANGED icon in summary
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
        """Called when a row is selected (Enter or 'l')."""
        if not self.step_dirs:
            return # No steps to select

        row_id = self.table.cursor_row
        if row_id is None or not (0 <= row_id < len(self.step_dirs)):
             return # Invalid selection

        # Get the step directory corresponding to the selected row
        step_path = self.step_dirs[row_id]

        # Push the StepScreen
        self.app.push_screen(StepScreen(self.session_path, self.task_path, step_path))

    # ADDED action
    def action_view_images(self) -> None:
        """Find and open all PNG images in the current task directory using sxiv."""
        sxiv_cmd = self._check_sxiv()
        if not sxiv_cmd:
            return # sxiv not found, notification already shown

        try:
            # Find all .png files recursively within the task directory
            image_files = sorted(list(self.task_path.rglob("*.png")))

            if not image_files:
                self.app.notify("No PNG images found in this task.", severity="information")
                return

            # Prepare the command list
            command = [sxiv_cmd] + [str(img_path) for img_path in image_files]

            log.info(f"Opening {len(image_files)} images with sxiv from {self.task_path}")
            subprocess.Popen(command)

        except FileNotFoundError:
            log.error(f"'sxiv' command not found when trying to execute.")
            self.app.notify("sxiv not found. Cannot open images.", severity="error")
        except Exception as e:
            log.error(f"Error finding or opening images with sxiv from {self.task_path}: {e}")
            self.app.notify(f"Error viewing images: {e}", severity="error")


    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        # kept for compatibility, triggers action_select_row
        self.action_select_row()
