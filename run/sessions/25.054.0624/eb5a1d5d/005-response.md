# eb5a1d5d • 005 • refine_coder

---
```python
"""
Transforms an input grid representing nested rectangles into a smaller, concentric representation of those rectangles.
The transformation identifies the sequence of colors in the nested rectangles, from outermost to innermost, and then
recreates these rectangles concentrically in a new, square grid. The side length of the output grid is (number of colors * 2) - 1.
"""

import numpy as np

def analyze_nested_rectangles(input_grid):
    """
    Analyzes the input grid to identify nested colored rectangles.

    Returns:
        - A list of colors, from outermost to innermost.
        - The dimensions (height, width) of the expected output grid.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape
    colors = []
    current_color = grid[0, 0]
    colors.append(current_color)

    while True:
        found_new_color = False
        for r in range(rows):
            for c in range(cols):
                if grid[r, c] != current_color:
                    if grid[r,c] not in colors:
                      current_color = grid[r, c]
                      colors.append(current_color)
                      found_new_color = True
        if not found_new_color:
            break

    output_height = len(colors) * 2 -1
    output_width = output_height

    return colors, (output_height, output_width)

def transform(input_grid):
    """
    Transforms the input grid into a concentric representation of nested rectangles.
    """
    # Analyze the input grid to get the color sequence and output dimensions
    colors, (output_height, output_width) = analyze_nested_rectangles(input_grid)

    # Create an empty output grid filled with the outermost color
    output_grid = np.full((output_height, output_width), colors[0], dtype=int)

    # Draw concentric rectangles
    for i in range(len(colors)):
        color = colors[i]
        # Calculate the boundaries for the current rectangle
        top = i
        left = i
        bottom = output_height - 1 - i
        right = output_width - 1 - i

        # Fill the rectangle with the current color
        output_grid[top:bottom + 1, left:right + 1] = color

    return output_grid
```
