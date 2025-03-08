from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse

# Import the screen classes
from geometor.seer.navigator.screens.sessions_screen import SessionsScreen, SessionInfo
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
        sessions = self._load_sessions()
        self.push_screen(SessionsScreen(sessions, self))  # Pass the list of SessionInfo

    def _load_sessions(self) -> list[SessionInfo]:
        """Loads session information from the session root directory."""
        sessions = []
        session_root_path = Path(self.session_root)
        for session_dir in session_root_path.iterdir():
            if session_dir.is_dir():
                sessions.append(SessionInfo(name=session_dir.name, path=session_dir))
        return sessions

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
