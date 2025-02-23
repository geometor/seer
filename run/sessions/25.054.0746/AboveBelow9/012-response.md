# AboveBelow9 • 012 • refine_coder

---
```python
"""
The transformation identifies a horizontal yellow line within the grid. Any complete object located entirely *below* this yellow line is removed (changed to white). The color of objects *above* the line do not change. The *color* of objects below the line that get changed to white (removed) appears to be either green(3) or orange(7) based on which example is being transformed.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions of the specified color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col):
        """Depth-first search to find connected components."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return []

        visited[row, col] = True
        object_pixels = [(row, col)]

        object_pixels.extend(dfs(row + 1, col))
        object_pixels.extend(dfs(row - 1, col))
        object_pixels.extend(dfs(row, col + 1))
        object_pixels.extend(dfs(row, col - 1))

        return object_pixels

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                objects.append(dfs(row, col))

    return objects

def find_yellow_line(grid):
    """Finds the row index of the horizontal yellow line."""
    for row_index, row in enumerate(grid):
        if all(pixel == 4 for pixel in row):
            return row_index
    return -1  # Return -1 indicates failure


def transform(input_grid):
    """Removes objects below the yellow (4) line."""
    # Initialize output grid
    output_grid = np.copy(input_grid)

    # Find the row index of the yellow line
    yellow_line_row = find_yellow_line(input_grid)
    
    if yellow_line_row == -1:
        return output_grid

    # Iterate over all colors present in the grid
    unique_colors = np.unique(input_grid)
    
    for color in unique_colors:
      if color != 4 and color != 0:  # don't process yellow or white
        # Find objects of the current color
        objects = find_objects(input_grid, color)

        # iterate over the objects, if below the yellow line, set output
        # pixels to white
        for obj in objects:
            # Check if the object is below the yellow line
            is_below = all(row > yellow_line_row for row, _ in obj)
            if is_below:
                # Remove the object from the output grid
                for row, col in obj:
                    output_grid[row, col] = 0

    return output_grid
```

