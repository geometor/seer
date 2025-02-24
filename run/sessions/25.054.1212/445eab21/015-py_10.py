import numpy as np
#from utils import code_execution

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
    
input_grids = [
    np.array([
        [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]),
    np.array([
        [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
        [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]),
    np.array([
        [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2]
    ])
]

example_results = []
for i, grid in enumerate(input_grids):
    objects = get_objects(grid)
    example_result = {'example': i+1, 'objects': []}
    for color, obj_list in objects.items():
        for obj_pixels in obj_list:
            analysis = analyze_object(obj_pixels)
            example_result['objects'].append({
                'color': color,
                'analysis': analysis
            })
    example_results.append(example_result)
    
for result in example_results:
    print(result)