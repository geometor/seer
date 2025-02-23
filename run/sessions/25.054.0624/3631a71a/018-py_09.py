"""
The transformation identifies and removes "noisy" objects based on size and
replaces them with a padding of the most common background color.
The objects are then filled back based on rules that apply to object size, shape, and color
and context, based on the comparison with the original input.
Single pixel object are handled differently, based on their context.
"""

import numpy as np
from collections import Counter

def get_objects(grid):
    """Identifies connected components (objects) in the grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] == 0:
            return
        visited.add((row, col))
        current_object.append(((row, col), grid[row, col]))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] != 0 and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects


def get_background_color(grid):
    """
    Determines the most common color on the edges of the grid.
    """
    rows, cols = grid.shape
    edge_pixels = []
    edge_pixels.extend(grid[0, :].tolist())  # Top row
    edge_pixels.extend(grid[rows - 1, :].tolist())  # Bottom row
    edge_pixels.extend(grid[:, 0].tolist())  # Left column
    edge_pixels.extend(grid[:, cols - 1].tolist())  # Right column
    
    color_counts = Counter(edge_pixels)
    
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color

def get_object_bounding_box(obj):
    """Calculates the bounding box of an object."""
    coords, _ = zip(*obj)
    coords_array = np.array(coords)
    rows_obj = coords_array[:, 0]
    cols_obj = coords_array[:, 1]
    min_row, max_row = np.min(rows_obj), np.max(rows_obj)
    min_col, max_col = np.min(cols_obj), np.max(cols_obj)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    """Transforms the input grid by removing and reconstructing objects."""
    
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid) # initialize to all zeros
    background_color = get_background_color(input_grid)
    output_grid[:] = background_color  # Fill with background

    # Get objects from the original grid
    original_objects = get_objects(input_grid)
    
    # Initial filtering: Keep large and medium structured objects.
    for obj in original_objects:
        coords, color = zip(*obj)
        min_row, max_row, min_col, max_col = get_object_bounding_box(obj)

        width = max_col - min_col + 1
        height = max_row - min_row + 1
        size = len(obj)

        if size >= 9: # large objects
            if height > 2 and width > 2: # Check for structured shape (not just a line)
                for (r, c), val in obj:
                    output_grid[r, c] = val
            
        elif size >= 3 and size <= 8: # medium-sized objects
            if height > 1 and width > 1:  # structured object
                for (r, c), val in obj:
                    output_grid[r, c] = val
            
    # Single pixel objects
    
    temp_grid = output_grid.copy()
    
    for obj in original_objects:
      if len(obj) == 1:  # single pixel
        ((r,c),val) = obj[0]
        
        # Check neighbors in original grid
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr, dc) != (0, 0):  # Exclude the pixel itself
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbors.append(input_grid[nr, nc])
        
        neighbor_counts = Counter(neighbors)
        most_common_neighbor = neighbor_counts.most_common(1)[0][0] if neighbor_counts else background_color # if empty use background
        if (most_common_neighbor != background_color and most_common_neighbor != 0):
          # Check if the object is a part of larger solid object
            temp_grid[r,c] = val
    
    output_grid = temp_grid

    return output_grid