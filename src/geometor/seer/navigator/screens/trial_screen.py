import json
from pathlib import Path
from typing import List, Tuple, Any

from rich.text import Text

from textual.app import ComposeResult
# Alias textual.containers.Grid to avoid name collision
from textual.containers import ScrollableContainer, Grid as TextualGrid, VerticalScroll
from textual.widgets import Static, DataTable # Removed Header, Footer, Screen
from textual import log
# Removed Binding import

# Import renderers (assuming they are accessible)
# Adjust the import path if necessary based on your project structure
from geometor.seer.tasks.grid import Grid, string_to_grid

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

class TrialViewer(ScrollableContainer):
    """Displays the input, expected output, and actual output grids from a trial.json file."""

    DEFAULT_CSS = """
    TrialViewer {
        /* Inherit background from parent */
    }
    .trial-grid {
        grid-size: 4; /* Details, Input, Expected, Actual */
        grid-gutter: 1 2;
        grid-rows: auto;
        padding: 1 2;
        align: center top;
        border-bottom: thick $accent-darken-1;
        height: auto; /* Fit content height */
        margin-bottom: 1;
    }
    .trial-details-table {
        height: auto; /* Fit content height */
        border: none; /* No border for summary tables */
        width: auto; /* Fit content width */
    }
    /* Ensure no focus border on summary tables */
    .trial-details-table:focus {
        border: none;
    }
    .trial-set-label {
        width: 100%;
        text-align: center;
        text-style: bold underline;
        margin-top: 2;
        margin-bottom: 1;
    }
    /* Style for grid labels (optional, if needed above each grid) */
    .grid-label {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }
    """

    def __init__(self, trial_path: Path | None = None, renderer: type[Static] = SolidGrid, **kwargs) -> None:
        super().__init__(**kwargs)
        self.trial_path = trial_path
        self.renderer = renderer
        self.trial_data = None
        # Container to hold all trial grids
        self.trials_container = VerticalScroll(id="trials-container")

    def compose(self) -> ComposeResult:
        # Yield the container that will hold the trial grids
        yield self.trials_container

    def on_mount(self) -> None:
        """Load data and display trials when the widget is mounted or path changes."""
        if self.trial_path:
            self.load_and_display()

    def load_and_display(self):
        """Loads the trial JSON and populates the trials container."""
        # Clear previous content first
        self.trials_container.remove_children()

        if not self.trial_path:
            self.trials_container.mount(Static("No trial file specified."))
            return

        try:
            with open(self.trial_path, "r") as f:
                self.trial_data = json.load(f)
        except FileNotFoundError:
            log.error(f"Trial file not found: {self.trial_path}")
            self.trials_container.mount(Static(f"Error: File not found\n{self.trial_path}"))
            return
        except json.JSONDecodeError as e:
            log.error(f"Error decoding JSON from {self.trial_path}: {e}")
            self.trials_container.mount(Static(f"Error: Invalid JSON file\n{self.trial_path}\n{e}"))
            return
        except Exception as e:
            log.error(f"An unexpected error occurred loading {self.trial_path}: {e}")
            self.trials_container.mount(Static(f"Error: Could not load file\n{self.trial_path}\n{e}"))
            return

        self.display_trials()
        self.scroll_home(animate=False) # Scroll viewer to top

    def _create_details_table(self, trial_dict: dict) -> DataTable:
        """Creates a DataTable widget for a single trial's details."""
        table = DataTable(
                classes="trial-details-table", 
                show_header=False, 
                cursor_type=None)
        table.add_columns("Metric", "Value")

        def format_bool(value):
            if value is True: return Text("✔", style="green")
            if value is False: return Text("✘", style="red")
            return Text("-")

        def format_float(value, precision=1):
            return Text(f"{value:.{precision}f}" if value is not None else "-")

        def format_int(value):
            return Text(str(value) if value is not None else "-")

        details = [
            ("Match", format_bool(trial_dict.get("match"))),
            ("Score", format_int(trial_dict.get("score"))),
            ("Size OK", format_bool(trial_dict.get("size_correct"))),
            ("Palette OK", format_bool(trial_dict.get("color_palette_correct"))),
            ("Count OK", format_bool(trial_dict.get("color_count_correct"))),
            ("Pixels Off", format_int(trial_dict.get("pixels_off"))),
            ("% Correct", format_float(trial_dict.get("percent_correct"))),
        ]

        for key, value in details:
            table.add_row(Text(f"{key}:", justify="right"), value)

        return table

    def display_trials(self) -> None:
        """Clears and repopulates the trials container with trial data using the current renderer."""
        # Clear previous content
        self.trials_container.remove_children()

        if not self.trial_data:
            self.trials_container.mount(Static("No trial data loaded."))
            return

        if not RENDERERS:
             log.error("Renderers failed to import.")
             self.trials_container.mount(Static("Error: Grid renderer not available."))
             return

        current_renderer = self.renderer # Use the renderer passed during init or updated

        widgets_to_mount = []

        # Process Train trials
        # Use `or {}` to handle cases where the key exists but the value is None
        train_trials = (self.trial_data.get("train") or {}).get("trials", [])
        if train_trials:
            widgets_to_mount.append(Static("Train Set", classes="trial-set-label"))
            # Optional: Add labels above the grid columns if desired
            # widgets_to_mount.append(Grid(
            #     Static("Details", classes="grid-label"),
            #     Static("Input", classes="grid-label"),
            #     Static("Expected", classes="grid-label"),
            #     Static("Actual", classes="grid-label"),
            #     classes="trial-grid-labels" # Add specific class if needed
            # ))
            for i, trial in enumerate(train_trials):
                # Use string_to_grid and extract the numpy array or use []
                input_grid_obj = string_to_grid(trial.get("input", ""))
                input_grid_data = input_grid_obj.grid if input_grid_obj else []
                expected_grid_obj = string_to_grid(trial.get("expected_output", ""))
                expected_grid_data = expected_grid_obj.grid if expected_grid_obj else []
                actual_grid_obj = string_to_grid(trial.get("transformed_output", ""))
                actual_grid_data = actual_grid_obj.grid if actual_grid_obj else []

                # Use the aliased TextualGrid for layout
                trial_grid = TextualGrid(
                    self._create_details_table(trial),
                    current_renderer(input_grid_data), # Pass numpy array or []
                    current_renderer(expected_grid_data), # Pass numpy array or []
                    current_renderer(actual_grid_data), # Pass numpy array or []
                    classes="trial-grid"
                    # id=f"train-trial-{i}" # REMOVED ID
                )
                widgets_to_mount.append(trial_grid)

        # Process Test trials
        # Use `or {}` to handle cases where the key exists but the value is None
        test_trials = (self.trial_data.get("test") or {}).get("trials", [])
        if test_trials:
            widgets_to_mount.append(Static("Test Set", classes="trial-set-label"))
            # Optional: Add labels above the grid columns if desired
            for i, trial in enumerate(test_trials):
                # Use string_to_grid and extract the numpy array or use []
                input_grid_obj = string_to_grid(trial.get("input", ""))
                input_grid_data = input_grid_obj.grid if input_grid_obj else []
                expected_grid_obj = string_to_grid(trial.get("expected_output", ""))
                expected_grid_data = expected_grid_obj.grid if expected_grid_obj else []
                actual_grid_obj = string_to_grid(trial.get("transformed_output", ""))
                actual_grid_data = actual_grid_obj.grid if actual_grid_obj else []

                # Use the aliased TextualGrid for layout
                trial_grid = TextualGrid(
                    self._create_details_table(trial),
                    current_renderer(input_grid_data), # Pass numpy array or []
                    current_renderer(expected_grid_data), # Pass numpy array or []
                    current_renderer(actual_grid_data), # Pass numpy array or []
                    classes="trial-grid"
                    # id=f"test-trial-{i}" # REMOVED ID
                )
                widgets_to_mount.append(trial_grid)

        if not widgets_to_mount:
            self.trials_container.mount(Static("No trial data found in file."))
        else:
            self.trials_container.mount_all(widgets_to_mount)


    def refresh_display(self) -> None:
        """Refreshes the grid display using the current renderer."""
        log.info(f"Refreshing TrialViewer display with renderer: {self.renderer.__name__}")
        # Reload and display data
        self.load_and_display()

