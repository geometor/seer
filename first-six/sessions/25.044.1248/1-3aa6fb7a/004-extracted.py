"""
1.  **Identify Objects:** The primary objects are squares of color '8' (light blue).

2.  **Locate Specific Predicates:** Find the '8' colored squares that satisfy *either* of these two conditions:
    *   **Condition 1:** The '8' is along the top edge of a contiguous block of '8's, *and* it is immediately to the left of another '8'.
    *   **Condition 2:** The '8' is along the bottom edge of a contiguous block of '8's, *and* it is immediately to the right of another '8'.

3.  **Transformation Action:**
    *   Change the color of the '8' square to '1' *only* if it meets one of the conditions above.
"""

import copy

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

def transform(grid):
    """Transforms the input grid according to the rule."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(grid)  # Create a copy to avoid modifying the original

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 8:
                # Check for top-left condition
                if (r > 0 and grid[r-1][c] == 0) and (c+1 < cols and grid[r][c+1] == 8):
                    output_grid[r][c] = 1
                #check for botton-right condition
                if (r+1 < rows and grid[r+1][c] == 0) and (c > 0 and grid[r][c-1] == 8):
                    output_grid[r][c] = 1

    return output_grid

if __name__ == '__main__':
    transformed_grid = transform(input_grid)

    if transformed_grid == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:\n", expected_output)
        print("\nTransformed Output:\n", transformed_grid)

    assert transformed_grid == expected_output, "Transformed output does not match expected output."