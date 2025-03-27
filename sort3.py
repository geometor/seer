from textual.app import App, ComposeResult
from textual.widgets import DataTable

class SortableTableApp(App):
    BINDINGS = [("q", "quit", "Quit")]
    _sorted_column: str | None = None
    _sort_reverse: bool = False

    def compose(self) -> ComposeResult:
        yield DataTable(show_header=True)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(("Name", {"key": "name"}), ("Age", {"key": "age"}), ("City", {"key": "city"}))
        table.add_rows([
            ("Alice", 30, "New York"),
            ("Bob", 25, "London"),
            ("Charlie", 35, "Paris"),
            ("David", 40, "New York"),
            ("Eve", 28, "London"),
        ])

    def on_data_table_header_selected(self, event: DataTable.HeaderSelected) -> None:
        event.prevent_default()
        column_key = event.column_key
        table = event.data_table

        if self._sorted_column == column_key:
            self._sort_reverse = not self._sort_reverse
        else:
            self._sorted_column = column_key
            self._sort_reverse = False

        table.sort(column_key, reverse=self._sort_reverse)

if __name__ == "__main__":
    app = SortableTableApp()
    app.run()
