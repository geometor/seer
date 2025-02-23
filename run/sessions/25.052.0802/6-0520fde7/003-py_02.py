import numpy as np

def find_vertical_line(grid, color):
    # Find contiguous vertical lines of the specified color
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 2):
            if grid[r, c] == color and grid[r+1, c] == color and grid[r+2, c] == color:
                return (r,c)  #return top of the vertical line
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Find the top cell of the vertical line of color 5
    top_cell = find_vertical_line(input_grid, 5)

    # Initialize the output grid as a 3x3 array filled with 0s
    output_grid = np.zeros((3, 3), dtype=int)

    # If a vertical line of color 5 is found, change the center cell to 2
    if top_cell:
        top_row, center_col = top_cell
        output_grid[1, 1] = 2
        output_grid[0,2] = input_grid[top_row,center_col]
        output_grid[2,2] = input_grid[top_row+2,center_col]

    return output_grid