# 6150a2bd • 006 • refine_coder

---
```python
"""
The input grid is rotated 90 degrees counter-clockwise. Individual connected components of the same color (single pixels or groups) are treated as distinct objects. These objects maintain their shape and internal arrangement of pixels, and their positions within the grid are updated based on the 90-degree counter-clockwise rotation of the entire grid, relative to the center of the grid.
"""

import numpy as np
from scipy.ndimage import label

def get_objects(grid):
    """
    Identifies and returns a list of objects within the grid.  Each object
    is represented as a dictionary containing its color and a list of
    its pixel coordinates.
    """
    grid_np = np.array(grid)
    labeled_grid, num_objects = label(grid_np)
    objects = []
    for i in range(1, num_objects + 1):
        positions = np.argwhere(labeled_grid == i)
        color = grid_np[positions[0][0], positions[0][1]]
        objects.append({
            'color': color,
            'positions': positions.tolist()
        })
    return objects

def rotate_point(point, center, angle_degrees):
    """Rotates a single point around a center point by a given angle."""
    angle_radians = np.radians(angle_degrees)
    x, y = point
    cx, cy = center
    rotated_x = cx + (x - cx) * np.cos(angle_radians) - (y - cy) * np.sin(angle_radians)
    rotated_y = cy + (x - cx) * np.sin(angle_radians) + (y - cy) * np.cos(angle_radians)
    return [int(round(rotated_x)), int(round(rotated_y))]

def transform(input_grid):
    """
    Transforms the input grid according to the defined rule.
    """
    # 1. Identify objects in the input grid.
    objects = get_objects(input_grid)

    # 2. Determine the dimensions of the input grid and its center.
    rows = len(input_grid)
    cols = len(input_grid[0])
    center = (cols / 2.0 - 0.5, rows / 2.0 - 0.5)  # Center for rotation (note the swap for correct rotation)

    # 3. Create an empty output grid of the rotated dimensions.
    output_grid = [[0] * rows for _ in range(cols)]  # Rotated dimensions

    # 4. Iterate through each object and its positions.
    for obj in objects:
        for pos in obj['positions']:
            # 5. Rotate each pixel position around the grid's center.
            #    The y and x coordinates are swapped in the 'center' calculation,
            #    and the rotation angle is -90 for counter-clockwise.
            rotated_pos = rotate_point([pos[1], pos[0]], center, -90) # Corrected: Swap x and y for rotation
            
            # 6. Place the object's color in the new, rotated positions.
            #   Check bounds for the output grid.
            if 0 <= rotated_pos[0] < cols and 0 <= rotated_pos[1] < rows:
                output_grid[rotated_pos[0]][rotated_pos[1]] = obj['color']

    return output_grid
```
