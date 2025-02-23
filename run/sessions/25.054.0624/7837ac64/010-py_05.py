"""
1. **Identify Background:** The background color is white (0).
2. **Identify Objects:** Find all contiguous regions (objects) of non-white colors.
3. **Downsample:** Create a 3x3 output grid.
4. **Select Colors:** Select a subset of the non-white colors from the input to use in the output.  The selection criteria are not fully understood but seem to involve prominence or relevance, possibly related to object size or interactions.
5. **Map Objects by Row:**  Rows of input grid contribute to single color rows.
6. **Fill Output Grid** fill output grid rows with the selected color for each row
"""

import numpy as np
from collections import Counter

def get_objects(grid):
    """Finds contiguous regions of the same color (objects) in a grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and grid[row, col] != 0:  # Not white
                obj = []
                dfs(row, col, grid[row, col], obj)
                objects.append((grid[row, col], obj))  # Store color and object pixels
    return objects

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Identify objects in the input grid
    objects = get_objects(input_grid)

    # Group pixels by row and color, ignoring white (0)
    row_colors = {}
    for r in range(input_grid.shape[0]):
        row_colors[r] = Counter(input_grid[r, :][input_grid[r, :] != 0])


    # Determine output row colors based on input row colors
    for output_row in range(3):
      input_row_start = (input_grid.shape[0] // 3) * output_row
      input_row_end = (input_grid.shape[0] // 3) * (output_row + 1) 
      combined_colors = Counter()      
      for input_row in range( input_row_start, input_row_end ):
        combined_colors += row_colors.get(input_row, Counter())
      
      if len(combined_colors) > 0:
        # select the most frequent color
        most_common_color = combined_colors.most_common(1)[0][0]
        output_grid[output_row, : ] = most_common_color

    return output_grid