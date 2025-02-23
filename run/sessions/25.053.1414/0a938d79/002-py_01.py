"""
The original colored pixels act as "seeds". Each seed grows into a
vertical column of its color. The spaces between these columns are filled with
alternating columns of the seed colors, repeating the pattern until the grid is full.
"""

import numpy as np

def get_source_pixels(grid):
    """Finds and returns a list of non-white pixels and their coordinates."""
    source_pixels = []
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            if color != 0:
                source_pixels.append(((x, y), color))
    return source_pixels

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    source_pixels = get_source_pixels(input_grid)

    # Sort source pixels by their x-coordinate to maintain left-to-right order
    source_pixels.sort()

    # Keep track of the colors used to alternate correctly.
    colors_used = []
    last_x = -1 # keep track of where we are in filling up grid
    
    # 3. Columnar Expansion
    for (x, _), color in source_pixels:
        output_grid[:, x] = color  # Fill the entire column
        if color not in colors_used:
          colors_used.append(color)
        last_x = x

    # 4. Alternating fill between colored columns.
    if len(colors_used) > 0:  # Handle cases with no source colors
      current_color_index = 0

      for x in range(output_grid.shape[1]):
          if output_grid[0,x] == 0:
            output_grid[:,x] = colors_used[current_color_index % len(colors_used)]
          else:
            # find next color
            current_color_index = (colors_used.index(output_grid[0,x]) + 1) % len(colors_used)


    return output_grid.tolist()