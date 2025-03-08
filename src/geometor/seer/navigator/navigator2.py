from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse

# Import the screen classes
from geometor.seer.navigator.screens.sessions_screen import SessionsScreen
from geometor.seer.navigator.screens.session_screen import SessionScreen  # Corrected import
from geometor.seer.navigator.screens.task_screen import TaskScreen  # Corrected import


class SessionNavigator(App):
    """Main application for navigating ARC test sessions."""

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),  # add quit binding
    ]

    def __init__(self, session_root: str = "./sessions"):
        super().__init__()
        self.session_root = session_root

    def compose(self) -> ComposeResult:
        """Creates the initial layout."""
        yield Static("Loading...")  # Placeholder

    def on_mount(self) -> None:
        """Sets up initial state."""
        self.push_screen(SessionsScreen(self.session_root, self))  # Pass self (the app)

    def action_quit(self) -> None:
        """Quits the application"""
        self.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Navigate ARC test sessions."
    )
    parser.add_argument(
        "--sessions-dir",
        type=str,
        default="./sessions",
        help="Path to the sessions directory",
    )
    args = parser.parse_args()

    app = SessionNavigator(session_root=args.sessions_dir)
    app.run()
