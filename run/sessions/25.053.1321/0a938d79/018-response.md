# 0a938d79 • 018 • example_3 - CODE

---
```python
"""
1.  **Identify Key Pixels:** Locate all pixels in the input grid that are not white (0).
2.  **Iterate Through Key Pixels:** For each non-white pixel:
    *   Get its color and the index of the row it's in.
    *   Fill the entire row with that pixel's color.
    *   Starting from the row immediately below, and repeating every other row after, fill those rows to the same color.
    * Continue the alternating row fills until reach bottom of the input.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds the coordinates and colors of all non-white pixels in a grid."""
    non_white_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel_value in enumerate(row):
            if pixel_value != 0:
                non_white_pixels.append({
                    "row": row_index,
                    "col": col_index,
                    "color": pixel_value
                })
    return non_white_pixels

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows = len(output_grid)
    cols = len(output_grid[0])

    # Find all non-white pixels.
    non_white_pixels = get_non_white_pixels(input_grid)

    # Iterate through the non-white pixels.
    for pixel_info in non_white_pixels:
        color = pixel_info["color"]
        start_row = pixel_info["row"]

        # Fill the initial row.
        output_grid[start_row, :] = color

        # Fill alternating rows below.
        for r in range(start_row + 2, rows, 2):
            output_grid[r, :] = color

    return output_grid
```
