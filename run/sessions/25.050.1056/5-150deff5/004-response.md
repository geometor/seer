# 5-150deff5 • 004 • example_2 - CODE

---
```python
"""
The transformation rule involves identifying a contiguous object of color 5 (gray) in the input grid. This gray object is then transformed in the output grid as follows:

1.  **Identify the Gray Object:** Locate the contiguous region of color 5 (gray).

2.  **Color Replacement 1 (Azure):** Specific parts of the gray object are replaced with color 8 (azure). The spatial pattern appears to be rule-based, favoring upper and right-side portions within the gray object.

3.  **Color Replacement 2 (Red):** The remaining parts of the gray object, not filled with azure, are replaced with color 2 (red). This fills the internal gaps and left/lower portions.

4. **Background Preservation:** The background color 0 (white) remains unchanged throughout the transformation.

"""

import numpy as np

def get_object(grid, color):
    """
    Finds the contiguous region of a specified color.

    Returns a mask where object pixels are True, and the background is False.
    """
    mask = (grid == color)
    return mask

def transform(input_grid):
    """
    Transforms the input grid by recoloring a gray (5) object with azure (8) and red (2) sub-shapes,
    while preserving the background (0).
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Get the mask for the gray object (color 5)
    gray_mask = get_object(input_grid, 5)

    # Get the coordinates of the gray object
    coords = np.argwhere(gray_mask)

    # Find the bounding box of the gray object
    min_row = np.min(coords[:, 0])
    max_row = np.max(coords[:, 0])
    min_col = np.min(coords[:, 1])
    max_col = np.max(coords[:, 1])
   
    # Iterate through the gray object's coordinates
    for r, c in coords:
        # Apply color replacement rules based on relative position within the object.
        # These rules are derived from observing the two examples and are heuristics.

        # Azure (8) rule: Prioritize top and right portions.
        if (r - min_row) <= (max_row - min_row) / 2 and (c-min_col) > (max_col - min_col) /2:
            output_grid[r, c] = 8
        elif (r - min_row) <= (max_row - min_row) / 2 and (c - min_col) <= (max_col - min_col)/2 and (r - min_row) <= (max_row-min_row)*0.2:
            output_grid[r,c] = 8;
        elif (r - min_row) > (max_row - min_row) / 2 and (c - min_col) > (max_col - min_col) /2 and c == max_col:
            output_grid[r,c] = 8


        # Red (2) rule: Fill the remaining parts.
        elif input_grid[r, c] == 5:
            output_grid[r, c] = 2

    return output_grid
```

