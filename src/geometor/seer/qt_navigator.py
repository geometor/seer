import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtGui, QtCore
from pathlib import Path
from geometor.seer.tasks.tasks import Tasks

class GridViewer(QtWidgets.QMainWindow):
    """
    Alternate Task Viewer using PyQtGraph.

    Displays a list of tasks and renders their train and test grids using a QGraphicsScene.
    """
    def __init__(self, tasks, cell_size: int = 32, parent=None):
        super().__init__(parent)
        self.tasks = tasks
        self.cell_size = cell_size
        self.map_colors = [
            '#FFFFFF',  # 0: white
            '#0074D9',  # 1: blue
            '#FF4136',  # 2: red
            '#2ECC40',  # 3: green
            '#FFDC00',  # 4: yellow
            '#AAAAAA',  # 5: gray
            '#F012BE',  # 6: magenta
            '#FF851B',  # 7: orange
            '#7FDBFF',  # 8: cyan
            '#870C25',  # 9: brown
        ]

        self.setWindowTitle("Task Viewer (PyQtGraph)")
        self.resize(1000, 800)

        # Central widget and layout
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        layout = QtWidgets.QHBoxLayout()
        centralWidget.setLayout(layout)

        # --- Task List Widget ---
        self.taskList = QtWidgets.QListWidget()
        layout.addWidget(self.taskList, 1)
        for task in self.tasks:
            item = QtWidgets.QListWidgetItem(str(task.id))
            self.taskList.addItem(item)
        self.taskList.currentRowChanged.connect(self.onTaskSelected)

        # --- Graphics View ---
        self.view = pg.GraphicsView()
        layout.addWidget(self.view, 4)
        self.scene = pg.GraphicsScene()
        self.view.setScene(self.scene)

        # Select the first task if available
        if self.tasks:
            self.taskList.setCurrentRow(0)

    def onTaskSelected(self, row: int):
        if row < 0 or row >= len(self.tasks):
            return
        task = self.tasks[row]
        self.displayTask(task)

    def displayTask(self, task):
        self.scene.clear()

        # --- Draw Training Pairs ---
        # For each training pair, we draw the input grid on top and (if available) output grid below.
        x_offset = 0
        for task_pair in task.train:
            # Draw input grid
            self.drawGrid(task_pair.input.grid, x_offset, 0)
            input_height = task_pair.input.grid.shape[0] * self.cell_size
            # Draw output grid (if it exists) below input with some vertical spacing
            if task_pair.output is not None:
                y_out = input_height + self.cell_size
                self.drawGrid(task_pair.output.grid, x_offset, y_out)
                output_height = task_pair.output.grid.shape[0] * self.cell_size
                pair_height = input_height + self.cell_size + output_height
            else:
                pair_height = input_height
            # Increase x_offset for next training pair (include horizontal spacing)
            grid_width = task_pair.input.grid.shape[1] * self.cell_size
            x_offset += grid_width + self.cell_size * 2

        # --- Draw Test Grids ---
        # We render test inputs in a row below the training pairs.
        if task.test:
            # Compute the maximum height of the training section to offset test grids
            max_train_height = 0
            for task_pair in task.train:
                h = task_pair.input.grid.shape[0] * self.cell_size
                if task_pair.output is not None:
                    h += self.cell_size + task_pair.output.grid.shape[0] * self.cell_size
                max_train_height = max(max_train_height, h)
            y_offset_test = max_train_height + self.cell_size * 4
            x_offset_test = 0
            for task_pair in task.test:
                if task_pair.input is not None:
                    self.drawGrid(task_pair.input.grid, x_offset_test, y_offset_test)
                    grid_width = task_pair.input.grid.shape[1] * self.cell_size
                    x_offset_test += grid_width + self.cell_size * 2

    def drawGrid(self, grid, x_offset, y_offset):
        """Draws a single grid using QGraphicsRectItem for each cell."""
        rows, cols = grid.shape
        for r in range(rows):
            for c in range(cols):
                value = grid[r, c]
                # Fallback to white if value is out of bounds
                if value < 0 or value >= len(self.map_colors):
                    color = self.map_colors[0]
                else:
                    color = self.map_colors[value]
                rect_item = QtWidgets.QGraphicsRectItem(
                    x_offset + c * self.cell_size,
                    y_offset + r * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                rect_item.setBrush(QtGui.QBrush(QtGui.QColor(color)))
                rect_item.setPen(QtGui.QPen(QtGui.QColor("black")))
                self.scene.addItem(rect_item)

def main():
    # --- Configuration ---
    TASKS_DIR = Path("/home/phi/PROJECTS/geometor/seer_sessions/run/tasks/ARC/training")

    # 1. Load tasks
    if not TASKS_DIR.exists():
        print(f"Error: Tasks directory '{TASKS_DIR}' not found.")
        print("Please create a 'tasks' directory and place your JSON task files in it.")
        return

    try:
        tasks = Tasks(TASKS_DIR)
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return

    if not tasks:
        print("No tasks found in the 'tasks' directory.")
        return

    app = QtWidgets.QApplication(sys.argv)
    viewer = GridViewer(tasks)  # Use loaded tasks
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
