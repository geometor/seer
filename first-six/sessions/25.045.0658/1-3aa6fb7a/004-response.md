# 25.045.0658 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
The transformation rule operates on each cell of the input grid. For every cell, we perform the following checks:

1. Check Cell Color: Determine the color of the current cell in the input grid.
2. White Cell Condition: If the cell's color is white (color 0), proceed to the next step. If the cell's color is not white, it remains unchanged in the output grid.
3. Neighbor Check: Examine the four immediate neighbors of the white cell: the cell directly above, below, to the left, and to the right.
4. Azure Neighbor Detection: Check if any of these neighboring cells are azure (color 8) in the input grid.
5. Color Transformation: If at least one neighbor is found to be azure (color 8), change the color of the current white cell to blue (color 1) in the output grid.
6. No Azure Neighbor: If none of the neighboring cells are azure (color 8), the current white cell remains white (color 0) in the output grid.
7. Non-White Cells: Cells that are not white in the input grid retain their original color in the output grid without any modification.

In summary, the transformation targets white cells and changes their color to blue only if they are adjacent (horizontally or vertically) to at least one azure cell in the input grid. All other cells remain unchanged.
"""

import copy

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0: # If the cell is white
                has_azure_neighbor = False
                # Check neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # right, left, down, up
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 8:
                        has_azure_neighbor = True
                        break
                if has_azure_neighbor:
                    output_grid[r][c] = 1 # Change to blue

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
