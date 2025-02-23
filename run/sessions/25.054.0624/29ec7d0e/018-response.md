# 29ec7d0e • 018 • refine_coder

---
```python
"""
1.  **Identify all connected components** of white (0) pixels in the input grid.
2.  **Count** the sizes of the components.
3.  **Determine Removal:** If there exists one or more connected component of color white, remove only the *largest* connected component of white pixels, if there are more than one. If there is only a single connected component, then remove it. If there are multiple components of the largest size, do not remove any.
4.  **Construct Output:** Copy all pixels from the input grid to the output grid *except* those belonging to the identified largest white connected component, as per the determination above.
"""

import numpy as np
from typing import List, Tuple

def find_connected_component(grid, start_row, start_col, visited):
    """
    Finds the connected component starting from a given seed pixel using Depth-First Search (DFS).
    """
    rows, cols = grid.shape
    component = []
    color = grid[start_row,start_col]

    def dfs(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row, col]
            or grid[row,col] != color
        ):
            return

        visited[row, col] = True
        component.append((row, col))

        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc)

    dfs(start_row, start_col)
    return component

def get_white_components(input_grid):
    """Finds all connected components of white pixels."""
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    components = []

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0 and not visited[r,c]:
                component = find_connected_component(input_grid, r, c, visited)
                components.append(component)
    return components

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find all connected components of white pixels
    white_components = get_white_components(input_grid)

    # 2. Count the sizes of the components
    component_sizes = [len(comp) for comp in white_components]

    # 3. Determine Removal
    if component_sizes:  # Check if there are any white components
        max_size = max(component_sizes)
        count_of_max_size = component_sizes.count(max_size)

        if count_of_max_size == 1:
            # Find the index of the largest component
            largest_component_index = component_sizes.index(max_size)
            largest_component = white_components[largest_component_index]

            # 4. Construct Output (remove largest component)
            for row, col in largest_component:
                # we are removing by not copying
                pass # removal is implicit
        # else: do not remove anything, so don't do anyting with the output
        # grid, it is already initialized with the correct value
    
    return output_grid
```

