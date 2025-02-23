# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Vertical Lines:** Examine the input grid and identify all distinct, contiguous vertical lines of azure (8) pixels. A vertical line is defined as a set of one or more vertically adjacent azure pixels.
2.  **Transform Top and Bottom:** For each identified vertical line:
    *   Change the color of the top-most azure pixel to blue (1).
    *   Change the color of the bottom-most azure pixel to blue (1).
3. **Preserve other Pixels:** All other pixels in the grid that are not the top or bottom pixel of an azure veritcal line retain their original color.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions and values as the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    def is_azure(grid, r, c):
        """Helper function to check if a pixel is azure."""
        return 0 <= r < rows and 0 <= c < cols and grid[r, c] == 8

    def find_vertical_lines(grid):
        """Helper function to find all distinct vertical lines of azure pixels."""
        lines = []
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if is_azure(grid, r, c) and (r, c) not in visited:
                    # Start a new line
                    current_line = []
                    current_row = r
                    while is_azure(grid, current_row, c):
                        current_line.append((current_row, c))
                        visited.add((current_row, c))
                        current_row += 1
                    lines.append(current_line)
        return lines

    # Identify all vertical lines
    vertical_lines = find_vertical_lines(output_grid)

    # Transform the top and bottom pixels of each line
    for line in vertical_lines:
        if line:  # Ensure the line is not empty
            top_pixel_row, top_pixel_col = line[0]
            bottom_pixel_row, bottom_pixel_col = line[-1]
            output_grid[top_pixel_row, top_pixel_col] = 1
            output_grid[bottom_pixel_row, bottom_pixel_col] = 1

    return output_grid
```
