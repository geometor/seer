"""
1. Identify 2x1 Vertical Azure Rectangles: Scan the input grid to locate all 2x1 vertical rectangles composed of azure (8) colored cells. A 2x1 vertical rectangle is defined as two vertically adjacent cells of the same color.
2. Place Blue Cell: For each identified 2x1 azure rectangle, place a single blue (1) colored cell immediately to the right of the *top* azure cell of the rectangle.
3. Boundary Condition: Make sure the added blue cell is still within boundaries.
"""

import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append((r, c))  # Only store the top coordinate
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Locate each 2x1 vertical rectangle of azure color (8).
    Add a blue cell (1) to the immediate right of the top cell of the 2x1 azure object.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    for top_coord in azure_rectangles:
        # Add a blue cell to the right of the top cell, if within bounds
        if top_coord[1] + 1 < output_grid.shape[1]:
            output_grid[top_coord[0], top_coord[1] + 1] = 1

    return output_grid