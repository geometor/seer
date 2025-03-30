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


# Import Grid
from textual.containers import Vertical, Grid


class TasksScreen(Screen):
    """Displays aggregated task data across all sessions."""

    CSS = """
    Screen > Vertical {
        grid-size: 2;
        grid-rows: auto 1fr; /* Summary auto height, table takes rest */
    }
    #summary-grid {
        grid-size: 3; /* Three columns for the summary tables */
        grid-gutter: 1 2;
        height: auto; /* Let the grid determine its height */
        padding: 0 1; /* Add some horizontal padding */
        margin-bottom: 1; /* Space below summary */
    }
    .summary-table {
        height: auto; /* Fit content height */
        border: none; /* No border for summary tables */
    }
    /* Ensure no focus border on summary tables */
    .summary-table:focus {
        border: none;
    }
    #tasks-table { /* Style for the main tasks table */
        height: 1fr;
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
        self.table = DataTable(id="tasks-table") # Main tasks table

        yield Header()
        with Vertical():
            # Summary Grid with three DataTables
            with Grid(id="summary-grid"):
                yield DataTable(id="summary-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="trials-table", show_header=False, cursor_type=None, classes="summary-table")
                yield DataTable(id="tokens-table", show_header=False, cursor_type=None, classes="summary-table") # Placeholder for now
            # Main tasks table
            yield self.table
        yield Footer()

    def on_mount(self) -> None:
        """Called when the screen is mounted."""
        self.title = "Tasks Navigator"
        self.sub_title = f"Root: {self.sessions_root}"

        # Add columns to summary tables
        summary_table = self.query_one("#summary-table", DataTable)
        summary_table.add_columns("Metric", "Value")
        trials_table = self.query_one("#trials-table", DataTable)
        trials_table.add_columns("Metric", "Value")
        tokens_table = self.query_one("#tokens-table", DataTable) # Placeholder
        tokens_table.add_columns("Metric", "Value") # Placeholder

        # Setup main table
        self.table.cursor_type = "row"
        # Add columns: TASK, SESSIONS, ERRORS, TEST, TRAIN, STEPS, TIME, BEST
        self.table.add_columns(
            "TASK",
            Text("SESSIONS", justify="right"),
            Text("ERRORS", justify="center"),
            Text("TEST", justify="right"),
            Text("TRAIN", justify="right"),
            Text("STEPS", justify="right"),
            Text("TIME", justify="right"),
            Text("BEST", justify="right"),
        )

        self.load_and_display_tasks() # This will now also call update_summary
        self.table.focus()

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

        # Populate the main DataTable
        self.table.clear()

        # Sort tasks by ID for consistent display order
        self.sorted_task_ids = sorted(self.tasks_summary.keys())

        if not self.sorted_task_ids:
            self.table.add_row("No tasks found.")
            self.update_summary() # Update summary even if no tasks
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


            self.table.add_row(
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
        self.update_summary() # Update summary after loading tasks

    @staticmethod
    def _format_duration(seconds: float | None) -> str:
        """Formats duration in HH:MM:SS format. (Copied from Level)"""
        # TODO: Consider moving this to a shared utility module
        if seconds is None or seconds < 0:
            return "-"
        # Use Level's static method directly
        from geometor.seer.session.level import Level
        return Level._format_duration(seconds)

    def update_summary(self):
        """Updates the summary DataTables with aggregated data."""
        summary_table = self.query_one("#summary-table", DataTable)
        trials_table = self.query_one("#trials-table", DataTable)
        tokens_table = self.query_one("#tokens-table", DataTable) # Placeholder

        total_unique_tasks = len(self.tasks_summary)
        total_sessions_involved = set()
        total_errors = 0
        total_test_passed = 0
        total_train_passed = 0
        grand_total_steps = 0
        grand_total_duration = 0.0
        best_scores = []

        for task_id, data in self.tasks_summary.items():
            total_sessions_involved.update(data['sessions'])
            total_errors += data['errors']
            total_test_passed += data['test_passed']
            total_train_passed += data['train_passed']
            grand_total_steps += data['total_steps']
            grand_total_duration += data['total_duration']
            if data['best_score'] != float('inf'):
                best_scores.append(data['best_score'])

        num_sessions = len(total_sessions_involved)
        best_overall_score = f"{min(best_scores):.2f}" if best_scores else "-"
        formatted_total_duration = self._format_duration(grand_total_duration)

        # Clear and update summary table
        summary_table.clear()
        summary_table.add_row(Text("tasks:", justify="right"), Text(str(total_unique_tasks), justify="right"))
        summary_table.add_row(Text("sessions:", justify="right"), Text(str(num_sessions), justify="right"))
        summary_table.add_row(Text("steps:", justify="right"), Text(str(grand_total_steps), justify="right"))
        summary_table.add_row(Text("time:", justify="right"), Text(formatted_total_duration, justify="right"))

        # Clear and update trials table
        trials_table.clear()
        trials_table.add_row(Text("test:", justify="right"), Text(str(total_test_passed), justify="right"))
        trials_table.add_row(Text("train:", justify="right"), Text(str(total_train_passed), justify="right"))
        trials_table.add_row(Text("errors:", justify="right"), Text(str(total_errors), justify="right"))
        trials_table.add_row(Text("best:", justify="right"), Text(best_overall_score, justify="right"))

        # Clear and update tokens table (Placeholder - needs data aggregation)
        tokens_table.clear()
        tokens_table.add_row(Text("in:", justify="right"), Text("-", justify="right"))
        tokens_table.add_row(Text("out:", justify="right"), Text("-", justify="right"))
        tokens_table.add_row(Text("total:", justify="right"), Text("-", justify="right"))


    def action_cursor_down(self) -> None:
        """Move the cursor down in the DataTable."""
        self.table.action_cursor_down()

    def action_cursor_up(self) -> None:
        """Move the cursor up in the DataTable."""
        self.table.action_cursor_up()

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
        # Store current cursor position
        current_cursor_row = self.table.cursor_row

        self.load_and_display_tasks() # Reloads table data and updates summary

        # Restore cursor position if possible
        if current_cursor_row is not None and 0 <= current_cursor_row < self.table.row_count:
            self.table.move_cursor(row=current_cursor_row, animate=False)
        elif self.table.row_count > 0:
            self.table.move_cursor(row=0, animate=False) # Move to top if previous row is gone

        self.table.focus() # Ensure table has focus
