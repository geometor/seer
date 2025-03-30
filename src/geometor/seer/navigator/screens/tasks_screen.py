import json
from pathlib import Path
from collections import defaultdict

from rich.text import Text

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Header, Footer, Static # Added Static
from textual.containers import Vertical
from textual.binding import Binding
from textual import log


class TasksScreen(Screen):
    """Displays aggregated task data across all sessions."""

    CSS = """
    Screen > Vertical {
        height: 1fr; /* Make Vertical fill the screen */
    }
    DataTable {
        height: 1fr; /* Make DataTable fill the Vertical container */
    }
    """

    BINDINGS = [
        Binding("j", "cursor_down", "Cursor Down", show=False),
        Binding("k", "cursor_up", "Cursor Up", show=False),
        # Binding("l,enter", "select_task", "Select Task", show=True), # Add later if needed
        Binding("h", "app.pop_screen", "Back", show=False), # Although it's the root screen now
    ]

    def __init__(self, sessions_root: Path) -> None:
        super().__init__()
        self.sessions_root = sessions_root
        self.tasks_summary = defaultdict(lambda: {
            'sessions': set(),
            'errors': 0,
            'test_passed': 0,
            'train_passed': 0,
            'total_steps': 0, # Add total steps
            'total_duration': 0.0, # Add total duration
            'best_score': float('inf'), # Initialize best score to infinity (lower is better)
        })
        self.sorted_task_ids = [] # To maintain table order

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield DataTable(id="tasks-table")
        yield Footer()

    def on_mount(self) -> None:
        """Called when the screen is mounted."""
        self.title = "Tasks Navigator"
        self.sub_title = f"Root: {self.sessions_root}"

        table = self.query_one(DataTable)
        table.cursor_type = "row"
        # Add columns: TASK, SESSIONS, ERRORS, TEST, TRAIN, STEPS, TIME, BEST
        table.add_columns(
            "TASK",
            Text("SESSIONS", justify="right"),
            Text("ERRORS", justify="center"),
            Text("TEST", justify="right"),
            Text("TRAIN", justify="right"),
            Text("STEPS", justify="right"),
            Text("TIME", justify="right"),
            Text("BEST", justify="right"),
        )

        self.load_and_display_tasks()
        table.focus()

    def load_and_display_tasks(self):
        """Scans sessions, aggregates task data, and populates the DataTable."""
        log.info(f"Scanning sessions in {self.sessions_root} to aggregate task data...")
        self.tasks_summary.clear() # Clear previous data before rescanning

        try:
            if not self.sessions_root.is_dir():
                log.error(f"Sessions root directory not found: {self.sessions_root}")
                self.notify(f"Error: Directory not found: {self.sessions_root}", severity="error")
                return

            for session_dir in self.sessions_root.iterdir():
                if session_dir.is_dir():
                    session_name = session_dir.name
                    for task_dir in session_dir.iterdir():
                        if task_dir.is_dir():
                            task_id = task_dir.name
                            summary_path = task_dir / "index.json"
                            task_data = self.tasks_summary[task_id] # Get or create entry

                            task_data['sessions'].add(session_name)

                            if summary_path.exists():
                                try:
                                    with open(summary_path, "r") as f:
                                        summary = json.load(f)

                                    # Aggregate counts
                                    task_data['errors'] += summary.get("errors", {}).get("count", 0)
                                    if summary.get("test_passed") is True:
                                        task_data['test_passed'] += 1
                                    if summary.get("train_passed") is True:
                                        task_data['train_passed'] += 1
                                    task_data['total_steps'] += summary.get("steps", 0)

                                    # Aggregate duration
                                    duration = summary.get("duration_seconds")
                                    if duration is not None:
                                        task_data['total_duration'] += duration

                                    # Find best (minimum) score
                                    score = summary.get("best_score")
                                    if score is not None and score < task_data['best_score']:
                                        task_data['best_score'] = score

                                except json.JSONDecodeError:
                                    log.warning(f"Could not decode JSON in {summary_path}")
                                    task_data['errors'] += 1 # Count decode error as an error
                                except Exception as e:
                                    log.error(f"Error reading {summary_path}: {e}")
                                    task_data['errors'] += 1 # Count other read errors
                            else:
                                # If index.json is missing, maybe log or count as error?
                                log.warning(f"Missing index.json for task {task_id} in session {session_name}")
                                # task_data['errors'] += 1 # Optionally count missing index as error

        except Exception as e:
            log.error(f"Error scanning directories: {e}")
            self.notify(f"Error scanning sessions: {e}", severity="error")
            # Display error in table?
            table = self.query_one(DataTable)
            table.clear()
            table.add_row(Text(f"Error scanning: {e}", style="bold red"))
            return

        # Populate the DataTable
        table = self.query_one(DataTable)
        table.clear()

        # Sort tasks by ID for consistent display order
        self.sorted_task_ids = sorted(self.tasks_summary.keys())

        if not self.sorted_task_ids:
            table.add_row("No tasks found.")
            return

        for task_id in self.sorted_task_ids:
            data = self.tasks_summary[task_id]
            session_count = len(data['sessions'])
            error_text = Text(str(data['errors']), style="bold yellow", justify="center") if data['errors'] > 0 else Text("-", justify="center")
            test_text = Text(str(data['test_passed']), justify="right")
            train_text = Text(str(data['train_passed']), justify="right")
            steps_text = Text(str(data['total_steps']), justify="right")
            # Format duration
            time_str = self._format_duration(data['total_duration'])
            # Format best score
            best_score_val = data['best_score']
            best_score_text = Text(f"{best_score_val:.2f}" if best_score_val != float('inf') else "-", justify="right")


            table.add_row(
                task_id,
                Text(str(session_count), justify="right"),
                error_text,
                test_text,
                train_text,
                steps_text,
                Text(time_str, justify="right"),
                best_score_text,
            )

        log.info(f"Finished aggregating data for {len(self.sorted_task_ids)} unique tasks.")

    @staticmethod
    def _format_duration(seconds: float | None) -> str:
        """Formats duration in HH:MM:SS format. (Copied from Level)"""
        # TODO: Consider moving this to a shared utility module
        if seconds is None or seconds < 0:
            return "-"
        # Use Level's static method directly
        from geometor.seer.session.level import Level
        return Level._format_duration(seconds)

    def action_cursor_down(self) -> None:
        """Move the cursor down in the DataTable."""
        table = self.query_one(DataTable)
        table.action_cursor_down()

    def action_cursor_up(self) -> None:
        """Move the cursor up in the DataTable."""
        table = self.query_one(DataTable)
        table.action_cursor_up()

    # def action_select_task(self) -> None:
    #     """Called when a task row is selected."""
    #     # TODO: Implement navigation to a screen showing sessions for this task?
    #     table = self.query_one(DataTable)
    #     if table.row_count > 0 and table.cursor_row is not None:
    #         task_id = self.sorted_task_ids[table.cursor_row]
    #         self.notify(f"Selected task: {task_id}")
    #         # Example: self.app.push_screen(TaskSessionsScreen(self.sessions_root, task_id))
    #     pass

    def refresh_content(self) -> None:
        """Reloads task data and updates the screen."""
        log.info("Refreshing TasksScreen content...")
        # Store current cursor position if needed, though simple reload might suffice
        # current_cursor_row = self.query_one(DataTable).cursor_row
        self.load_and_display_tasks()
        # Restore cursor position if needed and possible
        # ...
        self.query_one(DataTable).focus() # Ensure table has focus
