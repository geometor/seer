"""
The transformation rule is a color substitution based on a consistent mapping,
independent of the object's position or shape within the grid. The mapping is:

- 3 (Green) -> 4 (Yellow)
- 1 (Blue)  -> 5 (Gray)
- 2 (Red)   -> 6 (Magenta)
- 8 (Azure) -> 9 (Maroon)
- 5 (Gray)    -> 1 (Blue)
- 6 (Magenta) -> 2 (Red)
- 9 (Maroon)  -> 8 (Azure)
- 4 (Yellow)  -> 3 (Green)

The grid structure (dimensions and object shapes) is preserved. The
transformation acts uniformly on all cells of a given color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution based on the
    observed mappings across all provided examples.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Apply the color transformations using boolean indexing.
    output_grid[input_grid == 3] = 4  # Green to Yellow
    output_grid[input_grid == 1] = 5  # Blue to Gray
    output_grid[input_grid == 2] = 6  # Red to Magenta
    output_grid[input_grid == 8] = 9  # Azure to Maroon
    output_grid[input_grid == 5] = 1  # Gray to Blue
    output_grid[input_grid == 6] = 2  # Magenta to Red
    output_grid[input_grid == 9] = 8  # Maroon to Azure
    output_grid[input_grid == 4] = 3  # Yellow to Green

    return output_grid