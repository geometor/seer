# ed36ccf7 • 014 • example_3 • investigate_coder

---
```python
"""
Rotate the input grid 90 degrees clockwise to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)
    
    # Rotate the grid 90 degrees clockwise.
    output_np = np.rot90(input_np, k=-1) # k=-1 for 90-degree clockwise rotation
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()
    
    return output_grid
```
