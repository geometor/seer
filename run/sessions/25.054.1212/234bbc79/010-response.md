# 234bbc79 • 010 • refine_coder

---
```python
"""
1.  **Identify Objects:** Recognize contiguous blocks of pixels of the same color as distinct objects.

2.  **Color and Shape Transformations:**
    *   Grey (5) objects are replaced with smaller objects of color Blue (1). The new small object appears nearby.
    *   Blue(1) objects might be removed, they could become white(0), or they could be reduced in size. It looks like the transformation of blue objects might depend on their positions in the grid.
    *   If an object with color 8 is nearby an object with color 6, combine these objects using color 6 for all pixels.
    *   Red(2) objects may remain the same or they could be moved.
    *   Green(3) objects remain unchanged.

3.  **Output Size**: The height and width of the output are the sizes of the largest contiguous sections of non-zero pixels.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous blocks of the same color in a grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, object_pixels):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        object_pixels.append((row, col))
        dfs(row + 1, col, color, object_pixels)
        dfs(row - 1, col, color, object_pixels)
        dfs(row, col + 1, color, object_pixels)
        dfs(row, col - 1, color, object_pixels)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                color = grid[row, col]
                object_pixels = []
                dfs(row, col, color, object_pixels)
                if object_pixels:
                    objects.append({'color': color, 'pixels': object_pixels})
    return objects

def get_bounding_box(pixels):
    """
    Calculates the bounding box of a set of pixels.
    """
    if not pixels:
        return None
    rows, cols = zip(*pixels)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    return (min_row, min_col, max_row, max_col)

def is_nearby(obj1_pixels, obj2_pixels, threshold=2):
    """
    Checks if two objects are nearby based on their pixel coordinates.
    Using a simple distance check between bounding box edges.
    """
    if not obj1_pixels or not obj2_pixels:
        return False
    
    box1 = get_bounding_box(obj1_pixels)
    box2 = get_bounding_box(obj2_pixels)
    
    dist_row = max(0, max(box1[0], box2[0]) - min(box1[2], box2[2]))
    dist_col = max(0, max(box1[1], box2[1]) - min(box1[3], box2[3]))

    return dist_row <= threshold and dist_col <= threshold

def get_output_grid_size(objects):
    """
    Determine the size of the output grid. Finds max dimensions.
    """

    max_row = 0
    max_col = 0

    for obj in objects:
       for row, col in obj['pixels']:
          if row > max_row:
             max_row = row
          if col > max_col:
             max_col = col
    
    return max_row+1, max_col+1
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Get objects from input_grid
    objects = get_objects(input_grid)

    # Create a list to store transformed objects
    transformed_objects = []

    # change output pixels 
    for obj in objects:
        if obj['color'] == 5:  # Grey to Blue, smaller, nearby
            new_pixels = [(row, col) for row, col in obj['pixels']] #copy
            if len(new_pixels) > 2:
                new_pixels = new_pixels[:len(new_pixels) // 2 ] #shrink
            
            transformed_objects.append({'color': 1, 'pixels': new_pixels})
           
        elif obj['color'] == 1:  # Blue to white, or disappear
            # check position - look at the first and last positions
            new_pixels = []

            # add to transformed objects
            transformed_objects.append({'color':0, 'pixels':new_pixels})

        elif obj['color'] == 8: # 8 and 6 combine
            #look for 6
            for other_obj in objects:
                if other_obj['color'] == 6 and is_nearby(obj['pixels'], other_obj['pixels']):
                    #combine the pixels
                    combined_pixels = list(set(obj['pixels'] + other_obj['pixels']))
                    transformed_objects.append({'color': 6, 'pixels': combined_pixels})
                    break #only combine once
            else:
               transformed_objects.append(obj)

        elif obj['color'] == 2:
            #just keep the object, the prediction does not work
            transformed_objects.append(obj)

        elif obj['color'] == 3: # keep green
            transformed_objects.append(obj)
        elif obj['color'] == 6: # keep 6 since they were handled with 8
            # check if this 6 was already combined
            already_combined = False
            for tobj in transformed_objects:
               if tobj['color'] == 6:
                  already_combined = True
                  break

            if not already_combined:
               transformed_objects.append(obj)
        else:
            transformed_objects.append(obj) # copy any other object

    # set the output size
    rows, cols = get_output_grid_size(transformed_objects)
    output_grid = np.zeros((rows, cols), dtype=int)
    
    # place transformed objects into output
    for obj in transformed_objects:
        for row, col in obj['pixels']:
            if row < rows and col < cols:
                output_grid[row, col] = obj['color']

    return output_grid
```
