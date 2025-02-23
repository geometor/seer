# 0d3d703e • 011 • refine_coder

---
```python
"""
Applies a color substitution cipher to an input grid. The cipher is determined
uniquely for each input/output pair by creating a one-to-one mapping between
the sorted unique colors present in the input and output grids.
"""

import numpy as np

def get_unique_colors(grid):
    """Returns a sorted list of unique colors in a grid."""
    return sorted(list(np.unique(grid)))

def create_color_mapping(input_colors, output_colors):
    """
    Creates a dictionary mapping input colors to output colors.
    Assumes the two lists are of the same length.
    """
    color_map = {}
    for i in range(len(input_colors)):
        color_map[input_colors[i]] = output_colors[i]
    return color_map

def transform(input_grid):
    """
    Transforms an input grid by applying a color substitution cipher,
    determined uniquely for each input/output pair.
    """
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # get unique colors from input and expected output
    input_colors = get_unique_colors(input_grid)
    # NOTE:  we don't have the output grid at runtime
    # the following line would be invalid in final solution,
    # but it will help us generate correct intermediate code:
    output_colors = get_unique_colors(output_grid) # placeholder, will remove.


    # establish color mapping
    color_map = create_color_mapping(input_colors, output_colors)

    # apply color substitution
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid
```
