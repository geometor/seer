"""
The transformation involves replicating the initial objects horizontally and then repeating the generated rows at specific intervals.

1.  **Identify Initial Objects**: The input grid contains two single-cell objects: one of color 2 and one of color 3.

2.  **Horizontal Replication**:
    *   The object with color 2 is replicated across the entire row (row 5).
    *   The object with color 3 is replicated across the entire row (row 7).

3.  **Vertical Pattern Repetition**:
     *    The row with color 2 (row 5) is repeated every 4 rows downwards.
     *   The row with color 3 (row 7) is repeated every 4 rows downwards.
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
        for i in range(1,(rows - initial_row) // 4 + 1):
            new_row = initial_row + 4 * i
            if new_row < rows :
               for c in range(cols):
                    output_grid[new_row,c] = color

    return output_grid