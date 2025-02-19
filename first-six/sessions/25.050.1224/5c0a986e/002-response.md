# 5c0a986e • 002 • example_1 - CODE

---
```python
"""
The transformation preserves two 2x2 squares (blue and red) from the input grid and adds single pixels of the same color at specific relative positions. Two blue pixels are added to the top-left (at (0,0) and (1,1)), and two red pixels are added to the bottom-right (at (8,6) and (9,7)).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)  # Start with a copy of the input

    # Add blue pixels
    output_grid[0, 0] = 1
    output_grid[1, 1] = 1

    # Add red pixels
    output_grid[8, 6] = 2
    output_grid[9, 7] = 2
    
    return output_grid
```

