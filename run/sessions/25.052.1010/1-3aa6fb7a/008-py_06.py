"""
The transformation rule identifies vertical azure (color 8) rectangles of size 2x1. It then adds a blue cell (color 1) based on the rectangle's position relative to other azure rectangles:

1.  **Identify Azure Rectangles:** Locate all 2x1 vertical rectangles of color 8 (azure).
2.  **Topmost Rectangle Rule:** For the topmost 2x1 azure rectangle, a blue cell is added to its top-right.
3. **All the rest:** Add blue cell at bottom-left.
"""

import numpy as np

def find_vertical_rectangles(grid, color):
    """
    Find and return the positions of all 2x1 vertical rectangles of the specified color.
    """
    vertical_objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):  # Iterate up to the second-to-last row
        for c in range(cols):
            # Vertical 2x1 rectangle
            if grid[r, c] == color and grid[r + 1, c] == color:
                vertical_objects.append((r, c))
    return vertical_objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all 2x1 (vertical) rectangles of color 8 (azure)
    vertical_azure_objects = find_vertical_rectangles(output_grid, 8)
    
    # Apply rules for vertical rectangles
    for r, c in vertical_azure_objects:
        # Check if it's the top part of a vertical azure rectangle
        if r == 0 or output_grid[r - 1, c] != 8:  # Topmost part
            # Insert at top-right corner if possible
            if c + 1 < output_grid.shape[1]:
                output_grid[r, c + 1] = 1
        else:
            if c>0:
                output_grid[r+1,c-1]=1
    
    return output_grid