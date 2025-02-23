"""
Removes interior white (0) pixels from the input grid, leaving only white pixels that are on the edges of the grid or adjacent to non-white pixels.

The algorithm can be described as:

1.  Iterate through each pixel of the input grid.
2.  If a pixel is white (0):
    a. Check if it is on the edge of the grid. If yes, keep it.
    b. Check its immediate neighbors (up, down, left, right, and diagonals).
    c. If *all* valid neighbors are also white, change the pixel to a neighboring, non-white, color in the output grid. If there aren't any non-white neighbors, keep the original white pixel.
3. Copy all non-white pixels directly to the output grid in their original positions.

"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape
    output_grid = np.copy(input_grid)

    # change output pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:  # if pixel is white
                # keep edge pixels
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    continue

                neighbors = []
                neighbor_colors = []
                # check neighbors and collect colors, skip self
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            neighbors.append((nr, nc))
                            neighbor_colors.append(input_grid[nr, nc])

                # if all neighbor colors are white, replace current with a neighbor, non-white color
                if all(color == 0 for color in neighbor_colors):
                    replacement_color = 0
                    for color in neighbor_colors:
                      if color != 0:
                        replacement_color = color
                        break # use the first non-white color found
                    # if there were no non-white neighbors, we'll keep it white, otherwise, use replacement_color
                    if replacement_color != 0:
                      output_grid[r,c] = replacement_color # change this white pixel

    return output_grid