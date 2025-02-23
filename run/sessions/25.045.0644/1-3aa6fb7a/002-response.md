# 25.045.0644 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
Identifies connected regions of color '8' and modifies cells adjacent to their top-left cells.
For the first '8'-object, changes the cell to its right to '1'.
For the second '8'-object, changes the cell below it to '1'.
Modifications are only applied if the target cell is within grid boundaries and is '0'.
"""

import numpy as np

def transform(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid = np.copy(input_grid_np)
    rows, cols = input_grid_np.shape
    visited = np.zeros_like(input_grid_np, dtype=bool)
    components = []

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
        return neighbors

    def find_connected_component(r, c):
        component = []
        q = [(r, c)]
        visited[r, c] = True
        while q:
            row, col = q.pop(0)
            component.append((row, col))
            for nr, nc in get_neighbors(row, col):
                if input_grid_np[nr, nc] == 8 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    q.append((nr, nc))
        return component

    for r in range(rows):
        for c in range(cols):
            if input_grid_np[r, c] == 8 and not visited[r, c]:
                components.append(find_connected_component(r, c))

    for i, component in enumerate(components[:2]): # Process only the first two components
        top_left_cell = None
        min_row = float('inf')
        min_col = float('inf')
        for r, c in component:
            if r < min_row:
                min_row = r
                min_col = c
                top_left_cell = (r, c)
            elif r == min_row and c < min_col:
                min_col = c
                top_left_cell = (r, c)

        if top_left_cell:
            tl_r, tl_c = top_left_cell
            if i == 0: # First component: modify cell to the right
                target_r, target_c = tl_r, tl_c + 1
                if 0 <= target_r < rows and 0 <= target_c < cols and output_grid[target_r, target_c] == 0:
                    output_grid[target_r, target_c] = 1
            elif i == 1: # Second component: modify cell below
                target_r, target_c = tl_r + 1, tl_c
                if 0 <= target_r < rows and 0 <= target_c < cols and output_grid[target_r, target_c] == 0:
                    output_grid[target_r, target_c] = 1

    return output_grid.tolist()


if __name__ == '__main__':

    input = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

    expected_output = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```
