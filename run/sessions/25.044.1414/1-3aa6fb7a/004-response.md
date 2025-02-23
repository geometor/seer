# 25.044.1414 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
1. Identify '8' Corners: Examine each cell in the input grid. Identify cells containing the value '8' that have exactly two neighboring cells (up, down, left, right) that also contain the value '8'.

2. Locate '8' Neighbors: For each identified '8' corner cell, find its two neighboring cells that contain '8'.

3. Calculate Missing Square Corner: Using the coordinates of the '8' corner cell and its two '8' neighbors, calculate the coordinates of the cell that would complete a 2x2 square if connected with these three '8's.  The coordinates of this 'missing corner' (row_missing, column_missing) can be calculated as follows:
   `row_missing = row_neighbor1 + row_neighbor2 - row_corner`
   `column_missing = column_neighbor1 + column_neighbor2 - column_corner`
   where (row_corner, column_corner) is the location of the '8' corner, and (row_neighbor1, column_neighbor1) and (row_neighbor2, column_neighbor2) are the locations of its two '8' neighbors.

4. Conditional Fill: Check the value of the cell at the calculated 'missing corner' location in the *input* grid. If this value is '0', then in the *output* grid, change the value of this cell to '1'.

5. Retain Unchanged Values: For all other cells in the grid that are not modified in step 4, their values in the output grid should be identical to their values in the input grid.

This program describes a process of finding configurations of three '8's that form three corners of a 2x2 square and filling in the fourth corner with a '1' if it was initially '0'.
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
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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
