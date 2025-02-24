# be94b721 • 006 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all contiguous regions of non-white pixels in the input grid. Each of these is an "object."

2.  **Select Target Object:**
    *   Examine the objects in the grid, looking for non-edge objects (those not touching the edges of the input grid.)
    *   If there are non-edge objects, select the object with color '2'.  If there are no non-edge objects *OR* there are no non-edge objects with color 2, then select the *largest* object from the remaining objects.

3.  **Isolate:** Keep only the pixels of the target object.

4.  **Compress:** Remove all rows and columns that contain *only* white pixels (value '0'), resulting in the smallest possible grid containing the target object. This compressed grid is the output.
"""

import numpy as np
from scipy.ndimage import label

def find_objects(grid):
    """
    Finds contiguous regions of non-white pixels and returns their coordinates and colors.
    """
    labeled_grid, num_objects = label(grid != 0)
    objects = []
    for i in range(1, num_objects + 1):  # Label 0 is background
        coords = np.argwhere(labeled_grid == i)
        if len(coords) > 0:
            color = grid[coords[0][0], coords[0][1]] #get color of first pixel
            objects.append((coords, color))
    return objects

def is_edge_object(grid, object_coords):
    """
    Checks if an object is adjacent to the edge of the grid.
    """
    rows = object_coords[:, 0]
    cols = object_coords[:, 1]
    return np.min(rows) == 0 or np.max(rows) == grid.shape[0] - 1 or \
           np.min(cols) == 0 or np.max(cols) == grid.shape[1] - 1

def get_object_size(object_coords):
    """Calculates the number of pixels in the object"""
    return len(object_coords)

def compress_object(grid, object_coords):
    """
    Compresses the grid to the bounding box of the object.
    """
    if len(object_coords) == 0:
        return np.zeros((0,0), dtype=int)

    min_row = np.min(object_coords[:, 0])
    max_row = np.max(object_coords[:, 0])
    min_col = np.min(object_coords[:, 1])
    max_col = np.max(object_coords[:, 1])

    cropped_grid = grid[min_row:max_row + 1, min_col:max_col + 1]
    return cropped_grid

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)

    # 1. Identify Objects
    objects = find_objects(input_grid)

    # 2. Select Target Object
    non_edge_objects = [(coords, color) for coords, color in objects if not is_edge_object(input_grid, coords)]
    target_object_coords = None
    target_color = None

    # Prioritize non-edge objects with color 2
    for coords, color in non_edge_objects:
        if color == 2:
            target_object_coords = coords
            target_color = color
            break

    # If no non-edge object with color 2 is found, select the largest object
    if target_object_coords is None:
        if len(objects) > 0: #select largest
            largest_object_size = -1
            for coords, color in objects:
                object_size = get_object_size(coords)
                if object_size > largest_object_size:
                    largest_object_size = object_size
                    target_object_coords = coords
                    target_color = color
        else:
          return np.zeros((0, 0), dtype=int).tolist() #no objects


    # 3. Isolate (implicitly done by selecting coordinates) and 4. Compress
    output_grid = compress_object(input_grid, target_object_coords)

    return output_grid.tolist()
```
