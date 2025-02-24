# bbc9ae5d • 022 • refine_coder

---
```python
"""
Identify the sequence of non-zero color pixels in the input row and the sequence of trailing zero pixels.
Determine the length of the non-zero sequence and the index of the first zero in this sequence.
Create output rows. The number of output rows is equal to the count of non-zero colors in the input.
Extend For each output row:
    Copy the initial non-zero color sequence from the input.
    Extend the sequence by one pixel for each subsequent row, repeating the last color of the sequence.
    Append the original trailing zeros from the input to maintain their original length.
"""

import numpy as np

def transform(input_grid):
    # Identify the sequence of non-zero colors and trailing zeros.
    input_row = input_grid[0]
    first_zero_index = -1
    for i, pixel in enumerate(input_row):
        if pixel == 0:
            first_zero_index = i
            break
    if first_zero_index == -1:
        first_zero_index = len(input_row)

    non_zero_length = first_zero_index
    num_output_rows = non_zero_length

    # Create output rows.
    output_grid = np.zeros((num_output_rows, len(input_row)), dtype=int)

    # Extend non-zero sequence and append trailing zeros.
    for i in range(num_output_rows):
        # Copy and extend non-zero sequence.
        output_grid[i, :i+1] = input_row[:i+1]
        if i+1<first_zero_index:
            output_grid[i,i] = input_row[i]
        if i+1>0 and i+1 <= first_zero_index:
            output_grid[i,i] = input_row[i]

        # Append trailing zeros.
        output_grid[i, first_zero_index:] = input_row[first_zero_index:]

    return output_grid
```
