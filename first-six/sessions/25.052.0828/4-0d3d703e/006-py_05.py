"""
Transformation Rule:

1. **Identify Objects:** The input grid consists of colored vertical lines (columns).  Each column has a single color.
2. **Color Substitution:**  Each color in the input grid is mapped to a different color in the output grid.  The mapping is consistent across examples.
3. **Preserve Structure:** The shape and position of the columns are maintained. The transformation only changes the colors.
    - Example 1: 3 (Green) -> 4 (Yellow), 1 (Blue) -> 5 (Gray), 2 (Red) -> 6 (Magenta)
    - Example 2: 2 (Red) -> 6 (Magenta), 3 (Green) -> 4 (Yellow), 8 (Azure) -> 9 (Maroon)
4. **Combined Mapping:** Combining both examples gives the complete color transformation rule:
    - 1 (Blue) -> 5 (Gray)
    - 2 (Red) -> 6 (Magenta)
    - 3 (Green) -> 4 (Yellow)
    - 8 (Azure) -> 9 (Maroon)
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on a color substitution rule, preserving the structure.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping based on the observed transformations.
    color_map = {
        1: 5,  # Blue -> Gray
        2: 6,  # Red -> Magenta
        3: 4,  # Green -> Yellow
        8: 9,  # Azure -> Maroon
    }

    # Iterate through each cell in the grid and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            original_color = output_grid[i, j]
            # Check if the original color is in the color map.
            if original_color in color_map:
                output_grid[i, j] = color_map[original_color]

    return output_grid