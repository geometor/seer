# 25.045.0644 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
Identifies connected regions of color '8', orders them by discovery, and modifies cells adjacent to their top-left cells based on a cyclic direction pattern (right, down, left, up).
For each '8'-object in discovery order, it attempts to change the color of an adjacent cell to '1' in the cyclic directions.
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

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
    direction_index = 0

    for component in components:
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
            for _ in range(4): # Try all directions in cycle
                dr, dc = directions[direction_index % 4]
                target_r, target_c = tl_r + dr, tl_c + dc
                if 0 <= target_r < rows and 0 <= target_c < cols and output_grid[target_r, target_c] == 0:
                    output_grid[target_r, target_c] = 1
                    break # Stop after first successful modification
                direction_index += 1 # Move to the next direction for the next attempt (or next component)


    return output_grid.tolist()


if __name__ == '__main__':

    input = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

    expected_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
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
