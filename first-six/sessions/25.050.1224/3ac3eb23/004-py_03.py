"""
The transformation identifies cells with colors 2 (red) and 8 (azure) in the input grid. For each of these cells, it generates a "3" or mirrored "E" shaped pattern in the output grid. This pattern is centered around the original cell's column and extends downwards, repeating every other row. The pattern consists of the original color, with additional cells of the same color placed immediately to the left and right of the central cell in each patterned row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding cells of color 2 (red) and 8 (azure) into a
    "3" shaped pattern, repeated every other row downwards.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] in (2, 8):  # Check for color 2 or 8
                color = input_grid[r, c]
                # Create the "3" pattern
                for i in range(3):  # Iterate every other row, up to 3 repetitions
                    row = r + i * 2
                    if row < rows:
                        output_grid[row, c] = color  # Center cell
                        if c - 1 >= 0:
                            output_grid[row, c - 1] = color  # Left cell
                        if c + 1 < cols:
                            output_grid[row, c + 1] = color  # Right cell

    return output_grid