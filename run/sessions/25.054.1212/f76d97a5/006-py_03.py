"""
1. Iterate through each input example.
2. Identify the distinct non-zero colors present in the input grid, excluding zero. There will always be two colors.
3. The first color in the input changes to the color value of zero in the output.
4. The second color in the input grid changes to the color value of the first color in the output.
5. Zero values remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input
    output_grid = np.copy(input_grid)

    # Find the two distinct non-zero colors
    colors = np.unique(input_grid)
    colors = colors[colors != 0]
    if len(colors) == 2:
      color1 = colors[0]
      color2 = colors[1]

      # get the colors to map them to from output
      output_colors = np.unique(output_grid)
      output_colors = output_colors[output_colors != 0]
      output_color1 = output_colors[0]

      # Replace color1 with 0 and color2 with color 1
      output_grid[input_grid == color1] = 0  # color 1 becomes zero
      output_grid[input_grid == color2] = output_color1 # color 2 becomes color 1
    elif len(colors) == 1:
        color1 = colors[0]
        output_grid[input_grid == color1] = 0
    
    return output_grid