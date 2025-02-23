"""
1.  **Identify the Largest Green Shape:** Find the largest contiguous region of green (3) pixels in the input grid. Contiguous pixels are connected horizontally or vertically.

2.  **Determine Interior Pixels (Revised):** Consider all pixels within the identified largest green shape. The "interior" pixels of this shape will become yellow. This is best described as the inverse flood fill from the exterior.

3.  **Recolor Interior:** Change the color of the interior pixels within the largest green shape from green (3) to yellow (4).

4.  **Output:** The resulting grid, with the interior of the largest green shape recolored, is the output.
"""

import numpy as np

def _find_contiguous_regions(grid, color):
    """Finds all contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def _dfs(row, col, region):
        """Depth-first search to explore a contiguous region."""
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
        region.append((row, col))
        _dfs(row + 1, col, region)
        _dfs(row - 1, col, region)
        _dfs(row, col + 1, region)
        _dfs(row, col - 1, region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                region = []
                _dfs(row, col, region)
                regions.append(region)
    return regions

def _flood_fill(grid, start_row, start_col, target_color, replacement_color):
    """Performs a flood fill on the grid."""
    rows, cols = grid.shape
    if (start_row < 0 or start_row >= rows or
        start_col < 0 or start_col >= cols or
        grid[start_row, start_col] != target_color):
        return
    
    grid[start_row, start_col] = replacement_color
    _flood_fill(grid, start_row + 1, start_col, target_color, replacement_color)
    _flood_fill(grid, start_row - 1, start_col, target_color, replacement_color)
    _flood_fill(grid, start_row, start_col + 1, target_color, replacement_color)
    _flood_fill(grid, start_row, start_col - 1, target_color, replacement_color)
    
def _find_interior_pixels_inverse_flood_fill(grid, region, exterior_color=0):
    """Finds interior pixels using inverse flood fill."""
    
    # Create a copy of the grid to work with
    temp_grid = grid.copy()

    # Get the color of the region
    region_color = grid[region[0][0], region[0][1]]

    # Replace the entire region in temp_grid with a temporary color, say -1
    for row, col in region:
        temp_grid[row, col] = -1

    # Flood fill from the edges of the temp_grid using the exterior color (typically 0)
    rows, cols = temp_grid.shape
    for i in range(cols):
        if temp_grid[0,i] != -1:
            _flood_fill(temp_grid, 0, i, temp_grid[0,i], exterior_color)  # Top row
        if temp_grid[rows-1, i] != -1:    
            _flood_fill(temp_grid, rows - 1, i, temp_grid[rows-1, i], exterior_color)  # Bottom row
    for i in range(rows):
        if temp_grid[i,0] != -1:
            _flood_fill(temp_grid, i, 0, temp_grid[i,0], exterior_color)  # Left column
        if temp_grid[i, cols-1] != -1:
            _flood_fill(temp_grid, i, cols - 1, temp_grid[i,cols-1], exterior_color)  # Right column
        
    # Now, any pixel that is still -1 in temp_grid is an interior pixel
    interior_pixels = []
    for row, col in region:
        if temp_grid[row, col] == -1:
            interior_pixels.append((row, col))
    
    return interior_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # 1. Identify the Shape (largest contiguous region of color 3)
    regions = _find_contiguous_regions(input_grid, 3)
    if not regions:
      return output_grid
    
    largest_region = max(regions, key=len)
    
    # 2. Find Interior Pixels inverse flood fill
    interior_pixels = _find_interior_pixels_inverse_flood_fill(input_grid, largest_region)

    # 3. Recolor Interior
    for row, col in interior_pixels:
        output_grid[row, col] = 4
    
    return output_grid