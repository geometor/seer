"""
Replace all blue pixels (value '1') with red pixels (value '2') and add three rows to the bottom, repeating the last three rows of the input grid. Preserve all white pixels (value '0').
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy to work on
    output_grid = np.copy(input_grid)

    # Replace all '1' (blue) pixels with '2' (red)
    output_grid[output_grid == 1] = 2
    
    # get shape
    rows, cols = output_grid.shape

    # Extend by adding rows of the established pattern
    # Create a new empty array with space for the extended output
    extended_grid = np.zeros((rows + 3, cols), dtype=int)
    
    # copy original over
    extended_grid[:rows, :] = output_grid
        
    # fill using established rows, repeating the last three rows
    extended_grid[rows,:] = output_grid[rows-3,:]
    extended_grid[rows+1,:] = output_grid[rows-2,:]
    extended_grid[rows+2,:] = output_grid[rows-1,:]
    

    return extended_grid