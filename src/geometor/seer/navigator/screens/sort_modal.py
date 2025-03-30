from typing import Dict, TYPE_CHECKING

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Static # Import Static, remove Button
from textual.binding import Binding
from textual.widgets._data_table import ColumnKey # Import ColumnKey
from textual import log
from textual.screen import Screen # Import Screen directly

# Removed TYPE_CHECKING block and specific screen imports


class SortModal(Screen):
    """Modal dialog for selecting a column to sort."""

    CSS = """
    SortModal {
        align: center middle;
    }

    #sort-dialog {
        grid-size: 1; /* Changed to 1 column */
        grid-gutter: 1 2;
        grid-rows: auto auto; /* Explicitly define rows for label and instructions */
        padding: 0 1;
        width: auto;
        max-width: 80%; /* Limit width */
        height: auto;
        max-height: 80%; /* Limit height */
        border: thick $accent;
        background: $surface;
    }

    #sort-instructions { /* Style for the instructions */
        margin: 1 2;
        height: auto;
    }

    #sort-dialog > Label {
        /* width: 100%; */ /* No longer needed with grid-size: 1 */
        text-align: center;
        margin-bottom: 1;
    }
    """

    # BINDINGS will be generated dynamically

    def __init__(
        self,
        parent_screen: Screen, # Use the generic Screen type hint
        columns: Dict[ColumnKey, object], # Pass columns dict directly
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.parent_screen = parent_screen
        self.columns = columns
        self.key_to_column_map: Dict[str, ColumnKey] = {}
        self.key_bindings_text = ""
        bindings = [Binding("escape", "app.pop_screen", "Cancel", show=False)]
        key_options = "123456789abcdefghijklmnopqrstuvwxyz" # Available keys for binding
        key_index = 0

        key_lines = []
        for key, column in self.columns.items():
            if key_index >= len(key_options):
                log.warning("Ran out of keys for sort bindings!")
                break

            simple_key = key_options[key_index]
            self.key_to_column_map[simple_key] = key

            # Get column label safely
            column_label = "Unknown"
            if hasattr(column, 'label'):
                column_label = str(column.label.plain) if hasattr(column.label, 'plain') else str(column.label)

            key_lines.append(f"  Press '{simple_key}' to sort by '{column_label}'")
            bindings.append(Binding(simple_key, f"sort_by_key('{simple_key}')", f"Sort by {column_label}", show=False))
            key_index += 1

        self.key_bindings_text = "\n".join(key_lines)
        # Dynamically assign bindings
        self.BINDINGS = bindings # type: ignore

        log.info(f"SortModal initialized for screen: {parent_screen.__class__.__name__}")
        log.info(f"Sort bindings created: {self.key_bindings_text}")


    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Sort by which column?"),
            Static(self.key_bindings_text, id="sort-instructions"), # Display key bindings
            # Removed buttons
            id="sort-dialog",
        )

    def action_sort_by_key(self, key: str) -> None:
        """Sorts the parent screen's table based on the pressed key."""
        log.info(f"Sort key '{key}' pressed.")
        target_key = self.key_to_column_map.get(key)

        if target_key is not None:
            if hasattr(self.parent_screen, "perform_sort"):
                self.parent_screen.perform_sort(target_key)
                self.app.pop_screen() # Close modal after initiating sort
            else:
                log.error(f"Parent screen {self.parent_screen.__class__.__name__} has no perform_sort method.")
                self.app.notify("Sort function not implemented on parent screen.", severity="error")
                self.app.pop_screen()
        else:
            log.error(f"Could not find ColumnKey for sort key: {key}")
            self.app.notify("Error identifying sort column.", severity="error")
            self.app.pop_screen()

