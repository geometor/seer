# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The transformation rule is a consistent color mapping across all examples:
- 1 -> 5
- 2 -> 6
- 3 -> 4
- 4 -> 3
- 5 -> 1
- 6 -> 2
- 8 -> 9
- 9 -> 8
The structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a comprehensive color mapping derived from all examples:
        - 1 -> 5
        - 2 -> 6
        - 3 -> 4
        - 4 -> 3
        - 5 -> 1
        - 6 -> 2
        - 8 -> 9
        - 9 -> 8
    Maintains the original grid structure.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply the color mapping
    output_grid[input_grid == 1] = 5  # Replace all occurrences of 1 with 5
    output_grid[input_grid == 2] = 6  # Replace all occurrences of 2 with 6
    output_grid[input_grid == 3] = 4  # Replace all occurrences of 3 with 4
    output_grid[input_grid == 4] = 3  # Replace all occurrences of 4 with 3
    output_grid[input_grid == 5] = 1  # Replace all occurrences of 5 with 1
    output_grid[input_grid == 6] = 2  # Replace all occurrences of 6 with 2
    output_grid[input_grid == 8] = 9  # Replace all occurrences of 8 with 9
    output_grid[input_grid == 9] = 8  # Replace all occurrences of 9 with 8

    return output_grid
```



Test Input Transformed Output:
![Image](008-py_06-test_output.png)
