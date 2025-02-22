import numpy as np

def find_horizontal_objects(grid, color):
    """
    Find and return the positions of all *horizontal* 2x1 rectangles of the specified color.
    Returns a list of (row, col) tuples, where (row, col) is the top-left cell of the rectangle.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols - 1):
            if grid[r, c] == color and grid[r, c + 1] == color:
                objects.append((r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_horizontal_objects(output_grid, 8)

    if azure_objects:  # Check if the list is not empty
        # Find top-most rectangle
        top_most = min(azure_objects, key=lambda x: x[0])
        # Insert blue cell to the right
        top_right_pos = (top_most[0], top_most[1] + 2)
        if top_right_pos[1] < output_grid.shape[1]:
            output_grid[top_right_pos] = 1


        # Find bottom-most rectangle
        bottom_most = max(azure_objects, key=lambda x: x[0])

        #If many objects on the same row, we choose the left-most.
        bottom_objects_same_row = [obj for obj in azure_objects if obj[0] == bottom_most[0]]
        bottom_most = min(bottom_objects_same_row, key=lambda x: x[1])


        # Insert blue cell to the left
        bottom_left_pos = (bottom_most[0], bottom_most[1] - 1)
        if bottom_left_pos[1] >= 0:
            output_grid[bottom_left_pos] = 1

    return output_grid