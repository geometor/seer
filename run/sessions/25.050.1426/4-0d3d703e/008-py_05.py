"""
The transformation rule is a direct color substitution. Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically, based on the previous examples:

- Color 0 (black) likely remains unchanged or might follow a new pattern.
- Color 1 (blue) is transformed to color 5 (gray).
- Color 2 (red) is transformed to color 6 (magenta).
- Color 3 (green) is transformed to color 4 (yellow).
- Color 4 (yellow) is transformed to color 3 (green).
- Color 5 (gray) is transformed to color 1 (blue).
- Color 6 (magenta) is transformed to color 2 (red).
- Color 7 (orange) likely remains unchanged or might follow a new pattern.
- Color 8 (azure) is transformed to color 9 (maroon).
- Color 9 (maroon) is transformed to color 8 (azure).

This maintains the positions and arrangement of colors, only changing the color values, and preserves the grid dimensions.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): The input grid with integer color values.
    
    Returns:
        numpy.ndarray: The transformed grid with updated color values.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)
    
    # Define the color mapping based on observed transformations.
    color_map = {
        0: 0,  # Assuming black remains black, can be adjusted
        1: 5,  # Blue to Gray
        2: 6,  # Red to Magenta
        3: 4,  # Green to Yellow
        4: 3,  # Yellow to Green
        5: 1,  # Gray to Blue
        6: 2,  # Magenta to Red
        7: 7,  # Assuming orange remains orange, can be adjusted
        8: 9,  # Azure to Maroon
        9: 8   # Maroon to Azure
    }
    
    # Iterate through the color map and replace colors in the output grid.
    for old_color, new_color in color_map.items():
        output_grid[input_grid == old_color] = new_color
        
    return output_grid