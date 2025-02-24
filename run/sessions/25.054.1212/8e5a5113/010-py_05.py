"""
The input grid is transformed by replacing white (0) pixels following a grey (5) pixel with a repeating pattern. The pattern is seeded by the three colors immediately to the right of the grey (5). If fewer than three colors are available before another 5 or the end of the row, the available colors are used. The pattern repeats until another 5 is encountered, or the end of the row is reached.
"""

import numpy as np

def get_pattern(grid, row, col):
    """Extracts the pattern to the right of a grey (5) pixel."""
    rows, cols = grid.shape
    pattern = []
    for c in range(col + 1, cols):
        if grid[row, c] == 5:
          break;
        pattern.append(grid[row, c])
    return pattern

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        pattern = []
        pattern_index = 0
        filling = False  # Flag to indicate if we are in a filling state

        for c in range(cols):
            if input_grid[r, c] == 5:
                pattern = get_pattern(input_grid, r, c)
                pattern_index = 0
                filling = True
                continue # move to the next column after the 5

            if filling:  # we are after 5
                if input_grid[r,c] == 0: # and this pixel needs replacing
                    if pattern: # and the pattern is valid
                        output_grid[r, c] = pattern[pattern_index % len(pattern)]
                        pattern_index += 1
                else:
                  # stop filling if we see any other non-zero color
                  filling = False;
            # else, we are not after a 5, so just continue

    return output_grid