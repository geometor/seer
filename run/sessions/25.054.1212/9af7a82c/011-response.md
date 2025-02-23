# 9af7a82c • 011 • refine_coder

---
```python
"""
1.  **Analyze Input:** Examine the input grid and determine the unique colors present.
2.  **Sort Colors:** Sort the unique colors from the input grid in descending order.
3.  **Construct Output Grid - initial rows:** Create the output grid. The number of columns in the output equals the number of unique colors in the input. The sorted colors form the initial rows of the output. Iterate through the sorted colors in descending order. For each color, find the number of times that color occurs in the input. Create a row in the output grid, starting with a number of the sorted color equal to the number of columns remaining in the output, and fill the rest of the cells with 0.
4.  **Construct Output Grid - padding:** Determine the number of rows for the output. The number of rows is the number of input unique colors + a padding number (which appears to be consistently either +2 or +3 -- requires more examples to verify if always the case, or if there are other rules governing this).
5.  **Fill Padding:** Add rows of color 0 (white) to the bottom of the output grid until the determined number of rows is reached.
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    # Analyze Input: Determine unique colors and their counts.
    unique_colors = np.unique(input_grid)
    color_counts = Counter(input_grid.flatten())

    # Sort Colors: Sort unique colors in descending order.
    sorted_colors = sorted(unique_colors, reverse=True)

    # Construct Output Grid - initial rows:
    output_width = len(unique_colors)
    output_rows = []
    
    
    remaining_cols = output_width
    for color in sorted_colors:
      row = [color] * (remaining_cols) + [0] * (output_width - remaining_cols)
      output_rows.append(row)
      remaining_cols -= 1
      

    # Construct Output Grid - padding: Determine output height (padding).
    #  Here I am making an assumption about pad_rows of +2, which may not be always true.  Needs refinement
    pad_rows = 2
    output_height = len(unique_colors) + pad_rows
    
    # Fill Padding: Add rows of 0s.
    while len(output_rows) < output_height:
        output_rows.append([0] * output_width)

    output_grid = np.array(output_rows)
    return output_grid
```
