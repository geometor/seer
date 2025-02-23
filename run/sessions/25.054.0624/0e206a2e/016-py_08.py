"""
1.  **Identify Objects:** Find all azure (8) pixels, forming the "azure cluster."  Also, find all isolated blue (1) and red (2) pixels. Identify the yellow (4) pixel near the *original* position of the azure cluster.
2. **Determine Relative Shift:** Calculate the relative positional change of the azure cluster using the following approach:
    *  Find the relative vector from the centroid of the azure cluster to the average position of the blue and red pixels.
3.  **Move Azure Cluster:** Recreate the azure cluster. For each azure pixel in the original position, add the relative vector calculated in the previous step to place the azure cluster.
4.  **Preserve Other Colors:** Keep all other colors (besides azure and the deleted yellow) in their original positions.
5.  **Delete Yellow:** Remove the yellow (4) pixel that was adjacent to *any* of the original azure cluster pixels.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color)

def calculate_centroid(pixels):
    """Calculates the centroid of a set of pixels."""
    if len(pixels) == 0:
        return np.array([0, 0])
    return np.mean(pixels, axis=0)

def find_adjacent_pixels(grid, pixels):
    """finds adjacent pixels of a given color"""
    adjacent_pixels = set()
    for r, c in pixels:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                    adjacent_pixels.add((nr, nc))
    return adjacent_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure pixels.
    azure_pixels = find_pixels_by_color(input_grid, 8)
    
    # Find blue and red pixels
    blue_pixels = find_pixels_by_color(input_grid, 1)
    red_pixels = find_pixels_by_color(input_grid, 2)

    # Calculate centroid of azure cluster.
    azure_centroid = calculate_centroid(azure_pixels)

    # Calculate average position of blue and red pixels.
    blue_red_avg_pos = calculate_centroid(np.concatenate((blue_pixels, red_pixels)))


    # Determine relative shift
    if len(azure_pixels) >0:
       relative_shift = blue_red_avg_pos - azure_centroid
    else:
       relative_shift = np.array([0,0])

    # Move azure pixels.
    new_azure_pixels = []
    for r, c in azure_pixels:
        output_grid[r, c] = 0  # Remove original azure pixel
        new_r, new_c = r + relative_shift[0], c + relative_shift[1]
        new_r = int(round(new_r)) #convert to int
        new_c = int(round(new_c))

        if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
            new_azure_pixels.append( (new_r,new_c) )
            output_grid[new_r, new_c] = 8  # Place new azure pixel


    #find yellow to delete
    adjacent_to_azure = find_adjacent_pixels(input_grid, azure_pixels)
    for r, c in adjacent_to_azure:
       if output_grid[r,c] == 4:
          output_grid[r,c] = 0 #delete yellow

    return output_grid