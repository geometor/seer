# 3c9b0459 • 014 • example_3 • investigate_coder

---
```python
"""
The input grid is rotated 90 degrees counter-clockwise to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)
    
    # Rotate the NumPy array 90 degrees counter-clockwise.
    output_np = np.rot90(input_np, k=1)  # k=1 signifies 90-degree rotation
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid
```
