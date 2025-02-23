"""
1.  **Identify Non-Zero Border Values:** Locate all non-zero values (colors other than white) on the top and right borders of the input grid.
2.  **Preserve and Translate:**
    *   All non-zero pixels on the left and bottom borders stay.
    *   All non-zero pixels that were originally on the top border are placed on the bottom border, maintaining their original column.
    *   All non-zero pixels that were originally on the right border are placed on the bottom border after the original bottom border elements and the moved top border elements. The relative order of the original right border elements is maintained.
3.   **Clear Interior:** All non-zero digits not on the left or bottom border of the original image, are changed to zero.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Keep left border
    for i in range(rows):
        if input_grid[i, 0] != 0:
            output_grid[i, 0] = input_grid[i, 0]
            
    # Keep existing bottom border and move other border elements.
    bottom_row_index = rows - 1
    bottom_row_elements = []

    # Gather elements from the bottom row
    for j in range(cols):
        if input_grid[bottom_row_index, j] != 0:
            bottom_row_elements.append(input_grid[bottom_row_index, j])

   # Gather elements from the top row
    for j in range(cols):
        if input_grid[0, j] != 0:
             bottom_row_elements.append(input_grid[0,j])
    
    # Gather elements from right border (excluding the very bottom-right, which we handled in the last loop)
    for i in range(rows):
         if input_grid[i, cols-1] != 0:
            bottom_row_elements.append(input_grid[i,cols-1])

    # Place elements on the bottom of output
    for k in range(len(bottom_row_elements)):
       if k < cols:
            output_grid[rows-1,k] = bottom_row_elements[k]

    # Keep elements from interior that match the preserved bottom row
    for i in range(rows):
        for j in range(cols):
            if input_grid[i,j] != 0 and output_grid[i,j] == 0: #Iterating over the original input grid, if original val !=0
               if (i,j) != (0,j) and (i,j) !=(i,cols-1):
                   output_grid[i,j] = input_grid[i,j] #Copy the value to the same place in output grid if it matches.
               if i == rows -1:
                   continue #Don't check bottom row here
               if  input_grid[i,j] in bottom_row_elements: #Check
                    output_grid[i,j] = input_grid[i,j]
               else:
                   output_grid[i,j] = 0
    return output_grid