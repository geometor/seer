"""
1.  **Identify Objects:** Find all distinct objects in the input grid.  An object is a group of contiguous pixels of the same color.
2.  **Calculate Centroids:** For each object, calculate its centroid. The centroid is the average of the row and column indices of all pixels in the object.
3.  **Determine Target Row and Column:**
    *   The *target column* is the column index of the object's centroid.
    *   The *target row* is the maximum row index (bottom-most row) of the bounding box containing the object.
4.  **Apply Transformation:** For each object, change the pixel at the target row and target column to yellow (color value 4).
5.  **Preserve Other Pixels:** All pixels not modified in step 4 retain their original colors from the input grid.
"""

import numpy as np

def find_objects(grid):
    # Find distinct objects in the grid.
    objects = []
    visited = set()

    def is_valid(row, col):
        return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

    def dfs(row, col, color, obj):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        # Explore adjacent cells (up, down, left, right)
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row_index, row in enumerate(grid):
        for col_index, cell_value in enumerate(row):
            if (row_index, col_index) not in visited and cell_value != 0:
                obj = []
                dfs(row_index, col_index, cell_value, obj)
                objects.append(obj)
    return objects

def calculate_centroid(coords):
    # Calculate the centroid of a list of coordinates.
    if not coords:
        return None
    sum_row = sum(coord[0] for coord in coords)
    sum_col = sum(coord[1] for coord in coords)
    centroid_row = sum_row // len(coords)
    centroid_col = sum_col // len(coords)
    return (centroid_row, centroid_col)

def find_max_row(obj):
    # finds the lowest row (highest row value)
    max_row = -1
    for row, _ in obj:
        if row > max_row:
            max_row = row
    return max_row

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find distinct objects
    objects = find_objects(input_grid)

    # apply transformation for each object
    for obj in objects:
        # calculate centroid
        centroid = calculate_centroid(obj)

        # determine the target row (max row for the object)
        target_row = find_max_row(obj)

        # determine target column from centroid
        target_col = centroid[1]

        # apply transformation: change pixel to yellow (4)
        output_grid[target_row, target_col] = 4

    return output_grid