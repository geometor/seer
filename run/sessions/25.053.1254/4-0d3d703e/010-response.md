# 4-0d3d703e • 010 • example_2 - CODE

---
```python
"""
Transforms a 3x3 grid of integers based on a specific mapping: 2->6, 3->4, and 8->9.
"""

def transform(input_grid):
    """
    Transforms the input grid according to the specified mapping.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = [row[:] for row in input_grid]

    # Define the mapping
    mapping = {
        2: 6,
        3: 4,
        8: 9
    }

    # Iterate through the grid and apply the transformation
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Change output pixels based on mapping
            if input_grid[i][j] in mapping:
                output_grid[i][j] = mapping[input_grid[i][j]]

    return output_grid
```
