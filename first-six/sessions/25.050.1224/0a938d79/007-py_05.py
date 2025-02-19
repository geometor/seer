"""
The transformation involves replicating the initial objects horizontally and then repeating the generated rows at specific intervals.

1.  **Identify Initial Objects**: The input grid contains two single-cell objects.

2.  **Horizontal Replication**:
    *   Each object with a non-zero color is replicated across its entire row.

3.  **Vertical Pattern Repetition**:
     *    Each filled row is repeated every 8 rows downwards.

"""

import numpy as np

def transform(input_grid):
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find initial objects
    initial_objects = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                initial_objects.append(((r, c), input_grid[r, c]))

    # Replicate horizontally and then vertically
    for obj in initial_objects:
        pos, color = obj
        initial_row, _ = pos

        # Horizontal replication
        for c in range(cols):
            output_grid[initial_row, c] = color

        # Vertical repetition
        for i in range(1,(rows - initial_row) // 8 + 1):
            new_row = initial_row + 8 * i
            if new_row < rows:
               for c in range(cols):
                    output_grid[new_row,c] = color

    return output_grid