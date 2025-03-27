from pathlib import Path
import json
import yaml
import subprocess # Added for opening external programs
import shutil # Added to check if sxiv exists

from rich.text import Text

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import DataTable, Header, Footer, TextArea, Markdown, ContentSwitcher, Static # Added Static
from textual.binding import Binding
from textual import log


# Mapping file extensions to tree-sitter languages and TextArea theme
# Add more mappings as needed
LANGUAGE_MAP = {
    ".py": "python",
    ".md": "markdown", # Keep this for TextArea if needed, but Markdown widget handles .md
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

    /* Ensure ContentSwitcher and its children fill the container */
    ContentSwitcher {
        height: 1fr;
    }
    TextArea, Markdown, #image-viewer-placeholder { /* Added placeholder */
        height: 1fr;
        border: none; /* Remove default border if desired */
    }
    /* Ensure Markdown content is scrollable */
    Markdown {
        overflow-y: auto;
    }
    /* Center placeholder text */
    #image-viewer-placeholder {
        content-align: center middle;
        color: $text-muted;
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
        Binding("i", "view_images", "View Images", show=True), # ADDED binding
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
        self._sxiv_checked = False
        self._sxiv_path = None

    def _check_sxiv(self) -> str | None:
        """Check if sxiv exists and cache the path."""
        if not self._sxiv_checked:
            self._sxiv_path = shutil.which("sxiv")
            self._sxiv_checked = True
            if not self._sxiv_path:
                log.warning("'sxiv' command not found in PATH. Cannot open images externally.")
                self.app.notify("sxiv not found. Cannot open images.", severity="warning", timeout=5)
        return self._sxiv_path

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="file-list-container"):
                yield DataTable(id="file-list-table")
            with Vertical(id="file-content-container"):
                # Use a ContentSwitcher to toggle between viewers
                with ContentSwitcher(initial="text-viewer"):
                    yield TextArea.code_editor(
                        "",
                        read_only=True,
                        show_line_numbers=True,
                        theme=DEFAULT_THEME,
                        id="text-viewer" # ID for the TextArea
                    )
                    yield Markdown(id="markdown-viewer") # ID for the Markdown viewer
                    yield Static("Select a file to view its content.", id="image-viewer-placeholder") # Placeholder for images/other

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

    # Watch for changes in selected_file_path and update the appropriate viewer
    def watch_selected_file_path(self, old_path: Path | None, new_path: Path | None) -> None:
        """Called when selected_file_path changes."""
        switcher = self.query_one(ContentSwitcher)
        text_viewer = self.query_one("#text-viewer", TextArea)
        markdown_viewer = self.query_one("#markdown-viewer", Markdown)
        image_placeholder = self.query_one("#image-viewer-placeholder", Static) # Get placeholder

        if new_path:
            file_suffix = new_path.suffix.lower()

            if file_suffix == ".png":
                # Handle PNG files - show placeholder, don't open automatically
                image_placeholder.update(f"Selected: '{new_path.name}' (PNG)\n\nPress 'i' to view images.")
                switcher.current = "image-viewer-placeholder"

            elif file_suffix == ".md":
                # Handle Markdown files
                try:
                    content = new_path.read_text()
                    markdown_viewer.update(content)
                    switcher.current = "markdown-viewer"
                    markdown_viewer.scroll_home(animate=False) # Scroll Markdown to top
                except Exception as e:
                    log.error(f"Error loading Markdown file {new_path}: {e}")
                    # Display error in TextArea
                    error_content = f"Error loading file:\n\n{e}"
                    text_viewer.load_text(error_content)
                    text_viewer.language = None
                    switcher.current = "text-viewer"

            else:
                # Handle other text/code files
                try:
                    content = new_path.read_text()
                    language = LANGUAGE_MAP.get(file_suffix)

                    # Check if language requires the 'syntax' extra for TextArea
                    if language and language not in text_viewer.available_languages:
                         log.warning(f"Language '{language}' for {new_path.name} not available in TextArea. Install 'textual[syntax]' for highlighting.")
                         language = None # Fallback for TextArea

                    # Load text first, then set language for TextArea
                    text_viewer.load_text(content)
                    text_viewer.language = language
                    switcher.current = "text-viewer"
                    text_viewer.scroll_home(animate=False) # Scroll TextArea to top
                except Exception as e:
                    log.error(f"Error loading file {new_path}: {e}")
                    # Display error in TextArea
                    error_content = f"Error loading file:\n\n{e}"
                    text_viewer.load_text(error_content)
                    text_viewer.language = None
                    switcher.current = "text-viewer"

        else:
            # Clear all viewers if no file is selected
            text_viewer.load_text("")
            text_viewer.language = None
            markdown_viewer.update("")
            image_placeholder.update("No file selected.") # Reset placeholder
            switcher.current = "text-viewer" # Default to text viewer when empty

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
        # The watch_selected_file_path handles loading/opening, so this might not be needed
        # unless we want explicit confirmation or other actions on Enter.
        # For now, it does nothing extra as selection triggers the load/open.
        pass

    def action_view_images(self) -> None:
        """Find and open all PNG images in the current step directory using sxiv."""
        sxiv_cmd = self._check_sxiv()
        if not sxiv_cmd:
            return # sxiv not found, notification already shown

        try:
            # Find all .png files recursively within the step directory
            image_files = sorted(list(self.step_path.rglob("*.png")))

            if not image_files:
                self.app.notify("No PNG images found in this step.", severity="information")
                return

            # Prepare the command list
            command = [sxiv_cmd] + [str(img_path) for img_path in image_files]

            log.info(f"Opening {len(image_files)} images with sxiv from {self.step_path}")
            subprocess.Popen(command)

        except FileNotFoundError:
            # This case should be caught by _check_sxiv, but handle defensively
            log.error(f"'sxiv' command not found when trying to execute.")
            self.app.notify("sxiv not found. Cannot open images.", severity="error")
        except Exception as e:
            log.error(f"Error finding or opening images with sxiv from {self.step_path}: {e}")
            self.app.notify(f"Error viewing images: {e}", severity="error")


    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle row selection in the DataTable."""
        # Ensure the index is valid before selecting
        if event.cursor_row is not None and 0 <= event.cursor_row < len(self.file_paths):
             self.select_row_index(event.cursor_row)
        else:
             self.selected_file_path = None # Clear if selection is invalid
