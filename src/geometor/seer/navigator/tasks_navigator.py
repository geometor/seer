import argparse
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.binding import Binding
from textual import log

# Import screens
from geometor.seer.navigator.screens.tasks_screen import TasksScreen
from geometor.seer.navigator.screens.sort_modal import SortModal # ADDED


class TasksNavigator(App):
    """A Textual app to navigate aggregated task data across sessions."""

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh_screen", "Refresh", show=True),
        Binding("s", "sort_table", "Sort Table", show=True),   # ADDED sort binding
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)
        log.info(f"TasksNavigator initialized with sessions_root: {self.sessions_root}")

    def compose(self) -> ComposeResult:
        """Yield the initial container for the app's default screen."""
        yield Container() # Container to hold the pushed screen

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        # Push the initial screen
        self.push_screen(TasksScreen(self.sessions_root))

    def action_refresh_screen(self) -> None:
        """Calls the refresh method on the current screen if it exists."""
        current_screen = self.screen
        if hasattr(current_screen, "refresh_content"):
            log.info(f"Refreshing screen: {current_screen.__class__.__name__}")
            current_screen.refresh_content()
            self.notify("Screen refreshed")
        else:
            log.warning(f"Screen {current_screen.__class__.__name__} has no refresh_content method.")
            self.notify("Refresh not supported on this screen", severity="warning")

    # --- START ADDED SORT ACTION ---
    def action_sort_table(self) -> None:
        """Pushes the sort modal screen for the current data table."""
        current_screen = self.screen

        # Check if the current screen has a sortable table (TasksScreen)
        if isinstance(current_screen, TasksScreen) and hasattr(current_screen, "table") and hasattr(current_screen, "perform_sort"):
            table = current_screen.table
            columns = table.columns # Get the columns dictionary

            if not columns:
                self.notify("No columns available to sort.", severity="warning")
                return

            log.info(f"Pushing SortModal for screen: {current_screen.__class__.__name__}")
            # Pass the parent screen instance and the columns dict
            self.push_screen(SortModal(parent_screen=current_screen, columns=columns))
        else:
            log.warning(f"Sorting not supported on screen: {current_screen.__class__.__name__}")
            self.notify("Sorting not supported on this screen.", severity="warning")
    # --- END ADDED SORT ACTION ---

    def action_quit(self) -> None:
        """Quits the application"""
        self.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Navigate aggregated ARC task data across sessions.")
    parser.add_argument(
        "--sessions-dir",
        type=str,
        default="./sessions",
        help="Path to the root sessions directory",
    )
    args = parser.parse_args()

    app = TasksNavigator(sessions_root=args.sessions_dir)
    app.run()
