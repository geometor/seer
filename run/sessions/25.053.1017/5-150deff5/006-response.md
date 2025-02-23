# 5-150deff5 • 006 • example_3 - CODE

---
```python
"""
1.  **Identify the Foreground Object:** Locate the contiguous block of pixels that are not the background color (0). In this case, it's the gray (5) shape.
2.  **Decompose the Object:** Divide the foreground object into two distinct sub-objects. The division appears to be based on runs along the rows. The first two '5' pixels encountered on row 2 will be the starting elements of a breadth-first search. Pixels that are adjacent (not diagonal) to these pixels will be included in sub-shape_1.
3. **Recolor sub-shapes:** sub-shape_1 receives color red (2).
4.  **Remaining Pixels:** The pixels from the original shape that are not assigned to sub-shape_1 are assigned to sub-shape_2.
5. **Recolor sub-shapes:** sub-shape_2 receives color azure (8).
6.  **Output:** Create an output grid of the same dimensions as the input, with the background color (0) everywhere except for the locations of sub-shape_1 and sub-shape_2, colored as defined.
"""

import numpy as np

def get_object(grid, background_color):
    # returns a set of (row, col) tuples representing the object
    object_pixels = set()
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != background_color:
                object_pixels.add((r, c))
    return object_pixels

def breadth_first_search(grid, start_pixels, object_pixels):
    # performs a breadth-first search to find connected pixels
    visited = set()
    queue = list(start_pixels)  # convert set to list

    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited or (r, c) not in object_pixels:
            continue
        visited.add((r, c))

        # Add adjacent neighbors (not diagonal)
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                queue.append((nr, nc))
    return visited

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    background_color = 0
    foreground_color = 5
    sub_shape_1_color = 2
    sub_shape_2_color = 8

    # get the foreground object
    object_pixels = get_object(input_grid, background_color)

    # find start pixels for sub-shape 1 (first two foreground pixels on row 2)
    start_pixels = set()
    for r in range(input_grid.shape[0]):
        found_count = 0
        for c in range(input_grid.shape[1]):
           if input_grid[r,c] == foreground_color:
              start_pixels.add((r,c))
              found_count += 1
              if found_count == 2:
                break
        if found_count == 2:
            break
    
    # decompose the object using BFS
    sub_shape_1 = breadth_first_search(input_grid, start_pixels, object_pixels)
    sub_shape_2 = object_pixels - sub_shape_1

    # fill output grid with sub-shape 1
    for r, c in sub_shape_1:
        output_grid[r, c] = sub_shape_1_color
    
    # fill output grid with sub-shape 2
    for r, c in sub_shape_2:
        output_grid[r, c] = sub_shape_2_color
    
    return output_grid
```
