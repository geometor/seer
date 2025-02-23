"""
The transformation rule is as follows:
1.  **Static Objects:** The red cells (color 2) and azure cells (color 8) remain unchanged in their original positions.
2.  **Green Object Identification:** Identify the green cells (color 3).
3.  **Expansion procedure:**
    - Compute the integer average row index between two green cells.
    - If there is an azure block in this row, use this block as a "seed" for the green expansion.
    - Grow the green region horizontally to the right of the seed, and to the left, until the border or an object with color 8 is encountered.
    - Repeat with a new pair of green cells.
"""

import numpy as np

def get_object_positions(grid, color):
    """Finds the positions of all cells with a specific color."""
    return np.array(np.where(grid == color)).T

def find_closest_azure_seed(grid, row):
    """Finds the closest azure cell in the specified row to use as expansion seed."""
    azure_positions = get_object_positions(grid, 8)
    if len(azure_positions) == 0: # no azure objects
        return None
    
    azure_in_row = [pos for pos in azure_positions if pos[0] == row]

    if not azure_in_row: # no azure in this row
        return None
    
    return azure_in_row[0]

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    
    # 1. Keep red and azure cells unchanged (already in output_grid)
    
    # 2. Find green cells
    green_positions = get_object_positions(input_grid, 3)
    green_positions_copy = green_positions.copy()

    # 3. Expansion procedure
    
    while len(green_positions_copy) >= 2 :

        # compute average row
        row_indices = [pos[0] for pos in green_positions_copy[:2]]
        expansion_row = int(np.mean(row_indices))

        # find azure expansion seed
        seed = find_closest_azure_seed(input_grid, expansion_row)

        if seed is not None: # expansion can be applied
            # expand to the right
            col = seed[1] + 1
            while col < input_grid.shape[1] and input_grid[expansion_row, col] != 8:
                output_grid[expansion_row, col] = 3
                col += 1

            # expand to the left
            col = seed[1] - 1
            while col >= 0 and input_grid[expansion_row, col] != 8:
                output_grid[expansion_row, col] = 3
                col -= 1
        
        # remove the two first elements
        green_positions_copy = green_positions_copy[2:]
    
    return output_grid