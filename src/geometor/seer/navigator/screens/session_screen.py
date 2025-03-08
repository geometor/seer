from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem
#  from textual.widgets.list_view import ListItemSelected
from pathlib import Path
#  from ..navigator2 import SessionNavigator  # Import for type hinting
from geometor.seer.navigator.screens.task_screen import TaskScreen  # Import TaskScreen


class SessionScreen(Screen):
    def __init__(self, session_path: Path, navigator) -> None:
        super().__init__()
        self.session_path = session_path
        self.navigator = navigator

    def compose(self) -> ComposeResult:
        yield ListView(id="tasks_list")
        yield Static(id="session_summary")

    def on_mount(self) -> None:
        self.update_tasks_list()

    def update_tasks_list(self):
        """Populates the tasks ListView."""
        list_view = self.query_one("#tasks_list", ListView)
        list_view.clear()

        for task_dir in self.session_path.iterdir():
            if task_dir.is_dir():
                list_view.append(ListItem(Static(str(task_dir.name)), id=f"task-{task_dir.name}"))  # Add unique ID

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#session_summary", Static)
        num_tasks = self.query_one("#tasks_list", ListView).child_count
        summary.update(f"Tasks in {self.session_path.name}: {num_tasks}")

    def on_list_view_selected(self, event) -> None:
        """Handles task selection."""
        selected_task_id = event.item.id.removeprefix("task-")
        selected_task_path = self.session_path / selected_task_id
        self.navigator.push_screen(TaskScreen(selected_task_path, self.navigator))
