import json
from pathlib import Path
from typing import List, Tuple, Any

from rich.text import Text

from textual.app import ComposeResult, App
from textual.containers import ScrollableContainer, Grid
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual import log
from textual.binding import Binding # Added Binding import

# Import renderers (assuming they are accessible)
# Adjust the import path if necessary based on your project structure
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
    # Define dummy classes if import fails to prevent NameErrors later
    class DummyGrid(Static):
        def __init__(self, grid_data: Any, *args, **kwargs):
            super().__init__("Renderer Error", *args, **kwargs)
    SolidGrid = BlockGrid = CharGrid = TinyGrid = DummyGrid


# Helper function to parse grid strings
def _parse_grid_string(grid_str: str) -> List[List[int]]:
    """Parses a string like '0 1\n2 3' into a list of lists of ints."""
    if not grid_str:
        return []
    try:
        return [[int(cell) for cell in row.split()] for row in grid_str.strip().split('\n')]
    except ValueError:
        log.error(f"Failed to parse grid string: {grid_str}")
        return [] # Return empty list on parsing error

class TrialScreen(Screen):
    """Displays the input, expected output, and actual output grids from a trial.json file."""

    CSS = """
    Screen {
        layers: base overlay;
    }
    ScrollableContainer {
        width: 1fr;
        height: 1fr;
        border: heavy $accent;
        border-title-align: center;
    }
    Grid {
        grid-size: 3; /* Default, will be updated */
        grid-gutter: 1 2;
        grid-rows: auto;
        padding: 1 2;
        align: center top;
    }
    /* Style for labels */
    .label {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }
    .trial-set-label {
        column-span: 3;
        width: 100%;
        text-align: center;
        text-style: bold underline;
        margin-top: 2;
        margin-bottom: 1;
    }
    """

    # No specific bindings here, renderer switching is handled by the App
    BINDINGS = [
        Binding("h", "app.pop_screen", "Back", show=True),
        # Renderer bindings are inherited from the App level
    ]

    def __init__(self, trial_path: Path, session_name: str, task_name: str, step_name: str) -> None:
        super().__init__()
        self.trial_path = trial_path
        self.session_name = session_name
        self.task_name = task_name
        self.step_name = step_name
        self.trial_data = None
        self.grid_container = Grid() # Initialize Grid container

    def compose(self) -> ComposeResult:
        yield Header()
        # Use ScrollableContainer to ensure content can scroll if it exceeds screen size
        yield ScrollableContainer(self.grid_container)
        yield Footer()

    def on_mount(self) -> None:
        """Load data and display trials when the screen is mounted."""
        file_name = self.trial_path.name
        self.title = f"{self.session_name} • {self.task_name} • {self.step_name} • {file_name}"
        self.load_and_display()

    def load_and_display(self):
        """Loads the trial JSON and populates the grid."""
        try:
            with open(self.trial_path, "r") as f:
                self.trial_data = json.load(f)
        except FileNotFoundError:
            log.error(f"Trial file not found: {self.trial_path}")
            self.grid_container.mount(Static(f"Error: File not found\n{self.trial_path}"))
            return
        except json.JSONDecodeError as e:
            log.error(f"Error decoding JSON from {self.trial_path}: {e}")
            self.grid_container.mount(Static(f"Error: Invalid JSON file\n{self.trial_path}\n{e}"))
            return
        except Exception as e:
            log.error(f"An unexpected error occurred loading {self.trial_path}: {e}")
            self.grid_container.mount(Static(f"Error: Could not load file\n{self.trial_path}\n{e}"))
            return

        self.display_trials()

    def display_trials(self) -> None:
        """Clears and repopulates the grid container with trial data using the current renderer."""
        if not self.trial_data:
            return # Should have been handled by load_and_display, but check again

        # Get the current renderer from the App
        # Ensure the app instance is correctly typed or accessed
        app = self.app
        if not hasattr(app, 'renderer') or not RENDERERS:
             log.error("Renderer not available in App or renderers failed to import.")
             self.grid_container.mount(Static("Error: Grid renderer not available."))
             return

        current_renderer = app.renderer

        # Clear previous content
        self.grid_container.remove_children()
        self.grid_container.clear_styles() # Clear grid styles like grid-size

        row_count = 0
        widgets_to_mount = []

        # Process Train trials
        train_trials = self.trial_data.get("train", {}).get("trials", [])
        if train_trials:
            widgets_to_mount.append(Static("Train Set", classes="trial-set-label"))
            row_count += 1
            widgets_to_mount.extend([
                Static("Input", classes="label"),
                Static("Expected Output", classes="label"),
                Static("Actual Output", classes="label"),
            ])
            row_count += 1
            for i, trial in enumerate(train_trials):
                input_grid_data = _parse_grid_string(trial.get("input", ""))
                expected_grid_data = _parse_grid_string(trial.get("expected_output", ""))
                actual_grid_data = _parse_grid_string(trial.get("transformed_output", ""))

                widgets_to_mount.extend([
                    current_renderer(input_grid_data) if input_grid_data else Static("No Input"),
                    current_renderer(expected_grid_data) if expected_grid_data else Static("No Expected Output"),
                    current_renderer(actual_grid_data) if actual_grid_data else Static("No Actual Output"),
                ])
                row_count += 1

        # Process Test trials
        test_trials = self.trial_data.get("test", {}).get("trials", [])
        if test_trials:
            widgets_to_mount.append(Static("Test Set", classes="trial-set-label"))
            row_count += 1
            widgets_to_mount.extend([
                Static("Input", classes="label"),
                Static("Expected Output", classes="label"),
                Static("Actual Output", classes="label"),
            ])
            row_count += 1
            for i, trial in enumerate(test_trials):
                input_grid_data = _parse_grid_string(trial.get("input", ""))
                expected_grid_data = _parse_grid_string(trial.get("expected_output", ""))
                actual_grid_data = _parse_grid_string(trial.get("transformed_output", ""))

                widgets_to_mount.extend([
                    current_renderer(input_grid_data) if input_grid_data else Static("No Input"),
                    current_renderer(expected_grid_data) if expected_grid_data else Static("No Expected Output"),
                    current_renderer(actual_grid_data) if actual_grid_data else Static("No Actual Output"),
                ])
                row_count += 1

        if not widgets_to_mount:
            self.grid_container.mount(Static("No trial data found in file."))
        else:
            # Set grid size before mounting
            self.grid_container.styles.grid_size_columns = 3
            # Set grid_rows dynamically based on content
            self.grid_container.styles.grid_rows = " ".join(["auto"] * row_count)
            self.grid_container.mount_all(widgets_to_mount)

        self.query_one(ScrollableContainer).scroll_home(animate=False) # Scroll to top after refresh

    def refresh_display(self) -> None:
        """Refreshes the grid display using the current renderer."""
        log.info(f"Refreshing TrialScreen display with renderer: {self.app.renderer.__name__}")
        self.display_trials()

