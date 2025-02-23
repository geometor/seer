# 3c9b0459 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation is a 90-degree clockwise rotation of the grid. Elements maintain their color, each moving to their corresponding new location as dictated by the rotation.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid 90 degrees clockwise.
    """
    # Convert the input list of lists to a NumPy array for easier manipulation.
    input_np = np.array(input_grid)

    # Rotate the array 90 degrees clockwise.  np.rot90 uses k=-1 for clockwise.
    output_np = np.rot90(input_np, k=-1)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid
```
