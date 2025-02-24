"""
1.  **Duplicate:** Create a new output grid that is twice the height and twice the width of the input grid.
2.  **Copy:** Copy the input grid into each of the four quadrants of the output grid. This creates a 2x2 repetition of the input pattern.
3.  **Connect:** Iterate through all the empty cells (value 0) in the *output grid*. If an empty cell is horizontally or vertically adjacent to *any* non-zero pixel that originated from the input grid (i.e., it's part of the duplicated pattern), fill that empty cell with the value 8 (azure).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape

    # 1. Duplicate: Calculate output grid size.
    output_rows = 2 * input_rows
    output_cols = 2 * input_cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # 2. Copy to output: Copy the input grid to the four quadrants.
    for i in range(2):
        for j in range(2):
            start_row = i * input_rows
            start_col = j * input_cols
            output_grid[start_row:start_row + input_rows, start_col:start_col + input_cols] = input_grid

    # 3. Connect with 8's: Fill based on adjacency to copied input.
    for r in range(output_rows):
        for c in range(output_cols):
            if output_grid[r, c] == 0:  # Check only empty cells
                is_adjacent = False
                # Check adjacency within the duplicated areas
                for i in range(2):
                    for j in range(2):
                        start_row = i * input_rows
                        start_col = j * input_cols
                        # Check horizontal and vertical neighbors
                        if start_row <= r < start_row + input_rows and start_col <= c < start_col + input_cols:
                            if r > 0 and output_grid[r - 1, c] != 0 and output_grid[r-1,c] != 8:  
                                is_adjacent = True
                            if r < output_rows - 1 and output_grid[r + 1, c] != 0 and output_grid[r+1, c] != 8:
                                is_adjacent = True
                            if c > 0 and output_grid[r, c - 1] != 0 and output_grid[r, c-1] !=8:
                                is_adjacent = True
                            if c < output_cols - 1 and output_grid[r, c + 1] !=0 and output_grid[r,c+1] != 8:
                                is_adjacent = True
                if is_adjacent:
                    output_grid[r,c] = 8

    return output_grid.tolist()