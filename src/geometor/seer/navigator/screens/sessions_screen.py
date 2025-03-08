from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem
#  from textual.widgets.list_view import ListItemSelected
from pathlib import Path
#  from ..navigator2 import SessionNavigator  # Import for type hinting
from geometor.seer.navigator.screens.session_screen import SessionScreen  # Import SessionScreen


class SessionsScreen(Screen):
    def __init__(self, session_root: str, navigator) -> None:
        super().__init__()
        self.session_root = Path(session_root)
        self.navigator = navigator  # Store a reference to the main app

    def compose(self) -> ComposeResult:
        yield ListView(id="sessions_list")
        yield Static(id="sessions_summary")

    def on_mount(self) -> None:
        """Load initial sessions."""
        self.update_sessions_list()

    def update_sessions_list(self):
        """Populates the sessions ListView."""
        list_view = self.query_one("#sessions_list", ListView)
        list_view.clear()

        for session_dir in self.session_root.iterdir():
            if session_dir.is_dir():
                list_view.append(ListItem(Static(str(session_dir.name)), id=f"session-{session_dir.name.replace('.', '-')}"))  # Add unique ID

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#sessions_summary", Static)
        num_sessions = len(self.query_one("#sessions_list", ListView))
        summary.update(f"Total Sessions: {num_sessions}")

    def on_list_view_selected(self, event) -> None:
        """Handles session selection."""
        selected_session_id = event.item.id.removeprefix("session-")  # Extract session name from ID
        selected_session_path = self.session_root / selected_session_id
        self.navigator.push_screen(SessionScreen(selected_session_path, self.navigator))
