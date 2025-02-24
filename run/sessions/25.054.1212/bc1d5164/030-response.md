# bc1d5164 • 030 • refine_coder

---
```python
"""
The transformation identifies the dominant non-zero color in the input grid, then extracts a subgrid. The subgrid consists of cells whose row and column both contain the dominant color at least once.
"""

import numpy as np

def get_dominant_nonzero_color(grid):
    """
    Finds the most frequent non-zero color in the grid.
    """
    # Flatten the grid and convert to a list
    flat_grid = grid.flatten().tolist()
    # Find unique non-zero colors
    nonzero_colors = [color for color in set(flat_grid) if color != 0]

    # Handle the edge case of input containing all zeros
    if not nonzero_colors:
        return None

    if len(nonzero_colors) == 1:
        return nonzero_colors[0]

    # Count occurrences of each non-zero color
    color_counts = {color: flat_grid.count(color) for color in nonzero_colors}
    # Return the color with the maximum count
    dominant_color = max(color_counts, key=color_counts.get)
    return dominant_color

def get_rows_with_color(grid, color):
    """
    Returns a list of row indices that contain the specified color.
    """
    rows = []
    for i, row in enumerate(grid):
        if color in row:
            rows.append(i)
    return rows

def get_cols_with_color(grid, color):
    """
    Returns a list of column indices that contain the specified color.
    """
    cols = []
    for j in range(grid.shape[1]):
        if color in grid[:, j]:
            cols.append(j)
    return cols

def transform(input_grid):
    """
    Transforms the input grid by extracting a subgrid based on the dominant non-zero color.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # 1. Identify the dominant non-zero color
    dominant_color = get_dominant_nonzero_color(input_grid)

    if dominant_color is None:
        return []

    # 2. Identify Rows with the dominant color
    rows_with_color = get_rows_with_color(input_grid, dominant_color)

    # 3. Identify Columns with the dominant color
    cols_with_color = get_cols_with_color(input_grid, dominant_color)

    # 4. Construct Output - Intersection of rows and cols
    output_grid = []
    for i in rows_with_color:
        row = []
        for j in cols_with_color:
            row.append(input_grid[i, j])
        if row:  # avoid empty rows
          output_grid.append(row)

    return output_grid
```
