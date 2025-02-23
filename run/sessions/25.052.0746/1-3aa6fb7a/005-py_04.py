import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
      Identifies azure (8) colored "L" shaped objects and modifies specific adjacent cells.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find the objects and apply transformations
    for r in range(rows):
        for c in range(cols):
            # Check for a mirrored L-shape object (left-most cell of top-right)
            if (
                output_grid[r, c] == 8 and
                r + 1 < rows and
                c -1 >= 0 and
                output_grid[r, c - 1] == 8 and
                output_grid[r + 1, c - 1] == 8
            ):
                if c - 2 >= 0 :  # Boundary check for left cell
                    output_grid[r, c - 1] = 1

             # Check for a mirrored L-shape object (left-most cell of bottom-right)
            if (
                output_grid[r, c] == 8 and
                r - 1 >= 0 and
                c -1 >= 0 and
                output_grid[r, c - 1] == 8 and
                output_grid[r - 1, c - 1] == 8
            ):
                if c - 2 >= 0 :  # Boundary check for left cell
                    output_grid[r, c - 1] = 1

            # Check for the L-shape object (right-most cell)
            if (   output_grid[r, c] == 8 and
                r - 1 >= 0 and
                c + 1 < cols and
                output_grid[r - 1, c] == 8 and
                output_grid[r - 1, c + 1] == 8
            ):
                if c + 1 < cols :  # Boundary check for right cell
                    output_grid[r, c + 1] = 1

    return output_grid