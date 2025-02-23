"""
1. Examine the input grid: Determine the dimensions (height and width) and the unique colors present.
2. Count Pixels: Count how many pixels have each color.
3. Identify the Dominant Color: Find the unique color with the highest count.
4. Create Output Grid: Create a new grid with the same dimensions as the input grid.
5. Fill the Output Grid: Fill every pixel of the output grid with the dominant color identified in step 3.
"""

import numpy as np

def get_dominant_color(grid):
    # Count how many pixels have each color.
    unique_colors = np.unique(grid)
    color_counts = {}
    for color in unique_colors:
        color_counts[color] = np.sum(grid == color)

    # Find the unique color with the highest count.
    dominant_color = max(color_counts, key=color_counts.get)
    return dominant_color

def transform(input_grid):
    # Create a NumPy array from the input grid string.
    grid = np.array(input_grid)

    # Determine the dimensions (height and width)
    height, width = grid.shape

    # Identify the Dominant Color
    dominant_color = get_dominant_color(grid)
    
    # Create Output Grid: Create a new grid with the same dimensions as the input grid.
    output_grid = np.full((height, width), dominant_color)

    # Fill the Output Grid is done in initialization

    return output_grid