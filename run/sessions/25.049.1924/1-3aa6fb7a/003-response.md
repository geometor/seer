# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example of transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three separate azure objects"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three separate azure objects"
    - color: 1
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "three isolated pixels"
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify three distinct objects of color `8` (azure). One L-shaped object at the top right, composed by cells (0,4), (0,5) and (1,5). A second L-Shaped object in the center-left composed by cells (2,2), (3,2) and (3,3). The last one at the bottom, composed by cells (5,4), (6,3) and (6,4).

2.  **Detect Changes:** The azure objects remain unchanged between the input and output. In the output we can observe three new blue pixels (color code 1).

3.  **Describe New Objects:**
 *    The first new pixel in the output is at the position (1,4) of the original top-right shape centroid.
 *    The second new pixel in the output is at the position (2,3) the original center-left shape centroid.
 *    The third new pixel is at position (5,3) the original bottom shape centroid.

4. **Transformation rule**: For each azure object, compute the centroid and change the value of this cell to `1` (blue).

**Step-by-step transformation**
1. Find each isolated azure object.
2. For each of them: Paint with blue the cell corresponding to their centroid.

The transformation rule and the python program stay the same.
```python
"""
Transformation Rule:

1.  **Identify Objects:** Find all distinct azure (color code 8) objects in the input grid.
2.  **Calculate Centroids:** For each identified azure object, calculate its centroid.
3.  **Paint Centroids:** Change the color of the cells corresponding to the calculated centroids to blue (color code 1).
"""

import numpy as np
from scipy.ndimage import measurements

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates for each object found.
    """
    mask = (grid == color).astype(int)
    labeled_array, num_features = measurements.label(mask)
    objects = []
    for i in range(1, num_features + 1):
        coords = np.array(np.where(labeled_array == i)).T
        objects.append(coords)
    return objects

def calculate_centroid(coords):
    """
    Calculates the centroid of a set of coordinates.
    """
    return np.mean(coords, axis=0).astype(int)

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Calculate the centroid for each azure object and paint it blue
    for obj_coords in azure_objects:
        centroid = calculate_centroid(obj_coords)
        output_grid[centroid[0], centroid[1]] = 1  # Paint the centroid blue

    return output_grid
```

