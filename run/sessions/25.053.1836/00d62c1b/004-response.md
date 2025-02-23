# 00d62c1b • 004 • refine_coder

---
```python
"""
A green (3) pixel changes to yellow (4) if and only if it is part of a connected component of green pixels that includes *more than two* pixels. If a green pixel is isolated (no adjacent green pixels) or is part of a connected component of *only* two pixels, it remains green. The connected component must be connected either horizontally or vertically.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid according to the specified rule.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0])

    def get_connected_component(r, c, visited):
        """
        Performs a Depth-First Search (DFS) to find all pixels in a connected component.
        """
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                input_grid[r][c] != 3 or (r, c) in visited):
            return []

        visited.add((r, c))
        component = [(r, c)]

        component.extend(get_connected_component(r + 1, c, visited))
        component.extend(get_connected_component(r - 1, c, visited))
        component.extend(get_connected_component(r, c + 1, visited))
        component.extend(get_connected_component(r, c - 1, visited))

        return component

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is green
            if input_grid[r][c] == 3:
                visited = set()
                connected_component = get_connected_component(r, c, visited)
                #change connected components greater than 2 to yellow
                if len(connected_component) > 2:
                    for row, col in connected_component:
                        output_grid[row][col] = 4
    return output_grid
```
