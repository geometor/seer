# 0a938d79 • 008 • refine_coder

---
```python
"""
1.  **Identify Colored Rows:** Find rows that contain non-zero (colored) pixels.
2.  **Horizontal Pattern Detection:** For each colored row:
    *   Find the shortest repeating horizontal pattern of colors, including intervening zeros. Consider the entire row when looking for the pattern - if the pattern repeats, it must fill the entire row.
3.  **Vertical Pattern Detection:** If there are multiple colored rows, OR colored rows mixed with all-zero rows:
    * Find the shortest sequence of entire rows that repeat. This sequence becomes the vertical stacking pattern.
4. **Build Output:**
    * Create an output grid of the same dimensions as the input.
    *   If a vertical stacking pattern is found, repeat this sequence of rows to fill the output grid, starting with the top row.
    * If no colored row is found, return the empty grid.
"""

import numpy as np

def find_colored_rows(grid):
    """Finds indices of rows with at least one non-zero element."""
    colored_rows = []
    for i, row in enumerate(grid):
        if np.any(row != 0):
            colored_rows.append(i)
    return colored_rows

def detect_horizontal_pattern(row):
    """Detects the shortest repeating horizontal pattern in a row."""
    row = np.array(row)  # Ensure it's a NumPy array
    non_zero_row = row[row != 0]
    if len(non_zero_row) == 0:
        return row #return the all zero row

    for length in range(1, len(row) + 1):
        if len(row) % length == 0:
            pattern = row[:length]
            if np.array_equal(row, np.tile(pattern, len(row) // length)):
                return pattern
    return row  # No repeating pattern found


def detect_vertical_pattern(grid):
    """Detects the shortest repeating vertical pattern of rows."""
    rows, _ = grid.shape
    for length in range(1, rows + 1):
        if rows % length == 0:
            pattern = [detect_horizontal_pattern(grid[i]) for i in range(length)]
            
            valid_pattern = True
            for i in range(rows):
                if not np.array_equal(detect_horizontal_pattern(grid[i]), pattern[i % length]):
                    valid_pattern = False
                    break

            if valid_pattern:
                return pattern
    return None  # No repeating pattern found


def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Identify colored rows
    colored_rows_indices = find_colored_rows(input_grid)

    if not colored_rows_indices:
        return output_grid

    # Detect vertical pattern
    vertical_pattern = detect_vertical_pattern(input_grid)

    # Build output
    if vertical_pattern:
        pattern_length = len(vertical_pattern)
        for row_index in range(rows):
            pattern_row = vertical_pattern[row_index % pattern_length]
            output_grid[row_index, :len(pattern_row)] = pattern_row
            # handle cases where the detected pattern is shorter than row length
            if len(pattern_row) < cols:
              output_grid[row_index, len(pattern_row):] = np.tile(pattern_row, (cols // len(pattern_row)) + 1)[:cols-len(pattern_row)]

    return output_grid
```
