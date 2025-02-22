"""
1.  **Identify the Target Object:** The input grid contains a single, contiguous object of gray color (5).

2.  **Object Segmentation:** Imagine dividing the gray shape (5) of the input, in columns, into two subsections:

    *   **Subsection 1:** The columns of the gray shape that encompass a filled square with at least one white (0) element on its top.
    *   **Subsection 2:** The remaining columns (with elements on top different than white (0)).
    
3.  **Determine starting column** Compute dynamically, the column where the Subsection 2 starts

4.  **Recolor Subsection 1:** Change the color of all cells in Subsection 1 of the gray shape to red (2).

5.  **Recolor Subsection 2:** Change the color of the remaining cells (Subsection 2) in the gray object to azure (8).

6.  **Preserve Background:** The white background (color 0) remains unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color.
    coords = np.argwhere(grid == color)
    return coords

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5).
    gray_coords = find_object(input_grid, 5)

    #If no gray object is present return the original
    if gray_coords.size == 0:
      return output_grid

    # Get the min and max column indices of the gray object.
    min_col = np.min(gray_coords[:, 1])
    max_col = np.max(gray_coords[:, 1])
    
    # 3. Determine starting column
    start_col_subsection_2 = -1
    for col in range(min_col, max_col + 1):
        # Check if any cell above the current column is white
        cells_above = input_grid[:np.min(gray_coords[:, 0]), col]
        if (cells_above != 0).any():
            start_col_subsection_2 = col
            break
    
    if start_col_subsection_2 == -1: #If no 2nd section, they are all section 2.
        start_col_subsection_2 = max_col + 1

    # 4. & 5. Recolour subsections based on starting column
    for row, col in gray_coords:
      if col < start_col_subsection_2:
        output_grid[row,col] = 2 #Subsection 1
      else:
        output_grid[row,col] = 8
    
    return output_grid