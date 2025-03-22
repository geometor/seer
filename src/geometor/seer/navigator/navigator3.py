from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse
import json
import re

from geometor.seer.navigator.screens.sessions_screen import SessionsScreen
from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.navigator.screens.task_screen import TaskScreen


class SessionNavigator(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("[", "previous_sibling", "Previous Sibling"),
        ("]", "next_sibling", "Next Sibling"),
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)
        # Removed index and dir lists from App level

    def compose(self) -> ComposeResult:
        yield Static("Loading...")

    def on_mount(self) -> None:
        self.push_screen(SessionsScreen(self.sessions_root))

    def action_previous_sibling(self) -> None:
        """Navigate to the previous sibling directory."""
        current_screen = self.screen
        if hasattr(current_screen, "previous_sibling"):
            current_screen.previous_sibling()


    def action_next_sibling(self) -> None:
        """Navigate to the next sibling directory."""
        current_screen = self.screen
        if hasattr(current_screen, "next_sibling"):
            current_screen.next_sibling()

    def action_quit(self) -> None:
        """Quits the application"""
        self.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Navigate ARC test sessions.")
    parser.add_argument(
        "--sessions-dir",
        type=str,
        default="./sessions",
        help="Path to the sessions directory",
    )
    args = parser.parse_args()

    app = SessionNavigator(sessions_root=args.sessions_dir)
    app.run()
