"""
Identify the largest contiguous shape in the input grid. This shape can be of any color. The identified shape remains unchanged.
The pixels on the border of this central shape are updated based on the output grid. If a border pixel has the same color in both input and output,
it remains unchanged. Otherwise, the border pixel's color is updated to its color in the output grid.
"""

import numpy as np
from collections import Counter

def find_largest_shape(grid):
    # Initialize variables to track the largest shape
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    max_shape_coords = []
    max_shape_color = -1

    # Depth-first search to find contiguous shapes
    def dfs(row, col, color, shape_coords):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        shape_coords.append((row, col))
        dfs(row + 1, col, color, shape_coords)
        dfs(row - 1, col, color, shape_coords)
        dfs(row, col + 1, color, shape_coords)
        dfs(row, col - 1, color, shape_coords)
        dfs(row + 1, col + 1, color, shape_coords)
        dfs(row + 1, col-1, color, shape_coords)
        dfs(row -1, col + 1, color, shape_coords)
        dfs(row - 1, col -1, color, shape_coords)
    # Iterate through all pixels to find shapes
    for i in range(rows):
        for j in range(cols):
            if not visited[i, j]:
                current_shape_coords = []
                current_color = grid[i, j]
                dfs(i, j, current_color, current_shape_coords)
                if len(current_shape_coords) > len(max_shape_coords):
                    max_shape_coords = current_shape_coords
                    max_shape_color = current_color

    return max_shape_coords, max_shape_color

def find_border_pixels(grid, shape_pixels):
    border_pixels = set()
    rows, cols = grid.shape
    shape_color = grid[shape_pixels[0][0], shape_pixels[0][1]] #get color from the shape pixels
    
    # Directions to check for neighbors (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for r, c in shape_pixels:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != shape_color:
                border_pixels.add((nr, nc))

    return list(border_pixels)

def transform(input_grid, output_grid):
    # Create a copy of the input grid to modify
    output_grid_copy = np.copy(input_grid)

    # Find the central largest shape
    shape_pixels, _ = find_largest_shape(input_grid)

    # Find pixels on border of shape
    border_pixels = find_border_pixels(input_grid, shape_pixels)

    # Modify colors other than yellow at border
    for r, c in border_pixels:
        #if the colors in the input and the given output grids are the same
        if input_grid[r,c] == output_grid[r,c]:
            #keep colors
            output_grid_copy[r,c] = input_grid[r,c]
        else:
            #update border color to the color in the output_grid
            output_grid_copy[r, c] = output_grid[r,c]

    return output_grid_copy