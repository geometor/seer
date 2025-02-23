# 890034e9 • 012 • refine_coder

---

Previous Code:
```python
"""
The transformation rule is: Move the yellow objects to be adjacent to green objects.
The shape, size and color of the yellow objects are preserved.
If there is already a yellow object that is adjacent to a green object, do not move it.
If a yellow object is adjacent to more than one green object, choose one arbitrarily.
Azure (8) objects are not moved.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find contiguous regions (objects) of a specific color in the grid.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_adjacent_objects(grid, objects, target_color):
    """Find the location and count the adjacent blocks given a target color"""
    adjacencies = []

    for obj in objects:
      for cell in obj:
        row,col = cell

        #check neighbors
        neighbors = [
            (row -1, col),
            (row + 1, col),
            (row, col-1),
            (row, col + 1)
        ]

        for neighbor_row, neighbor_col in neighbors:
            if (0 <= neighbor_row < grid.shape[0] and
                0 <= neighbor_col < grid.shape[1] and
                grid[neighbor_row, neighbor_col] == target_color):
                adjacencies.append( (neighbor_row, neighbor_col) )

    return adjacencies

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find green (3) objects
    green_objects = find_objects(output_grid, 3)

    # Find yellow (4) objects
    yellow_objects = find_objects(output_grid, 4)

    #iterate through yellow objects
    for yellow_object in yellow_objects:

      # find green objects adjacent to this yellow object
      adjacent_greens = find_adjacent_objects(output_grid, [yellow_object], 3)

      # If the yellow object is NOT already adjacent to a green object, then move
      if not adjacent_greens:

        #clear current yellow object
        for row, col in yellow_object:
          output_grid[row, col] = input_grid[row,col]


        # find *any* green and use its location for the move
        if green_objects:
          #arbitrarily choose the first green object, and first cell within that object
          target_row, target_col = green_objects[0][0]

          #attempt to move the yellow object, based on relative location to the target
          for i in range(len(yellow_object)):
              row_offset = yellow_object[i][0] - yellow_object[0][0]
              col_offset = yellow_object[i][1] - yellow_object[0][1]

              new_row = target_row + row_offset
              new_col = target_col + col_offset

              #make sure it is valid move
              if (0 <= new_row < output_grid.shape[0] and
                  0 <= new_col < output_grid.shape[1] ):

                #check if spot is available, prioritize green
                if output_grid[new_row, new_col] == 3:
                  output_grid[new_row, new_col] = 4
                elif output_grid[new_row, new_col] == 0:
                  output_grid[new_row,new_col] = 4


    return output_grid
```

Train Set Results:

## Example 1:

Input:
```
0 8 1 1 0 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1
1 1 0 8 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 1 1
1 0 0 1 0 0 2 2 2 2 1 1 1 1 1 8 1 1 1 1 0
0 1 1 1 1 1 2 0 0 2 1 1 1 1 1 1 1 8 1 0 1
1 1 1 1 1 0 2 0 0 2 1 0 0 1 1 0 1 0 1 1 0
1 0 0 0 0 1 2 0 0 2 1 8 1 1 1 1 1 0 1 1 1
0 0 1 1 0 1 2 2 2 2 1 0 1 0 0 1 1 8 0 0 8
0 1 8 0 0 1 1 0 0 1 1 0 1 1 1 1 8 1 1 0 0
1 1 1 8 8 1 1 1 0 0 8 1 1 1 1 1 8 1 0 0 1
8 1 0 1 1 1 1 0 8 1 1 0 1 1 1 1 0 0 1 0 1
8 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 8 1 1 8 1
1 1 1 8 1 0 1 1 8 1 0 1 1 1 0 1 1 1 1 0 1
1 0 8 1 1 8 0 1 1 1 1 1 1 1 0 1 0 8 1 1 1
1 1 8 1 1 1 0 1 0 0 1 1 0 8 1 0 1 0 1 1 8
1 1 1 1 1 1 0 0 8 1 0 0 1 1 8 1 1 8 1 0 1
8 8 8 1 1 1 1 8 1 1 0 0 1 1 0 1 1 1 1 0 1
1 1 0 1 8 0 0 8 1 1 0 0 1 1 1 1 0 1 0 1 0
1 8 8 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0
1 1 8 0 1 0 1 1 0 1 1 1 1 1 1 0 1 0 0 1 1
1 1 0 0 8 1 0 1 0 0 0 0 1 1 1 0 8 0 0 0 0
1 0 0 1 0 0 1 0 0 1 1 1 1 0 1 1 0 8 1 8 0
```
Expected Output:
```
0 8 1 1 0 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1
1 1 0 8 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 1 1
1 0 0 1 0 0 2 2 2 2 1 1 1 1 1 8 1 1 1 1 0
0 1 1 1 1 1 2 0 0 2 1 1 1 1 1 1 1 8 1 0 1
1 1 1 1 1 0 2 0 0 2 1 0 0 1 1 0 1 0 1 1 0
1 0 0 0 0 1 2 0 0 2 1 8 1 1 1 1 1 0 1 1 1
0 0 1 1 0 1 2 2 2 2 1 0 1 0 0 1 1 8 0 0 8
0 1 8 0 0 1 1 0 0 1 1 0 1 1 1 1 8 1 1 0 0
1 1 1 8 8 1 1 1 0 0 8 1 1 1 1 1 8 1 0 0 1
8 1 0 1 1 1 1 0 8 1 1 0 1 1 1 1 0 0 1 0 1
8 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 8 1 1 8 1
1 1 1 8 1 0 1 1 8 1 0 1 1 1 0 1 1 1 1 0 1
1 0 8 1 1 8 0 1 1 1 1 1 1 1 0 1 0 8 1 1 1
1 1 8 1 1 1 0 1 0 2 2 2 2 8 1 0 1 0 1 1 8
1 1 1 1 1 1 0 0 8 2 0 0 2 1 8 1 1 8 1 0 1
8 8 8 1 1 1 1 8 1 2 0 0 2 1 0 1 1 1 1 0 1
1 1 0 1 8 0 0 8 1 2 0 0 2 1 1 1 0 1 0 1 0
1 8 8 1 1 1 1 1 1 2 2 2 2 1 1 1 0 0 1 1 0
1 1 8 0 1 0 1 1 0 1 1 1 1 1 1 0 1 0 0 1 1
1 1 0 0 8 1 0 1 0 0 0 0 1 1 1 0 8 0 0 0 0
1 0 0 1 0 0 1 0 0 1 1 1 1 0 1 1 0 8 1 8 0
```
Transformed Output:
```
0 8 1 1 0 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1
1 1 0 8 1 1 1 0 1 0 0 0 1 1 1 1 0 1 1 1 1
1 0 0 1 0 0 2 2 2 2 1 1 1 1 1 8 1 1 1 1 0
0 1 1 1 1 1 2 0 0 2 1 1 1 1 1 1 1 8 1 0 1
1 1 1 1 1 0 2 0 0 2 1 0 0 1 1 0 1 0 1 1 0
1 0 0 0 0 1 2 0 0 2 1 8 1 1 1 1 1 0 1 1 1
0 0 1 1 0 1 2 2 2 2 1 0 1 0 0 1 1 8 0 0 8
0 1 8 0 0 1 1 0 0 1 1 0 1 1 1 1 8 1 1 0 0
1 1 1 8 8 1 1 1 0 0 8 1 1 1 1 1 8 1 0 0 1
8 1 0 1 1 1 1 0 8 1 1 0 1 1 1 1 0 0 1 0 1
8 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 8 1 1 8 1
1 1 1 8 1 0 1 1 8 1 0 1 1 1 0 1 1 1 1 0 1
1 0 8 1 1 8 0 1 1 1 1 1 1 1 0 1 0 8 1 1 1
1 1 8 1 1 1 0 1 0 0 1 1 0 8 1 0 1 0 1 1 8
1 1 1 1 1 1 0 0 8 1 0 0 1 1 8 1 1 8 1 0 1
8 8 8 1 1 1 1 8 1 1 0 0 1 1 0 1 1 1 1 0 1
1 1 0 1 8 0 0 8 1 1 0 0 1 1 1 1 0 1 0 1 0
1 8 8 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 1 0
1 1 8 0 1 0 1 1 0 1 1 1 1 1 1 0 1 0 0 1 1
1 1 0 0 8 1 0 1 0 0 0 0 1 1 1 0 8 0 0 0 0
1 0 0 1 0 0 1 0 0 1 1 1 1 0 1 1 0 8 1 8 0
```
![Transformed Image](010-py_05-train-example_1.png)
match: False
pixels_off: 14
size_correct: True
color_palette_correct: True
correct_pixel_counts: False

## Example 2:

Input:
```
3 0 3 4 3 3 3 3 0 3 3 4 0 3 0 4 3 4 4 0 0
3 3 0 0 3 3 3 4 0 0 4 4 4 3 0 0 3 3 4 0 3
4 4 4 3 4 3 0 3 0 0 4 3 0 3 3 4 3 0 0 3 0
0 4 4 4 3 0 3 3 3 0 3 0 3 0 0 0 0 3 4 3 3
3 3 0 4 3 3 0 0 0 0 3 0 4 4 4 3 0 3 0 0 0
0 3 0 0 3 0 0 3 0 3 0 0 0 3 3 3 3 4 3 0 3
0 3 0 0 3 4 0 3 4 0 4 4 0 0 3 4 0 0 0 3 3
0 3 3 3 0 4 4 3 4 3 0 3 3 3 4 0 3 0 3 3 3
4 0 4 3 4 3 4 4 0 0 4 0 0 0 0 3 0 3 3 0 0
0 0 4 0 0 0 0 3 4 4 3 4 0 0 0 4 0 0 4 3 3
3 0 0 8 8 8 8 8 4 3 0 3 3 0 4 4 0 4 4 4 4
3 3 0 8 0 0 0 8 3 0 0 0 0 4 0 3 3 0 4 3 3
0 0 0 8 0 0 0 8 3 3 0 3 3 4 3 0 4 0 3 0 0
3 0 4 8 8 8 8 8 0 3 0 3 0 0 3 3 3 0 4 3 0
4 0 0 0 0 3 0 4 0 0 3 0 0 3 3 3 4 0 4 0 3
0 0 4 3 0 0 0 3 0 0 3 4 0 0 4 0 0 3 4 3 4
4 4 0 0 3 0 3 4 4 3 4 3 4 0 4 4 0 3 4 3 4
3 4 3 3 0 0 0 0 3 0 3 4 0 0 0 3 3 3 3 0 3
0 0 0 0 0 3 0 3 3 4 0 3 3 3 4 0 4 0 3 4 0
3 3 3 0 4 0 4 3 0 0 0 3 0 0 3 3 0 0 4 3 0
0 4 3 3 3 0 4 4 3 4 3 4 0 4 3 4 4 0 0 4 0
```
Expected Output:
```
3 0 3 4 3 3 3 3 0 3 3 4 0 3 0 4 3 4 4 0 0
3 3 0 0 3 3 3 4 0 0 4 4 4 3 0 0 3 3 4 0 3
4 4 4 3 4 3 0 3 0 0 4 3 0 3 3 4 3 0 0 3 0
0 4 4 4 3 0 3 3 3 0 3 0 3 0 0 0 0 3 4 3 3
3 3 0 4 3 3 0 0 0 0 3 0 4 4 4 3 0 3 0 0 0
0 3 0 0 3 0 0 3 0 3 0 0 0 3 3 3 3 4 3 0 3
0 3 0 0 3 4 0 3 4 0 4 4 0 0 3 4 0 0 0 3 3
0 3 3 3 0 4 4 3 4 3 0 8 8 8 8 8 3 0 3 3 3
4 0 4 3 4 3 4 4 0 0 4 8 0 0 0 8 0 3 3 0 0
0 0 4 0 0 0 0 3 4 4 3 8 0 0 0 8 0 0 4 3 3
3 0 0 8 8 8 8 8 4 3 0 8 8 8 8 8 0 4 4 4 4
3 3 0 8 0 0 0 8 3 0 0 0 0 4 0 3 3 0 4 3 3
0 0 0 8 0 0 0 8 3 3 0 3 3 4 3 0 4 0 3 0 0
3 0 4 8 8 8 8 8 0 3 0 3 0 0 3 3 3 0 4 3 0
4 0 0 0 0 3 0 4 0 0 3 0 0 3 3 3 4 0 4 0 3
0 0 4 3 0 0 0 3 0 0 3 4 0 0 4 0 0 3 4 3 4
4 4 0 0 3 0 3 4 4 3 4 3 4 0 4 4 0 3 4 3 4
3 4 3 3 0 0 0 0 3 0 3 4 0 0 0 3 3 3 3 0 3
0 0 0 0 0 3 0 3 3 4 0 3 3 3 4 0 4 0 3 4 0
3 3 3 0 4 0 4 3 0 0 0 3 0 0 3 3 0 0 4 3 0
0 4 3 3 3 0 4 4 3 4 3 4 0 4 3 4 4 0 0 4 0
```
Transformed Output:
```
4 0 3 4 3 3 3 3 0 3 3 4 0 3 0 4 3 4 4 0 0
3 3 0 0 3 3 3 4 0 0 4 4 4 3 0 0 3 3 4 0 3
4 4 4 3 4 3 0 3 0 0 4 3 0 3 3 4 3 0 0 3 0
0 4 4 4 3 0 3 3 3 0 3 0 3 0 0 0 0 3 4 3 3
3 3 0 4 3 3 0 0 0 0 3 0 4 4 4 3 0 3 0 0 0
0 3 0 0 3 0 0 3 0 3 0 0 0 3 3 3 3 4 3 0 3
0 3 0 0 3 4 0 3 4 0 4 4 0 0 3 4 0 0 0 3 3
0 3 3 3 0 4 4 3 4 3 0 3 3 3 4 0 3 0 3 3 3
4 0 4 3 4 3 4 4 0 0 4 0 0 0 0 3 0 3 3 0 0
0 0 4 0 0 0 0 3 4 4 3 4 0 0 0 4 0 0 4 3 3
3 0 0 8 8 8 8 8 4 3 0 3 3 0 4 4 0 4 4 4 4
3 3 0 8 0 0 0 8 3 0 0 0 0 4 0 3 3 0 4 3 3
0 0 0 8 0 0 0 8 3 3 0 3 3 4 3 0 4 0 3 0 0
3 0 4 8 8 8 8 8 0 3 0 3 0 0 3 3 3 0 4 3 0
4 0 0 0 0 3 0 4 0 0 3 0 0 3 3 3 4 0 4 0 3
0 0 4 3 0 0 0 3 0 0 3 4 0 0 4 0 0 3 4 3 4
4 4 0 0 3 0 3 4 4 3 4 3 4 0 4 4 0 3 4 3 4
3 4 3 3 0 0 0 0 3 0 3 4 0 0 0 3 3 3 3 0 3
0 0 0 0 0 3 0 3 3 4 0 3 3 3 4 0 4 0 3 4 0
3 3 3 0 4 0 4 3 0 0 0 3 0 0 3 3 0 0 4 3 0
0 4 3 3 3 0 4 4 3 4 3 4 0 4 3 4 4 0 0 4 0
```
![Transformed Image](010-py_05-train-example_2.png)
match: False
pixels_off: 15
size_correct: True
color_palette_correct: True
correct_pixel_counts: False

## Example 3:

Input:
```
0 0 3 0 3 2 0 2 0 3 3 2 2 2 2 2 2 2 2 3 3
3 2 2 0 3 2 0 2 2 2 2 2 2 2 2 3 2 2 0 3 2
3 3 0 3 0 0 3 2 2 2 2 3 2 2 2 2 3 0 0 3 2
2 2 3 2 4 4 4 4 4 4 3 0 3 2 0 2 2 2 0 0 3
3 3 2 0 4 0 0 0 0 4 2 0 2 2 0 2 3 0 2 2 0
3 2 2 2 4 0 0 0 0 4 0 3 2 2 3 2 2 3 3 2 0
2 0 2 0 4 0 0 0 0 4 2 0 0 0 2 2 2 0 2 2 2
0 2 0 2 4 4 4 4 4 4 2 2 0 2 0 2 0 0 2 2 2
2 0 2 2 2 0 2 0 2 0 3 2 3 3 0 2 0 0 0 2 2
0 2 3 0 3 0 2 3 2 2 2 0 2 0 0 0 2 2 3 2 0
3 0 2 0 2 0 0 2 2 0 3 3 2 3 0 3 3 0 0 3 0
2 3 0 3 2 2 2 2 2 0 0 0 0 2 0 2 0 3 0 0 2
3 2 2 0 2 0 2 2 0 3 2 2 2 2 3 0 2 2 2 2 2
3 3 3 2 0 2 0 2 0 3 2 2 2 0 0 3 2 2 3 2 2
0 0 2 2 2 3 2 0 0 2 3 2 0 3 0 2 2 3 2 2 0
2 2 2 2 2 3 2 3 3 3 2 0 0 0 0 2 0 0 2 3 0
2 2 2 2 3 0 0 3 3 2 0 0 0 0 0 0 2 2 3 2 0
2 0 3 2 2 2 3 2 3 3 3 0 0 0 0 0 2 0 0 2 3
2 2 0 0 0 0 0 0 0 3 2 3 2 2 3 0 0 2 2 0 0
0 3 0 2 2 2 0 0 0 2 2 2 2 3 0 2 0 0 0 3 2
2 3 2 2 2 0 0 3 2 0 3 2 0 2 2 2 3 0 0 2 2
```
Expected Output:
```
0 0 3 0 3 2 0 2 0 3 3 2 2 2 2 2 2 2 2 3 3
3 2 2 0 3 2 0 2 2 2 2 2 2 2 2 3 2 2 0 3 2
3 3 0 3 0 0 3 2 2 2 2 3 2 2 2 2 3 0 0 3 2
2 2 3 2 4 4 4 4 4 4 3 0 3 2 0 2 2 2 0 0 3
3 3 2 0 4 0 0 0 0 4 2 0 2 2 0 2 3 0 2 2 0
3 2 2 2 4 0 0 0 0 4 0 3 2 2 3 2 2 3 3 2 0
2 0 2 0 4 0 0 0 0 4 2 0 0 0 2 2 2 0 2 2 2
0 2 0 2 4 4 4 4 4 4 2 2 0 2 0 2 0 0 2 2 2
2 0 2 2 2 0 2 0 2 0 3 2 3 3 0 2 0 0 0 2 2
0 2 3 0 3 0 2 3 2 2 2 0 2 0 0 0 2 2 3 2 0
3 0 2 0 2 0 0 2 2 0 3 3 2 3 0 3 3 0 0 3 0
2 3 0 3 2 2 2 2 2 0 0 0 0 2 0 2 0 3 0 0 2
3 2 2 0 2 0 2 2 0 3 2 2 2 2 3 0 2 2 2 2 2
3 3 3 2 0 2 0 2 0 3 2 2 2 0 0 3 2 2 3 2 2
0 0 2 2 2 3 2 0 0 2 4 4 4 4 4 4 2 3 2 2 0
2 2 2 2 2 3 2 3 3 3 4 0 0 0 0 4 0 0 2 3 0
2 2 2 2 3 0 0 3 3 2 4 0 0 0 0 4 2 2 3 2 0
2 0 3 2 2 2 3 2 3 3 4 0 0 0 0 4 2 0 0 2 3
2 2 0 0 0 0 0 0 0 3 4 4 4 4 4 4 0 2 2 0 0
0 3 0 2 2 2 0 0 0 2 2 2 2 3 0 2 0 0 0 3 2
2 3 2 2 2 0 0 3 2 0 3 2 0 2 2 2 3 0 0 2 2
```
Transformed Output:
```
0 0 3 0 3 2 0 2 0 3 3 2 2 2 2 2 2 2 2 3 3
3 2 2 0 3 2 0 2 2 2 2 2 2 2 2 3 2 2 0 3 2
3 3 0 3 0 0 3 2 2 2 2 3 2 2 2 2 3 0 0 3 2
2 2 3 2 4 4 4 4 4 4 3 0 3 2 0 2 2 2 0 0 3
3 3 2 0 4 0 0 0 0 4 2 0 2 2 0 2 3 0 2 2 0
3 2 2 2 4 0 0 0 0 4 0 3 2 2 3 2 2 3 3 2 0
2 0 2 0 4 0 0 0 0 4 2 0 0 0 2 2 2 0 2 2 2
0 2 0 2 4 4 4 4 4 4 2 2 0 2 0 2 0 0 2 2 2
2 0 2 2 2 0 2 0 2 0 3 2 3 3 0 2 0 0 0 2 2
0 2 3 0 3 0 2 3 2 2 2 0 2 0 0 0 2 2 3 2 0
3 0 2 0 2 0 0 2 2 0 3 3 2 3 0 3 3 0 0 3 0
2 3 0 3 2 2 2 2 2 0 0 0 0 2 0 2 0 3 0 0 2
3 2 2 0 2 0 2 2 0 3 2 2 2 2 3 0 2 2 2 2 2
3 3 3 2 0 2 0 2 0 3 2 2 2 0 0 3 2 2 3 2 2
0 0 2 2 2 3 2 0 0 2 3 2 0 3 0 2 2 3 2 2 0
2 2 2 2 2 3 2 3 3 3 2 0 0 0 0 2 0 0 2 3 0
2 2 2 2 3 0 0 3 3 2 0 0 0 0 0 0 2 2 3 2 0
2 0 3 2 2 2 3 2 3 3 3 0 0 0 0 0 2 0 0 2 3
2 2 0 0 0 0 0 0 0 3 2 3 2 2 3 0 0 2 2 0 0
0 3 0 2 2 2 0 0 0 2 2 2 2 3 0 2 0 0 0 3 2
2 3 2 2 2 0 0 3 2 0 3 2 0 2 2 2 3 0 0 2 2
```
![Transformed Image](010-py_05-train-example_3.png)
match: False
pixels_off: 18
size_correct: True
color_palette_correct: True
correct_pixel_counts: False
Okay, let's analyze the results and update the natural language program.

**General Assessment:**

The current code attempts to move yellow objects adjacent to green objects. However, the strategy for moving yellow objects is flawed, as it simply uses the first green object found and its top-left position, rather than finding the _nearest_ green, and moving next to it. Also, it is attempting a 1:1 translation of the entire object, rather than moving individual pixels of the yellow object, and does not take into account obstacles, like azure or other colored objects.
It also does not account for cases where a yellow object may split when moved, and only moves relative to the yellow objects initial position.

The examples reveal the following issues:

1.  **Incorrect Movement:** The yellow objects are not consistently moved to the closest available position adjacent to a green object. The current implementation seems to pick an arbitrary green object and uses that one location, leading to incorrect placement. It's clear that there's not a well-defined movement rule regarding obstacles.
2.  **Object Integrity is not Preserved:** The relative position of the yellow object should be better preserved and only moved based on adjacent pixels.
3. **Splitting:** in Example 3, the yellow objects are split because of obstacles and the simple movement rule.

**Strategy for Resolving Errors:**

1.  **Nearest Green:** Instead of simply using the location of the first encountered green object, we should move individual pixels of the yellow object to the nearest valid location, taking obstacles into account.
2.  **Obstacle Handling:** Consider all colors as potential obstacles for movement.
3. **Adjacent Pixel Movement**: Move each individual pixel of yellow object adjacent to the _nearest_ green.

**Metrics and Observations (Examples 1-3):**

Here's a breakdown of each example, incorporating observations:

*Example 1:*

*   **Input:** Several yellow and green objects scattered, some large azure areas.
*   **Expected Output:** Yellow objects moved next to green, preserving shape.
*   **Actual Output:** Yellow objects only partially moved, no clear logic, large chunk of the yellow objects has disappeared and not preserved.
*   **Mismatch:** 14 pixels. Many yellow pixels have disappeared.

*Example 2:*

*   **Input:** Many small yellow and green objects, some larger azure area in the middle.
*   **Expected Output:** Yellow objects moved next to green.
*   **Actual Output:** Very little movement, some green have changed to yellow
*   **Mismatch:** 15 pixels. Many green pixels changed to yellow.

*Example 3:*

*   **Input:** large horizontal yellow rectangle, surrounded by green, some red.
*   **Expected Output:** Yellow rectangle should split up and move to the nearest green, with yellow filling any open adjacent spots.
*   **Actual Output:** No movement, and green has disappeared
*   **Mismatch:** 18 pixels. Green pixels have disappeared.

**YAML Block (Facts):**

```yaml
observations:
  - example: 1
    objects:
      - color: yellow
        shape: variable
        moved: true
        movement_rule: adjacent_to_green
        integrity: partially_preserved
      - color: green
        shape: variable
        moved: false
      - color: azure
        shape: variable
        moved: false
    notes: "Yellow objects should be moved next to green, preserving shape if possible. Current code moves incorrectly and removes parts of the yellow objects."

  - example: 2
    objects:
      - color: yellow
        shape: variable
        moved: true
        movement_rule: adjacent_to_green
        integrity: not_preserved
      - color: green
        shape: variable
        moved: false
      - color: azure
        shape: variable
        moved: false
    notes: "Yellow objects move very little. Many green objects are incorrectly colored yellow."

  - example: 3
    objects:
      - color: yellow
        shape: rectangle
        moved: true
        movement_rule: adjacent_to_green
        integrity: not_preserved, splits into many parts
      - color: green
        shape: variable
        moved: false
    notes: "The large yellow rectangle should be split to move parts adjacent to green.  Current implementation removes many green and makes no movement."
```

**Natural Language Program:**

1.  **Identify Objects:** Find all contiguous regions (objects) of yellow (4) and green (3) pixels in the input grid.
2.  **Iterate Pixels**: Iterate through each pixel of each yellow object.
3.  **Find Nearest Green:** For each yellow pixel, search for the nearest green pixel. "Nearest" is defined by the minimum number of moves (up, down, left, or right) required to reach a position that is adjacent to a green pixel without crossing other objects.
4. **Move Yellow Pixels:** Move each yellow pixel to an available adjacent cell of the _nearest_ green pixel, if a position is free (value is 0).
5. **Preserve:** Keep the relative shape of yellow objects intact as much as possible, moving individual pixels rather than entire objects at once.
6.  **Obstacles:** Azure (8) pixels, red (2) pixels, and other yellow pixels act as obstacles - do not move through them.


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
