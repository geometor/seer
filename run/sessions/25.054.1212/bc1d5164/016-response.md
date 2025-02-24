# bc1d5164 • 016 • refine_coder

---
```python
"""
The transformation rule identifies the outermost pixels of a non-zero color in the input grid and maps them onto a 3x3 output grid, preserving their relative positions. The remaining cells in the output grid are filled with white (0) pixels.
"""

import numpy as np

def get_outermost_pixels(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    outermost_pixels = []
    outermost_color = 0

    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and input_grid[r, c] != 0:
                if outermost_color == 0:
                  outermost_color = input_grid[r,c]
                outermost_pixels.append((r, c))
    return outermost_pixels, outermost_color

def transform(input_grid):
    """
    Transforms the input grid according to the rule: extracts outermost pixels,
    places them on 3x3 grid, and fills the rest with '0's.
    """
    outermost_pixels, outermost_color = get_outermost_pixels(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)

    # Map outermost pixels to output grid based on relative position
    num_pixels = len(outermost_pixels)

    if num_pixels > 0:
        # get corners
        min_row = min(outermost_pixels, key=lambda item: item[0])[0]
        max_row = max(outermost_pixels, key=lambda item: item[0])[0]
        min_col = min(outermost_pixels, key=lambda item: item[1])[1]
        max_col = max(outermost_pixels, key=lambda item: item[1])[1]

        for r, c in outermost_pixels:
            # map corners
            if r == min_row and c == min_col:
                output_grid[0, 0] = outermost_color
            elif r == min_row and c == max_col:
                output_grid[0, 2] = outermost_color
            elif r == max_row and c == min_col:
                output_grid[2, 0] = outermost_color
            elif r == max_row and c == max_col:
                output_grid[2, 2] = outermost_color
            # map edges
            elif r == min_row:
                output_grid[0, 1] = outermost_color
            elif r == max_row:
                output_grid[2, 1] = outermost_color
            elif c == min_col:
                output_grid[1, 0] = outermost_color
            elif c == max_col:
                output_grid[1, 2] = outermost_color
            else: # center, should not happen, but...
                output_grid[1,1] = outermost_color

    return output_grid.tolist()
```
