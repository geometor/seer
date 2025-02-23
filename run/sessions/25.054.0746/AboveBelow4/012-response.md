# AboveBelow4 • 012 • refine_coder

---
```python
"""
1.  **Identify Objects:** Divide the input grid into distinct objects, where each object is a contiguous region of pixels of the same color.

2.  **Identify Stable and Changing Colors:** Compare each input/output pair. Determine which color expands into the other color. The expanding color is *stable*, the other color is *changing*.

3. **Find Horizontal Neighbors:** For each pixel in the input grid check its left and right neighbors.

4.  **Apply Rule:**
    *   If a pixel is the *changing* color, and is horizontally adjacent (left or right) to a pixel of *stable* color, the *changing* pixel becomes the *stable* color in the output grid.
"""

import numpy as np
from collections import deque

def find_objects(grid):
    """Finds all contiguous objects in a grid."""
    rows, cols = grid.shape
    visited = set()
    objects = []

    def bfs(r, c, color):
        """Performs breadth-first search to find contiguous pixels of the same color."""
        obj = []
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()
            obj.append((row, col))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr, nc] == color:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return obj

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                obj = bfs(r, c, grid[r, c])
                objects.append(obj)
    return objects


def find_stable_and_changing_colors(input_grid, output_grid):
    """Identifies the stable and changing colors based on input/output comparison."""
    rows, cols = input_grid.shape
    stable_color = None
    changing_color = None

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != output_grid[r, c]:
                changing_color = input_grid[r, c]
                stable_color = output_grid[r,c]
                return stable_color, changing_color  # Return as soon as a difference is found

    return stable_color, changing_color


def transform(input_grid, input_grid_2=None, output_grid_2=None):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find Objects (not strictly needed for this rule, but good practice)
    # objects = find_objects(input_grid)

    # 2. Determine Stable and Changing Colors (using both examples)
    stable_color, changing_color = find_stable_and_changing_colors(input_grid, output_grid)
    if input_grid_2 is not None and output_grid_2 is not None:
      stable_color_2, changing_color_2 = find_stable_and_changing_colors(input_grid_2, output_grid_2)
      if stable_color_2 is not None:  # possible no change in the 2nd example
        stable_color = stable_color_2
        changing_color = changing_color_2


    if stable_color is None: # all input pixels match output - return
        return output_grid

    # 3. Iterate and apply transformations
    for r in range(rows):
        for c in range(cols):
            # 4. Apply Rule
            if input_grid[r, c] == changing_color:
                # Check left neighbor
                if c > 0 and input_grid[r, c - 1] == stable_color:
                    output_grid[r, c] = stable_color
                # Check right neighbor
                if c < cols - 1 and input_grid[r, c + 1] == stable_color:
                    output_grid[r, c] = stable_color

    return output_grid
```
