# 9565186b • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule is: Replace all azure (8) pixels in the input grid with gray (5) pixels. Keep all red (2) pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Replace azure (8) with gray (5), keep red (2) unchanged.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Replace all instances of 8 (azure) with 5 (gray).
    output_grid[output_grid == 8] = 5

    return output_grid
```
