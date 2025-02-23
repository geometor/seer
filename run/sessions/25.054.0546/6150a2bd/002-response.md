# 6150a2bd • 002 • example_1 • investigate_coder

---
```python
"""
The transformation is a 180-degree rotation of the input grid. Each element's position (row, col) in the input grid is mapped to (2-row, 2-col) in the output grid. Alternatively, swap the first and last rows and then reverse the middle row.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.
    """
    # Convert input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)
    
    # Get the dimensions of the input grid
    rows, cols = input_array.shape
    
    # Initialize the output grid with zeros
    output_array = np.zeros_like(input_array)
    
    # Rotate by swapping rows and reversing the middle row
    output_array[0, :] = input_array[rows-1, :]
    output_array[rows-1, :] = input_array[0, :]
    output_array[1, :] = input_array[1, ::-1]  # Reverse the middle row


    return output_array.tolist()
```

