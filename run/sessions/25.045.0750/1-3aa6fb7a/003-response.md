# 25.045.0750 • 1-3aa6fb7a • 003 Response

---

*text:*

**Natural Language Program:**

1. **Identify Objects:** Find all connected regions of color 8 in the input grid. Regions are connected if cells of color 8 are adjacent horizontally or vertically.
2. **Iterate through Objects:** For each identified region of color 8:
    a. **Find Top-Leftmost Cell:** Locate the cell within the region that has the smallest row index. If there are multiple cells with the same smallest row index, choose the one with the smallest column index among them. Let's call the coordinates of this cell (top_row, top_col).
    b. **Check Neighbors in Order:** Check the neighbors of the top-leftmost cell in the following order:
        i. **Right Neighbor:** Examine the cell at coordinates (top_row, top_col + 1). If it is within the grid boundaries and its color is 0 (white), change its color to 1 (blue) and proceed to the next region.
        ii. **Bottom Neighbor:** If the right neighbor was not changed, examine the cell at coordinates (top_row + 1, top_col). If it is within the grid boundaries and its color is 0 (white), change its color to 1 (blue) and proceed to the next region.
        iii. **Left Neighbor:** If neither right nor bottom neighbor was changed, examine the cell at coordinates (top_row, top_col - 1). If it is within the grid boundaries and its color is 0 (white), change its color to 1 (blue) and proceed to the next region.
        iv. **Top Neighbor:** If none of the above neighbors were changed, examine the cell at coordinates (top_row - 1, top_col). If it is within the grid boundaries and its color is 0 (white), change its color to 1 (blue) and proceed to the next region.
3. **Output Grid:** The modified grid after processing all regions of color 8 is the output grid.

**Python Implementation:**
```python
import copy

def find_regions(grid, color_to_find):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    def explore_region(r, c, current_region):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != color_to_find:
            return
        visited[r][c] = True
        current_region.append((r, c))
        explore_region(r + 1, c, current_region)
        explore_region(r - 1, c, current_region)
        explore_region(r, c + 1, current_region)
        explore_region(r, c - 1, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color_to_find and not visited[r][c]:
                current_region = []
                explore_region(r, c, current_region)
                regions.append(current_region)
    return regions

def find_top_leftmost_cell(region):
    top_row = min(r for r, c in region)
    top_leftmost_col = min(c for r, c in region if r == top_row)
    return top_row, top_leftmost_col

def transform(input_grid):
    output_grid = copy.deepcopy(input_grid)
    regions = find_regions(input_grid, 8)

    for region in regions:
        if not region:
            continue

        top_left_row, top_left_col = find_top_leftmost_cell(region)

        # Check neighbors in order: Right, Bottom, Left, Top
        neighbors_check = [
            (0, 1),  # Right
            (1, 0),  # Bottom
            (0, -1), # Left
            (-1, 0)  # Top
        ]

        for dr, dc in neighbors_check:
            neighbor_row, neighbor_col = top_left_row + dr, top_left_col + dc
            if 0 <= neighbor_row < len(input_grid) and 0 <= neighbor_col < len(input_grid[0]) and output_grid[neighbor_row][neighbor_col] == 0:
                output_grid[neighbor_row][neighbor_col] = 1
                break # Move to the next region after changing color

    return output_grid


if __name__ == '__main__':

    input_grids = [
        [
            [0, 0, 0, 0, 8, 8, 0],
            [0, 0, 0, 0, 0, 8, 0],
            [0, 0, 8, 0, 0, 0, 0],
            [0, 0, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 8, 8, 0, 0]
        ]
    ]

    expected_outputs = [
        [
            [0, 0, 0, 0, 8, 8, 0],
            [0, 0, 0, 0, 1, 8, 0],
            [0, 0, 8, 1, 0, 0, 0],
            [0, 0, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 8, 0, 0],
            [0, 0, 0, 8, 8, 0, 0]
        ]
    ]

    for input, expected_output in zip(input_grids, expected_outputs):
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
