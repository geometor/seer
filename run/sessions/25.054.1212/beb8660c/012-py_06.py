"""
Shift all contiguous non-zero color blocks down, filling the spaces, but keep the bottom row fixed.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by shifting non-zero color blocks down, keeping the bottom row fixed.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape
    output_grid = np.zeros_like(grid)

    # 1. Keep the bottom row fixed
    output_grid[-1, :] = grid[-1, :]

    # 2. Iterate through columns
    for c in range(cols):
        # 3. Extract non-zero pixels from the column (excluding the bottom row)
        column_pixels = []
        for r in range(rows - 1):
            if grid[r, c] != 0:
                column_pixels.append(grid[r, c])

        # 4. Shift pixels down in the column, maintaining order
        pixel_index = 0
        for r in range(rows - 2, -1, -1):
            if pixel_index < len(column_pixels):
                # Find the next available spot, moving upwards from the bottom
                current_row = rows - 2
                while current_row >= 0:
                    if output_grid[current_row + 1, c] == 0:
                        output_grid[current_row + 1, c] = column_pixels[pixel_index]
                        pixel_index += 1
                        break # move to next pixel
                    else:
                        current_row -= 1 # move check up one row.
            else:
                break


    return output_grid.tolist()