from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container # Import Container
from pathlib import Path
import argparse
import json
import re
import subprocess # ADDED import
import shutil # ADDED import
from textual import log # Added log
from textual.binding import Binding # Added Binding

# Import screens
from geometor.seer.navigator.screens.sessions_screen import SessionsScreen
from geometor.seer.navigator.screens.session_screen import SessionScreen
from geometor.seer.navigator.screens.task_screen import TaskScreen
from geometor.seer.navigator.screens.step_screen import StepScreen
# Import TrialViewer instead of TrialScreen
from geometor.seer.navigator.screens.trial_screen import TrialViewer
# Import the modal screen
from geometor.seer.navigator.screens.image_view_modal import ImageViewModal

# Define DummyGrid first so it's always available
class DummyGrid(Static):
    """Placeholder widget used when real renderers fail to import."""
    def __init__(self, grid_data: list, *args, **kwargs):
        super().__init__("Renderer Import Error", *args, **kwargs)
        log.error("DummyGrid used - real renderer import failed.")

# Import renderers (adjust path if needed)
try:
    from geometor.seer_navigator.renderers import (
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
        #  Binding("[", "previous_sibling", "Previous Sibling"),
        #  Binding("]", "next_sibling", "Next Sibling"),
        # Add renderer bindings
        Binding("s", "set_renderer('solid')", "Solid", show=False), # Hide from footer
        Binding("c", "set_renderer('char')", "Char", show=False),   # Hide from footer
        Binding("b", "set_renderer('block')", "Block", show=False),
        Binding("t", "set_renderer('tiny')", "Tiny", show=False),
        Binding("r", "refresh_screen", "Refresh", show=True),
        Binding("i", "view_images", "View Images", show=True), # ADDED image view binding
        Binding("s", "sort_table", "Sort Table", show=True),   # ADDED sort binding
    ]

    def __init__(self, sessions_root: str = "./sessions"):
        super().__init__()
        self.sessions_root = Path(sessions_root)
        # Initialize renderer state - DummyGrid is now guaranteed to be defined
        self.renderer = RENDERERS.get("solid", DummyGrid) # Default to SolidGrid or Dummy
        #  log.info(f"Initial renderer set to: {self.renderer.__name__}")
        self._sxiv_checked = False # ADDED sxiv check state
        self._sxiv_path = None     # ADDED sxiv path cache


    def compose(self) -> ComposeResult:
        """Yield the initial container for the app's default screen."""
        # Yield an empty container to satisfy compose requirement.
        # The actual content is managed by pushing screens in on_mount.
        yield Container()

    def on_mount(self) -> None:
        # Push the initial screen
        # Import screen locally to avoid circular dependency if ScreensScreen imports App features implicitly
        from geometor.seer_navigator.screens.sessions_screen import SessionsScreen
        self.push_screen(SessionsScreen(self.sessions_root))

    # --- START ADDED SXIV CHECK ---
    def _check_sxiv(self) -> str | None:
        """Check if sxiv exists and cache the path."""
        if not self._sxiv_checked:
            self._sxiv_path = shutil.which("sxiv")
            self._sxiv_checked = True
            if not self._sxiv_path:
                log.warning("'sxiv' command not found in PATH. Cannot open images externally.")
                self.notify("sxiv not found. Cannot open images.", severity="warning", timeout=5)
        return self._sxiv_path
    # --- END ADDED SXIV CHECK ---

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

    # --- START ADDED IMAGE VIEWING ACTIONS ---
    def action_view_images(self) -> None:
        """Pushes the image view modal screen."""
        current_screen = self.screen
        context_path = None

        # Determine context path based on the current screen
        if isinstance(current_screen, SessionsScreen):
            context_path = current_screen.sessions_root
        elif isinstance(current_screen, SessionScreen):
            context_path = current_screen.session_path
        elif isinstance(current_screen, TaskScreen):
            context_path = current_screen.task_path
        elif isinstance(current_screen, StepScreen):
            context_path = current_screen.step_path
        else:
            log.warning(f"Image viewing not supported on screen: {current_screen.__class__.__name__}")
            self.notify("Image viewing not supported here.", severity="warning")
            return

        if context_path:
            log.info(f"Pushing ImageViewModal with context: {context_path}")
            self.push_screen(ImageViewModal(context_path=context_path))
        else:
            log.error("Could not determine context path for image viewing.")
            self.notify("Error determining context for image viewing.", severity="error")

    def launch_sxiv(self, context_path: Path, filter_type: str) -> None:
        """Finds images based on filter and launches sxiv."""
        sxiv_cmd = self._check_sxiv()
        if not sxiv_cmd:
            return # sxiv not found, notification already shown

        image_files = []
        try:
            log.info(f"Searching for images in {context_path} with filter: {filter_type}")
            if filter_type == "all":
                image_files = sorted(list(context_path.rglob("*.png")))
            elif filter_type == "tasks":
                # Find task.png files recursively
                image_files = sorted(list(context_path.rglob("task.png")))
            elif filter_type == "trials":
                # Find *trial.png files recursively
                image_files = sorted(list(context_path.rglob("*trial.png")))
            elif filter_type == "passed_trials":
                # Find *trial.png files where the corresponding .json shows test success
                image_files = []
                json_files = list(context_path.rglob("*trial.json")) # Find all trial json files first
                log.info(f"Found {len(json_files)} *trial.json files for passed_trials filter.")
                for json_file in json_files:
                    try:
                        with open(json_file, "r") as f:
                            trial_data = json.load(f)
                        # Check if 'test' trials exist and any have "match": true
                        test_trials = (trial_data.get("test") or {}).get("trials", [])
                        if any(trial.get("match") is True for trial in test_trials):
                            # Construct the expected PNG filename
                            png_filename = json_file.stem + ".png" # e.g., "code_00_trial.json" -> "code_00_trial.png"
                            png_path = json_file.with_name(png_filename)
                            if png_path.exists():
                                image_files.append(png_path)
                                log.debug(f"Adding passed trial image: {png_path}")
                            else:
                                log.warning(f"Passed trial JSON found ({json_file}), but corresponding PNG not found: {png_path}")
                    except json.JSONDecodeError:
                        log.error(f"Could not decode JSON for passed_trials filter: {json_file}")
                    except Exception as e:
                        log.error(f"Error processing {json_file} for passed_trials filter: {e}")
                image_files = sorted(image_files) # Sort the found images
            else:
                log.warning(f"Unknown image filter type: {filter_type}")
                self.notify(f"Unknown image filter: {filter_type}", severity="warning")
                return

            if not image_files:
                self.notify(f"No images found for filter '{filter_type}' in {context_path.name}.", severity="information")
                log.info(f"No images found for filter '{filter_type}' in {context_path}")
                return

            # Prepare the command list
            command = [sxiv_cmd] + [str(img_path) for img_path in image_files]

            log.info(f"Opening {len(image_files)} images with sxiv (filter: {filter_type})")
            subprocess.Popen(command)

        except FileNotFoundError:
            # This case should be caught by _check_sxiv, but handle defensively
            log.error(f"'sxiv' command not found when trying to execute.")
            self.notify("sxiv not found. Cannot open images.", severity="error")
        except Exception as e:
            log.error(f"Error finding or opening images with sxiv from {context_path}: {e}")
            self.notify(f"Error viewing images: {e}", severity="error")
    # --- END ADDED IMAGE VIEWING ACTIONS ---

    # --- START ADDED SORT ACTION ---
    def action_sort_table(self) -> None:
        """Pushes the sort modal screen for the current data table."""
        current_screen = self.screen

        # Check if the current screen has a sortable table
        if hasattr(current_screen, "table") and hasattr(current_screen, "perform_sort"):
            table = current_screen.table
            columns = table.columns # Get the columns dictionary

            if not columns:
                self.notify("No columns available to sort.", severity="warning")
                return

            log.info(f"Pushing SortModal for screen: {current_screen.__class__.__name__}")
            # Pass the parent screen instance and the columns dict
            self.push_screen(SortModal(parent_screen=current_screen, columns=columns))
        else:
            log.warning(f"Sorting not supported on screen: {current_screen.__class__.__name__}")
            self.notify("Sorting not supported on this screen.", severity="warning")
    # --- END ADDED SORT ACTION ---

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
