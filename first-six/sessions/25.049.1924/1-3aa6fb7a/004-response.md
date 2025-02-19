# 1-3aa6fb7a • 004 • example_2 - CODE

---
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

