"""
The transformation rule is as follows:

1. **Identify 2x1 Azure Rectangles:** Find all vertical 2x1 rectangles (objects) of azure color (8) within the input grid.

2. **Add Blue Cells:**  For each identified azure rectangle:
   -  Find the *top* azure cell. Add a blue cell (1) immediately to the *right* of this top cell.
   -  Find the *bottom* azure cell. Add a blue cell (1) immediately to the *left* of the bottom cell.

3. **Preserve Other Cells:**  All other cells in the input grid that are not part of the identified 2x1 azure rectangles remain unchanged in the output grid.
"""

import numpy as np

def find_objects(grid):
    """
    Finds contiguous regions of the same color and returns them as a list of objects.
    Each object is a dictionary with 'color' and 'positions' (list of (row, col) tuples).
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, positions):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        positions.append((row, col))
        dfs(row + 1, col, color, positions)
        dfs(row - 1, col, color, positions)
        dfs(row, col + 1, color, positions)
        dfs(row, col - 1, color, positions)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                positions = []
                dfs(row, col, color, positions)
                if positions:
                    objects.append({'color': color, 'positions': positions})
    return objects

def is_2x1_vertical_rectangle(positions):
    """
    Checks if the given positions form a 2x1 vertical rectangle.
    """
    if len(positions) != 2:
        return False
    row1, col1 = positions[0]
    row2, col2 = positions[1]
    return (col1 == col2) and (abs(row1 - row2) == 1)

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each 2x1 azure rectangle, add a blue (1) cell to the
    right of its top cell, and to the left of its bottom cell.
    """
    output_grid = np.copy(input_grid) # Initialize the output grid as a copy of the input grid.
    objects = find_objects(input_grid) # Find all objects in the input grid.

    for obj in objects: # Iterate over each found object.
        if obj['color'] == 8 and is_2x1_vertical_rectangle(obj['positions']): # Check if the object is a 2x1 vertical azure rectangle.
            # Sort positions to ensure we get top and bottom cells correctly.
            positions = sorted(obj['positions'])
            top_row, top_col = positions[0]  # Get the row and column of the top cell.
            bottom_row, bottom_col = positions[1] # Get the row and column of the bottom cell.

            # Add a blue cell to the right of the top cell.
            if top_col + 1 < output_grid.shape[1]:  # Check if adding a column is within bounds.
                output_grid[top_row, top_col + 1] = 1 # Set the cell to blue (1).

            # Add a blue cell to the left of the bottom cell.
            if bottom_col - 1 >= 0: # Check if subtracting a column is within bounds.
                output_grid[bottom_row, bottom_col - 1] = 1 # Set the cell to blue (1).

    return output_grid # Return the modified grid.