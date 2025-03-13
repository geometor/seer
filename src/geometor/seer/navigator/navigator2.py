from textual.app import App, ComposeResult
from textual.widgets import Static
from pathlib import Path
import argparse
import json
import re  # Import the regular expression module
from geometor.seer.navigator.screens.sessions_screen import SessionsScreen


class Step:
    def __init__(self, step_prefix: str, task_dir: Path):
        self.prefix = step_prefix
        self.task_dir = task_dir
        self.prompt_file = None
        self.total_prompt_file = None
        self.response_json_file = None
        self.response_md_file = None
        self.py_files = {}  # Store as a dictionary with index as key
        self.train_json_files = {}
        self.test_json_files = {}
        self.yaml_files = []
        self.error_files = []

        self.usage_metadata = None
        self.response_time = None
        self.train_results = {}  # Store train results by index
        self.test_results = {}  # Store test results by index
        self.train_match = False
        self.test_match = False

        self._load_files()
        self._load_data()

    def _load_files(self):
        for file in self.task_dir.iterdir():
            if file.name.startswith(self.prefix):
                if file.name.endswith("prompt.md"):
                    self.prompt_file = file
                elif file.name.endswith("total_prompt.md"):
                    self.total_prompt_file = file
                elif file.name.endswith("response.json"):
                    self.response_json_file = file
                elif file.name.endswith("response.md"):
                    self.response_md_file = file
                elif file.name.startswith(f"{self.prefix}py_") and file.name.endswith(".py"):
                    match = re.match(rf"{self.prefix}py_(\d+)\.py", file.name)
                    if match:
                        index = int(match.group(1))
                        self.py_files[index] = file
                elif file.name.startswith(f"{self.prefix}py_") and file.name.endswith("-train.json"):
                    match = re.match(rf"{self.prefix}py_(\d+)-train\.json", file.name)
                    if match:
                        index = int(match.group(1))
                        self.train_json_files[index] = file
                elif file.name.startswith(f"{self.prefix}py_") and file.name.endswith("-test.json"):
                    match = re.match(rf"{self.prefix}py_(\d+)-test\.json", file.name)
                    if match:
                        index = int(match.group(1))
                        self.test_json_files[index] = file
                elif file.suffix == ".yaml":
                    self.yaml_files.append(file)
                elif file.name.startswith("error"):
                    self.error_files.append(file)

    def _load_data(self):
        if self.response_json_file:
            try:
                with open(self.response_json_file, "r") as f:
                    data = json.load(f)
                    self.usage_metadata = data.get("usage_metadata")
                    self.response_time = data.get("response_time")
            except (FileNotFoundError, json.JSONDecodeError):
                pass  # Handle missing or invalid JSON

        for index, train_file in self.train_json_files.items():
            try:
                with open(train_file, "r") as f:
                    data = json.load(f)
                    self.train_results[index] = data
                    for example in data.get("examples", []):
                        if example.get("match"):
                            self.train_match = True
                            break  # Exit inner loop once a match is found
            except (FileNotFoundError, json.JSONDecodeError):
                pass

        for index, test_file in self.test_json_files.items():
            try:
                with open(test_file, "r") as f:
                    data = json.load(f)
                    self.test_results[index] = data
                    for example in data.get("examples", []):
                        if example.get("match"):
                            self.test_match = True
                            break
            except (FileNotFoundError, json.JSONDecodeError):
                pass


class SessionNavigator(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)

    def compose(self) -> ComposeResult:
        yield Static("Loading...")
        self.sessions = self._load_sessions()

    def on_mount(self) -> None:
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
                        steps = {}
                        # Find all prefixes
                        prefixes = set()
                        for file in task_dir.iterdir():
                            match = re.match(r"(\d{3})-.*", file.name)
                            if match:
                                prefixes.add(match.group(1))

                        # Create Step objects
                        for prefix in sorted(prefixes):
                            steps[prefix] = Step(prefix, task_dir)

                        tasks[task_dir.name] = steps  # Store steps dict
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
