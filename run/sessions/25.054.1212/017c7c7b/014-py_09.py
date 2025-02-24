"""
Replace all blue pixels (value '1') with red pixels (value '2') and add three rows of the established pattern to the bottom. Preserve all white pixels (value '0').
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
        
    # fill using established rows
    extended_grid[6,:] = extended_grid[5,:]
    extended_grid[7,:] = extended_grid[4,:]
    extended_grid[8,:] = extended_grid[5,:]
    

    return extended_grid