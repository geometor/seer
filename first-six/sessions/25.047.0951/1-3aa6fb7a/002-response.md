# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The rule preserves every pixel of color 8. The input contains two distinct objects composed by pixels of color 8. The program turns to color 1 the rightmost and leftmost pixels of the objects found on the input, iterating the search from top to down.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    input_array = np.array(input_grid)
    
    # Find the connected components of color 8
    visited = np.zeros_like(input_array, dtype=bool)
    objects = []
    
    def dfs(r, c, current_object):
        if (r < 0 or r >= input_array.shape[0] or
            c < 0 or c >= input_array.shape[1] or
            visited[r, c] or input_array[r, c] != 8):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(input_array.shape[0]):
        for c in range(input_array.shape[1]):
            if input_array[r, c] == 8 and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)

    # change output pixels
    for obj in objects:
      #find rightmost
      rightmost = obj[0]
      for (r,c) in obj:
        if c > rightmost[1]:
          rightmost = (r,c)
      #find leftmost
      leftmost = obj[0]
      for (r,c) in obj:
        if c < leftmost[1]:
          leftmost = (r,c)

      output_grid[rightmost] = 1
      output_grid[leftmost] = 1


    return output_grid.tolist()


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
