"""
The transformation rule is a color mapping where each color in the input grid is
incremented or decremented by a specific value based on consistent patterns observed
across multiple examples:

- Colors 2 (Red) and 6 (Magenta) are consistently transformed by adding 4.
- Colors 3 (Green) and 8 (Azure) are consistently transformed by adding 1.
- Color 5 (Gray) becomes 1 (Blue) by subtracting 4.
- Color 1 (Blue) becomes 5 (Gray) by adding 4.

The positions, sizes, and shapes of the colored regions remain the same.
Effectively there are two groups of transformations: +4,-4 and +1.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply color transformation based on the rules
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 2 or output_grid[i,j] == 1:  # Red and Blue
                output_grid[i, j] += 4  # increment by 4
            elif output_grid[i,j] == 6 or output_grid[i,j] == 5: # Magenta and Gray
                output_grid[i,j] = (output_grid[i,j] + 6) % 10 # decrement by 4 implemented by +6 mod 10
            elif output_grid[i, j] == 3 or output_grid[i,j] == 8:  # Green and Azure
                output_grid[i, j] += 1  # Yellow and Maroon
            

    return output_grid