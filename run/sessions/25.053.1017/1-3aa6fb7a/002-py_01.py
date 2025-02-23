"""
1.  **Identify Objects:** Locate all contiguous blocks of azure (8) pixels within the grid. These form the primary objects.
2.  **Select Target Pixel:** Within each object, find the azure pixel, either on the second row or second to last row
3.  **Modify Pixel:** Change the color value of the selected pixel from azure (8) to blue (1).
4.  **Output:** The output grid is identical to the input grid except for the single modified pixel.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous blocks of the specified color
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8 (azure)
    azure_objects = find_objects(output_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Find the top and bottom rows of the object
        rows = [pixel[0] for pixel in obj]
        top_row = min(rows)
        bottom_row = max(rows)

        #select pixels on the second or second to last row
        target_pixels = []
        
        for pixel in obj:
            if pixel[0] == top_row + 1 or pixel[0] == bottom_row - 1:
                target_pixels.append(pixel)

        #choose the first target pixel and change it
        if (len(target_pixels) > 0):
            target_row, target_col = target_pixels[0]
            output_grid[target_row, target_col] = 1

    return output_grid