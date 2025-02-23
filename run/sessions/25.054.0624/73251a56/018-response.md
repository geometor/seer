# 73251a56 • 018 • refine_coder

---
```python
"""
The transformation rule involves identifying connected regions of non-white pixels and then changing the color of white pixels based on their adjacency to these regions.

1.  **Identify Connected Regions:** Find all connected regions of non-white pixels.  A connected region is a group of pixels of the same color that are directly adjacent (up, down, left, right).
2.  **White Pixel Examination:** For each white pixel (color 0) in the grid:
    a. Find all neighboring pixels (up, down, left, right).
    b. Determine if a neighboring pixel is part of a connected region (identified in step 1).
3. **Prioritized color change** If, among all the neighbors found, select only one using a method to be determined.
4.  **Apply Color Change:** Change the white pixel's color to the selected neighboring pixel.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Gets the valid neighbors (up, down, left, right) of a pixel.
    """
    rows, cols = grid.shape
    neighbors = []
    
    # Up
    if row > 0:
        neighbors.append((row-1, col))
    # Down
    if row < rows - 1:
        neighbors.append((row+1, col))
    # Left
    if col > 0:
        neighbors.append((row, col-1))
    # Right
    if col < cols - 1:
        neighbors.append((row, col+1))

    return neighbors

def find_connected_regions(grid):
    """
    Finds all connected regions of non-white pixels.
    Returns a dictionary where keys are (row, col) of pixels in regions,
    and values are the color of the region.
    """
    rows, cols = grid.shape
    visited = set()
    regions = {}

    def dfs(row, col, color):
        """Depth-first search to find connected components."""
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        regions[(row, col)] = color
        for r, c in get_neighbors(grid, row, col):
            dfs(r, c, color)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                dfs(r, c, grid[r, c])
    return regions

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels based on connected regions.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # 1. Identify Connected Regions
    regions = find_connected_regions(input_grid)

    # 2. White Pixel Examination
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 0:
                # a. Find all neighboring pixels
                neighbors = get_neighbors(input_grid, r, c)
                neighboring_colors = []

                # b. Determine if a neighboring pixel is part of a connected region
                for nr, nc in neighbors:
                    if (nr, nc) in regions:
                        neighboring_colors.append(regions[(nr, nc)])

                # 3. Prioritized color change (Placeholder - needs refinement)
                if neighboring_colors:
                    # Simple strategy: use the most frequent color
                    from collections import Counter
                    color_counts = Counter(neighboring_colors)

                    # Check for ties
                    max_count = max(color_counts.values())
                    most_frequent_colors = [color for color, count in color_counts.items() if count == max_count]
                    if len(most_frequent_colors) > 0:
                        #still picking the first, we need a tie break rule.
                        selected_color = most_frequent_colors[0]
                    
                    # 4. Apply Color Change
                        output_grid[r, c] = selected_color

    return output_grid
```
