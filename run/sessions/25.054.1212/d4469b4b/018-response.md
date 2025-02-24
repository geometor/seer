# d4469b4b • 018 • refine_coder

---
```python
"""
1.  **Input and Output:** The input is a 5x5 grid, and the output is a 3x3 grid.

2.  **Color Mapping:** The output grid will contain only colors 0 (white) and 5 (gray).

3.  **Conditional Transformation:** The transformation depends on whether color 3 (green) is present anywhere in the input grid.

4.  **Green IS Present:**
    *   Iterate through all nine possible 3x3 regions within the 5x5 input grid.
    *   The output grid's corresponding cell (at the same row,col as the top,left of the input 3x3) becomes gray (5) if the *corresponding* 3x3 region in the input contains any green (3) pixels. Otherwise, the output cell is white (0). For example: If the top-left 3x3 region of the input contains green, the top-left cell of the output is gray.

5.  **Green is NOT Present:**
    *   If green is not present anywhere in the input grid, the output will be a "cross" pattern of gray pixels:
        *   The entire top row of the output is gray (5).
        *   The entire bottom row of the output is gray (5)
        *    The center *column* of the output is gray (5).
        *   All other cells are white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as 3x3 with all white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check if green exists in the input grid
    if np.any(input_grid == 3):
        # Iterate through all 3x3 regions
        for i in range(3):
            for j in range(3):
                # Check if green is present in the current 3x3 region
                if np.any(input_grid[i:i+3, j:j+3] == 3):
                    output_grid[i, j] = 5
    else:
        # Create a gray cross pattern
        output_grid[0, :] = 5  # Top row
        output_grid[:, 1] = 5  # Center column
        output_grid[2, :] = 5  # Bottom row

    return output_grid
```
