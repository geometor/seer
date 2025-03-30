from typing import Dict, TYPE_CHECKING

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Label
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
        grid-size: 2; /* Adjust grid size if needed */
        grid-gutter: 1 2;
        grid-rows: auto;
        padding: 0 1;
        width: auto;
        max-width: 80%; /* Limit width */
        height: auto;
        max-height: 80%; /* Limit height */
        border: thick $accent;
        background: $surface;
    }

    #sort-dialog > Label {
        column-span: 2;
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }

    #sort-dialog > Button {
        width: 100%;
    }
    """

    BINDINGS = [
        Binding("escape", "app.pop_screen", "Cancel", show=False),
    ]

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
        self.button_id_to_key_map: Dict[str, ColumnKey] = {} # Map generated ID to ColumnKey
        log.info(f"SortModal initialized for screen: {parent_screen.__class__.__name__}")

    def compose(self) -> ComposeResult:
        buttons = []
        # Create buttons for all columns passed to the modal
        # Use enumerate to get index for generating valid IDs
        for index, (key, column) in enumerate(self.columns.items()):
            # Generate a valid ID using the column index
            button_id = f"sort_col_{index}"
            self.button_id_to_key_map[button_id] = key # Store mapping
            # Ensure column has a label attribute before accessing it
            if hasattr(column, 'label'):
                    # Use column label as button text
                    button_label = str(column.label.plain) if hasattr(column.label, 'plain') else str(column.label)
                    buttons.append(Button(button_label, id=button_id, variant="primary"))
            else:
                # Fallback if somehow a column object without a label is passed
                log.warning(f"Column with key {key} has no 'label' attribute in SortModal.")
                buttons.append(Button(f"Column {index}", id=button_id, variant="primary"))


        yield Grid(
            Label("Sort by which column?"),
            *buttons,
            Button("Cancel", id="cancel_sort", variant="default"),
            id="sort-dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        log.info(f"SortModal button pressed: {button_id}")
        if button_id == "cancel_sort":
            self.app.pop_screen()
        else:
            # Look up the ColumnKey using the generated button ID from the map
            target_key = self.button_id_to_key_map.get(button_id)

            if target_key is not None:
                # Call the parent screen's sort method
                if hasattr(self.parent_screen, "perform_sort"):
                    self.parent_screen.perform_sort(target_key)
                    self.app.pop_screen() # Close modal after initiating sort
                else:
                    log.error(f"Parent screen {self.parent_screen.__class__.__name__} has no perform_sort method.")
                    self.app.notify("Sort function not implemented on parent screen.", severity="error")
                    self.app.pop_screen()
            else:
                log.error(f"Could not find ColumnKey for button ID: {button_id}")
                self.app.notify("Error identifying sort column.", severity="error")
                self.app.pop_screen()

