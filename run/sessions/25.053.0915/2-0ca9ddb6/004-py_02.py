"""
1. **Preservation:** The original positions of colors 1 (blue), 2 (red), and 8 (azure) in the input grid remain unchanged in the output grid.

2.  **Orange (7) Expansion:**  An orange (7) pixel appears to the immediate left, right, and below each blue (1) and red (2) pixel. If these positions are occupied, the existing color is prioritized.

3. **Yellow(4) Expansion**: Yellow pixels appear. Looking at the output, a yellow pixel appears to the immediate left, right, above, below of positions occupied by color 7, with the following two conditions: a- do not place color 4 over existing colors 1,2,7 or 8. b- Do not add additional pixels on the edges of the grid (9x9).

4. **Fill:** all other positions are filled with color 0.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find the positions of colors 1, 2, and 8
    positions_1 = np.argwhere(input_grid == 1)
    positions_2 = np.argwhere(input_grid == 2)
    # positions_8 = np.argwhere(input_grid == 8) # Color 8 is handled correctly by initialization

    # Orange (7) expansion around 1 and 2
    for pos in np.concatenate((positions_1, positions_2)):
        row, col = pos
        # Add orange to the left, right, and below
        neighbors = [(row, col - 1), (row, col + 1), (row + 1, col)]
        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and output_grid[r, c] == 0:
                output_grid[r, c] = 7

    #find positions of color 7
    positions_7 = np.argwhere(output_grid == 7)
    # Yellow (4) expansion around 7
    for pos in positions_7:
        row, col = pos
        neighbors = [(row-1,col),(row + 1, col), (row, col - 1), (row, col + 1)]

        for r,c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and output_grid[r,c] == 0:
                output_grid[r,c] = 4


    return output_grid