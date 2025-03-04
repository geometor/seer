import numpy as np
import os

class HTMLReport:
    """Generates an HTML report visualizing ARC tasks."""

    def __init__(self, tasks: list, cell_size: int = 24, line_width: int = 1):
        """
        Initializes the HTMLReport generator.

        :param tasks: List of Task objects.
        :param cell_size: Size of each cell in the SVG (pixels).
        :param line_width: Width of the grid lines in the SVG.
        """
        self.tasks = tasks
        self.cell_size = cell_size
        self.line_width = line_width
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

    def _grid_to_svg(self, grid_obj, title=None):
        """Converts a single grid (NumPy array) to an SVG string."""
        if grid_obj is None:
            return ""  # Handle missing output grids

        grid = grid_obj.grid
        rows, cols = grid.shape
        width = cols * (self.cell_size + self.line_width) - self.line_width
        height = rows * (self.cell_size + self.line_width) - self.line_width

        svg_str = f'<svg width="{width}" height="{height}" style="margin-right: 16px; margin-bottom: 8px;">\n'  # Add margins

        for row in range(rows):
            for col in range(cols):
                x = col * (self.cell_size + self.line_width)
                y = row * (self.cell_size + self.line_width)
                color = self.map_colors[grid[row, col]]
                svg_str += f'  <rect x="{x}" y="{y}" width="{self.cell_size}" height="{self.cell_size}" fill="{color}" stroke="black" stroke-width="{self.line_width}"/>\n'

        svg_str += '</svg>\n'
        return svg_str

    def generate_html(self):
        """Generates the complete HTML report string."""
        html_str = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ARC Task Report</title>
    <style>
        body {{ font-family: sans-serif; }}
        .task-container {{ margin-bottom: 32px; border: 1px solid #ccc; padding: 16px; }}
        .task-title {{ font-weight: bold; margin-bottom: 8px; }}
        .grid-pair {{ display: flex; flex-direction: row; align-items: flex-start; margin-bottom: 8px; }}
        .grid-title {{ font-size: smaller; margin-bottom: 4px; }}
        .train-grids {{ margin-bottom: 16px; }}
        .test-grids {{ margin-bottom: 16px; }}
    </style>
</head>
<body>
"""

        for task in self.tasks:
            html_str += f'    <div class="task-container">\n'
            html_str += f'        <h2 class="task-title">Task ID: {task.id}</h2>\n'

            # Training grids
            html_str += '        <div class="train-grids">\n'
            html_str += '            <h3>Train:</h3>\n'
            for i, task_pair in enumerate(task.train):
                html_str += f'            <div class="grid-pair">\n'
                html_str += f'                <div><div class="grid-title">Input {i+1}:</div>{self._grid_to_svg(task_pair.input)}</div>\n'
                html_str += f'                <div><div class="grid-title">Output {i+1}:</div>{self._grid_to_svg(task_pair.output)}</div>\n'
                html_str += f'            </div>\n'
            html_str += '        </div>\n'

            # Test grids
            html_str += '        <div class="test-grids">\n'
            html_str += '            <h3>Test:</h3>\n'
            for i, task_pair in enumerate(task.test):
                html_str += f'            <div class="grid-pair">\n'
                html_str += f'                <div><div class="grid-title">Input {i+1}:</div>{self._grid_to_svg(task_pair.input)}</div>\n'
                if task_pair.output:  # Check if output exists
                    html_str += f'                <div><div class="grid-title">Output {i+1}:</div>{self._grid_to_svg(task_pair.output)}</div>\n'
                html_str += f'            </div>\n'
            html_str += '        </div>\n'

            html_str += '    </div>\n'  # Close task-container

        html_str += """</body>
</html>
"""
        return html_str

    def save_report(self, output_path: str):
        """Saves the generated HTML report to a file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(self.generate_html())
