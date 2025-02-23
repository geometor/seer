# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The transformation rule is a simple color substitution. Each color in the input grid is replaced by a specific different color in the output grid, according to this mapping:

1.  Maroon (9) is replaced by Azure (8).
2.  Yellow (4) is replaced by Green (3).
3.  Red (2) is replaced by Magenta (6).

The grid dimensions (3x3) and structure stay unchanged. Only the cell values, representing colors are altered following this rule.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by applying a direct color mapping.
    """
    # Create a copy of the input grid to serve as the output grid.  We modify the copy.
    output_grid = input_grid.copy()

    # Define the color mapping
    color_map = {
        9: 8,  # Maroon to Azure
        4: 3,  # Yellow to Green
        2: 6   # Red to Magenta
    }

    # Iterate through the color map and apply the substitution
    for input_color, output_color in color_map.items():
        output_grid[input_grid == input_color] = output_color

    return output_grid
```
