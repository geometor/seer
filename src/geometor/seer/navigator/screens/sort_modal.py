from typing import Dict, TYPE_CHECKING

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Label
from textual.binding import Binding
from textual.widgets._data_table import ColumnKey # Import ColumnKey
from textual import log

if TYPE_CHECKING:
    from textual.widgets import DataTable
    # Import the screen types that will use this modal
    from .sessions_screen import SessionsScreen
    from .session_screen import SessionScreen
    from .task_screen import TaskScreen
    from .tasks_screen import TasksScreen
    SortableScreen = SessionsScreen | SessionScreen | TaskScreen | TasksScreen


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
        parent_screen: SortableScreen,
        columns: Dict[ColumnKey, object], # Pass columns dict directly
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.parent_screen = parent_screen
        self.columns = columns
        log.info(f"SortModal initialized for screen: {parent_screen.__class__.__name__}")

    def compose(self) -> ComposeResult:
        buttons = []
        # Create buttons only for columns that have a label (visible columns)
        for key, column in self.columns.items():
            if hasattr(column, 'label') and column.label:
                # Use column key as button ID, ensure it's a string
                button_id = str(key)
                # Use column label as button text
                button_label = str(column.label.plain) if hasattr(column.label, 'plain') else str(column.label)
                buttons.append(Button(button_label, id=button_id, variant="primary"))

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
            # Find the ColumnKey corresponding to the button ID (which is the key string)
            target_key = None
            for key in self.columns.keys():
                if str(key) == button_id:
                    target_key = key
                    break

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

```

**2. Update `navigator3.py` (SessionNavigator)**

src/geometor/seer/navigator/navigator3.py
```python
<<<<<<< SEARCH
# Import the modal screen
from geometor.seer.navigator.screens.image_view_modal import ImageViewModal
# Import the modal screen
from geometor.seer.navigator.screens.image_view_modal import ImageViewModal
