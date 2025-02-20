# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The input grid contains two L-shaped objects of color 8 (azure). The output grid preserves these L-shaped objects. 
Additionally, a single blue (color 1) cell is added at the vertex of each L-shape.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds the vertices of L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the vertex coordinates.
    """
    vertices = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for 2x2 blocks and identify L-shapes
            block = grid[r:r+2, c:c+2]
            if np.sum(block == color) == 3:
                # Find the vertex of the L-shape within the 2x2 block
                if block[0, 0] == color and block[0, 1] == color and block[1, 0] == color:
                  if r > 0 and grid[r-1,c] == color:
                    continue
                  vertices.append((r + 1, c + 1))
                elif block[0, 0] == color and block[0, 1] == color and block[1, 1] == color:
                  if r > 0 and grid[r-1,c+1] == color:
                    continue
                  vertices.append((r + 1, c))
                elif block[0, 0] == color and block[1, 0] == color and block[1, 1] == color:
                  if c+2 < cols and grid[r+1,c+2] == color:
                      continue;
                  vertices.append((r, c + 1))

                elif block[0, 1] == color and block[1, 0] == color and block[1, 1] == color:
                  if c > 0 and grid[r+1,c-1] == color:
                    continue;
                  vertices.append((r, c))
    return vertices

def transform(input_grid):
    """
    Transforms the input grid according to the L-shape vertex rule.
    """
    output_grid = np.copy(input_grid)
    l_shape_vertices = find_l_shapes(input_grid, 8)

    # Add blue cells at the vertices
    for r, c in l_shape_vertices:
        output_grid[r, c] = 1

    return output_grid
```

