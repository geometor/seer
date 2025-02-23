# 4-0d3d703e • 007 • example_4 - NLP

---
**Natural Language Program:**

The transformation rule is a color-to-color replacement applied to each cell in the input grid. Specifically, color 9 (maroon) is replaced with color 8 (azure), color 4 (yellow) is replaced with color 3 (green), and color 2 (red) is replaced with color 6 (magenta). Each instance of these input colors is substituted with their corresponding output colors to generate the output grid.

```python
"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.
Specifically, color 9 (maroon) is replaced with color 8 (azure), color 4 (yellow) is replaced with color 3 (green), and color 2 (red) is replaced with color 6 (magenta).
Each instance of these input colors is substituted with their corresponding output colors to generate the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    9 (maroon) -> 8 (azure)
    4 (yellow) -> 3 (green)
    2 (red) -> 6 (magenta)
    """
    output_grid = np.copy(input_grid)

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 9:
                output_grid[i, j] = 8
            elif output_grid[i, j] == 4:
                output_grid[i, j] = 3
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6

    return output_grid
```
