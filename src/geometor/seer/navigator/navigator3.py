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
        self.sessions = self._load_sessions()
        self.push_screen(SessionsScreen())

    def _load_sessions(self) -> dict:
        sessions = {}
        session_dirs = sorted(self.sessions_root.iterdir(), key=lambda x: x.name)
        for session_dir in session_dirs:
            if session_dir.is_dir():
                summary_path = session_dir / "session_summary.json"
                # TODO handle errors
                with open(summary_path, 'r') as f:
                    summary = json.load(f)

                tasks = {}
                task_dirs = sorted(session_dir.iterdir(), key=lambda x: x.name)
                for task_dir in task_dirs:
                    if task_dir.is_dir():
                        steps = {}
                        step_dirs = sorted(task_dir.iterdir(), key=lambda x: x.name)
                        for step_dir in step_dirs:
                            step = {}
                            if step_dir.is_dir():
                                for file in step_dir.iterdir():
                                    step[file] = ""

                            steps[step_dir.name] = step
                        tasks[task_dir.name] = steps  
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
