# 1-3aa6fb7a • 002 Response

---

*text:*

Okay, let's craft the Python code based on the natural language program and the provided template.




*text:*

```python
"""
The transformation rule identifies isolated azure pixels (color 8) and converts them to blue (color 1).
An isolated azure pixel is defined as one that does not have azure neighbors to its immediate top, bottom, left, and right.
Azure blocks remain unchanged.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = input_np.copy()
    rows, cols = input_np.shape

    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check neighbors (up, down, left, right)
                up = input_np[r - 1, c] if r > 0 else 0
                down = input_np[r + 1, c] if r < rows - 1 else 0
                left = input_np[r, c - 1] if c > 0 else 0
                right = input_np[r, c + 1] if c < cols - 1 else 0

                if up != 8 and down != 8 and left != 8 and right != 8:
                    output_np[r, c] = 1

    return output_np.tolist()


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
