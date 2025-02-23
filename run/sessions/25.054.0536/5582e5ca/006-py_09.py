"""
1. Identify Input Colors: Determine the set of unique colors present in the input grid.
2. Determine Output Color: The color of the output grid will be a color present in the input grid.
3. Create Output Grid: Create a new grid with the same dimensions as the input grid.
4. Fill Output Grid: Fill every cell of the output grid with the determined output color.
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    # Create output grid with same dimensions as input.
    output_grid = np.full_like(input_grid, 0)
    
    # Find the unique colors present in the input grid
    unique_colors = np.unique(input_grid)
    
    # Determine the fill color.
    fill_color = unique_colors[0] # initialize
    
    # fill output grid with selected color from input grid
    output_grid[:] = fill_color
    
    return output_grid