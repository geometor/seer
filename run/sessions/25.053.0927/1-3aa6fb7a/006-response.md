# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify** all *horizontal sequences* of one or more contiguous azure pixels (value `8`) in each row of the input grid.
2.  **Preserve** all azure pixels in these sequences in their original positions in the output grid.
3.  **For each row**, *if* there is a horizontal azure sequence:
    *   **Introduce** a *single* blue pixel (value `1`) immediately to the right of the *end* of the azure pixel sequence, if there is available space within the grid boundaries and in the current row.
    *   **Introduce** a *single* blue pixel (value `1`) immediately to the left of the *start* of the azure pixel sequence, if there is available space within the grid boundaries and in the current row.
4.  **Fill** all other positions in the output grid with `0` (white).
"""

import numpy as np

def get_horizontal_sequences_per_row(grid, value):
    sequences_per_row = []
    for row in range(grid.shape[0]):
        row_sequences = []
        in_sequence = False
        start = -1
        for col in range(grid.shape[1]):
            if grid[row, col] == value:
                if not in_sequence:
                    in_sequence = True
                    start = col
            elif in_sequence:
                in_sequence = False
                row_sequences.append(((row, start), (row, col - 1)))
                start = -1
        if in_sequence:
            row_sequences.append(((row, start), (row, grid.shape[1] - 1)))
        sequences_per_row.append(row_sequences)
    return sequences_per_row

def transform(input_grid):
    # Initialize output_grid with zeros (white)
    output_grid = np.zeros_like(input_grid)
    
    # Get horizontal sequences of azure pixels (value 8) for each row
    azure_sequences_per_row = get_horizontal_sequences_per_row(input_grid, 8)
    
    # Process each row separately
    for row_sequences in azure_sequences_per_row:
        # Preserve azure pixels in the output grid
        for start, end in row_sequences:
            for col in range(start[1], end[1] + 1):
                output_grid[start[0], col] = 8

        # Introduce blue pixels (value 1) at the boundaries of azure sequences in the same row
        for start, end in row_sequences:
            # To the left of the start
            if start[1] - 1 >= 0:
                output_grid[start[0], start[1] - 1] = 1
            # To the right of the end
            if end[1] + 1 < output_grid.shape[1]:
                output_grid[end[0], end[1] + 1] = 1
    
    return output_grid
```
