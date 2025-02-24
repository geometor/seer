"""
1.  **Identify:** Locate all pixels with a value of '2' (red) in the input grid.
2.  **Extract and Replicate**: Create copies of red pixels.
3. **Resize:** create a new blank grid which is height of the bottom three rows of the input and the width that is sum of leftmost and rightmost non zero column indices.
4.  **Fill**: Fill the new grid: if the input pixel value is '2', place a '2' else place '0'
5. **Replicate row 1**: copy all values from the first row to complete the new row.
6.  **Fill Top Row**: Scan across the filled row. Whereever there is a 2, copy to top row.
"""

import numpy as np

def transform(input_grid):
    # Create a NumPy array from the input grid
    input_array = np.array(input_grid)

    # 3. Resize: create a new blank grid which is height of the bottom three rows of the input
    #    and the width that is sum of leftmost and rightmost non-zero column indices.
    
    rows, cols = input_array.shape
    non_zero_cols = np.where(np.any(input_array != 0, axis=0))[0]
    if non_zero_cols.size > 0:  # Check if there are any non-zero columns
        leftmost_col = non_zero_cols[0]
        rightmost_col = non_zero_cols[-1]
        new_width = rightmost_col - leftmost_col + 1
    else:
      return []
    
    output_grid = np.zeros((3, new_width*2), dtype=int) # doubled


    # 4. Fill: Fill the new grid: if the input pixel value is '2', place a '2' else place '0'
    # Copy bottom three rows using slice
    start_row = rows-3
    
    output_grid[0:3, 0:new_width] = input_array[start_row:rows,leftmost_col:rightmost_col+1]


    # 5. Replicate row 1: copy all values from the first row to complete the new row.
    output_grid[0:3,new_width:] = output_grid[0:3, 0:new_width]
    output_grid[0:3,:] = np.where(output_grid[0:3,:]==2,2,0) #clear zeros

    # 6. Fill Top Row: Scan across the filled row. Wherever there is a 2, copy to top row.
    # This is done as part of filling above

    return output_grid.tolist()