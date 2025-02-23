# 0a938d79 • 032 • refine_coder

---
```python
"""
1.  **Examine Each Row:** Iterate through each row of the input grid.
2.  **Identify Background Rows:** If a row contains *only* black (0), it remains unchanged in the output.
3.  **Identify and Process Non-Background Rows:**
    *   If a row contains black (0) and one or more other colors, extend the row by repeating the sequence of non-zero colors horizontally across the whole row.
4.  **Vertical Pattern Application:** The first processed row is copied to the output. Subsequent processed rows alternate with any previously identified processed rows, cycling through the available fill colors for the entire height of the output grid.
"""

import numpy as np

def extend_row(row):
    """Extends a row by repeating its non-zero color sequence."""
    non_zero_colors = row[row != 0]
    if len(non_zero_colors) == 0:
        return row  # Return original row if all zeros

    extended_row = np.zeros_like(row)
    for i in range(len(row)):
        extended_row[i] = non_zero_colors[i % len(non_zero_colors)]
    return extended_row

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    
    processed_rows = []

    # Identify and process non-background rows
    for i in range(rows):
        row = input_grid[i]
        if np.all(row == 0):  # Background row
            continue
        else:
            processed_rows.append(extend_row(row))

    # Apply vertical pattern
    if not processed_rows:  # If no non-background rows, return original
        return output_grid

    processed_row_index = 0
    for i in range(rows):
        if np.all(input_grid[i] == 0):
            continue #skip background
        else:
            output_grid[i] = processed_rows[processed_row_index % len(processed_rows)]
            processed_row_index += 1
            
    return output_grid
```
