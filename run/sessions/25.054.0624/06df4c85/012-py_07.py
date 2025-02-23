"""
1.  **Identify Initial Objects:** Locate contiguous blocks of pixels of the same color (excluding white (0) and blue (1)) in the input grid. These form the initial "vertical strips."

2.  **Horizontal Expansion:**
    *   Iterate through each row of the grid.
    *   For each blue (1) pixel:
        *   Check horizontally adjacent pixels. If an adjacent pixel belongs to a colored strip (non-white and non-blue), change the blue pixel to that strip's color.
        *   Continue propagation: repeat the check for the newly colored pixel and propagate the change.

3.  **Vertical Expansion:**
    *   Iterate through each *newly colored* pixel (resulting from horizontal expansion).
    *   For each blue pixel directly above or below a newly colored pixel, change the blue pixel to the same color, but only if there is a pixel of the same color directly adjacent vertically.
    *   Continue propagation: repeat the check for the newly colored pixel and propagate the change.

4.  **Preservation:** White (0) pixels act as boundaries and should not be changed.
"""

import numpy as np

def get_vertical_strips(grid):
    """Identifies initial vertical strips (objects) in the grid."""
    rows, cols = grid.shape
    strips = []
    for col in range(cols):
        current_strip = []
        for row in range(rows):
            color = grid[row, col]
            if color not in [0, 1]:
                if not current_strip or current_strip[-1][1] == color:
                    current_strip.append((row, col, color))
                else:
                    strips.append(current_strip)
                    current_strip = [(row, col, color)]
            elif current_strip:
                strips.append(current_strip)
                current_strip = []
        if current_strip:
            strips.append(current_strip)
    return strips

def horizontal_expansion(grid):
    """Expands colors horizontally, replacing blue pixels."""
    rows, cols = grid.shape
    new_grid = np.copy(grid)
    changed_pixels = []

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:
                # Check left
                if c > 0 and grid[r, c-1] not in [0, 1]:
                    new_grid[r, c] = grid[r, c-1]
                    changed_pixels.append((r, c, grid[r, c-1]))
                # Check Right
                elif c < cols - 1 and grid[r, c+1] not in [0, 1]:
                    new_grid[r,c] = grid[r, c+1]
                    changed_pixels.append((r, c, grid[r, c+1]))

    # propagate changes horizontally
    while len(changed_pixels) > 0:
      new_changed_pixels = []
      for r, c, color in changed_pixels:
        # propagate left
        if c > 0 and new_grid[r, c-1] == 1:
          new_grid[r, c-1] = color
          new_changed_pixels.append( (r, c-1, color) )
        # propagate right
        if c < cols - 1 and new_grid[r, c+1] == 1:
          new_grid[r, c+1] = color
          new_changed_pixels.append( (r, c+1, color) )
      changed_pixels = new_changed_pixels

    return new_grid, changed_pixels

def vertical_expansion(grid, changed_pixels):
    """Expands colors vertically from changed pixels."""
    rows, cols = grid.shape
    new_grid = np.copy(grid)
    new_changed_pixels = []

    while len(changed_pixels) > 0:
       for r, c, color in changed_pixels:
           # Check above
           if r > 0 and new_grid[r - 1, c] == 1:
               new_grid[r - 1, c] = color
               new_changed_pixels.append((r - 1, c, color))
           # Check below
           if r < rows - 1 and new_grid[r + 1, c] == 1:
               new_grid[r + 1, c] = color
               new_changed_pixels.append((r + 1, c, color))
       changed_pixels = new_changed_pixels

    return new_grid


def transform(input_grid):
    """Transforms the input grid according to the rules."""
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify initial objects (vertical strips) - not used
    # vertical_strips = get_vertical_strips(output_grid)

    # Horizontal Expansion and get changed pixels
    output_grid, changed_pixels = horizontal_expansion(output_grid)


    # Vertical Expansion from changed pixels
    output_grid = vertical_expansion(output_grid, changed_pixels)

    return output_grid