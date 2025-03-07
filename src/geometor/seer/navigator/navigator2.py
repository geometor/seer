from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Footer, Header, Static, ListView, ListItem
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
import os
from pathlib import Path


class TaskSummary(Static):
    """A widget to display summary information about the selected task."""

    # Reactive variable to store file list
    files: reactive[list[str]] = reactive([])
    num_files: reactive[int] = reactive(0)

    def watch_files(self, files: list[str]) -> None:
        """Called when the 'files' reactive attribute changes."""
        self.num_files = len(files)
        self.update(self.render_summary())  # updates when list of files is updated

    def render_summary(self) -> str:
        """Generates the summary content based on the current task."""
        summary_lines = []
        # Add some basic information
        summary_lines.append(f"Number of Files: {self.num_files}")

        for file_path in self.files:
            summary_lines.append(f"- {file_path}")

        return "\n".join(summary_lines)


class SessionNavigator(App):
    """Main application for navigating ARC test sessions."""

    BINDINGS = [
        ("j", "move_down", "Move Down"),
        ("k", "move_up", "Move Up"),
        ("h", "move_left", "Move Left"),
        ("l", "move_right", "Move Right"),
        ("/", "filter_files", "Filter Files"),
        (
            "t",
            "show_test_results",
            "Show Test Results",
        ),  # Example: Switch to test results screen
        ("ctrl+q", "quit", "Quit"),  # add quit binding
    ]

    selected_path: reactive[Path | None] = reactive(None)

    def compose(self) -> ComposeResult:
        """Creates the initial layout."""
        with Horizontal():
            self.directory_tree = DirectoryTree(
                "./sessions", id="tree"
            )  # starts in sessions folder
            yield self.directory_tree
            self.task_summary = TaskSummary(id="summary")
            yield self.task_summary

    def on_mount(self) -> None:
        """Sets up initial state."""
        self.directory_tree.focus()

    def on_directory_tree_directory_selected(
        self, event: DirectoryTree.DirectorySelected
    ):
        """Handles directory selection in the DirectoryTree."""
        self.selected_path = event.path
        self.update_summary()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        """Handles file selection (if needed for preview).  For now, just does nothing"""
        pass

    def update_summary(self):
        """Updates the summary panel based on the selected path."""
        if self.selected_path:
            if self.selected_path.is_dir():
                # get all the files
                all_files = [f.name for f in self.selected_path.iterdir()]
                # update the task summary with files
                self.task_summary.files = all_files

    def action_move_down(self) -> None:
        """Moves the selection down in the DirectoryTree."""
        self.directory_tree.action_cursor_down()

    def action_move_up(self) -> None:
        """Moves the selection up in the DirectoryTree."""
        self.directory_tree.action_cursor_up()

    def action_move_left(self) -> None:
        """Moves to parent directory"""
        self.directory_tree.action_select_parent()

    def action_move_right(self) -> None:
        """Moves to the child directory"""
        self.directory_tree.action_select_node()

    def action_filter_files(self) -> None:
        """Placeholder for file filtering (implementation details below)."""
        # 1.  Prompt the user for a filter string (e.g., using an Input widget on a modal screen).
        # 2.  Use self.selected_path.glob(filter_string) to get a filtered list of files.
        # 3.  Update self.task_summary.files with the filtered list.
        pass

    def action_show_test_results(self) -> None:
        """Switches to the test results screen (implementation details below)."""
        # self.push_screen(TestResultsScreen(self.selected_path))  # Assuming you create a TestResultsScreen
        pass

    def action_quit(self) -> None:
        """Quits the application"""
        self.exit()


if __name__ == "__main__":
    app = SessionNavigator()
    app.run()
