# 25.044.1414 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
1. Identify Corner '8's: Locate cells in the input grid that contain the value '8' and have exactly two neighboring cells that also contain the value '8'.
2. Find '8'-Neighbors: For each identified corner '8', determine its two neighboring cells that contain '8'.
3. Calculate Missing Corner Position: Calculate the coordinates of the 'missing corner' to complete a 2x2 square.
4. Check and Fill: If the cell at the 'missing corner' is '0', change it to '1' in the output grid.
5. Maintain Unchanged Cells: Keep other cells unchanged.
"""

def transform(input_grid):
    # initialize output grid as a copy of the input grid
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8:
                neighbor_8s = []
                # Check 4 neighbors (up, down, left, right)
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 8:
                        neighbor_8s.append((nr, nc))

                # Identify corner '8's (those with exactly two '8' neighbors)
                if len(neighbor_8s) == 2:
                    r1, c1 = neighbor_8s[0]
                    r2, c2 = neighbor_8s[1]

                    # Calculate missing corner position
                    missing_r = r1 + r2 - r
                    missing_c = c1 + c2 - c

                    # Check if the missing corner is within grid bounds and is '0'
                    if 0 <= missing_r < rows and 0 <= missing_c < cols and input_grid[missing_r][missing_c] == 0:
                        output_grid[missing_r][missing_c] = 1 # Fill with '1'

    return output_grid


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid)

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."
```
