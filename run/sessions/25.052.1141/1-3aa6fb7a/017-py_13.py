"""
1.  **Identify 2x1 Vertical Azure Rectangles:** Find all 2x1 vertical rectangles composed of azure (8) colored cells within the grid. These rectangles are defined by two vertically adjacent cells of the same color.

2.  **Place Blue Cell to the Right of Top Azure Cell:** For each identified 2x1 azure rectangle, if the cell immediately to the *right* of the *top* azure cell is empty (color 0) *and* within the grid boundaries, change that cell to blue (1).
"""

import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find all 2x1 azure rectangles
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    # Iterate through each rectangle
    for top_coord, _ in azure_rectangles:
        # Calculate the position to the right of the top cell
        right_pos = (top_coord[0], top_coord[1] + 1)

        # Check if within bounds and empty
        if 0 <= right_pos[0] < rows and 0 <= right_pos[1] < cols and output_grid[right_pos] == 0:
            # Place the blue cell
            output_grid[right_pos] = 1

    return output_grid