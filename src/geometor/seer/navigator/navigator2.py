from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse

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
        self.sessions = self._load_sessions()
        self.push_screen(SessionsScreen())

    def _load_sessions(self) -> dict:
        sessions = {}
        session_dirs = sorted(self.sessions_root.iterdir(), key=lambda x: x.name)
        for session_dir in session_dirs:
            if session_dir.is_dir():
                tasks = {}
                task_dirs = sorted(session_dir.iterdir(), key=lambda x: x.name)
                for task_dir in task_dirs:
                    if task_dir.is_dir():
                        task_files = sorted(task_dir.iterdir(), key=lambda x: x.name)
                        #  for task_file in task_files:
                            #  if task_file.is_file():
                                #  task_files.append(task_file)

                        tasks[task_dir.name] = task_files

                sessions[session_dir.name] = tasks
        return sessions

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
