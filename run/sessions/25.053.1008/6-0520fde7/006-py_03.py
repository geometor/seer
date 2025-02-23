"""
1.  **Identify Center Column:** Locate the central vertical column (column index 3, since there are 7 total) in the input grid.
2.  **Remove Central column**: Vertical central column is completely removed from the grid.
3. **Locate blue pixels**: Check surrounding areas of central column to find blue(1) pixels.
4.  **Change color of blue pixels to red:** For surrounding blue(1) pixels, transform them to red(2)
5. **Final Output:** The final result of the transformation is produced.
"""

import numpy as np

def get_center_column_index(grid):
    """Helper function to find the index of the central column."""
    return grid.shape[1] // 2

def remove_center_column(grid):
    """
    Removes the central column from the input grid.
    """
    center_column_index = get_center_column_index(grid)
    return np.delete(grid, center_column_index, axis=1)
    
def transform(input_grid):
    # Remove the central column
    modified_grid = remove_center_column(input_grid)
    
    # Get dimensions of the modified grid for the new output
    rows = modified_grid.shape[0]
    cols = modified_grid.shape[1]
    output_grid = np.zeros((rows, cols -3 ), dtype=int)
    # print(modified_grid.shape) # (3, 6)
    
    # Populate the output grid and change blue(1) to red(2)
    for i in range(rows):
        k=0
        for j in range(cols):
            if j == 3:
                continue;
            
            if modified_grid[i,j] == 1:
                if (j==2 or j==4):   
                    output_grid[i,k] = 2
                else:
                    output_grid[i,k] = 0
            else:
                output_grid[i,k] = 0
            k=k+1

    return output_grid