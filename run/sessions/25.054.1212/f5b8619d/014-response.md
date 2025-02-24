# f5b8619d • 014 • example_3 • investigate_coder

---
```python
"""
Expands the input grid to double its size, creating 2x2 blocks in the output
grid based on each input cell. White cells are expanded to a block with
alternating white and azure pixels, while other colored cells are expanded to
a block where the top-left cell remains the same, while the cells below and
diagonally from it are azure.
"""

import numpy as np

def transform(input_grid):
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    for i in range(input_height):
        for j in range(input_width):
            # Get the original cell value
            original_value = input_grid[i, j]

            # Calculate the top-left corner of the 2x2 block in the output grid
            output_row = i * 2
            output_col = j * 2

            # Assign values to the 2x2 block
            output_grid[output_row, output_col] = original_value  # Top-left

            if original_value == 0:  # White
                 output_grid[output_row + 1, output_col] = 8      # Bottom-left
                 output_grid[output_row, output_col + 1] = 0      # Top-right
                 output_grid[output_row + 1, output_col + 1] = 8  # Bottom-right
            else:
                output_grid[output_row + 1, output_col] = 8      # Bottom-left
                output_grid[output_row, output_col + 1] = original_value     # Top-right
                output_grid[output_row + 1, output_col + 1] = 8  # Bottom-right

    return output_grid
```
