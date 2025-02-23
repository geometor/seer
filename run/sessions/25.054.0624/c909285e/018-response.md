# c909285e • 018 • refine_coder

---
```python
"""
1.  **Find the Outermost Border:** Scan the input grid to identify the outermost rectangular border. The border is defined as a contiguous region of a single color that completely encloses an inner rectangular area. The border must be the outermost, connected set of pixels of same color.
2.  **Extract Inner Region:** Once the border is identified, extract the rectangular region located *inside* the border. This inner region is the area of interest.
3.  **Conditional Color Substitution:** Examine the *extracted inner region*. If color 5 is present within the inner region, replace all instances of color 5 with color 6.
4. **Output:** The transformed "inner region" from step 3 becomes the output grid.
"""

import numpy as np

def find_outermost_border(grid):
    """
    Finds the outermost rectangular border and returns its boundaries and color.
    Handles borders that are on the edges of the grid.
    """
    rows, cols = grid.shape

    # Iterate through all possible border colors
    for border_color in np.unique(grid):
        # Find top-left corner candidates for this color
        for top in range(rows):
            for left in range(cols):
                if grid[top, left] == border_color:
                    # Check if this is a valid outermost border
                    bottom, right = find_bottom_right(grid, top, left, border_color)
                    if bottom != -1:  # Valid corner found
                        if is_valid_outermost_border(grid, top, left, bottom, right, border_color):
                            return top, left, bottom, right, border_color
    return None, None, None, None, None

def find_bottom_right(grid, top, left, border_color):
    """Finds the bottom-right corner of a potential border."""
    rows, cols = grid.shape

    # Find bottom edge
    bottom = top
    while bottom + 1 < rows and grid[bottom + 1, left] == border_color:
        bottom += 1

    # Find right edge
    right = left
    while right + 1 < cols and grid[top, right + 1] == border_color:
        right += 1

    # Check if it's a valid corner (rectangle)
    if grid[bottom, right] != border_color:
        return -1, -1  # Invalid corner

    return bottom, right

def is_valid_outermost_border(grid, top, left, bottom, right, border_color):
    """Checks if the identified border is valid and outermost."""
    rows, cols = grid.shape

    # Check border consistency (all sides)
    for row in range(top, bottom + 1):
        if grid[row, left] != border_color or grid[row, right] != border_color:
            return False
    for col in range(left, right + 1):
        if grid[top, col] != border_color or grid[bottom, col] != border_color:
            return False

    # Check for no internal pixels of the same border color (outermost)
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            if grid[row, col] == border_color:
                return False

    return True

def extract_inner_region(grid, top, left, bottom, right):
    """Extracts the inner region of the border."""
    return grid[top+1:bottom, left+1:right]

def conditional_color_substitution(inner_region):
    """Replaces all instances of 5 with 6 in the inner region if 5 exists."""
    if 5 in inner_region:
        return np.where(inner_region == 5, 6, inner_region)
    else:
        return inner_region
    

def transform(input_grid):
    """
    Transforms the input grid according to the defined rules.
    """
    grid = np.array(input_grid)

    # 1. Find the Outermost Border
    top, left, bottom, right, border_color = find_outermost_border(grid)
    
    if top is None:
        return [] # No border found, return empty grid

    # 2. Extract Inner Region
    inner_region = extract_inner_region(grid, top, left, bottom, right)

    # 3. Conditional Color Substitution
    transformed_inner_region = conditional_color_substitution(inner_region)

    # 4. Output the transformed inner region
    return transformed_inner_region.tolist()
```
