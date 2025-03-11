from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem
from textual.binding import Binding

from pathlib import Path


class TaskScreen(Screen):
    BINDINGS = [
        Binding("l", "select_row", "Select", show=False),
        Binding("k", "move_up", "Cursor up", show=False),
        Binding("j", "move_down", "Cursor down", show=False),
        Binding("h", "app.pop_screen", "back", show=False),
    ]

    def __init__(self, task_path: Path, navigator) -> None:
        super().__init__()
        self.task_path = task_path
        self.navigator = navigator

    def compose(self) -> ComposeResult:
        yield ListView(id="files_list")  # List files within the task
        yield Static(id="task_summary")

    def on_mount(self) -> None:
        self.update_files_list()

    def update_files_list(self):
        """Populates the files ListView."""
        list_view = self.query_one("#files_list", ListView)
        list_view.clear()

        for item in self.task_path.iterdir():
            list_view.append(ListItem(Static(str(item.name)), id=f"{item.name}"))  # Add unique ID

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#task_summary", Static)
        num_files = len(self.query_one("#files_list", ListView))
        summary.update(f"Files in {self.task_path.name}: {num_files}")

    def on_list_view_selected(self, event) -> None:
        """Handles file/directory selection within a task (if needed)."""
        selected_item_id = event.item.id #.removeprefix("file-")
        selected_item_path = self.task_path / selected_item_id
        #  Example: If you want to handle directory selection within a task:
        if selected_item_path.is_dir():
            # Do something, e.g., push another screen or update the current one
            pass  # Replace with your logic
        else:
            # It's a file.  Do something else (e.g., preview, open, etc.)
            pass # Replace with your logic
