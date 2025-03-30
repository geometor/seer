import json
from pathlib import Path
from collections import defaultdict

from rich.text import Text

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Header, Footer, Static # Added Static
from textual.reactive import reactive # ADDED reactive
from textual.containers import Vertical
from textual.binding import Binding
from textual.widgets._data_table import ColumnKey # ADDED ColumnKey
from textual import log


# Import Grid
from textual.containers import Vertical, Grid

# Import Task for weight calculation
from geometor.seer.tasks.tasks import Task


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
            # ADDED token aggregation fields
            'total_prompt_tokens': 0,
            'total_candidates_tokens': 0,
            'total_tokens': 0,
            'weight': 0, # ADDED weight field
        })
        self.sorted_task_ids = [] # To maintain table order
        self.current_sort_key: ColumnKey | None = None # ADDED sort state
        self.current_sort_reverse: bool = False      # ADDED sort state

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
        trials_table.add_columns("Metric", "Value", "±") # Add third column header
        tokens_table = self.query_one("#tokens-table", DataTable)
        tokens_table.add_columns("Metric", "Value")

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
            # ADDED Token Columns
            Text("IN", justify="right"),
            Text("OUT", justify="right"),
            Text("TOTAL", justify="right"),
            Text("WEIGHT", justify="right"), # ADDED WEIGHT column
        )

        self.load_and_display_tasks() # This will now also call update_summary
        self.table.focus()
        # Add sort key tracking
        self.current_sort_key = None
        self.current_sort_reverse = False

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

                                    # --- START ADDED TOKEN AGGREGATION ---
                                    tokens_data = summary.get("tokens", {})
                                    prompt_tokens = tokens_data.get("prompt_tokens")
                                    candidates_tokens = tokens_data.get("candidates_tokens")
                                    total_tokens = tokens_data.get("total_tokens")

                                    if prompt_tokens is not None:
                                        task_data['total_prompt_tokens'] += prompt_tokens
                                    if candidates_tokens is not None:
                                        task_data['total_candidates_tokens'] += candidates_tokens
                                    if total_tokens is not None:
                                        task_data['total_tokens'] += total_tokens
                                    # --- END ADDED TOKEN AGGREGATION ---

                                    # --- START ADDED WEIGHT CALCULATION ---
                                    # Find the corresponding task.json in *any* session dir for this task
                                    task_json_path = None
                                    for s_dir in self.sessions_root.iterdir():
                                        potential_path = s_dir / task_id / "task.json"
                                        if potential_path.exists():
                                            task_json_path = potential_path
                                            break # Found one, no need to check others

                                    if task_json_path:
                                        try:
                                            with open(task_json_path, "r") as f_task:
                                                task_json_data = json.load(f_task)
                                            task_obj = Task(task_id, task_json_data)
                                            task_data['weight'] = task_obj.weight # Store weight
                                        except (json.JSONDecodeError, Exception) as e_task:
                                            log.error(f"Error loading/processing {task_json_path} for weight: {e_task}")
                                            task_data['weight'] = -1 # Indicate error
                                    else:
                                        log.warning(f"Could not find task.json for task {task_id} in any session.")
                                        task_data['weight'] = -2 # Indicate not found
                                    # --- END ADDED WEIGHT CALCULATION ---

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

            # Color TEST and TRAIN counts
            test_passed_count = data['test_passed']
            test_text = (
                Text(str(test_passed_count), style="bold green", justify="right")
                if test_passed_count > 0
                else Text("0", style="red", justify="right")
            )
            train_passed_count = data['train_passed']
            train_text = (
                Text(str(train_passed_count), style="bold green", justify="right")
                if train_passed_count > 0
                else Text("0", style="red", justify="right")
            )

            steps_text = Text(str(data['total_steps']), justify="right")
            # Format duration
            time_str = self._format_duration(data['total_duration'])
            # Format best score
            best_score_val = data['best_score']
            best_score_text = Text(f"{best_score_val:.2f}" if best_score_val != float('inf') else "-", justify="right")

            # --- START ADDED TOKEN TEXT ---
            in_tokens_text = Text(f"{data['total_prompt_tokens']:,}" if data['total_prompt_tokens'] > 0 else "-", justify="right")
            out_tokens_text = Text(f"{data['total_candidates_tokens']:,}" if data['total_candidates_tokens'] > 0 else "-", justify="right")
            total_tokens_text = Text(f"{data['total_tokens']:,}" if data['total_tokens'] > 0 else "-", justify="right")
            # --- END ADDED TOKEN TEXT ---

            # --- START ADDED WEIGHT TEXT ---
            weight_val = data.get('weight', 0)
            if weight_val == -1:
                weight_text = Text("ERR", style="bold red", justify="right")
            elif weight_val == -2:
                weight_text = Text("?", style="dim", justify="right")
            else:
                weight_text = Text(f"{weight_val:,}", justify="right")
            # --- END ADDED WEIGHT TEXT ---

            self.table.add_row(
                task_id,                       # TASK
                Text(str(session_count), justify="right"), # SESSIONS
                error_text,                    # ERRORS
                test_text,                     # TEST
                train_text,                    # TRAIN
                steps_text,                    # STEPS
                Text(time_str, justify="right"), # TIME
                best_score_text,               # BEST
                # ADDED Token Columns
                in_tokens_text,                # IN
                out_tokens_text,               # OUT
                total_tokens_text,             # TOTAL
                weight_text,                   # WEIGHT (ADDED)
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
        total_errors = 0 # Keep this for the main table column aggregation logic if needed elsewhere
        tasks_failed_all_sessions = 0 # New counter for tasks failing in all their sessions
        # --- START: Counters for unique task passes ---
        unique_tasks_passed_test = 0
        unique_tasks_passed_train = 0
        # --- END: Counters for unique task passes ---
        grand_total_steps = 0
        grand_total_duration = 0.0
        best_scores = []
        # ADDED token counters for summary
        grand_total_prompt_tokens = 0
        grand_total_candidates_tokens = 0
        grand_total_tokens_all_tasks = 0
        grand_total_weight = 0 # ADDED total weight counter

        for task_id, data in self.tasks_summary.items():
            num_sessions_for_task = len(data['sessions'])
            task_error_count = data['errors']

            total_sessions_involved.update(data['sessions'])
            total_errors += task_error_count # Keep aggregating total errors

            # --- START: Check if task failed in all its sessions ---
            if num_sessions_for_task > 0 and num_sessions_for_task == task_error_count:
                tasks_failed_all_sessions += 1
            # --- END: Check if task failed in all its sessions ---

            # --- START: Increment unique task pass counters ---
            if data['test_passed'] > 0: # Check if task passed test at least once
                unique_tasks_passed_test += 1
            if data['train_passed'] > 0: # Check if task passed train at least once
                unique_tasks_passed_train += 1
            # --- END: Increment unique task pass counters ---
            # Keep aggregating total passes if needed elsewhere, but don't use for summary display
            total_test_passed = data['test_passed'] # Example: If you still need the raw total somewhere
            total_train_passed = data['train_passed'] # Example: If you still need the raw total somewhere
            grand_total_steps += data['total_steps']
            grand_total_duration += data['total_duration']
            if data['best_score'] != float('inf'):
                best_scores.append(data['best_score'])
            # ADDED token aggregation for summary
            grand_total_prompt_tokens += data['total_prompt_tokens']
            grand_total_candidates_tokens += data['total_candidates_tokens']
            grand_total_tokens_all_tasks += data['total_tokens']
            # ADDED weight aggregation for summary
            weight_val = data.get('weight', 0)
            if weight_val >= 0: # Only add valid weights
                grand_total_weight += weight_val

        num_sessions = len(total_sessions_involved)
        best_overall_score = f"{min(best_scores):.2f}" if best_scores else "-"
        formatted_total_duration = self._format_duration(grand_total_duration)

        # --- START Calculate summary percentages/diffs ---
        test_percent = (unique_tasks_passed_test / total_unique_tasks * 100) if total_unique_tasks > 0 else 0.0
        test_percent_str = f"{test_percent:.1f}%"

        train_diff = unique_tasks_passed_test - unique_tasks_passed_train
        train_diff_str = f"{train_diff:+}" # Format with sign (+/-)

        error_percent = (tasks_failed_all_sessions / total_unique_tasks * 100) if total_unique_tasks > 0 else 0.0
        error_percent_str = f"{error_percent:.1f}%"
        # --- END Calculate summary percentages/diffs ---

        # Clear and update summary table
        summary_table.clear()
        summary_table.add_row(Text("tasks:", justify="right"), Text(str(total_unique_tasks), justify="right"))
        summary_table.add_row(Text("sessions:", justify="right"), Text(str(num_sessions), justify="right"))
        summary_table.add_row(Text("steps:", justify="right"), Text(str(grand_total_steps), justify="right"))
        summary_table.add_row(Text("time:", justify="right"), Text(formatted_total_duration, justify="right"))
        summary_table.add_row(Text("weight:", justify="right"), Text(f"{grand_total_weight:,}", justify="right")) # ADDED total weight

        # Clear and update trials table using unique task pass counts and calculated stats
        trials_table.clear()
        trials_table.add_row(
            Text("test:", justify="right"),
            Text(str(unique_tasks_passed_test), justify="right"),
            Text(test_percent_str, justify="right") # Add percentage
        )
        trials_table.add_row(
            Text("train:", justify="right"),
            Text(str(unique_tasks_passed_train), justify="right"),
            Text(train_diff_str, justify="right") # Add difference
        )
        trials_table.add_row(
            Text("errors:", justify="right"),
            Text(str(tasks_failed_all_sessions), justify="right"),
            Text(error_percent_str, justify="right") # Add percentage
        )
        # Removed best score row

        # Clear and update tokens table
        # Clear and update tokens table (Placeholder - needs data aggregation)
        tokens_table.clear()
        tokens_table.add_row(Text("in:", justify="right"), Text(f"{grand_total_prompt_tokens:,}", justify="right"))
        tokens_table.add_row(Text("out:", justify="right"), Text(f"{grand_total_candidates_tokens:,}", justify="right"))
        tokens_table.add_row(Text("total:", justify="right"), Text(f"{grand_total_tokens_all_tasks:,}", justify="right"))


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

    # --- START ADDED SORT METHOD ---
    def perform_sort(self, sort_key: ColumnKey) -> None:
        """Sorts the DataTable by the given column key."""
        log.info(f"Performing sort on TasksScreen by key: {sort_key}")

        # Determine sort direction
        reverse = False
        if self.current_sort_key == sort_key:
            reverse = not self.current_sort_reverse
        else:
            reverse = False # Default to ascending for new column

        self.current_sort_key = sort_key
        self.current_sort_reverse = reverse

        # Define key functions for different columns
        def get_sort_key(row_data):
            try:
                col_index = list(self.table.columns.keys()).index(sort_key)
                cell_data = row_data[col_index]
            except (ValueError, IndexError):
                log.error(f"Could not find index for sort key '{sort_key}'")
                return None

            key_str = str(sort_key)

            if key_str == "TASK":
                return cell_data # Simple string sort

            if key_str in ["SESSIONS", "ERRORS", "TEST", "TRAIN", "STEPS", "BEST", "IN", "OUT", "TOTAL", "WEIGHT"]: # ADDED WEIGHT
                # Handle numbers (potentially in Text objects)
                plain_text = cell_data.plain if hasattr(cell_data, 'plain') else str(cell_data)
                plain_text = plain_text.replace(',', '') # Remove commas
                if key_str == "WEIGHT" and plain_text in ["ERR", "?"]: return float('-inf') # Sort weight errors/unknown first
                if plain_text == "-": return float('-inf') # Sort '-' first
                try:
                    return float(plain_text)
                except ValueError:
                    log.warning(f"Could not convert '{plain_text}' to float for sorting key '{key_str}'")
                    return float('-inf') # Sort errors consistently first

            if key_str == "TIME":
                # Parse HH:MM:SS string into seconds
                time_str = cell_data.plain if hasattr(cell_data, 'plain') else str(cell_data)
                if time_str == "-": return -1
                try:
                    parts = list(map(int, time_str.split(':')))
                    if len(parts) == 3: return parts[0] * 3600 + parts[1] * 60 + parts[2]
                    else: return float('-inf')
                except ValueError:
                    log.warning(f"Could not parse time string '{time_str}' for sorting")
                    return float('-inf')

            # Fallback
            return cell_data.plain if hasattr(cell_data, 'plain') else str(cell_data)

        # Perform the sort
        try:
            # We need to sort the underlying data (self.tasks_summary) and then reload the table
            # DataTable.sort() works on the current rows, but we aggregate data dynamically.

            # 1. Get the current data into a list of tuples/dicts including the sort key value
            data_to_sort = []
            for task_id in self.sorted_task_ids:
                task_details = self.tasks_summary[task_id]
                # Create a temporary row structure similar to what get_sort_key expects
                # This needs to match the order of columns in the table
                row_tuple = (
                    task_id, # TASK
                    Text(str(len(task_details['sessions']))), # SESSIONS
                    Text(str(task_details['errors'])) if task_details['errors'] > 0 else Text("-"), # ERRORS
                    Text(str(task_details['test_passed'])), # TEST
                    Text(str(task_details['train_passed'])), # TRAIN
                    Text(str(task_details['total_steps'])), # STEPS
                    Text(self._format_duration(task_details['total_duration'])), # TIME
                    Text(f"{task_details['best_score']:.2f}" if task_details['best_score'] != float('inf') else "-"), # BEST
                    Text(f"{task_details['total_prompt_tokens']:,}" if task_details['total_prompt_tokens'] > 0 else "-"), # IN
                    Text(f"{task_details['total_candidates_tokens']:,}" if task_details['total_candidates_tokens'] > 0 else "-"), # OUT
                    Text(f"{task_details['total_tokens']:,}" if task_details['total_tokens'] > 0 else "-"), # TOTAL
                    # ADDED WEIGHT to tuple for sorting
                    Text(f"{task_details['weight']:,}" if task_details.get('weight', -2) >= 0 else ("ERR" if task_details.get('weight') == -1 else "?")), # WEIGHT
                )
                sort_value = get_sort_key(row_tuple)
                data_to_sort.append((task_id, sort_value))

            # 2. Sort the list based on the calculated sort_value
            data_to_sort.sort(key=lambda item: item[1], reverse=reverse)

            # 3. Update the order of task IDs
            self.sorted_task_ids = [item[0] for item in data_to_sort]

            # 4. Reload the table content using the new sorted order
            self.load_and_display_tasks() # This already clears and repopulates

            self.notify(f"Sorted by {str(self.table.columns[sort_key].label)} {'(desc)' if reverse else '(asc)'}")

        except Exception as e:
            log.error(f"Error during TasksScreen sort preparation or reload: {e}")
            self.notify(f"Error sorting table: {e}", severity="error")
            # Attempt to restore original sort order? Maybe just log.
            self.sorted_task_ids = sorted(self.tasks_summary.keys()) # Restore default sort
            self.load_and_display_tasks() # Reload with default sort

    # --- END ADDED SORT METHOD ---
