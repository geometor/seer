import csv
from io import StringIO  # To simulate a CSV file in memory for demo data
from typing import Any

from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import var
from textual.widgets import DataTable, Footer, Header, Input

# --- Sample Data (as a CSV string) ---
CSV_DATA = """ID,Name,City,Country,Age
1,Alice,New York,USA,30
2,Bob,London,UK,25
3,Charlie,Paris,France,35
4,David,New York,USA,40
5,Eve,London,UK,28
6,Frank,Tokyo,Japan,45
7,Grace,Paris,France,22
8,Heidi,Berlin,Germany,31
9,Ivan,Moscow,Russia,38
10,Judy,Sydney,Australia,29
"""

# --- Helper to load data ---
def load_data_from_csv(csv_string: str) -> tuple[list[str], list[list[Any]]]:
    """Loads headers and rows from a CSV string."""
    f = StringIO(csv_string)
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)
    return headers, data

# --- The Textual App ---
class FilterSortTableApp(App[None]):
    """Textual app with a filterable and sortable DataTable."""

    CSS = """
    Screen {
        layout: vertical;
    }

    #data-table {
        height: 1fr; /* Make table fill available space */
        border: thick $accent;
        margin-top: 1;
    }

    Input {
        dock: top;
        width: 100%;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    # Store the original, unfiltered data
    full_data: var[list[list[Any]]] = var([])
    headers: var[list[str]] = var([])

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Filter data (case-insensitive)...", id="filter-input")
        yield DataTable(id="data-table")
        yield Footer()

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        # Load data
        self.headers, self.full_data = load_data_from_csv(CSV_DATA)

        table = self.query_one(DataTable)
        table.cursor_type = "row" # Highlight the whole row on hover/selection

        # --- Add Columns and Enable Sorting ---
        # Add columns with headers and capture the generated keys
        column_keys = table.add_columns(*self.headers)

        # Create a mapping from header label to ColumnKey for robust access
        header_to_key = {header: key for header, key in zip(self.headers, column_keys)}

        # Make specific columns sortable using the ColumnKey
        id_key = header_to_key["ID"]
        table.columns[id_key].sortable = True
        table.columns[id_key].key = lambda cell: int(cell) if str(cell).isdigit() else -1 # Sort ID as integer

        name_key = header_to_key["Name"]
        table.columns[name_key].sortable = True # Default string sort is fine

        city_key = header_to_key["City"]
        table.columns[city_key].sortable = True

        country_key = header_to_key["Country"]
        table.columns[country_key].sortable = True

        age_key = header_to_key["Age"]
        table.columns[age_key].sortable = True
        table.columns[age_key].key = lambda cell: int(cell) if str(cell).isdigit() else -1 # Sort Age as integer

        # Add initial (unfiltered) data
        self.update_table_data(self.full_data)


    def update_table_data(self, data: list[list[Any]]) -> None:
        """Clears and repopulates the table with new data."""
        table = self.query_one(DataTable)
        table.clear() # Clear rows but keep columns and sorting settings

        # Use add_rows for efficiency if adding many rows
        # Add styling or Text objects if needed
        styled_rows = []
        for i, row_data in enumerate(data):
            # Example: Alternate row styling (optional)
            style = "dim" if i % 2 != 0 else ""
            styled_row = [Text(str(cell), style=style) for cell in row_data]
            styled_rows.append(styled_row)

        # Add row keys if you need to reference rows later (e.g., row_key=row_data[0])
        if styled_rows:
            table.add_rows(styled_rows)
        else:
            # Optional: Show a message if no data matches filter
            table.add_row(Text("No matching data found.", style="italic dim", justify="center"))

    def on_input_changed(self, event: Input.Changed) -> None:
        """Called when the filter input text changes."""
        filter_text = event.value.strip().lower()

        if not filter_text:
            # If filter is empty, show all data
            filtered_data = self.full_data
        else:
            # Filter the full_data based on the input text (case-insensitive)
            filtered_data = [
                row for row in self.full_data
                if any(filter_text in str(cell).lower() for cell in row)
            ]

        # Update the table with filtered results
        self.update_table_data(filtered_data)

# --- Run the App ---
if __name__ == "__main__":
    app = FilterSortTableApp()
    app.run()
