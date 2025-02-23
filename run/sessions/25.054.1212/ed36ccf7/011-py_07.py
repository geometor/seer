"""
The transformation rule appears to involve these steps:

1.  **Identify the Dominant Non-Zero Color:** In each input grid, there's one non-black (non-zero) color that appears most frequently. Let's call this the "dominant color."

2.  **Top-Left Alignment:** The pixels of the dominant color are shifted (moved as a group) so that *one or more* of the dominant-colored pixels occupy the top-left most positions that are occupied by that color in the flattened input grid.

3. **Preserve relative positions.** The internal arrangement of the dominant color's shape appears to be the same in input and output, only its absolute positioning is what changes.

4. **Fill Remaining:** Fill in any newly vacated spots by shifting the background color (0) appropriately. The shape of color(0) might change, as needed to complete the grid.
"""

import numpy as np

def get_dominant_color(grid):
    # Count the occurrences of each color
    unique_colors, counts = np.unique(grid, return_counts=True)
    
    # Exclude black (color 0)
    color_counts = {color: count for color, count in zip(unique_colors, counts) if color != 0}
    
    # If there is any other color than zero
    if len(color_counts) > 0:    
      # Find the color with the maximum count
      dominant_color = max(color_counts, key=color_counts.get)
    else:
       dominant_color = 0

    return dominant_color

def get_color_positions(grid, color):
     # Get the indices where the grid matches the specified color
    return np.array(np.where(grid == color)).T # Transpose for (row, col) pairs


def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    
    # 1. Identify the Dominant Non-Zero Color
    dominant_color = get_dominant_color(input_grid)

    if dominant_color==0:
        return output_grid

    # 2. Find positions of the dominant color
    dominant_positions = get_color_positions(input_grid, dominant_color)
    
    # 3. Determine the top-left most position of the dominant color in input
    if len(dominant_positions)>0:
        top_left_most = dominant_positions[0]
    
        # 4. Calculate the shift needed
        shift = top_left_most
    
    
        # 5. Clear the original positions of dominant color in output, set to zero
        for pos in dominant_positions:
          output_grid[pos[0], pos[1]] = 0

        # 6. Apply the shift to get new positions, set dominant color
        for pos in dominant_positions:
            new_pos = pos - shift
            output_grid[new_pos[0], new_pos[1]] = dominant_color

    return output_grid