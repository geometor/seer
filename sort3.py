from dataclasses import dataclass
from typing import Any, Final, Callable, Union

from typing_extensions import Self

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import DataTable
from textual.widgets.data_table import Column, ColumnKey, CellKey


# --- Constants and Helper Functions from Example ---
SORT_INDICATOR_UP: Final[str] = ' \u25b4'
SORT_INDICATOR_DOWN: Final[str] = ' \u25be'


def sort_column(value: Any) -> Any:
    """Default sorting key function. Tries numeric conversion."""
    if value is None:
        # Treat None as minimal value for sorting consistency
        # Adjust if different behavior is needed
        return float('-inf')

    if isinstance(value, Text):
        value = value.plain

    try:
        # Attempt conversion to float for numeric sorting
        return float(value)
    except (ValueError, TypeError):
        # Fallback to string representation if not numeric
        return str(value)


@dataclass
class Sort:
    """Keeps track of the current sort state."""
    key: Union[ColumnKey, None] = None
    # label: str = '' # Label not strictly needed if using key
    direction: bool = False  # False = Ascending (Down Arrow), True = Descending (Up Arrow)

    def reverse(self) -> None:
        self.direction = not self.direction

    @property
    def indicator(self) -> str:
        # Swapped indicators to match common convention: Up=Asc, Down=Desc
        return SORT_INDICATOR_UP if not self.direction else SORT_INDICATOR_DOWN


# --- Custom Sortable DataTable ---
class SortableDataTable(DataTable):
    """A DataTable that allows sorting by clicking headers."""
    DEFAULT_CSS = """
    SortableDataTable {
        height: 1fr;
        /* border: $foreground 80%; Optional border */
    }
    """
    BINDINGS = [
        Binding('z', 'toggle_zebra', 'Toggle Zebra'),
        Binding('ctrl+r', 'show_row_labels', 'Toggle Row labels', show=False) # Hidden by default
    ]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._sort = Sort()
        self.cursor_type = 'row'
        self.show_row_labels = False # Match example, can be toggled
        # Use the default sort_column function, can be overridden if needed
        self.sort_function: Callable[[Any], Any] = sort_column

    @property
    def sort_column_state(self) -> Sort:
        """Returns the current sort state."""
        return self._sort

    def _get_column_by_label(self, _label: str) -> Union[ColumnKey, None]:
        """Finds a column key by its string label."""
        for key, column in self.columns.items():
            # Compare plain text of labels
            current_label = column.label.plain.strip()
            # Remove potential sort indicator before comparing
            if current_label.endswith(SORT_INDICATOR_UP):
                current_label = current_label[:-len(SORT_INDICATOR_UP)].rstrip()
            elif current_label.endswith(SORT_INDICATOR_DOWN):
                current_label = current_label[:-len(SORT_INDICATOR_DOWN)].rstrip()

            if current_label == _label:
                return key
        return None

    def clear(self, columns: bool = False) -> Self:
        """Clears rows and optionally columns, resetting sort state if columns are cleared."""
        super().clear(columns)
        if columns:
            # Reset sort state if columns are removed
            self._sort = Sort()
        return self

    @on(DataTable.HeaderSelected)
    def _handle_header_clicked(self, event: DataTable.HeaderSelected) -> None:
        """Handles clicks on column headers to trigger sorting."""
        self.sort_on_column(event.column_key)

    def sort_on_column(self, key: Union[ColumnKey, str], direction: Union[bool, None] = None) -> None:
        """Sorts the table based on the provided column key or label."""
        if isinstance(key, str):
            key = self._get_column_by_label(key)
            if key is None:
                self.notify(f"Column label '{key}' not found for sorting.", severity="warning")
                return

        assert isinstance(key, ColumnKey), "Column key must be valid"

        # --- Update Labels ---
        # Remove indicator from the previously sorted column, if any
        if self._sort.key is not None and self._sort.key in self.columns:
            try:
                old_column = self.columns[self._sort.key]
                old_label_text = old_column.label.plain
                if old_label_text.endswith(self._sort.indicator):
                     old_column.label = Text(old_label_text[:-len(self._sort.indicator)].rstrip())
                     self._update_column_width(self._sort.key) # Adjust width after removing indicator
            except KeyError:
                pass # Old column might have been removed

        # Determine new sort direction
        new_sort = Sort(key=key)
        if self._sort.key == new_sort.key:
            # If clicking the same column, reverse direction
            new_sort.direction = not self._sort.direction
        else:
            # Default to ascending for a new column
            new_sort.direction = False

        # Override direction if explicitly provided
        if direction is not None:
            new_sort.direction = direction

        # Add indicator to the new sort column
        if key in self.columns:
            new_column = self.columns[key]
            new_label_text = new_column.label.plain.rstrip() # Ensure no trailing space before adding indicator
            new_column.label = Text(f"{new_label_text}{new_sort.indicator}")
            self._update_column_width(key) # Adjust width after adding indicator
        else:
             self.notify(f"Column key '{key}' not found when adding indicator.", severity="error")
             return # Should not happen if key is valid

        # --- Perform Sort ---
        try:
            # Use the instance's sort_function as the key for sorting
            self.sort(key, reverse=new_sort.direction, key=self.sort_function)
            self._sort = new_sort # Update the current sort state
        except TypeError as e:
            # Revert label change on error
            if key in self.columns:
                 current_label = self.columns[key].label.plain
                 if current_label.endswith(new_sort.indicator):
                     self.columns[key].label = Text(current_label[:-len(new_sort.indicator)].rstrip())
            self.notify(f"Error sorting column '{self.columns[key].label.plain}': {e}", severity="error", timeout=10)
        except Exception as e: # Catch other potential errors during sort
             self.notify(f"An unexpected error occurred during sorting: {e}", severity="error", timeout=10)


    def _update_column_width(self, key: ColumnKey) -> None:
        """Triggers a column width update for the given key."""
        # This is a simplified way; Textual might adjust automatically or
        # require more specific handling depending on version and layout.
        # If column widths don't adjust correctly, this might need refinement.
        if self.show_header and key in self.columns:
             self.refresh_header() # Refresh header to reflect label changes

        # A more forceful refresh if needed, but can be less efficient:
        # self.refresh(layout=True)


    def action_toggle_zebra(self) -> None:
        """Toggles zebra striping."""
        self.zebra_stripes = not self.zebra_stripes

    def action_show_row_labels(self) -> None:
        """Toggles visibility of row labels."""
        self.show_row_labels = not self.show_row_labels


# --- Main Application ---
class SortableTableApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        # Use the custom SortableDataTable
        yield SortableDataTable(id="sortable-table", show_header=True)

    def on_mount(self) -> None:
        # Get the custom table instance
        table = self.query_one(SortableDataTable)

        # Add columns - no need to capture keys or set sortable=True here
        # The SortableDataTable handles sorting via header clicks internally.
        # The 'key' argument helps identify the column, though the sorting comparison
        # itself uses the `sort_function` defined in SortableDataTable.
        table.add_column("Name", key="name")
        table.add_column("Age", key="age")
        table.add_column("City", key="city")

        # Add data rows
        table.add_rows([
            ("Alice", 30, "New York"),
            ("Bob", 25, "London"),
            ("Charlie", 35, "Paris"),
            ("David", 40, "New York"),
            ("Eve", 28, "London"),
        ])

if __name__ == "__main__":
    app = SortableTableApp()
    app.run()
