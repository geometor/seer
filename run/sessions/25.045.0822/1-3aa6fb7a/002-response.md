# 25.045.0822 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
For the first connected component of color 8, change the cell to the right of its top-left cell to color 1.
For the second connected component of color 8, change the cell to the left of its bottom-right cell to color 1.
"""

import copy

def find_connected_components(grid, color):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    def bfs(r, c, current_component):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != color:
            return
        visited[r][c] = True
        current_component.append((r, c))
        bfs(r + 1, c, current_component)
        bfs(r - 1, c, current_component)
        bfs(r, c + 1, current_component)
        bfs(r, c - 1, current_component)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                current_component = []
                bfs(r, c, current_component)
                components.append(current_component)
    return components

def get_top_left_cell(component):
    top_left_cell = component[0]
    for r, c in component:
        if r < top_left_cell[0] or (r == top_left_cell[0] and c < top_left_cell[1]):
            top_left_cell = (r, c)
    return top_left_cell

def get_bottom_right_cell(component):
    bottom_right_cell = component[0]
    for r, c in component:
        if r > bottom_right_cell[0] or (r == bottom_right_cell[0] and c > bottom_right_cell[1]):
            bottom_right_cell = (r, c)
    return bottom_right_cell

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    components = find_connected_components(input_grid, 8)

    if not components:
        return output_grid

    # Process first component
    first_component = components[0]
    top_left_r, top_left_c = get_top_left_cell(first_component)
    right_c = top_left_c + 1
    if 0 <= right_c < cols and output_grid[top_left_r][right_c] == 0:
        output_grid[top_left_r][right_c] = 1

    if len(components) >= 2:
        # Process second component
        second_component = components[1]
        bottom_right_r, bottom_right_c = get_bottom_right_cell(second_component)
        left_c = bottom_right_c - 1
        if 0 <= left_c < cols and output_grid[bottom_right_r][left_c] == 0:
            output_grid[bottom_right_r][left_c] = 1

    return output_grid


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
