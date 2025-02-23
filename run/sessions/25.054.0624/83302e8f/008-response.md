# 83302e8f • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Blue Lines:** Locate all blue (1) pixels in the input grid. These pixels form the "blue lines" object.
2.  **Identify Enclosed Regions.** Determine the regions enclosed by the continuous blue lines. An enclosed region is a set of contiguous white pixels that are completely surrounded by blue pixels, directly adjacent, forming a closed loop.
3. **Change color of first enclosed area:** Change the enclosed area above the first horizontal solid line of 1's to green (3)
4. **Change color of second enclosed area:** Change the enclosed area below the first horizontal solid line of 1's to yellow (4).
5.  **Preserve Blue Lines:** Maintain the blue (1) pixels in their original positions in the output grid.
6.  **Other areas:** All other enclosed areas not specified before get a fill value according to their position, if they are above the first line of 1's then the value is 3, otherwise the value is 4.
"""

import numpy as np

def find_blue_lines(grid):
    # Find the coordinates of all blue pixels.
    return np.where(grid == 1)

def is_enclosed(grid, coord, blue_lines_set):
    """
    Checks if a given coordinate is within an enclosed region.
    Uses a flood-fill algorithm.
    """
    rows, cols = grid.shape
    x, y = coord

    # If the starting coordinate is blue, it's not enclosed.
    if grid[x, y] == 1:
        return False

    visited = set()
    queue = [(x, y)]

    while queue:
        curr_x, curr_y = queue.pop(0)

        if (curr_x, curr_y) in visited:
            continue
        visited.add((curr_x, curr_y))

        # If we hit a boundary, it's not enclosed.
        if curr_x == 0 or curr_x == rows - 1 or curr_y == 0 or curr_y == cols - 1:
            return False

        # Check neighbors
        neighbors = [
            (curr_x - 1, curr_y),
            (curr_x + 1, curr_y),
            (curr_x, curr_y - 1),
            (curr_x, curr_y + 1),
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx, ny] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                elif grid[nx,ny] == 1:
                    continue #part of boundary, do nothing
                else:
                    return False #hit a color other than blue or white
    return True

def find_first_solid_line(grid):
     rows, cols = grid.shape
     for r in range(rows):
        if all(grid[r,c] == 1 for c in range(cols)):
            return r
     return -1 #no line found

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    blue_lines = find_blue_lines(input_grid)
    blue_lines_set = set(zip(blue_lines[0], blue_lines[1]))

    first_line = find_first_solid_line(input_grid)


    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in blue_lines_set:
                if is_enclosed(input_grid, (r, c), blue_lines_set):
                    if r < first_line:
                        output_grid[r,c] = 3
                    else:
                        output_grid[r, c] = 4

    return output_grid
```
