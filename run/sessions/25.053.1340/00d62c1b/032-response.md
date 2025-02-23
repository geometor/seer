# 00d62c1b • 032 • refine_coder

---
```python
"""
Identifies connected regions of green pixels and recolors the internal pixels of enclosed regions to yellow.
Internal pixels are defined as those having all four orthogonal neighbors (up, down, left, right) 
either within the same green region or being the implied black border.
"""

import numpy as np

def get_neighbors(grid, row, col, orthogonal_only=False):
    """Gets the neighbors of a given pixel."""
    rows, cols = grid.shape
    neighbors = []

    # Orthogonal neighbors
    possible_neighbors = [
        (row - 1, col), (row + 1, col),
        (row, col - 1), (row, col + 1)
    ]

    if not orthogonal_only:
        possible_neighbors.extend([
            (row - 1, col - 1), (row - 1, col + 1),
            (row + 1, col - 1), (row + 1, col + 1)
        ])

    for r, c in possible_neighbors:
        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append((r, c))

    return neighbors

def is_enclosed(grid, region):
    """Checks if a region is fully enclosed (not touching the edge)."""
    rows, cols = grid.shape
    for r, c in region:
        # Check if the pixel is on the edge
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return False  # Touches edge, so not enclosed

    return True #if no pixels are on the edge, then it IS enclosed

def get_internal_pixels(grid, region):
    """Returns the internal pixels of the region, considering only orthogonal neighbors."""
    internal_pixels = set()
    rows, cols = grid.shape
    for r, c in region:
        neighbors = get_neighbors(grid, r, c, orthogonal_only=True)
        all_neighbors_valid = True
        for nr, nc in neighbors:
            # Check if neighbor is within the region or is the implied black border (value 0)
            if (nr, nc) not in region:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr,nc] != 0:
                        all_neighbors_valid = False
                        break
                #else, implied border - valid, do nothing
        if all_neighbors_valid:
            internal_pixels.add((r, c))
    return internal_pixels


def get_connected_region(grid, start_row, start_col, color):
    """Finds a connected region of a given color starting from a given pixel."""
    rows, cols = grid.shape
    region = set()
    queue = [(start_row, start_col)]

    while queue:
        row, col = queue.pop(0)
        if (row, col) in region:
            continue
        if not (0 <= row < rows and 0 <= col < cols):
            continue
        if grid[row, col] == color:
            region.add((row, col))
            neighbors = get_neighbors(grid, row, col, orthogonal_only=True)
            for neighbor in neighbors:
                if neighbor not in region:
                    queue.append(neighbor)

    return region

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = set()

    # Iterate to find all green regions
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 3 and (row, col) not in visited:
                region = get_connected_region(input_grid, row, col, 3)
                visited.update(region)

                # Check if the region is enclosed
                if is_enclosed(input_grid, region):
                    # Get the internal pixels, considering only orthogonal neighbors
                    internal_pixels = get_internal_pixels(input_grid, region)
                    # Recolor all internal pixels in the enclosed region to yellow
                    for r, c in internal_pixels:
                        output_grid[r, c] = 4

    return output_grid
```

