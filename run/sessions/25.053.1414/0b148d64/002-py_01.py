"""
1.  **Identify the Target Region:** Locate the largest contiguous region of red (2) pixels in the input grid. Note its position relative to the edges of the grid (lower-left).

2.  **Crop:** Remove all rows and columns that contain only azure (8) pixels to isolate the large red area with some of the surrounding white area.

3.  **Filter:**  After the cropping operation, eliminate all azure (8) pixels that remains. The output contains only red (2) and white (0) pixels.

4.  **Output:** the transformed grid
"""

import numpy as np

def find_largest_object(grid, color):
    """Find the largest contiguous object of a specific color."""
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    max_object_coords = []

    def dfs(row, col, current_object_coords):
        """Depth-first search to find contiguous regions."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return 0
        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        size += dfs(row + 1, col, current_object_coords)
        size += dfs(row - 1, col, current_object_coords)
        size += dfs(row, col + 1, current_object_coords)
        size += dfs(row, col - 1, current_object_coords)
        return size

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object_coords = []
                size = dfs(row, col, current_object_coords)
                if size > max_size:
                    max_size = size
                    max_object_coords = current_object_coords

    return max_object_coords

def crop_grid(grid, coords):
    """Crops the grid to the bounding box defined by the coordinates."""
    min_row = min(r for r, _ in coords)
    max_row = max(r for r, _ in coords)
    min_col = min(c for _, c in coords)
    max_col = max(c for _, c in coords)

    return grid[min_row:max_row + 1, min_col:max_col + 1]

def transform(input_grid):
    # Find the largest red object
    red_object_coords = find_largest_object(input_grid, 2)

    # Crop the grid to the bounding box of the red object
    cropped_grid = crop_grid(input_grid, red_object_coords)
    
    output_grid = cropped_grid.copy()

    #remove azure
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i,j] == 8:
                output_grid[i,j] = 0

    return output_grid