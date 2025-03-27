from pathlib import Path
import json
import yaml

from rich.text import Text

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import DataTable, Header, Footer, TextArea
from textual.binding import Binding
from textual import log


# Mapping file extensions to tree-sitter languages and TextArea theme
# Add more mappings as needed
LANGUAGE_MAP = {
    ".py": "python",
    ".md": "markdown",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".txt": None, # No specific language for plain text
    # Add other extensions if necessary
}
DEFAULT_THEME = "vscode_dark" # Changed from github_light to vscode_dark

class StepScreen(Screen):
    """Displays the files within a step folder and their content."""

    CSS = """
    Screen {
        layers: base overlay;
    }

    Horizontal {
        height: 1fr;
    }

    #file-list-container {
        width: 30%;
        border-right: thick $accent;
        height: 1fr;
        overflow-y: auto; /* Ensure DataTable scrolls if needed */
    }

    #file-content-container {
        width: 70%;
        height: 1fr;
    }

    DataTable {
       height: 100%; /* Make DataTable fill its container */
       width: 100%;
    }

    TextArea {
        height: 1fr;
        border: none; /* Remove default border if desired */
    }

    /* Style the focused row in the DataTable */
    DataTable > .datatable--cursor {
        background: $accent;
        color: $text;
    }
    DataTable:focus > .datatable--cursor {
         background: $accent-darken-1;
    }

    """

    BINDINGS = [
        Binding("j", "cursor_down", "Cursor Down", show=False),
        Binding("k", "cursor_up", "Cursor Up", show=False),
        Binding("enter", "select_file", "Select File", show=False),
        Binding("h", "app.pop_screen", "Back", show=True),
        # Binding("[", "previous_sibling", "Previous Sibling", show=True), # Handled by App
        # Binding("]", "next_sibling", "Next Sibling", show=True),     # Handled by App
    ]

    # Reactive variable to store the list of files
    file_paths = reactive([])
    selected_file_path = reactive(None)

    def __init__(self, session_path: Path, task_path: Path, step_path: Path) -> None:
        super().__init__()
        self.session_path = session_path
        self.task_path = task_path
        self.step_path = step_path
        self.step_name = step_path.name
        self.task_name = task_path.name
        self.session_name = session_path.name

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="file-list-container"):
                yield DataTable(id="file-list-table")
            with Vertical(id="file-content-container"):
                # Use code_editor for better defaults, but override read_only
                yield TextArea.code_editor(
                    "",
                    read_only=True,
                    show_line_numbers=True,
                    theme=DEFAULT_THEME,
                    id="file-content-area"
                )
        yield Footer()

    def on_mount(self) -> None:
        """Called when the screen is mounted."""
        self.title = f"{self.session_name} • {self.task_name} • {self.step_name}"

        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_column("Files", width=None) # Let width be automatic

        # List files in the step directory, sorted alphabetically
        try:
            # Filter for files only, ignore directories
            self.file_paths = sorted([f for f in self.step_path.iterdir() if f.is_file()])
        except FileNotFoundError:
            self.app.pop_screen() # Go back if path doesn't exist
            self.app.notify("Error: Step directory not found.", severity="error")
            return
        except Exception as e:
            log.error(f"Error listing files in {self.step_path}: {e}")
            self.app.pop_screen()
            self.app.notify(f"Error listing files: {e}", severity="error")
            return

        if not self.file_paths:
            table.add_row("No files found.")
            # Disable table focus if empty? Or allow focus but handle selection gracefully.
        else:
            for file_path in self.file_paths:
                table.add_row(file_path.name)

            # Select the first file by default and load its content
            self.select_row_index(0)
            table.focus() # Focus the table

    def select_row_index(self, index: int):
        """Selects a row by index and loads the corresponding file."""
        if 0 <= index < len(self.file_paths):
            table = self.query_one(DataTable)
            table.move_cursor(row=index, animate=False)
            self.selected_file_path = self.file_paths[index]
        else:
            self.selected_file_path = None # Clear selection if index is out of bounds

    # Watch for changes in selected_file_path and update TextArea
    def watch_selected_file_path(self, old_path: Path | None, new_path: Path | None) -> None:
        """Called when selected_file_path changes."""
        text_area = self.query_one(TextArea)
        if new_path:
            try:
                content = new_path.read_text()
                language = LANGUAGE_MAP.get(new_path.suffix.lower())

                # Check if language requires the 'syntax' extra
                if language and language not in text_area.available_languages:
                     # If language not available (likely missing 'syntax' extra),
                     # log a warning and fall back to no language.
                     log.warning(f"Language '{language}' for {new_path.name} not available. Install 'textual[syntax]' for highlighting.")
                     language = None # Fallback

                # Load text first, then set language
                text_area.load_text(content)
                text_area.language = language
                text_area.scroll_home(animate=False) # Scroll to top

            except Exception as e:
                log.error(f"Error loading file {new_path}: {e}")
                text_area.load_text(f"Error loading file:\n\n{e}")
                text_area.language = None # Reset language on error
        else:
            text_area.load_text("") # Clear text area if no file selected
            text_area.language = None

    def action_cursor_down(self) -> None:
        """Move the cursor down in the DataTable."""
        table = self.query_one(DataTable)
        current_row = table.cursor_row
        next_row = min(len(self.file_paths) - 1, current_row + 1)
        self.select_row_index(next_row)

    def action_cursor_up(self) -> None:
        """Move the cursor up in the DataTable."""
        table = self.query_one(DataTable)
        current_row = table.cursor_row
        prev_row = max(0, current_row - 1)
        self.select_row_index(prev_row)

    def action_select_file(self) -> None:
        """Action triggered by pressing Enter on the table (redundant with watch)."""
        # The watch_selected_file_path handles loading, so this might not be needed
        # unless we want explicit confirmation or other actions on Enter.
        # For now, it does nothing extra as selection triggers the load.
        pass

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle row selection in the DataTable."""
        # Ensure the index is valid before selecting
        if event.cursor_row is not None and 0 <= event.cursor_row < len(self.file_paths):
             self.select_row_index(event.cursor_row)
        else:
             self.selected_file_path = None # Clear if selection is invalid
