from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container # Import Container
from pathlib import Path
import argparse
import json
import re
from textual import log # Added log
from textual.binding import Binding # Added Binding

from geometor.seer.navigator.screens.sessions_screen import SessionsScreen
from geometor.seer.navigator.screens.sessions_screen import SessionsScreen
from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.navigator.screens.task_screen import TaskScreen
from geometor.seer.navigator.screens.step_screen import StepScreen
# Import TrialViewer instead of TrialScreen
from geometor.seer.navigator.screens.trial_screen import TrialViewer

# Define DummyGrid first so it's always available
class DummyGrid(Static):
    """Placeholder widget used when real renderers fail to import."""
    def __init__(self, grid_data: list, *args, **kwargs):
        super().__init__("Renderer Import Error", *args, **kwargs)
        log.error("DummyGrid used - real renderer import failed.")

# Import renderers (adjust path if needed)
try:
    from geometor.seer.navigator.renderers import (
        SolidGrid,
        BlockGrid,
        CharGrid,
        TinyGrid,
    )
    RENDERERS = {
        "solid": SolidGrid,
        "block": BlockGrid,
        "char": CharGrid,
        "tiny": TinyGrid,
    }
except ImportError:
    log.error("Could not import grid renderers. Grid visualization will fail.")
    RENDERERS = {}
    # Assign the already defined DummyGrid in case of import failure
    SolidGrid = BlockGrid = CharGrid = TinyGrid = DummyGrid


class SessionNavigator(App):

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("[", "previous_sibling", "Previous Sibling"),
        Binding("]", "next_sibling", "Next Sibling"),
        # Add renderer bindings
        Binding("s", "set_renderer('solid')", "Solid", show=False), # Hide from footer
        Binding("c", "set_renderer('char')", "Char", show=False),   # Hide from footer
        Binding("b", "set_renderer('block')", "Block", show=False), # Hide from footer
        Binding("t", "set_renderer('tiny')", "Tiny", show=False),   # Hide from footer
        Binding("r", "refresh_screen", "Refresh", show=True),      # ADDED Refresh binding
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)
        # Initialize renderer state - DummyGrid is now guaranteed to be defined
        self.renderer = RENDERERS.get("solid", DummyGrid) # Default to SolidGrid or Dummy
        log.info(f"Initial renderer set to: {self.renderer.__name__}")


    def compose(self) -> ComposeResult:
        """Yield the initial container for the app's default screen."""
        # Yield an empty container to satisfy compose requirement.
        # The actual content is managed by pushing screens in on_mount.
        yield Container()

    def on_mount(self) -> None:
        # Push the initial screen
        self.push_screen(SessionsScreen(self.sessions_root))

    def action_previous_sibling(self) -> None:
        """Navigate to the previous sibling directory."""
        current_screen = self.screen
        if hasattr(current_screen, "previous_sibling"):
            current_screen.previous_sibling()


    def action_next_sibling(self) -> None:
        """Navigate to the next sibling directory."""
        current_screen = self.screen
        if hasattr(current_screen, "next_sibling"):
            current_screen.next_sibling()

    # Action to switch renderer
    def action_set_renderer(self, renderer_name: str) -> None:
        """Sets the grid renderer and refreshes the TrialScreen if active."""
        new_renderer = RENDERERS.get(renderer_name)
        if new_renderer and new_renderer != self.renderer:
            self.renderer = new_renderer
            log.info(f"Renderer changed to: {renderer_name}")
            self.notify(f"Renderer: {renderer_name.capitalize()}")

            # If the current screen is StepScreen, find the TrialViewer and refresh it
            if isinstance(self.screen, StepScreen):
                try:
                    # Find the TrialViewer widget within the StepScreen
                    trial_viewer = self.screen.query_one(TrialViewer)
                    # Update its renderer attribute
                    trial_viewer.renderer = new_renderer
                    # Refresh its display if it's the currently active view in the switcher
                    if self.screen.query_one("ContentSwitcher").current == "trial-viewer":
                        trial_viewer.refresh_display()
                except Exception as e:
                    # Catch potential errors if TrialViewer isn't found or refresh fails
                    log.error(f"Error refreshing TrialViewer in StepScreen: {e}")

        elif not new_renderer:
            log.warning(f"Unknown renderer name: {renderer_name}")

    def action_refresh_screen(self) -> None:
        """Calls the refresh method on the current screen if it exists."""
        current_screen = self.screen
        if hasattr(current_screen, "refresh_content"):
            log.info(f"Refreshing screen: {current_screen.__class__.__name__}")
            current_screen.refresh_content()
            self.notify("Screen refreshed")
        else:
            log.warning(f"Screen {current_screen.__class__.__name__} has no refresh_content method.")
            self.notify("Refresh not supported on this screen", severity="warning")


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
