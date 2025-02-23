"""
1.  **Identify the Foreground:** Locate the contiguous region of gray (5) pixels. This is the foreground shape.

2.  **Identify the Background:** Everything that is not part of the foreground shape is the background and should not be changed.

3.  **Segment the Foreground Shape:** Divide the gray shape into two parts: the outline and the inside.

    *   **Outline:** A gray pixel is part of the outline if it is directly adjacent (up, down, left, or right) to at least one non-gray pixel.

    *   **Inside:** A gray pixel is part of the inside if it is part of the foreground shape *and* is not part of the outline.

4.  **Recolor the Outline:** Change the color of all outline pixels to azure (8).

5.  **Recolor the Inside:** Change the color of all inside pixels to red (2).

6. **Preserve background.** All non-gray input pixels should be unchanged.
"""

import numpy as np

def get_contiguous_regions(grid, color):
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, current_region):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return

        visited[row, col] = True
        current_region.append((row, col))

        dfs(row + 1, col, current_region)
        dfs(row - 1, col, current_region)
        dfs(row, col + 1, current_region)
        dfs(row, col - 1, current_region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)
    return regions


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify the Foreground Shape
    gray_regions = get_contiguous_regions(input_grid, 5)
    if not gray_regions:  # Handle cases with no gray regions
        return output_grid
    gray_pixels = gray_regions[0] # Assume only 1 region

    # Segment the Shape (Outline & Inside)
    outline_pixels = []
    inside_pixels = []

    for r, c in gray_pixels:
        # Check neighbors (up, down, left, right)
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        ]
        is_outline = False
        for nr, nc in neighbors:
            if (
                nr < 0
                or nr >= input_grid.shape[0]
                or nc < 0
                or nc >= input_grid.shape[1]
                or input_grid[nr, nc] != 5  # Check for NON-gray neighbor
            ):
                is_outline = True
                break
        if is_outline:
            outline_pixels.append((r,c))
        else:
            inside_pixels.append((r,c))
    
    # Recolor the outline
    for r, c in outline_pixels:
        output_grid[r, c] = 8
        
    # Recolor the inside
    for r, c in inside_pixels:
        output_grid[r, c] = 2
        

    return output_grid