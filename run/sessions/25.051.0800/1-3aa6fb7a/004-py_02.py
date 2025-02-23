"""
The transformation rule preserves the azure (color 8) rectangles and adds a single blue (color 1) pixel adjacent to each azure rectangle. The blue pixel is added to the right of the rectangle if it is in the top-left quadrant, to the left if in the top-right or bottom-right quadrant, and above if in the bottom-left quadrant and close to the border.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of (row, col) tuples for each object found.
    """
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_2x1_rectangle(object_coords):
    """
    Checks if the object represented by the given coordinates is a 2x1 rectangle.
    """
    if len(object_coords) != 2:
        return False

    row_coords = sorted(list(set([coord[0] for coord in object_coords])))
    col_coords = sorted(list(set([coord[1] for coord in object_coords])))

    if len(row_coords) == 2 and len(col_coords) == 1 and row_coords[1] - row_coords[0] == 1:
        return True
    elif len(col_coords) == 2 and len(row_coords) == 1 and col_coords[1] - col_coords[0] == 1:
        return True
    
    return False
    

def transform(input_grid):
    """
    Transforms the input grid according to the rule: adds a blue pixel next to azure 2x1 rectangles.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for azure_object in azure_objects:
        if is_2x1_rectangle(azure_object):
            #get centroid
            centroid_row = sum([coord[0] for coord in azure_object]) / len(azure_object)
            centroid_col = sum([coord[1] for coord in azure_object]) / len(azure_object)

            rows, cols = input_grid.shape
            
            # get sorted row and cols
            row_coords = sorted(list(set([coord[0] for coord in azure_object])))
            col_coords = sorted(list(set([coord[1] for coord in azure_object])))
            
            if centroid_row < rows / 2 and centroid_col < cols/2:  # Top-left quadrant
                output_grid[row_coords[0], col_coords[0] + 1] = 1
            elif centroid_row < rows/2 and centroid_col >= cols/2: # Top Right Quadrant
                output_grid[row_coords[0], col_coords[0] - 1] = 1
            elif centroid_row >= rows/2 and centroid_col >= cols/2: # Bottom Right Quadrant
                output_grid[row_coords[0], col_coords[0] - 1] = 1
            elif centroid_row >= rows/2 and centroid_col < cols/2:
                output_grid[row_coords[0]-1, col_coords[0]] = 1
    return output_grid