import numpy as np

def find_isolated_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of *isolated* 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                # Check for isolation:
                is_isolated = True

                # Check above and below
                if r > 0 and grid[r - 1, c] == color:
                    is_isolated = False
                if r + 2 < rows and grid[r + 2, c] == color:
                    is_isolated = False

                # Check left and right of both cells
                if c > 0:
                    if grid[r, c - 1] == color or grid[r+1, c-1] == color:
                        is_isolated = False
                if c + 1 < cols:
                    if grid[r, c + 1] == color or grid[r+1, c+1] == color :
                        is_isolated = False
                

                if is_isolated:
                    rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule:
    Locate each *isolated* 2x1 vertical rectangle of azure color (8).
    Add a blue cell (1) to the immediate right of the top cell of the 2x1 azure object.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_isolated_2x1_vertical_rectangles(output_grid, 8)

    for top_coord, _ in azure_rectangles:
        # Add a blue cell to the right of the top cell, if within bounds
        if top_coord[1] + 1 < output_grid.shape[1]:
            output_grid[top_coord[0], top_coord[1] + 1] = 1

    return output_grid