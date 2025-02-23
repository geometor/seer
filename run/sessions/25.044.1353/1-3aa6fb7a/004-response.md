# 25.044.1353 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
For every empty square (represented by 0) in the input grid, check its adjacent squares (up, down, left, right) in the *same input grid*. If any of these adjacent squares is an '8', then change the empty square to a '1' in the output grid. If none of the adjacent squares are '8', or if the square was not empty to begin with, leave it as it was in the output grid.
"""

def transform(input_grid):
    # Get the dimensions of the input grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # Initialize the output grid as a copy of the input grid
    output_grid = [row[:] for row in input_grid]

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0:
                # Check neighbors for value 8
                neighbors = [
                    (r - 1, c),  # Up
                    (r + 1, c),  # Down
                    (r, c - 1),  # Left
                    (r, c + 1)   # Right
                ]
                found_neighbor_8 = False
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 8:
                        found_neighbor_8 = True
                        break
                if found_neighbor_8:
                    output_grid[r][c] = 1

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

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```
