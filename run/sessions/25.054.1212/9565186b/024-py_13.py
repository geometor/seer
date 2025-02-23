"""
1.  **Identify the Middle Row:** Determine the row at index `height // 2` of the input grid.
2.  **Identify all colors in the middle row**
3.  **Identify Contiguous Vertical Blocks:** For each color present in the middle row, check if it forms a contiguous vertical block of pixels of the same color. A contiguous vertical block is defined as a set of pixels where each pixel is directly above or below another pixel of the same color, and this chain extends from the middle row upwards, downwards, or both.
4.  **Preserve Qualifying Blocks:** If a color from the middle row forms such a contiguous vertical block, preserve all pixels within that block in the output grid.
5. **Replace other pixels:** Change all other pixels that don't meet the requirements to gray (color code 5).
"""

import numpy as np

def _is_valid(r, c, grid):
    """Helper function to check if a coordinate is within grid bounds."""
    return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

def _find_vertical_block(grid, r, c, color):
    """
    Finds a contiguous vertical block of the given color starting from (r, c).
    """
    if not _is_valid(r, c, grid) or grid[r, c] != color:
        return []

    block = [(r, c)]
    # Check upwards
    up_r = r - 1
    while _is_valid(up_r, c, grid) and grid[up_r, c] == color:
        block.append((up_r, c))
        up_r -= 1

    # Check downwards
    down_r = r + 1
    while _is_valid(down_r, c, grid) and grid[down_r, c] == color:
        block.append((down_r, c))
        down_r -= 1

    return block

def transform(input_grid):
    # Initialize output_grid with gray (5)
    output_grid = np.full_like(input_grid, 5)
    height = input_grid.shape[0]
    middle_row_index = height // 2

    # Get colors present in the middle row
    middle_row_colors = set(input_grid[middle_row_index])

    # Iterate through each cell in the middle row
    for c in range(input_grid.shape[1]):
        color = input_grid[middle_row_index, c]
        
        # Check for vertical block and preserve
        if color in middle_row_colors:
            vertical_block = _find_vertical_block(input_grid, middle_row_index, c, color)
            if vertical_block:  # If a vertical block exists
               for br, bc in vertical_block:
                   output_grid[br, bc] = color

    return output_grid