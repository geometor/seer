# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
1. Identify all non-zero pixels (objects) in the input grid.
2. Move all objects to the last two rows.
3. The blue pixel (1) remains in its original column (index 0).
4. The two yellow pixels (4) are stacked - one in row index 2, the other directly below in row index 3.
5. The remaining pixels, magenta (6) and maroon (9), shift to the bottom row and maintain their original column position relative to each other.
"""

import numpy as np

def get_objects(grid):
    objects = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0:
                objects.append({"value": grid[r, c], "row": r, "col": c})
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # get objects
    objects = get_objects(input_grid)

    # sort by rules
    yellow_objects = [obj for obj in objects if obj["value"] == 4]
    other_objects = [obj for obj in objects if obj["value"] != 4]
    blue_object = [obj for obj in other_objects if obj["value"] == 1]
    other_objects = [obj for obj in other_objects if obj["value"] != 1]


    # handle blue object
    if blue_object:
        output_grid[3, 0] = 1

    # handle yellow object

    if len(yellow_objects) > 0:
        output_grid[2,1] = 4

    if len(yellow_objects) > 1:
        output_grid[3, 1] = 4


    # handle remaining
    other_objects.sort(key=lambda x: x["col"])
    row_index = 3
    for obj in other_objects:
        output_grid[row_index, obj["col"]] = obj["value"]

    return output_grid
```
