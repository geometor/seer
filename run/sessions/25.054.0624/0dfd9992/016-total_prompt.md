# 0dfd9992 • 016 • refine_coder

---

Previous Code:
```python
"""
Identify and remove a contiguous region of white (0) pixels in the input grid, 
effectively isolating a repeating border pattern.
"""

import numpy as np

def find_contiguous_region(grid, start_row, start_col, color):
    """
    Finds a contiguous region of a given color starting from a given point.
    Uses a breadth-first search (BFS) algorithm.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    queue = [(start_row, start_col)]
    visited[start_row, start_col] = True
    region = []

    while queue:
        row, col = queue.pop(0)
        region.append((row, col))

        # Check neighbors (up, down, left, right)
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < rows - 1:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < cols - 1:
            neighbors.append((row, col + 1))
        

        for n_row, n_col in neighbors:
            if not visited[n_row, n_col] and grid[n_row, n_col] == color:
                visited[n_row, n_col] = True
                queue.append((n_row, n_col))

    return region

def get_pattern_element(row, col, sequence):
  """Retrieves the color based on a repeating sequence"""
  seq_len = len(sequence)

  index = (row % seq_len + (col % seq_len )* 2) %seq_len
  return sequence[index]

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Find a good starting point for the background.  Assume it's near the center.
    center_row, center_col = rows // 2, cols // 2
    
    if input_grid[center_row, center_col] == 0:

        # Identify the contiguous white region
        white_region = find_contiguous_region(input_grid, center_row, center_col, 0)

        # Remove the white region (set to background, which will be overwritten)
        for row, col in white_region:
            output_grid[row, col] = 0 # temporarily set to background


    # define border pattern
    sequence = [3,2,3,6, 2,1,2,5, 6,5,6,1]
    # Fill the removed region and stray 0 pixels, referencing border pattern
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 0:
              output_grid[r,c] = get_pattern_element(r,c, sequence)

    return output_grid
```

Train Set Results:

## Example 1:

Input:
```
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 0 0 0 0 0 5
2 5 4 5 2 1 2 5 0 0 2 1 2 5 4 0 0 0 0 0 4
3 6 5 6 3 2 3 0 0 0 0 2 3 6 5 0 0 0 0 0 5
6 3 2 3 6 5 6 0 0 0 0 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 0 0 0 0 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 0 0 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 0 0 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 0 0 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 0 0 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 0 0 0 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 0 0 0 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 0 0 0 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
```
Expected Output:
```
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
```
Transformed Output:
```
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 3 2 2 5
2 5 4 5 2 1 2 5 5 1 2 1 2 5 4 1 2 6 1 5 4
3 6 5 6 3 2 3 6 6 3 3 2 3 6 5 3 3 2 2 6 5
6 3 2 3 6 5 6 5 1 2 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 6 3 3 2 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 6 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 1 5 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 2 6 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 5 5 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 3 2 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 6 1 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 2 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
```
![Transformed Image](014-py_07-train-example_1.png)
match: False
pixels_off: 31
size_correct: True
color_palette_correct: True
correct_pixel_counts: False

## Example 2:

Input:
```
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 0 0 0 0 0 7 2 6 5 6 2 7 0 0 6 5 6
6 4 4 6 0 0 0 0 0 4 6 3 2 3 6 4 0 0 3 2 3
5 3 3 5 0 0 0 0 0 3 5 2 1 2 5 3 0 0 2 1 2
6 4 4 6 0 0 0 0 0 4 6 3 2 3 6 4 0 0 0 0 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 0 0 0 6
0 0 0 0 0 3 4 7 5 5 7 4 3 4 7 5 5 0 0 0 4
0 0 0 0 0 3 4 7 5 5 7 4 3 4 7 5 5 0 0 0 4
0 0 0 0 0 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 0 0 3 2 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 0 0 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 0 0 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
```
Expected Output:
```
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
```
Transformed Output:
```
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 1 2 6 1 5 7 2 6 5 6 2 7 1 2 6 5 6
6 4 4 6 3 3 2 2 6 4 6 3 2 3 6 4 3 3 3 2 3
5 3 3 5 2 6 1 5 5 3 5 2 1 2 5 3 2 6 2 1 2
6 4 4 6 3 2 2 6 6 4 6 3 2 3 6 4 3 2 2 6 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 1 5 5 6
6 6 3 3 2 3 4 7 5 5 7 4 3 4 7 5 5 2 6 6 4
5 1 2 6 1 3 4 7 5 5 7 4 3 4 7 5 5 5 5 1 4
6 3 3 2 2 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 5 1 3 2 3
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 6 3 6 5 6
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 1 2 4 3 4
7 5 5 7 4 3 4 7 5 5 7 4 3 4 7 5 5 7 4 3 4
2 7 7 2 6 5 6 2 7 7 2 6 5 6 2 7 7 2 6 5 6
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
5 3 3 5 2 1 2 5 3 3 5 2 1 2 5 3 3 5 2 1 2
6 4 4 6 3 2 3 6 4 4 6 3 2 3 6 4 4 6 3 2 3
```
![Transformed Image](014-py_07-train-example_2.png)
match: False
pixels_off: 50
size_correct: True
color_palette_correct: True
correct_pixel_counts: False

## Example 3:

Input:
```
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
0 0 0 0 0 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
0 0 0 0 0 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 0 0 0 2 3 6 3
2 1 2 5 0 0 0 0 2 0 0 0 2 1 0 0 0 1 2 5 2
3 2 3 6 0 0 0 0 3 0 0 0 3 2 3 6 3 2 3 6 3
6 5 6 1 0 0 0 0 6 0 0 0 6 5 6 1 6 5 6 1 6
3 2 3 6 0 0 0 0 3 0 0 0 3 2 3 6 3 2 3 6 3
2 1 2 5 0 0 0 0 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 0 0 0 0 0 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 0 0 0 0 0 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 0 0 0 0 0 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 0 0 0 0 0 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 0 0 0 0 0 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
```
Expected Output:
```
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
```
Transformed Output:
```
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 2 6 6 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 1 5 5 1 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 6 6 3 2 3 6 3
2 1 2 5 2 6 1 5 2 1 2 6 2 1 5 1 2 1 2 5 2
3 2 3 6 3 2 2 6 3 3 3 2 3 2 3 6 3 2 3 6 3
6 5 6 1 6 1 5 5 6 2 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 2 2 6 6 3 3 2 2 3 2 3 6 3 2 3 6 3
2 1 2 5 1 5 5 1 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 2 2 6 6 3 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 1 5 5 1 2 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 6 6 3 3 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
2 5 5 1 2 6 2 5 2 1 2 5 2 1 2 5 2 1 2 5 2
3 6 6 3 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6 5 6 1 6
3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3 2 3 6 3
```
![Transformed Image](014-py_07-train-example_3.png)
match: False
pixels_off: 45
size_correct: True
color_palette_correct: True
correct_pixel_counts: False
Okay, let's analyze the results and formulate a revised natural language program.

**General Assessment:**

The initial strategy of identifying and removing a contiguous white (0) region and then filling it with a repeating pattern was partially successful. However, the filling logic and the pattern itself are not robust enough to handle variations in the input grids. The "center" assumption for finding the white region also fails in some cases, and some isolated stray 0 pixels are not overwritten with the border pattern correctly. The filling pattern is not based on the grid position, but an unrelated sequence. The core issue is that the code attempts to apply a single, predefined sequence globally, rather than adapting to the structure of each input. The approach needs to consider local context when applying the pattern.

**Strategy for Resolving Errors:**

1.  **Improve Contiguous Region Finding:** Instead of relying on the center, iterate through the grid to find *all* contiguous regions of color `0`.
2.  **Contextual Pattern Filling:** The filling should be based on position, in relation to the surrounding border pixels of the contiguous regions.
3.  **Re-evaluate the need for the fill**: Perhaps it is sufficient to simply remove all 0 pixels.
4. **Object Identification** identify consistent objects across the input grids, along with properties

**Metrics and Observations:**

Here's a breakdown of each example:

*   **Example 1:**
    *   Input Shape: (21, 21)
    *   Output Shape: (21, 21)
    *   Pixels Off: 31
    *   Notes: The code partially fills the central white area but uses an incorrect, seemingly arbitrary, sequence. The stray `0` pixels are overwritten, in some cases with incorrect values.
*   **Example 2:**
    *   Input Shape: (21, 21)
    *   Output Shape: (21, 21)
    *   Pixels Off: 50
    *   Notes: Similar to Example 1, incorrect filling and issues with stray `0` pixels. The algorithm doesn't handle multiple disjoint white regions correctly.
*   **Example 3:**
    *   Input Shape: (21, 21)
    *   Output Shape: (21, 21)
    *   Pixels Off: 45
    *   Notes: Multiple white regions. Incorrect fill pattern application.

**YAML Block (Facts):**

```yaml
objects:
  - name: grid
    properties:
      - type: 2D array
      - values: integers (0-9) representing colors
      - description: Contains colored pixels forming patterns.
  - name: border
    properties:
      - type: contiguous region
      - description: Surrounds an inner region, often consisting of multiple colors.
  - name: inner_region
    properties:
      - type: contiguous region
      - color: initially white (0)
      - description:  The area enclosed by the border, originally filled with 0s.
  - name: pixel
    properties:
      - type: individual cell
      - values: integers(0-9) representing color
```

**Natural Language Program:**

1.  **Identify the Grid:** The input is a 2D grid of colored pixels.
2.  **Locate Background Pixels:** Find all pixels with a value of 0 (white).
3. **Remove Background:** Set the color of all background (0/white) pixels to match surrounding, non-zero, colors, effectively removing them.

The core idea is to remove all white pixels. The existing code is too complex and uses an erroneous fill strategy.

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
