from textual.app import App, ComposeResult
from textual.widgets import DataTable

class SortableTableApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield DataTable(show_header=True)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        # Add columns and capture their keys
        # Provide a sort key for Age to sort numerically
        name_key = table.add_column("Name", key="name")
        age_key = table.add_column("Age", key=lambda cell: int(cell) if isinstance(cell, (int, str)) and str(cell).isdigit() else -1)
        city_key = table.add_column("City", key="city")

        # Mark columns as sortable using the captured ColumnKey objects
        table.columns[name_key].sortable = True
        table.columns[age_key].sortable = True
        table.columns[city_key].sortable = True

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
