"""
1.  **Identify Non-Zero Pixels:** Find all pixels in the input grid that have a non-zero color.
2.  **Extract Unique Colors:** Create a list of unique colors present in the input grid.
3. **Determine Axis**: If all detected pixels are in one row use columns, otherwise use rows.
4.  **Establish Replication Pattern:** The replication pattern is composed by the ordered list of unique colors.
5. **Replicate Pattern**:
    *  If the axis is `rows`, extend the found pattern by replicating it on each row of the grid. The pattern should be replicated in an alternating sequence that covers all rows.
    *  If the axis is `columns`, extend the found pattern by replicating it on each column of the grid. The pattern should be replicated in an alternating sequence that covers all columns.
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

    if len(rows) == 1:
      return "column"
    else:
      return "row"


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

    # Replicate by rows
    if axis == "row":
        for i in range(output_grid.shape[0]):
          row_index = i % len(pattern)
          output_grid[i, :] = pattern[row_index]
    # Replicate by columns
    elif axis == "column":
        for j in range(output_grid.shape[1]):
          col_index = j % len(pattern)
          output_grid[:, j] = pattern[col_index]


    return output_grid