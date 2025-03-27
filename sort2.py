from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header

class SortableDataTable(DataTable):
    def on_click(self, event):
        if event.row == 0:  # Header row
            column = self.columns[event.column]
            self.sort(column.key, key=self.custom_sort, reverse=False)

    def custom_sort(self, row_data):
        # Example: Sort by the length of the 'Name' field
        return len(row_data[0])

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield SortableDataTable()

    def on_mount(self) -> None:
        table = self.query_one(SortableDataTable)
        table.add_columns("Name", "Age", "Country")
        table.add_rows([
            ("Alice", 28, "USA"),
            ("Bob", 35, "Canada"),
            ("Charlie", 22, "UK"),
            ("David", 41, "Australia"),
        ])

if __name__ == "__main__":
    app = TableApp()
    app.run()

