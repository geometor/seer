"""
1.  **Identify the Cluster:** Find the smallest contiguous block (cluster) of non-black (non-zero) pixels in the input grid.
2.  **Determine Bounding Box:** Calculate the bounding box (min/max rows and columns) of this cluster.
3.  **Calculate Output Dimensions:**
    *   The output grid always has 3 rows.
    *   The output grid's width is twice the width of the cluster's bounding box.
4.  **Create Output Grid:** Initialize an output grid filled with black (0) pixels, with the calculated dimensions.
5.  **Populate Output Grid with Alternating Pattern:**
      Iterate through each *row* of the **cluster within the input grid**.
      *   For each row in the cluster:
          *    Copy that row from the input grid into the output grid.
          * Insert one black column after each original column of the cluster

6.  **Return:** the output grid.
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

    # construct output - iterate through cluster rows, not input grid
    for i in range(min_row, min_row + output_rows):
        output_col_index = 0

        # check for the valid range
        if i <= max_row:
            for j in range(min_col, max_col + 1):
                output_grid[i-min_row, output_col_index] = input_grid[i, j]
                output_col_index += 1
                output_grid[i-min_row, output_col_index] = 0  # black pixel
                output_col_index += 1
        else:
            # if out of the range of the input, fill with background
             for j in range(output_cols):
                output_grid[i-min_row, j]=0

    
    return output_grid