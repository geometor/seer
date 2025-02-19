"""
The input azure pixels are ordered by the sum of coordinates x+y. The first two azure pixels with minimal x+y sum and the last azure pixel with maximal x+y sum are chosen.
The blue pixel (color 1) is placed by moving +1 on the y-axis for the first two chosen azure pixels and by moving -1 on the x-axis of the last chosen azure pixel.
"""

import numpy as np

def find_azure_objects(grid):
    # Find coordinates of all azure (8) pixels.
    azure_coords = np.argwhere(grid == 8)
    return azure_coords

def find_top_leftmost_n(coords, n):
    # Sort by x+y
    coords_sum = coords[:,0] + coords[:,1]
    coords_sort_idx = np.argsort(coords_sum)
    coords = coords[coords_sort_idx]
    coords_sum = coords_sum[coords_sort_idx]

    result = []
    for i in range(len(coords)):
        if len(result) >= n and coords_sum[i] > coords_sum[result[-1][0]] :
            break
        
        
        is_new = True
        for j,_ in result:
            if coords[i,0] == coords[j,0] and coords[i,1] == coords[j,1]:
                is_new = False
                break
        if is_new:
            result.append((i, coords[i]))

    
    return [x[1] for x in result[:n]]
    

def find_bottom_rightmost(coords):
      # Sort by x+y
    coords_sum = coords[:,0] + coords[:,1]
    coords_sort_idx = np.argsort(coords_sum)
    coords = coords[coords_sort_idx]
    return coords[-1]
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find all azure objects.
    azure_coords = find_azure_objects(input_grid)

    if len(azure_coords) >=2:
        # Find the top-leftmost and bottom-rightmost azure pixels.
        top_leftmost_list = find_top_leftmost_n(azure_coords, 2)
        
        bottom_rightmost = find_bottom_rightmost(azure_coords)

        # Create blue pixels based on the top-leftmost and bottom-rightmost azure pixels.
        for top_leftmost in top_leftmost_list:
            output_grid[top_leftmost[0] + 1, top_leftmost[1]] = 1  # +1 on the y-axis

        output_grid[bottom_rightmost[0] - 1, bottom_rightmost[1]] = 1

    return output_grid