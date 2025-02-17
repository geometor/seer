import numpy as np

def transform_grid(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all azure (color 8) objects
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:
                # Check if this is the top-left cell of a new object

                is_new_object = True
                if r > 0 and input_grid[r-1,c] == 8:
                    is_new_object = False # part of a vertical object from above
                if c > 0 and input_grid[r,c-1] == 8:
                    is_new_object = False

                if is_new_object:
                    #find the top cell
                    top_row = r
                    top_col = c

                    # Place a blue pixel to the right
                    if top_col + 1 < cols:
                            output_grid[top_row, top_col + 1] = 1
    return output_grid