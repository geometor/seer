# 25.046.0932 • 1-3aa6fb7a • 004 Response

---

*text:*

The previously written code should work correctly for this example as well, since the transformation rule is the same. I will run the code with the new input and expected output to confirm.




*text:*

```python
"""
Identify Azure Objects: Locate all azure (color 8) objects in the input grid.
Locate Upper-Leftmost Azure Pixel: Within each azure object, find the pixel with the smallest row and column indices (top-leftmost).
Change to Blue: Change the color of this identified pixel from azure (8) to blue (1).
Repeat for all azure objects.
"""

import numpy as np

def get_objects(grid):
    """
    Detects contiguous regions (objects) of the same color.

    Args:
        grid: A 2D numpy array representing the input grid.

    Returns:
        A list of objects, where each object is a list of (row, col) tuples.
    """
    
    visited = set()
    objects = []

    def dfs(row, col, color, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, color, current_object)
        

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if (r, c) not in visited and grid[r,c]!=0:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append(current_object)
    return objects


def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Find each azure (8) object and change the color of its top-leftmost pixel to blue (1).
    """
    # Initialize output as a copy of the input
    output_grid = np.copy(input_grid)
    grid = np.array(input_grid)

    # Get all objects in the grid
    objects = get_objects(grid)

    # Iterate through each object
    for obj in objects:
        # Filter for azure objects
        if grid[obj[0][0], obj[0][1]] == 8:  # Check color of the first pixel in object
            # Find the top-leftmost pixel
            top_leftmost = min(obj, key=lambda p: (p[0], p[1]))

            # Change its color to blue (1)
            output_grid[top_leftmost] = 1

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

    if (np.array(output) == np.array(expected_output)).all():
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert (np.array(output) == np.array(expected_output)).all(), "Transformed output does not match expected output."
```
