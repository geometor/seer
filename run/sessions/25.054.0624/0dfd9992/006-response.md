# 0dfd9992 • 006 • refine_coder

---
```python
"""
Removes the largest contiguous region of white (0) pixels from the input grid
and replaces it with the most frequent non-white color in the entire input grid.
"""

import numpy as np
from collections import Counter

def find_largest_object(grid, color):
    """
    Finds the largest connected region of pixels with the given color.
    Uses Depth First Search (DFS).
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    max_size = 0
    largest_object_coords = []

    def dfs(row, col, current_object_coords):
        """
        Recursive Depth First Search helper function.
        """
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return 0

        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                size += dfs(row + dr, col + dc, current_object_coords)
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object_coords = []
                object_size = dfs(r, c, current_object_coords)
                if object_size > max_size:
                    max_size = object_size
                    largest_object_coords = current_object_coords

    return largest_object_coords

def transform(input_grid):
    """
    Transforms the input grid by removing the largest contiguous region of '0' (white) pixels
    and replacing it with the most frequent non-white color in the input.
    """
    # Convert to numpy array
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find the coordinates of the largest object with color 0
    largest_object_coords = find_largest_object(input_grid, 0)

    # Find the most frequent color in the input grid (excluding white)
    color_counts = Counter(input_grid.flatten())
    if 0 in color_counts:
        del color_counts[0]  # Remove white
    
    if color_counts:
      most_frequent_color = color_counts.most_common(1)[0][0]
    else:
        return output_grid.tolist() # Return original if no other colors.


    # Remove the largest object by setting to most frequent color
    for row, col in largest_object_coords:
        output_grid[row, col] = most_frequent_color

    return output_grid.tolist()
```

