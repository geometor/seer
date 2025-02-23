# aedd82e4 • 018 • refine_coder

---
```python
"""
Transforms red pixels to blue based on their adjacency to 2x2 red squares or partial 2x2 red squares, and isolated red pixels.
"""

import numpy as np

def find_2x2_squares(grid, color):
    """Finds all 2x2 squares of the specified color."""
    rows, cols = grid.shape
    squares = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i, j] == color and
                grid[i + 1, j] == color and
                grid[i, j + 1] == color and
                grid[i + 1, j + 1] == color):
                squares.append((i, j))
    return squares

def find_partial_2x2_squares(grid, color):
    """Finds instances where three pixels of the specified color form a corner of a 2x2 square."""
    rows, cols = grid.shape
    partials = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            count = 0
            if grid[i, j] == color:
                count += 1
            if grid[i + 1, j] == color:
                count += 1
            if grid[i, j + 1] == color:
                count += 1
            if grid[i + 1, j + 1] == color:
                count += 1
            if count == 3:
                partials.append((i, j))
    return partials
    
def transform(input_grid):
    """
    Transforms the input grid based on 2x2, partial 2x2 red squares, and isolated red pixels.
    """
    output_grid = np.copy(input_grid)
    red_squares = find_2x2_squares(output_grid, 2)
    partial_red_squares = find_partial_2x2_squares(output_grid, 2)
    
    rows, cols = output_grid.shape

    # Handle complete 2x2 squares (Example 3 logic)
    for i, j in red_squares:
        output_grid[i + 1, j + 1] = 1

    # Handle partial 2x2 squares (Examples 2 and 4 logic)
    for i, j in partial_red_squares:
        # Check which corner is missing and change adjacent red pixels accordingly.
        if output_grid[i, j] != 2:  # Top-left missing
            if i > 0 and output_grid[i - 1, j] == 2 :
                output_grid[i-1,j] = 1
            if j > 0 and output_grid[i,j-1] == 2:
                output_grid[i,j-1] = 1
        if output_grid[i + 1, j] != 2:  # Bottom-left missing
            if i + 2 < output_grid.shape[0] and output_grid[i + 2, j] == 2:
                 output_grid[i+2,j] = 1
            if j > 0 and output_grid[i+1,j-1] ==2:
                output_grid[i+1,j-1] = 1

        if output_grid[i, j + 1] != 2:  # Top-right missing
            if i > 0 and output_grid[i -1, j+1] == 2:
                output_grid[i-1,j+1] = 1
            if j + 2 < output_grid.shape[1] and output_grid[i, j+2] == 2:
                output_grid[i,j+2] = 1
        if output_grid[i + 1, j + 1] != 2:  # Bottom-right missing
            if i + 2 < output_grid.shape[0] and output_grid[i+2,j+1] ==2:
                output_grid[i + 2, j+1] = 1
            if j + 2 < output_grid.shape[1] and output_grid[i+1,j+2] == 2:
                output_grid[i+1,j+2] = 1

    # Handle red pixels above complete 2x2 squares (Example 1)
    for i, j in red_squares:
        if i > 0 and output_grid[i - 1, j] == 2:
            output_grid[i - 1, j] = 1
        if i > 0 and output_grid[i - 1, j + 1] == 2:
            output_grid[i - 1, j + 1] = 1

    # handle isolated red pixels in example 2
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 2:
                is_isolated = True
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                         if (i != r or j != c) and output_grid[i,j] == 2:
                            is_isolated = False
                            break
                    if not is_isolated:
                        break
                if is_isolated:
                    output_grid[r,c] = 1
    return output_grid
```
