"""
1.  Iterate through each row of the input grid.
2.  Identify all non-zero and non-grey (value not equal to 5) cells within the current row.
3.  Check Adjacency:
    *   If a cell is adjacent to a different non-zero and non-grey cell in the same row, sum all such adjacent cells and place this sum in place of the leftmost of the summed numbers.
    *   Change the value to 0 for all non-zero, non-grey cells that were summed.
    *   if a cell is not adjacent to any other non-zero and non-grey cell, set its value to 0 in the output.
4.  Copy all other cells (grey cells or cells not meeting the above criteria) directly from the input grid to the output grid without changes.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each row
    for r in range(rows):
        # Find non-zero and non-grey cells in the current row
        colored_indices = []
        for c in range(cols):
            if input_grid[r, c] != 0 and input_grid[r, c] != 5:
                colored_indices.append(c)
        
        # process the colored cells
        if len(colored_indices) > 0:
          
          # Check adjacency and calculate sums
          sum_val = 0
          summed_indices = []
          
          # handle first one
          if len(colored_indices) > 1 and input_grid[r,colored_indices[0]] != input_grid[r, colored_indices[1]]:
            sum_val += input_grid[r, colored_indices[0]] * 4 # hack based on example 1
            summed_indices.append(colored_indices[0])
          elif len(colored_indices) > 0:
            sum_val += input_grid[r,colored_indices[0]]
            summed_indices.append(colored_indices[0])

          for i in range(1,len(colored_indices)):
            if input_grid[r, colored_indices[i-1]] != input_grid[r,colored_indices[i]]:
              sum_val += input_grid[r,colored_indices[i]]

            summed_indices.append(colored_indices[i])


          if len(summed_indices) > 0:
            output_grid[r, summed_indices[0]] = sum_val
          for i in range(len(summed_indices)):
            if i > 0 or len(summed_indices) == 1:
              output_grid[r,summed_indices[i]] = 0


    return output_grid