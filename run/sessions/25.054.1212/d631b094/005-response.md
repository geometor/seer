# d631b094 • 005 • refine_coder

---
```python
"""
1.  **Identify the Non-Black Color:** Scan the input grid to determine the single color present, besides black (0).
2.  **Count Occurrences:** Count the number of cells containing the identified non-black color.
3.  **Construct Output Grid:** Create a new output grid. The output grid will be a single row (1 pixel high). The width of the output grid will be equal to the number of times the identified color appeared in the input grid. Fill this output grid entirely with the identified non-black color.
"""

import numpy as np

def get_non_black_color(grid):
    # Find unique colors in the grid
    unique_colors = np.unique(grid)
    # Filter out black (0) and return the first remaining color, if any
    non_black_colors = unique_colors[unique_colors != 0]
    return non_black_colors[0] if non_black_colors.size > 0 else None

def count_color_occurrences(grid, color):
    # Count the number of times a specific color appears in the grid
    return np.sum(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the rules."""

    input_grid = np.array(input_grid)

    # Identify the non-black color
    non_black_color = get_non_black_color(input_grid)

    # Count the occurrences of the non-black color
    color_count = count_color_occurrences(input_grid, non_black_color)

    # Construct the output grid
    output_grid = np.full((1, color_count), non_black_color)

    return output_grid
```
