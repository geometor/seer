# 2dee498d • 012 • refine_coder

---
```python
"""
The transformation identifies the shortest repeating horizontal pattern within each input grid. This pattern is determined by finding the smallest width such that the input grid's rows can be constructed by repeating a sub-grid of that width. The output grid is then formed by extracting this shortest repeating pattern from the left side of the input grid. The height of the output is the same as the input.
"""

import numpy as np

def get_shortest_pattern_width(row):
    """
    Finds the width of the shortest repeating pattern in a single row.
    """
    cols = len(row)
    for width in range(1, cols + 1):
        if cols % width == 0:  # Check if width is a divisor
            is_repeating = True
            for i in range(width, cols):
                if row[i] != row[i % width]:
                    is_repeating = False
                    break
            if is_repeating:
                return width
    return cols  # If no repetition is found, return full width

def transform(input_grid):
    """
    Extracts the shortest repeating horizontal pattern from the input grid.
    """
    # Get the dimensions of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Determine the width of the repeating unit (output grid width)
    # by checking the shortest repeating width across all rows.
    pattern_widths = [get_shortest_pattern_width(row) for row in input_grid]
    
    # Find the most common (mode) pattern width. This handles cases where
    # different rows suggest slightly different pattern lengths, prioritizing the most frequent.
    output_cols = max(set(pattern_widths), key=pattern_widths.count)


    # Initialize the output grid.
    output_grid = []

    # Extract the leftmost sub-grid of the determined width.
    for i in range(rows):
        output_grid.append(input_grid[i][:output_cols])

    return output_grid
```
