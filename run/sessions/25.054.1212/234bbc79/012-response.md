# 234bbc79 • 012 • refine_coder

---
```python
"""
1.  **Object Identification:** Identify contiguous regions of the same color as distinct objects.

2.  **Grey Object Transformation:** Grey (5) objects are replaced with smaller Blue (1) objects. The size of the new blue object is approximately half the original grey object's size (rounded down). The new object appears in a location that was occupied by the grey object.

3.  **Blue Object Transformation:** Blue(1) objects may be reduced in size. If they become smaller, the new location is one occupied by the original.

4.  **Azure and Magenta Object Combination:** If an Azure (8) object and a Magenta (6) object are "nearby" (adjacent horizontally or vertically, or overlapping), combine them into a single object with the color Magenta (6).

5.  **Red and Green Object Preservation:** Red (2) and Green (3) objects retain their color.

6. **Object Movement:** Red(2) objects may change their positions.

7.  **Output Grid Sizing:** The output grid size is determined by finding the smallest rectangle that contains all non-zero pixels after the above transformations.
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

def is_nearby(obj1_pixels, obj2_pixels):
    """
    Checks if two objects are nearby (adjacent or overlapping).
    """
    if not obj1_pixels or not obj2_pixels:
        return False

    box1 = get_bounding_box(obj1_pixels)
    box2 = get_bounding_box(obj2_pixels)

    # Check for overlap
    if (box1[0] <= box2[2] and box1[2] >= box2[0] and
        box1[1] <= box2[3] and box1[3] >= box2[1]):
        return True

    # Check for adjacency
    if (abs(box1[0] - box2[2]) <= 1 and abs(box1[1] - box2[1]) <=1 ) or \
            (abs(box1[2] - box2[0]) <=1 and abs(box1[3] - box2[1]) <= 1)  or \
            (abs(box1[2] - box2[0]) <= 1 and abs(box1[1] - box2[3]) <= 1 ) or \
            (abs(box1[0] - box2[2]) <=1 and abs(box1[3] - box2[1]) <=1):
        return True

    return False

def calculate_output_size(transformed_objects):
    """Calculates the output size based on non-zero pixels."""
    if not transformed_objects:
        return 0, 0

    all_pixels = []
    for obj in transformed_objects:
        all_pixels.extend(obj['pixels'])

    if not all_pixels:
        return 0,0
    
    rows, cols = zip(*all_pixels)
    return max(rows) + 1, max(cols) + 1

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
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
           
        elif obj['color'] == 1:  # Blue - reduce
            # check position - look at the first and last positions
            new_pixels = [(row, col) for row, col in obj['pixels']]
            if len(new_pixels) > 2:
                new_pixels = new_pixels[:len(new_pixels) // 2 ]

            # add to transformed objects
            transformed_objects.append({'color':1, 'pixels':new_pixels})

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
    rows, cols = calculate_output_size(transformed_objects)
    output_grid = np.zeros((rows, cols), dtype=int)
    
    # place transformed objects into output
    for obj in transformed_objects:
        for row, col in obj['pixels']:
            if row < rows and col < cols:
                output_grid[row, col] = obj['color']

    return output_grid
```

