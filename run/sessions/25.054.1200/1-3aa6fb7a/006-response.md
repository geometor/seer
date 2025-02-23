# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Groups:** In the input grid, locate all azure pixels (value 8). Group them into contiguous horizontal sequences. An isolated azure pixel is its own group.
2.  **Find Leftmost Azure:** Within each contiguous group of azure pixels, identify the leftmost azure pixel. If a row contains multiple such groups, treat each group separately.
3. **Change to blue:** The *leftmost* azure of each group in each row is changed to blue.
"""

import numpy as np

def find_contiguous_groups(grid, color):
    """Finds contiguous horizontal groups of a specified color."""
    groups = []
    rows, cols = grid.shape
    for r in range(rows):
        current_group = []
        for c in range(cols):
            if grid[r, c] == color:
                current_group.append((r, c))
            else:
                if current_group:
                    groups.append(current_group)
                    current_group = []
        if current_group:  # Handle groups at the end of a row
            groups.append(current_group)
    return groups

def find_leftmost_in_groups(groups):
    """Identifies the leftmost pixel in each group."""
    leftmost_pixels = []
    for group in groups:
        leftmost_pixel = min(group, key=lambda x: x[1])  # min by column index
        leftmost_pixels.append(leftmost_pixel)
    return leftmost_pixels

def transform(input_grid):
    # Initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)

    # Find all contiguous groups of azure pixels
    azure_groups = find_contiguous_groups(input_grid, 8)

    # Find the leftmost azure pixel in each group
    leftmost_azures = find_leftmost_in_groups(azure_groups)

    # Change the leftmost azure pixels to blue
    for r, c in leftmost_azures:
        output_grid[r, c] = 1

    return output_grid
```

