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
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)

    def compose(self) -> ComposeResult:
        yield Static("Loading...")

    def on_mount(self) -> None:
        self.push_screen(SessionsScreen(self.sessions_root)) # Pass sessions_root

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
