# 25.045.0717 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
The task is to identify connected regions of color 8 and modify a single cell adjacent to one of these regions.
1. Identify Connected Regions: Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. Order Regions: Order these regions based on their top-leftmost cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions first by row index and then by column index in ascending order.
3. Directions Cycle: Define a cycle of directions in the order: Right, Down, Left, Up.
4. Iterate and Modify: For each region in the ordered list, starting from the first region:
   a. Determine the direction from the directions cycle based on the region's order (1st region uses 'Right', 2nd uses 'Down', 3rd uses 'Left', 4th uses 'Up', and then the cycle repeats for subsequent regions if any).
   b. Calculate the coordinates of the target cell by taking the top-leftmost cell of the current region and moving one step in the determined direction.
   c. Check if the target cell is within the grid boundaries and if its color is 0.
   d. If both conditions are true, change the color of the target cell to 1, and stop the entire process. Only one cell's color is changed in the output grid.
"""

import copy

def find_connected_regions(grid, color):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def get_neighbors(r, c):
        return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

    def dfs(r, c, current_region):
        visited[r][c] = True
        current_region.append((r, c))
        for nr, nc in get_neighbors(r, c):
            if is_valid(nr, nc) and grid[nr][nc] == color and not visited[nr][nc]:
                dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                current_region = []
                dfs(r, c, current_region)
                regions.append(current_region)
    return regions

def get_top_leftmost_cell(region):
    top_leftmost_cell = region[0]
    for r, c in region:
        if r < top_leftmost_cell[0] or (r == top_leftmost_cell[0] and c < top_leftmost_cell[1]):
            top_leftmost_cell = (r, c)
    return top_leftmost_cell

def transform(input_grid):
    output_grid = copy.deepcopy(input_grid)
    regions = find_connected_regions(input_grid, 8)

    if not regions:
        return output_grid

    regions.sort(key=lambda region: get_top_leftmost_cell(region))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up

    for i, region in enumerate(regions):
        top_left_r, top_left_c = get_top_leftmost_cell(region)
        direction_index = i % 4
        dr, dc = directions[direction_index]
        target_r, target_c = top_left_r + dr, top_left_c + dc

        if 0 <= target_r < len(input_grid) and 0 <= target_c < len(input_grid[0]) and input_grid[target_r][target_c] == 0:
            output_grid[target_r][target_c] = 1
            return output_grid # Modify only one cell and stop

    return output_grid


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
