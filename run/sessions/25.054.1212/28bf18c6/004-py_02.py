"""
1.  **Find the Cluster:** Identify a contiguous cluster of non-black (non-zero) pixels within the input grid.
2.  **Determine Bounding Box:** Calculate the bounding box of this cluster.
3.  **Calculate Output Dimensions:** The output grid always has 3 rows. The number of columns is twice the width of the bounding box.
4.  **Construct Output Grid:** Create a new grid. Fill by alternating between the color in the original image and black (0), starting from the top-left of the bounding box in the input, and inserting black.
5.  Return the result.
"""

import numpy as np

def find_cluster(grid):
    # Find coordinates of all non-zero pixels.
    coords = np.argwhere(grid != 0)
    if coords.size == 0:
        return None, None, None, None  # No cluster found
    min_row = np.min(coords[:, 0])
    max_row = np.max(coords[:, 0])
    min_col = np.min(coords[:, 1])
    max_col = np.max(coords[:, 1])
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    input_grid = np.array(input_grid)
    # Find the bounding box of the non-zero cluster.
    min_row, max_row, min_col, max_col = find_cluster(input_grid)
    
    if min_row is None:  # Handle cases where no cluster is found
       return [[0]] # Return a 1x1 grid with a black pixel

    # Calculate output dimensions.
    output_rows = 3
    output_cols = (max_col - min_col + 1) * 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # construct output
    for i in range(output_rows):
        output_col_index = 0
        for j in range(min_col, max_col + 1):
            # get input row, add modulo in case outside range
            input_row = min_row + i
            if input_row < input_grid.shape[0] and j < input_grid.shape[1]:
              output_grid[i, output_col_index] = input_grid[input_row, j]
            else:
                # if out of range use background
                output_grid[i, output_col_index] = 0
            output_col_index += 1
            # next is background
            output_grid[i, output_col_index] = 0  # black pixel
            output_col_index += 1

    
    return output_grid