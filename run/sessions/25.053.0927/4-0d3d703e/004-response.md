# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
The transformation is a simple color substitution. Each pixel in the input grid is replaced by a corresponding pixel in the output grid based on the following mapping:

*   Red (2) becomes Magenta (6)
*   Green (3) becomes Yellow (4)
*   Azure (8) becomes Maroon (9)

The spatial location of pixels is maintained; only the values change according to the substitution rule.
"""

def transform(input_grid):
    """
    Transforms an input grid by applying a color substitution cipher.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = []
    for i in range(len(input_grid)):
        output_grid.append([0] * len(input_grid[0]))

    # Create the mapping dictionary.
    mapping = {
        2: 6,  # red to magenta
        3: 4,  # green to yellow
        8: 9   # azure to maroon
    }

    # Iterate through each pixel of the input grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Apply the color substitution based on the mapping.
            output_grid[i][j] = mapping.get(input_grid[i][j], input_grid[i][j]) # Default to original if not found

    return output_grid
```

