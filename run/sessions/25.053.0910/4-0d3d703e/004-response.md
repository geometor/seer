# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
The transformation rule is a direct color substitution. Replace every instance of red (2) with magenta (6), green (3) with yellow (4), and azure (8) with maroon (9). The spatial arrangement of the pixels does not change, only their colors.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        2: 6,  # Red to Magenta
        3: 4,  # Green to Yellow
        8: 9   # Azure to Maroon
    }

    # Iterate through the color map and perform the substitution.
    for input_color, output_color in color_map.items():
        output_grid[output_grid == input_color] = output_color

    return output_grid
```
