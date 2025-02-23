# d631b094 • 004 • refine_coder

---
```python
"""
The program identifies the non-zero color in the input grid, counts its occurrences, and creates a 1-row output grid filled with that color, with the width equal to the count.
"""

import numpy as np

def _find_key_color(grid):
    # Find unique colors, excluding 0 (background).
    unique_colors = np.unique(grid)
    colors = unique_colors[unique_colors != 0]
    if len(colors) >= 1:
      return colors[0]
    else:
       return 0

def _count_key_color(grid, key_color):
    # Count occurrences of the key color.
    return np.sum(grid == key_color)

def transform(input_grid):
    # Find the key color (non-zero color).
    key_color = _find_key_color(input_grid)

    # Count occurrences of the key color.
    color_count = _count_key_color(input_grid, key_color)

    # Create the output grid (1 x color_count) filled with the key color.
    if color_count > 0:
        output_grid = np.full((1, color_count), key_color, dtype=int)
    else:
        output_grid = np.array([]) #return empty array when color_count is 0

    return output_grid
```
