"""
1. Find all non-zero colored pixels in the input.
2. If these pixels share a column but have different rows, replicate colors by rows. Otherwise, if pixels share a row but have different columns, replicate by columns. If neither condition is met (different rows and columns) replicate by row.
3. Start Replication from the row/column index of the color that has the smallest value, and extend the filled colors over the complete output grid.
4. Order the colors for replication by their values.
"""

import numpy as np

def find_objects(grid):
    """Finds all unique non-zero colored pixels and their positions."""
    objects = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != 0:
                objects.append((grid[i, j], (i, j)))
    # remove duplicate color entries
    unique_objects = []
    seen_colors = set()
    for color, pos in objects:
        if color not in seen_colors:
            unique_objects.append((color, pos))
            seen_colors.add(color)

    return unique_objects

def determine_axis(objects):
    """Determines the axis of replication (row or column)."""
    if not objects:
        return "row"  # Default to row if no objects

    rows = set()
    cols = set()
    for _, (row, col) in objects:
        rows.add(row)
        cols.add(col)

    if len(cols) == 1 and len(rows) > 1:
        return "row"
    elif len(rows) == 1 and len(cols) > 1:
        return "column"
    else:
        return "row" # Default to rows in all other situations


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero colored pixels (objects)
    objects = find_objects(input_grid)
    
    if not objects:
        return output_grid

    # Determine the axis of replication
    axis = determine_axis(objects)

    # Sort objects by color value
    objects.sort()

    # Get the pattern of colors
    pattern = [color for color, _ in objects]

    # Find Start position
    start_position_index = objects[0][1][0] if axis == 'row' else objects[0][1][1]


    # Replicate by rows
    if axis == "row":
        for i in range(output_grid.shape[0]):
          row_index = (i - start_position_index) % len(pattern)
          output_grid[i, :] = pattern[row_index]
    # Replicate by columns
    elif axis == "column":
        for j in range(output_grid.shape[1]):
          col_index = (j-start_position_index) % len(pattern)
          output_grid[:, j] = pattern[col_index]


    return output_grid