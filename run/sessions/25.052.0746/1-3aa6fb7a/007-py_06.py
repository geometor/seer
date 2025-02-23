import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on identifying 'L' shaped objects of color 8 and changing adjacent cells to color 1.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            # Check for right-facing L
            if (r > 0 and c < cols - 1 and
                output_grid[r, c] == 8 and
                output_grid[r - 1, c] == 8 and
                output_grid[r - 1, c + 1] == 8):
                output_grid[r, c + 1] = 1

            # Check for left-facing L
            if (r < rows - 1 and c > 0 and
                output_grid[r, c] == 8 and
                output_grid[r, c - 1] == 8 and
                output_grid[r + 1, c - 1] == 8):
                output_grid[r, c - 1] = 1

            # Check for bottom-left-facing L
            if (r > 0 and c > 0 and
                output_grid[r, c] == 8 and
                output_grid[r, c - 1] == 8 and
                output_grid[r - 1, c - 1] == 8):
                    output_grid[r, c-1] = 1

            # Check for top-right-facing L
            if (r < rows -1 and c < cols - 1 and
                output_grid[r,c] == 8 and
                output_grid[r, c+1] == 8 and
                output_grid[r+1,c+1] == 8):
                    output_grid[r,c+1] = 1
    return output_grid