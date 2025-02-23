# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
1.  **Identify L-Shaped Objects:** Locate all "L" shaped objects within the input grid. These objects are composed of three contiguous cells of color 8 (azure) that form a 2x2 square with one cell missing. The "L" can be in any of the four possible orientations.

2.  **Locate the Inner Corner:** For each identified L-shaped object, pinpoint the "inner corner." The inner corner is the single cell *adjacent* to the three cells forming the "L" in a diagonal direction. Specifically, it's the cell that would complete the 2x2 square. It's important to determine the correct inner corner based on the orientation of the "L".

3. **Add blue to internal corner** Change the value (color) of the inner corner to 1 (blue).

4.  **Preserve Other Cells:** All other cells in the grid that are not identified as the inner corner of an L-shape should remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates (row, col) of the "tip" of each L.
    The tip is defined as the cell which has neighbors to the right and down.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (tip at top-left)
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
                # Check for L-shape (tip at top-right)
                elif grid[r + 1, c] == color and grid[r, c-1] == color and c > 0:
                    l_shapes.append((r,c))
                # Check for L-shape (tip at bottom-left)
                elif grid[r-1,c] == color and grid[r,c+1] == color and r > 0:
                    l_shapes.append((r,c))
                 # Check for L-shape (tip at bottom-right)
                elif grid[r-1,c] == color and grid[r,c-1] == color and r > 0 and c > 0:
                    l_shapes.append((r,c))    
    return l_shapes

def get_inner_corner(grid, tip, color):
    """
    Finds the inner corner coordinate for a given L-shape tip.
    """
    r, c = tip
    # Check which type of L-shape it is and calculate the inner corner
    
    if grid[r + 1, c] == color and grid[r, c + 1] == color:
         return (r + 1, c + 1)

    elif grid[r + 1, c] == color and grid[r, c - 1] == color:
        return (r+1, c-1)
        
    elif grid[r - 1, c] == color and grid[r, c + 1] == color:
        return (r-1, c+1)
        
    elif grid[r - 1, c] == color and grid[r, c - 1] == color:
        return (r-1,c-1)

    return None  # Should not happen if the tip is correctly identified


def transform(input_grid):
    """
    Transforms the input grid according to the L-shape rule.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all L-shapes of color 8
    l_shapes = find_l_shapes(output_grid, 8)

    # For each L-shape, find the inner corner and change its color to 1
    for tip in l_shapes:
        inner_corner = get_inner_corner(output_grid, tip, 8)
        if inner_corner:
            output_grid[inner_corner] = 1

    return output_grid
```

