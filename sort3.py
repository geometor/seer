from textual.app import App, ComposeResult
from textual.widgets import DataTable

class SortableTableApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield DataTable(show_header=True)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        # Add columns and mark them as sortable
        # Provide a key for Age to sort numerically
        table.add_column("Name", key="name")
        table.add_column("Age", key=lambda cell: int(cell) if isinstance(cell, (int, str)) and str(cell).isdigit() else -1)
        table.add_column("City", key="city")

        # Mark columns as sortable using their keys
        table.columns["name"].sortable = True
        table.columns["Age"].sortable = True # Note: Accessing by label here as the key is a lambda
        table.columns["city"].sortable = True


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
