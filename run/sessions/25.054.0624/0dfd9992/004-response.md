# 0dfd9992 • 004 • refine_coder

---
```python
"""
Removes the largest contiguous region of white (0) pixels from the input grid
and replaces it with the most frequent color adjacent to the removed region.
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

def get_adjacent_colors(grid, coords):
    """
    Gets the colors of the pixels adjacent to the given coordinates.
    """
    rows, cols = grid.shape
    adjacent_colors = []
    for row, col in coords:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                adj_row, adj_col = row + dr, col + dc
                if 0 <= adj_row < rows and 0 <= adj_col < cols:
                    adjacent_colors.append(grid[adj_row, adj_col])
    return adjacent_colors


def transform(input_grid):
    """
    Transforms the input grid by removing the largest contiguous region of '0' (white) pixels
    and replacing it with the most frequent adjacent color.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find the coordinates of the largest object with color 0
    largest_object_coords = find_largest_object(input_grid, 0)

    # Get adjacent colors to the largest white object
    adjacent_colors = get_adjacent_colors(input_grid, largest_object_coords)
    
    # Exclude white (0) from adjacent colors, we are replacing, not keeping
    adjacent_colors = [color for color in adjacent_colors if color != 0]

    # Find the most frequent adjacent color, if no adjacent non-white - default to input
    if adjacent_colors:
      most_frequent_color = Counter(adjacent_colors).most_common(1)[0][0]
    else:
      most_frequent_color = 0 # should we return the input grid in this case? No

    # Remove the largest object by setting those coordinates in output to the most frequent color
    for row, col in largest_object_coords:
        output_grid[row, col] = most_frequent_color

    return output_grid.tolist()
```
