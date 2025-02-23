"""
The transformation counts the number of horizontally separated blue regions in the input grid and creates a single-row output grid where each cell corresponds to one of these regions. The presence of any blue region creates a blue pixel; otherwise, the result will be a white pixel.
"""

import numpy as np

def count_horizontal_blue_regions(grid):
    """Counts distinct blue regions separated horizontally."""
    count = 0
    in_blue_region = False
    for row in grid:
        for cell in row:
            if cell == 1:  # Blue
                if not in_blue_region:
                    count += 1
                    in_blue_region = True
            else:
                in_blue_region = False
        in_blue_region = False #reset at end of row
    return count

def transform(input_grid):
    """Transforms the input grid to output grid"""
    # Convert to numpy array for easier manipulation.
    grid = np.array(input_grid)

    # Count distinct blue regions horizontally.
    blue_region_count = count_horizontal_blue_regions(grid)
    
    # Create output grid.
    if blue_region_count > 0:
        output_grid = np.ones((1, blue_region_count), dtype=int)
    else:
      output_grid = np.zeros((1,1),dtype=int)

    return output_grid.tolist()