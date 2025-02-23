"""
Transforms an input grid by expanding colored blocks horizontally and vertically.  Each colored block is duplicated a number of times corresponding to the number of pixels in that color.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous blocks of non-zero pixels in the grid.
    Returns a dictionary of objects, keyed by color, with their bounding box coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, coords):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        coords.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, color, coords)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                coords = []
                dfs(r, c, grid[r, c], coords)
                if grid[r,c] not in objects:
                    objects[grid[r,c]] = []

                objects[grid[r,c]].append(coords)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the expansion rules.
    """
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape
    objects = get_objects(input_grid)

    # print(objects)

    # Find objects by color
    red_coords_list = objects.get(2, [])
    green_coords_list = objects.get(3, [])
    azure_coords_list = objects.get(8,[])
    yellow_coords_list = objects.get(4,[])

    
    # iterate through all red coords
    for red_coords in red_coords_list:
        # Number of copies of pixels
        red_count = len(red_coords)
        # iterate through all coordinates of red object
        for i in range(len(red_coords)):
            # get coordinates of red pixel
            rx,ry = red_coords[i]
            # change output pixels to red color
            for j in range(red_count):
                output_grid[rx+j][ry]=2
        
        # iterate through azure pixels
        for azure_coords in azure_coords_list:
            # Number of copies of pixels
            azure_count = len(azure_coords)
            ax,ay = azure_coords[0]   
            # if the azure color is connected to red then expand that color
            if (rx == ax) and (ry+1==ay):
                for i in range(len(red_coords)):
                    rx,ry = red_coords[i]
                    for j in range(azure_count):
                        output_grid[rx+j][ry+azure_count]=8


    for green_coords in green_coords_list:
        green_count = len(green_coords)
        for i in range(len(green_coords)):
            gx,gy = green_coords[i]
            for j in range(green_count):
                output_grid[gx+j][gy]=3
        
        for yellow_coords in yellow_coords_list:
            # Number of copies of pixels
            yellow_count = len(yellow_coords)
            yx,yy = yellow_coords[0]   
            # if the azure color is connected to red then expand that color
            if (gx == yx) and (gy-1==yy):
                for i in range(len(green_coords)):
                    gx,gy = green_coords[i]
                    for j in range(yellow_count):
                        output_grid[gx+j][gy-yellow_count]=4
        
    return output_grid