"""
1. **Identify Highlighted Colors:** Ignore the background striping of blue (1) and white (0), and the solid blue (1) separator lines. Focus only on colors that "interrupt" the striped pattern within a section, specifically magenta (6) and green (3).
2. **Create Output Grid:** Construct a 3x3 grid.
3. **Populate Output Grid:** Scan for rows with highlighted colors in input.
   - For each highlight color in the input grid that exists
   - Add that color to the output
   - Fill the rest with '0'
4. The result will be a compressed representation with the highlighted colors.
"""

import numpy as np

def get_highlighted_colors(grid):
    # Find unique colors in the grid
    unique_colors = np.unique(grid)
    # remove white/background
    highlighted_colors = [color for color in unique_colors if color != 0 and color !=1]

    return highlighted_colors

def transform(input_grid):
    """Transforms the input grid to the output grid by extracting highlighted colors."""

    # Identify highlighted colors
    highlighted_colors = get_highlighted_colors(input_grid)

    # initialize 3x3 output grid with 0
    output_grid = np.zeros((3, 3), dtype=int)

    # Populate the output grid with highlighted_colors,
    row = 0
    col = 0
    for color in highlighted_colors:
      output_grid[row,col] = color
      col += 1
      if col >=3:
        col = 0
        row += 1
      if row >=3:
        break

    return output_grid