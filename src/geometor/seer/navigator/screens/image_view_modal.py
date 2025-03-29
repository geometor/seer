from pathlib import Path

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Static
from textual.binding import Binding # Added Binding
from textual import log


class ImageViewModal(Screen):
    """Screen with a dialog to select image view filters."""

    BINDINGS = [
        Binding("a", "select_filter('all')", "All", show=False),
        Binding("t", "select_filter('tasks')", "Tasks", show=False),
        Binding("r", "select_filter('trials')", "Trials", show=False),
        Binding("p", "select_filter('passed_trials')", "Passed Trials", show=False), # ADDED binding
        Binding("escape", "app.pop_screen", "Cancel", show=False),
    ]

    def __init__(self, context_path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.context_path = context_path
        log.info(f"ImageViewModal initialized with context: {self.context_path}")

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Select images to view:", id="question"),
            Static(f"Context: {self.context_path}", id="context-label"), # Show context path
            Button("All (.png)", variant="primary", id="all"),
            Button("Tasks (task.png)", variant="primary", id="tasks"),
            Button("Trials (*trial.png)", variant="primary", id="trials"),
            Button("Passed Trials (*trial.png)", variant="success", id="passed_trials"), # ADDED button
            Button("Cancel", variant="default", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        filter_type = event.button.id
        if filter_type == "cancel":
            self.app.pop_screen()
        else:
            # Call the launch method on the main app
            try:
                # Check if the app has the launch_sxiv method
                if hasattr(self.app, "launch_sxiv"):
                    log.info(f"Calling launch_sxiv with context={self.context_path}, filter='{filter_type}'")
                    self.app.launch_sxiv(self.context_path, filter_type)
                else:
                    log.error("App does not have launch_sxiv method.")
                    self.app.notify("Error: Image launch function not found.", severity="error")
            except Exception as e:
                 log.error(f"Error calling launch_sxiv: {e}")
                 self.app.notify(f"Error launching image viewer: {e}", severity="error")
            finally:
                self.app.pop_screen() # Close modal regardless of success/failure

    def action_select_filter(self, filter_type: str) -> None:
        """Called by key bindings."""
        log.info(f"Filter '{filter_type}' selected via key binding.")
        # Simulate button press to reuse the logic
        button = self.query_one(f"#{filter_type}", Button)
        self.on_button_pressed(Button.Pressed(button))

