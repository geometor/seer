"""
Transforms the input grid by extracting a 3x3 sub-grid centered around the vertically middle gray cell,
changing the central cell to red (2), and setting all other cells in the sub-grid to white (0).
"""

import numpy as np

def get_gray_positions(grid):
    # return the positions of gray cells (5) in the grid
    return np.array(np.where(grid == 5)).T

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    gray_positions = get_gray_positions(input_grid)
    
    # Check if gray cells exist
    if len(gray_positions) == 0:
        # Return a default 3x3 grid filled with 0, but ideally, handle the error
        return np.zeros((3, 3), dtype=int)
        
    # Find the vertically middle gray cell
    gray_positions = gray_positions[gray_positions[:, 0].argsort()] #sort by y
    middle_gray_y = gray_positions[len(gray_positions) // 2,0]

    middle_gray_positions = gray_positions[gray_positions[:,0]==middle_gray_y]
    middle_gray_positions = middle_gray_positions[middle_gray_positions[:, 1].argsort()] #sort by x
    
    center_x = middle_gray_positions[len(middle_gray_positions)//2,1]
    center_y = middle_gray_y
    
    # Initialize the output grid with zeros
    output_grid = np.zeros((3, 3), dtype=int)

    # Calculate the boundaries for extraction, ensuring we stay within bounds
    y_start = max(0, center_y - 1)
    y_end = min(input_grid.shape[0], center_y + 2)
    x_start = max(0, center_x - 1)
    x_end = min(input_grid.shape[1], center_x + 2)

    # Extract the subgrid.
    subgrid = input_grid[y_start:y_end, x_start:x_end]
    
    
    # Determine center in output_grid
    out_center_y = min(1,center_y)
    out_center_x = min(1, center_x)

    # change center to 2
    output_grid[out_center_y, out_center_x] = 2

    # Check immediate vertical neighbors
    if center_y > 0 and input_grid[center_y-1, center_x] == 5:
      if center_y-1 >= y_start:
        output_grid[out_center_y-1, out_center_x] = 2
    if center_y < input_grid.shape[0]-1 and input_grid[center_y+1, center_x] == 5:
      if center_y+1 < y_end:
        output_grid[out_center_y+1, out_center_x] = 2
        

    return output_grid