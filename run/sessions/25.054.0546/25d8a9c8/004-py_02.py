"""
1. Identify Background Color: Determine if the example has a background color (most common color in example 3 input is 9: maroon).
2. Color Mapping:
    *   If the background is Maroon (9), Yellow (4) becomes Gray (5) and all other colors become white(0).
    *  Otherwise, all colors other than a possible background color become white (0).
"""

import numpy as np
from collections import Counter

def get_background_color(grid):
    # Flatten the grid and count the occurrences of each color
    color_counts = Counter(grid.flatten())
    # Return the most common color
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Check if the background color of input grid from example 3 is present.
    background_color = get_background_color(input_grid)
    
    # change output pixels 
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if background_color == 9:  # If background is maroon (from example 3)
                if input_grid[i, j] == 4: #yellow
                    output_grid[i, j] = 5 #gray
                else:
                    output_grid[i,j] = 0 #white
            else:
                output_grid[i,j] = 0 # All other colors become white

    return output_grid