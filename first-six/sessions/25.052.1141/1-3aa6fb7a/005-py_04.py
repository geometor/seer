import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def find_1x2_horizontal_rectangles(grid, color):
    """
    Finds coordinates of 1x2 horizontal rectangles
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols-1):
            if grid[r,c] == color and grid[r,c+1] == color:
                rectangles.append(((r,c),(r,c+1)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles_v = find_2x1_vertical_rectangles(output_grid, 8)
    azure_rectangles_h = find_1x2_horizontal_rectangles(output_grid, 8)

    for top_coord, bottom_coord in azure_rectangles_v:
        r_top, c_top = top_coord
        r_bot, c_bot = bottom_coord

        # Check if a 2x2 square can *only* be formed to the right
        can_form_right = (c_top + 1 < output_grid.shape[1] and
                          output_grid[r_top, c_top + 1] == 8 and
                          output_grid[r_bot, c_bot + 1] == 8)
        
        can_form_left = (c_top -1 >= 0 and c_top -2 >=0 and
                        output_grid[r_top, c_top -1] == 8 and
                        output_grid[r_bot, c_top -1] == 8)

        if can_form_right and not can_form_left:
            if c_top - 1 >= 0:
                output_grid[r_top, c_top - 1] = 1  # Place blue to the left

    for left_coord, right_coord in azure_rectangles_h:
        r_left, c_left = left_coord
        r_right, c_right = right_coord

        #Check if 2x2 can only be formed below
        can_form_below = (r_left + 1 < output_grid.shape[0] and
                         output_grid[r_left + 1, c_left] == 8 and
                         output_grid[r_right + 1, c_right] == 8)

        can_form_above = (r_left -1 >= 0 and r_left -2 >= 0 and
                          output_grid[r_left - 1, c_left] == 8 and
                         output_grid[r_left - 1, c_right] == 8)
        if can_form_below and not can_form_above:
            if r_left - 1 >= 0:
                output_grid[r_left - 1, c_left] = 1  # Place blue above
    return output_grid