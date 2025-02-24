"""
1.  **Locate the Azure Line:** Find the vertical azure line in the input grid.
2.  **Extend the Azure Line:** Copy this line to the output grid. Extend this line downwards by two pixels. The extension starts from where the original azure line ends, *always adding two more pixels*.
3.  **Locate the Red Line:** Find the horizontal red line in the input grid.
4.  **Fill the Red Line Row:** Copy the red line to the same row in the output grid. Fill the rest of that row with red, stopping one pixel *before* the column containing the azure line. Continue filling with red one pixel *after* the azure line column.
5.  **Create Yellow Intersection:** Place a single yellow pixel where the extended azure line and the original red line intersect. The yellow pixel's row is the same as the original red line, and its column is the same as the original azure line.
6. All other cells in the output match the corresponding cells in the input.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None
    return coords

def transform(input_grid):
    output_grid = np.copy(input_grid)

    # 1. Locate the Azure Line
    azure_coords = find_object(input_grid, 8)

    # 2. Extend the Azure Line
    if azure_coords is not None:
        min_row = np.min(azure_coords[:, 0])
        max_row = np.max(azure_coords[:, 0])
        col = azure_coords[0, 1]
        for row in range(min_row, max_row + 3):  # Extend by two *additional* rows
            if 0 <= row < output_grid.shape[0]:
                output_grid[row, col] = 8

    # 3. Locate the Red Line
    red_coords = find_object(input_grid, 2)

    # 4. Fill the Red Line Row
    if red_coords is not None:
        row = red_coords[0, 0]
        if azure_coords is not None:
          azure_col = azure_coords[0,1]
          #fill red to the left of azure
          for col in range(0, azure_col):
            output_grid[row, col] = 2
          # fill red to the right of azure
          for col in range(azure_col + 1, output_grid.shape[1]):
              output_grid[row,col] = 2

    # 5. Create Yellow Intersection (placed after azure extension for correctness)
    if azure_coords is not None and red_coords is not None:
        red_row = red_coords[0, 0]
        azure_col = azure_coords[0, 1]
        if 0 <= red_row < output_grid.shape[0] and 0 <= azure_col < output_grid.shape[1] :
          output_grid[red_row, azure_col] = 4

    return output_grid