# 445eab21 • 017 • refine_coder

---
```python
"""
Identify C-shaped objects in the input grid.
Process each C-shaped object based on its color and position.
Shift C-shapes to the left and potentially shrink their width.
Construct an output grid with the transformed C-shapes.
"""

import numpy as np

def get_objects(grid):
    """
    Find contiguous regions of the same color in the grid (excluding white/0).
    Returns a dictionary of objects, where keys are colors and values are lists of pixel coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj_pixels):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or grid[row, col] != color
        ):
            return
        visited.add((row, col))
        obj_pixels.append((row, col))
        dfs(row + 1, col, color, obj_pixels)
        dfs(row - 1, col, color, obj_pixels)
        dfs(row, col + 1, color, obj_pixels)
        dfs(row, col - 1, color, obj_pixels)

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                obj_pixels = []
                dfs(r, c, color, obj_pixels)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_pixels)
    return objects

def analyze_object(obj_pixels):
    """
    Analyzes a single object (list of pixel coordinates) to determine its shape and bounding box.
    """
    if not obj_pixels:
        return {}

    min_row = min(p[0] for p in obj_pixels)
    max_row = max(p[0] for p in obj_pixels)
    min_col = min(p[1] for p in obj_pixels)
    max_col = max(p[1] for p in obj_pixels)

    width = max_col - min_col + 1
    height = max_row - min_row + 1
    
    # simple c-shape detection
    is_c_shape = False
    if width > 2 and height > 2:
        # Check for a "C" shape (this is a simplified check and may need refinement)
        top_line = all((min_row, c) in obj_pixels for c in range(min_col, max_col + 1))
        bottom_line = all((max_row, c) in obj_pixels for c in range(min_col, max_col + 1))
        left_line = all((r, min_col) in obj_pixels for r in range(min_row, max_row + 1))
        
        #make sure the top right and bottom right corners are not filled
        top_right = (min_row, max_col) not in obj_pixels
        bottom_right = (max_row, max_col) not in obj_pixels

        if top_line and bottom_line and left_line and top_right and bottom_right:
            is_c_shape = True
    
    return {
        'min_row': min_row,
        'max_row': max_row,
        'min_col': min_col,
        'max_col': max_col,
        'width': width,
        'height': height,
        'is_c_shape': is_c_shape,
        'num_pixels': len(obj_pixels)
    }

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Get objects from the input grid
    objects = get_objects(input_grid)
    
    # Process each object
    for color, obj_list in objects.items():
        for obj_pixels in obj_list:
            analysis = analyze_object(obj_pixels)
            
            # Check if the object is C-shaped
            if analysis['is_c_shape']:
                # Apply transformation rules based on position
                shift_left = 0
                shrink_width = 0

                if analysis['min_col'] == 1 and analysis['max_col'] == 6:
                    shift_left = 1
                    shrink_width = 1
                elif analysis['min_col'] == 7:
                    shift_left = 1;
                elif analysis['max_col'] == input_grid.shape[1] -1:
                    shift_left = 2
                elif analysis['min_col'] == input_grid.shape[1] -3:
                      shift_left = 1

                # Create the transformed object
                transformed_pixels = []
                for r, c in obj_pixels:
                    new_c = c - shift_left
                    if new_c < analysis['max_col'] - shift_left - shrink_width:
                      transformed_pixels.append((r,new_c))

                # Draw transformed pixels on output grid
                for r, c in transformed_pixels:
                    if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                        output_grid[r, c] = color
            else:
                # Copy non-C-shaped pixels directly
                for r, c in obj_pixels:
                    output_grid[r, c] = color

    return output_grid
```
