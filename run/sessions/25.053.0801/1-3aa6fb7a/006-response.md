# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Sequences:** Find all contiguous horizontal sequences of azure (8) pixels.
2.  **Check Left Neighbor:** For each azure sequence, examine the pixel immediately to its left.
3.  **Conditional Insertion:** If the left neighbor is a 0, replace that 0 with a blue (1) pixel. If at the left edge, do not insert anything.
4. **All Other Pixels:** All pixels that are not azure, or a zero to the left of an azure sequence, remain unchanged.
"""

import numpy as np

def find_azure_sequences(grid):
    """Finds contiguous horizontal sequences of azure (8) pixels."""
    sequences = []
    rows, cols = grid.shape
    for r in range(rows):
        in_sequence = False
        start_col = -1
        for c in range(cols):
            if grid[r, c] == 8:
                if not in_sequence:
                    in_sequence = True
                    start_col = c
            elif in_sequence:
                sequences.append((r, start_col, c - 1))  # (row, start_col, end_col)
                in_sequence = False
        if in_sequence:
            sequences.append((r, start_col, cols - 1))
    return sequences

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all azure sequences
    azure_sequences = find_azure_sequences(input_grid)

    # Iterate through each azure sequence
    for row, start_col, end_col in azure_sequences:
        # Check left neighbor
        if start_col > 0:  # Not at the left edge
            if input_grid[row, start_col - 1] == 0:
                # Conditional Insertion: Replace 0 with blue (1)
                output_grid[row, start_col - 1] = 1

    return output_grid
```
