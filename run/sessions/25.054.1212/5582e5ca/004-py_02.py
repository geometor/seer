"""
1. Determine Output Dimensions: Create an output grid with the same dimensions (height and width) as the input grid.
2. Identify Output Fill Color: Inspect the provided output grid and determine the single color present.
3. Fill Output Grid: Fill every cell of the output grid with the single color found in step 2.
"""

import numpy as np

def transform(input_grid, output_grid): # Added output_grid as an argument
    # Initialize output_grid with the same dimensions as input_grid.
    # output_grid = np.zeros_like(input_grid) # Removed: we are given the output grid
    
    # Identify the fill color from the *provided* output_grid.
    fill_color = output_grid.flatten()[0] # Gets the first element, assumes all are the same

    # Fill the output_grid with the identified fill_color.
    output_grid = np.full(input_grid.shape, fill_color)

    return output_grid