"""
Identify and remove a contiguous region of white (0) pixels in the input grid, 
effectively isolating a repeating border pattern.
"""

import numpy as np

def find_contiguous_region(grid, start_row, start_col, color):
    """
    Finds a contiguous region of a given color starting from a given point.
    Uses a breadth-first search (BFS) algorithm.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    queue = [(start_row, start_col)]
    visited[start_row, start_col] = True
    region = []

    while queue:
        row, col = queue.pop(0)
        region.append((row, col))

        # Check neighbors (up, down, left, right)
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < rows - 1:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < cols - 1:
            neighbors.append((row, col + 1))
        

        for n_row, n_col in neighbors:
            if not visited[n_row, n_col] and grid[n_row, n_col] == color:
                visited[n_row, n_col] = True
                queue.append((n_row, n_col))

    return region

def get_pattern_element(row, col, sequence):
  """Retrieves the color based on a repeating sequence"""
  seq_len = len(sequence)

  index = (row % seq_len + (col % seq_len )* 2) %seq_len
  return sequence[index]

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Find a good starting point for the background.  Assume it's near the center.
    center_row, center_col = rows // 2, cols // 2
    
    if input_grid[center_row, center_col] == 0:

        # Identify the contiguous white region
        white_region = find_contiguous_region(input_grid, center_row, center_col, 0)

        # Remove the white region (set to background, which will be overwritten)
        for row, col in white_region:
            output_grid[row, col] = 0 # temporarily set to background


    # define border pattern
    sequence = [3,2,3,6, 2,1,2,5, 6,5,6,1]
    # Fill the removed region and stray 0 pixels, referencing border pattern
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 0:
              output_grid[r,c] = get_pattern_element(r,c, sequence)

    return output_grid