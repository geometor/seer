# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The transformation rule is a color mapping where each color in the input grid is replaced by a new color in the output grid. The new color is determined by adding 4 to the original color value and taking the modulo 10 of the result. This ensures that the new color value remains within the range 0-9.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping based on adding 4 and taking modulo 10.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # Apply the transformation rule directly using NumPy's vectorized operations.
    output_grid = (input_grid + 4) % 10

    return output_grid
```

