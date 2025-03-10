import os
from pathlib import Path

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ListView, ListItem, DataTable
from textual import log  
from textual.containers import Horizontal, Vertical, Grid, ScrollableContainer # Import Grid

from geometor.seer.navigator.screens.session_screen import SessionScreen  # Import SessionScreen
from dataclasses import dataclass

@dataclass
class SessionInfo:
    name: str
    path: Path
    #  You can add other fields here later, like task count, etc.

class SessionsScreen(Screen):
    CSS = """
    DataTable {height: auto;}
    Static {padding: 1;}
    """

    def __init__(self, sessions: list[SessionInfo]) -> None:
        super().__init__()
        self.sessions = sessions
        #  self.navigator = navigator  # Store a reference to the main app


    def compose(self) -> ComposeResult:
        self.table = DataTable()
        self.table.add_columns("session", "tasks", "matches")
        with Vertical():
            yield self.table
            yield Static(id="sessions_summary")

    def on_mount(self) -> None:
        """Load initial sessions."""
        self.update_sessions_list()

    def update_sessions_list(self):
        for idx, session_info in enumerate(self.sessions):
            self.table.add_row(session_info.name)

        self.table.cursor_type = "row"
        self.table.focus()

        self.update_summary()

    def update_summary(self):
        summary = self.query_one("#sessions_summary", Static)
        num_sessions = len(self.sessions)  # Use the length of the sessions list
        summary.update(f"Total Sessions: {num_sessions}")

    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        row = self.table.get_row(event.row_key)
        selected_session = row[0]
        log(f"{event.row_key=}")
        session_path = self.app.sessions_root / selected_session
        log(f"{session_path=}")
        self.app.push_screen(SessionScreen(session_path))

    #  def on_list_view_selected(self, event) -> None:
        #  """Handles session selection."""
        #  selected_session_index = int(event.item.id.removeprefix("session-"))  # Extract index
        #  selected_session_info = self.sessions[selected_session_index]
        #  self.navigator.push_screen(SessionScreen(selected_session_info.path, self.navigator))
