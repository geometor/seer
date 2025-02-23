# e9afcf9a • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule can be described as follows:

1.  **Maintain Grid Dimensions:** The output grid has the same width and height as the input grid.
2.  **Checkerboard Pattern:** Create a checkerboard pattern of alternating colors in the output grid.
3.  **Color Mapping:** Use green (3) and maroon (9) as the alternating colors.
4.  **Starting Colors**:
    *   The first row of the output starts with the color of the first row of the input (green/3).
    *   The second row of the output starts with the color of the second row of the input (maroon/9).
5. **Alternation**: within each row, alternate between original row color and the other row color.
"""

import numpy as np

def transform(input_grid):
    """Transforms an input grid into a checkerboard pattern of green and maroon."""

    # Get the dimensions of the input grid.
    height, width = input_grid.shape

    # Initialize the output grid with the same dimensions.
    output_grid = np.zeros((height, width), dtype=int)

    # Get the colors from the input grid.  Assume rows are uniform color.
    color1 = input_grid[0, 0]  # first row color
    color2 = input_grid[1, 0]  # second row color

    # Create the checkerboard pattern.
    for row in range(height):
        for col in range(width):
            if row % 2 == 0:  # Even row
                if col % 2 == 0:
                    output_grid[row, col] = color1
                else:
                    output_grid[row, col] = color2
            else:  # Odd row
                if col % 2 == 0:
                    output_grid[row, col] = color2
                else:
                    output_grid[row, col] = color1

    return output_grid
```
