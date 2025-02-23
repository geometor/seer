# 1-3aa6fb7a • 004 • Response

---

*text:*

```python
"""
The transformation rule is as follows:
1. Copy all azure (color 8) pixels from the input grid to the output grid without changing their positions.
2. For each 3-pixel 'L' shape formed by the azure pixels, insert a blue (color 1) pixel in the corner of the "L".
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def detect_l_shape(object_coords):
    """Detects if a set of coordinates forms an L shape."""
    if len(object_coords) != 3:
        return None

    # Convert to numpy array for easier calculations
    coords = np.array(object_coords)
    
    # Calculate distances between all pairs of points
    dist_matrix = np.sum((coords[:, np.newaxis, :] - coords[np.newaxis, :, :]) ** 2, axis=2)
    
    # Check for two distances of 1 and one distance of 2 (squared distances)
    distances = sorted(dist_matrix[np.triu_indices(3, 1)])

    if distances == [1, 1, 2]:       
        # Find the corner point (the point with distances 1 to both other points)
        for i in range(3):
            if dist_matrix[i, (i+1)%3] == 1 and dist_matrix[i, (i+2)%3] == 1:
                
                corner_index=i
                #find elbow
                other_indices = [(j % 3) for j in range(i + 1, i + 3)]

                elbow_row = object_coords[other_indices[0]][0] + object_coords[other_indices[1]][0] - object_coords[corner_index][0]
                elbow_col = object_coords[other_indices[0]][1] + object_coords[other_indices[1]][1] - object_coords[corner_index][1]



                return (elbow_row, elbow_col)

    return None


def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through objects and check for L-shapes
    for obj in azure_objects:
        l_corner = detect_l_shape(obj)
        if l_corner:
            output_grid[l_corner] = 1

    return output_grid
```

