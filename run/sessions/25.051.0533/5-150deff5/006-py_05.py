"""
The transformation rule can be summarized as follows:

1.  Locate all gray (5) colored regions.
2.  Within each contiguous horizontal segment of a gray region, change all gray cells to red (2) except the rightmost cell.
3.  Change the rightmost gray cell in each contiguous horizontal segment to azure (8).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                # Find the rightmost cell in this contiguous horizontal segment
                c_end = c
                while c_end + 1 < cols and output_grid[r, c_end + 1] == 5:
                    c_end += 1

                # Change the rightmost cell to azure (8)
                output_grid[r, c_end] = 8

                # Change the remaining cells in the segment to red (2)
                for c_inner in range(c, c_end):
                    output_grid[r, c_inner] = 2
                
                c = c_end # optimization

    return output_grid