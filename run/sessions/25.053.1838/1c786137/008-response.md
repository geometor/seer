# 1c786137 • 008 • example_2 - CODE

---
```python
"""
1. **Identify distinct objects:** In the input grid, locate contiguous blocks of pixels with the same color. Consider each of these blocks as a separate object.

2. **Object Representation**: Extract the object in the top, left-most, corner of the input grid.

3.  **Object Truncation and Sampling**: select the top-left 3x3 sub-grid of the input grid, and transform each of its 3 columns to 5 rows to create the output grid by the following sub-steps:
   * For column 1: Keep, the 3rd, 6th, 9th, 12th, and 13th element.
   * For column 2: Keep, the 3rd, 6th, 9th, 12th, and 13th element.
   * For column 3: Keep, the 1st, 3rd, 7th, 9th, and 10th element.

4. **Output Formation:** Arrange the truncated columns side-by-side to create output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 5x3 array filled with zeros.
    output_grid = np.zeros((5, 3), dtype=int)

    # Extract the top-left 3x3 sub-grid.
    sub_grid = input_grid[:13, :3]

    # Process each column of the sub-grid.
    # Column 1: Keep the 3rd, 6th, 9th, 12th, and 13th elements.
    output_grid[:, 0] = sub_grid[[2, 5, 8, 11, 12], 0]

    # Column 2: Keep the 3rd, 6th, 9th, 12th, and 13th elements.
    output_grid[:, 1] = sub_grid[[2, 5, 8, 11, 12], 1]

    # Column 3: Keep the 1st, 3rd, 7th, 9th, and 10th elements.
    output_grid[:, 2] = sub_grid[[0, 2, 6, 8, 9], 2]
    
    return output_grid
```
