"""
1.  **Identify Blue Blocks:** Find all contiguous groups of blue (1) pixels in the input grid.
2.  **Top-Row Blocks (Rows 0 and 1):**
    *   Iterate through the first two rows (row indices 0 and 1).
    *   For each blue pixel, check for "skipped" blue pixels horizontally. A "skipped" blue pixel is defined as another blue pixel two positions away (either left or right) with one pixel (of any color) between them, all within the top two rows.
    *   If a "skipped" blue pixel is found, change the color of the pixel in between to orange (7).
3. **Check position (1,1):**
    * If pixel at (1,1) is blue set it to orange.
4.  **Other Blue Blocks:**
    *   For blue blocks *not* entirely within the top two rows: If a block contains 3 or more pixels, change all pixels within that block to red (2).
5.  **White Pixels:** White (0) pixels always remain unchanged.
"""

import numpy as np

def find_contiguous_blocks(grid, color):
    """Finds contiguous blocks of a specified color in a grid."""
    visited = set()
    blocks = []

    def dfs(row, col, current_block):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_block.append((row, col))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_block)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_block = []
                dfs(row, col, current_block)
                blocks.append(current_block)
    return blocks

def transform(input_grid):
    """Transforms the input grid according to the rules."""

    # initialize output_grid
    output_grid = input_grid.copy()

    # Find all blue blocks
    blue_blocks = find_contiguous_blocks(input_grid, 1)

    # Top-row transforms (skip transform)
    for r in range(min(2, output_grid.shape[0])):  # Iterate through the first two rows
        for c in range(output_grid.shape[1]):
            if output_grid[r, c] == 1:
                # Check for skipped pixels to the right
                if c + 2 < output_grid.shape[1] and output_grid[r, c + 2] == 1:
                    output_grid[r, c + 1] = 7
                # Check for skipped pixels to the left
                if c - 2 >= 0 and output_grid[r, c - 2] == 1:
                    output_grid[r, c - 1] = 7

    # Check (1,1) and set to orange if blue
    if output_grid.shape[0] > 1 and output_grid.shape[1] > 1 and output_grid[1,1] == 1:
        output_grid[1,1] = 7
                    
    # Transform other blue blocks to red if size >= 3
    for block in blue_blocks:
        is_top_row = False
        for row, _ in block:
            if row in (0, 1):
                is_top_row = True
                break
        if not is_top_row and len(block) >= 3:
            for row, col in block:
                output_grid[row, col] = 2

    return output_grid