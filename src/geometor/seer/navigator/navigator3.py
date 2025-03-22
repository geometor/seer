from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse
import json
import re

from geometor.seer.navigator.screens.sessions_screen import SessionsScreen


class SessionNavigator(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("[", "previous_sibling", "Previous Sibling"),
        ("]", "next_sibling", "Next Sibling"),
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)
        self.session_index = 0
        self.task_index = 0
        self.step_index = 0
        self.session_dirs = []
        self.task_dirs = []
        self.step_dirs = []

    def compose(self) -> ComposeResult:
        yield Static("Loading...")

    def on_mount(self) -> None:
        self.push_screen(SessionsScreen(self.sessions_root))  # Pass sessions_root

    def action_previous_sibling(self) -> None:
        """Navigate to the previous sibling directory."""
        current_screen = self.screen
        if isinstance(current_screen, SessionsScreen):
            self.session_index = (self.session_index - 1) % len(self.session_dirs)
            current_screen.select_session_by_index(self.session_index)
        elif isinstance(current_screen, SessionScreen):
            self.task_index = (self.task_index - 1) % len(self.task_dirs)
            current_screen.select_task_by_index(self.task_index)
        elif isinstance(current_screen, TaskScreen):
            self.step_index = (self.step_index - 1) % len(self.step_dirs)
            current_screen.select_step_by_index(self.step_index)

    def action_next_sibling(self) -> None:
        """Navigate to the next sibling directory."""
        current_screen = self.screen
        if isinstance(current_screen, SessionsScreen):
            self.session_index = (self.session_index + 1) % len(self.session_dirs)
            current_screen.select_session_by_index(self.session_index)
        elif isinstance(current_screen, SessionScreen):
            self.task_index = (self.task_index + 1) % len(self.task_dirs)
            current_screen.select_task_by_index(self.task_index)
        elif isinstance(current_screen, TaskScreen):
            self.step_index = (self.step_index + 1) % len(self.step_dirs)
            current_screen.select_step_by_index(self.step_index)

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
