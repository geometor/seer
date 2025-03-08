from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem
#  from textual.widgets.list_view import ListItemSelected
from pathlib import Path
#  from ..navigator2 import SessionNavigator  # Import for type hinting
from geometor.seer.navigator.screens.session_screen import SessionScreen  # Import SessionScreen
from dataclasses import dataclass

@dataclass
class SessionInfo:
    name: str
    path: Path
    #  You can add other fields here later, like task count, etc.

class SessionsScreen(Screen):
    def __init__(self, sessions: list[SessionInfo], navigator) -> None:
        super().__init__()
        self.sessions = sessions
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

        for idx, session_info in enumerate(self.sessions):
            list_view.append(ListItem(Static(session_info.name), id=f"session-{idx}"))  # Use index as ID

        self.update_summary()

    def update_summary(self):
        """Updates the summary panel."""
        summary = self.query_one("#sessions_summary", Static)
        num_sessions = len(self.sessions)  # Use the length of the sessions list
        summary.update(f"Total Sessions: {num_sessions}")

    def on_list_view_selected(self, event) -> None:
        """Handles session selection."""
        selected_session_index = int(event.item.id.removeprefix("session-"))  # Extract index
        selected_session_info = self.sessions[selected_session_index]
        self.navigator.push_screen(SessionScreen(selected_session_info.path, self.navigator))
