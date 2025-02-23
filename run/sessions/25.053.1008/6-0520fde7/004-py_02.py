"""
The transformation rule is as follows:

1.  **Identify Trigger:** Locate all occurrences of gray (5) in the input grid.
2.  **Define Region:** Consider a vertical stripe defined by the column of each gray pixel.
3.  **Map to Output:** In the output grid, the corresponding column where the gray pixel was, set it to red (2).
4. **All Other Columns are White:** All other columns in output are set to White (0). In essence, the 3x7 input grid is reduced to a 3x3 output grid where each gray column in the input becomes a red column in the output, and all other colors columns are reduced to white.
"""

import numpy as np

def get_columns_with_color(grid, color):
    """
    Finds and returns a list of the indices of columns containing a specified color.
    """
    columns = []
    for x in range(grid.shape[1]):
        if color in grid[:, x]:
            columns.append(x)
    return columns

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    Identifies columns with gray (5) pixels, creates output grid,
    makes those columns Red(2), other columns White(0)
    """
    # initialize output_grid
    output_grid = np.zeros((input_grid.shape[0], 3), dtype=int)

    # Find columns in the input containing gray (5)
    gray_columns = get_columns_with_color(input_grid, 5)
    
    output_col_index = 0
    
    # Iterate a 'window' across the matrix from left to right one column at a time
    for x in range(0, input_grid.shape[1] - 2 ):
      window = input_grid[:, x:x+3]      
      window_gray_cols = get_columns_with_color(window, 5)
      
      #If gray is in the center of the window
      if len(window_gray_cols) > 0 and 5 in window[:,1]:          
          # Map corresponding columns to red (2) in output.
          output_grid[:, output_col_index] = 2
          
      output_col_index += 1       
      if output_col_index >= 3:
          break


    return output_grid