import numpy as np

def get_object_positions(grid, color):
    """Finds the positions of all cells with a specific color."""
    return np.array(np.where(grid == color)).T

def find_closest_azure_seed(grid, row, start_col, direction):
    """
    Finds the closest azure cell in the specified row, starting from a given column and searching in a given direction.
    
    Args:
        grid: The input grid.
        row: The row to search.
        start_col: start searching from this column
        direction: 1 for right, -1 for left.

    Returns: The position of the closest azure, or None.
    """

    if direction != 1 and direction != -1:
        raise Exception("direction must be -1 (left) or +1 (right)")

    azure_positions = get_object_positions(grid, 8)
    
    if len(azure_positions) == 0 :
        return None

    azure_in_row = [pos for pos in azure_positions if pos[0] == row]
    if not azure_in_row:
        return None
    
    if direction == 1: # search to the right
      
      valid_azure = [pos for pos in azure_in_row if pos[1] > start_col]

      if len(valid_azure) == 0: # no azure on the right, search closest
          return min(azure_in_row, key=lambda pos: abs(pos[1] - start_col), default=None)

      return min(valid_azure, key=lambda pos: abs(pos[1] - start_col), default=None)

    else: # search to the left
      valid_azure = [pos for pos in azure_in_row if pos[1] < start_col]

      if len(valid_azure) == 0:  # no azure on the left, search closest
            return min(azure_in_row, key=lambda pos: abs(pos[1] - start_col), default=None)
      
      return min(valid_azure, key=lambda pos: abs(pos[1] - start_col), default = None)

def transform(input_grid):
    """Transforms the input grid according to the final rule."""
    output_grid = np.copy(input_grid)
    
    # 1. Keep red and azure cells unchanged
    
    # 2 & 3. Green expansion
    green_positions = list(get_object_positions(input_grid, 3)) # Convert to list for easier manipulation
    
    
    processed_greens = []

    while len(green_positions) > 0:

      current_green = green_positions.pop(0) # Take one green as reference
      
      if (current_green[0],current_green[1]) in processed_greens: # already used
          continue
      
      # calculate average row with another green or azure
      
      if len(green_positions) > 0: # exist other green
            other_green = min(green_positions, key=lambda pos: abs(pos[0] - current_green[0]) +  abs(pos[1] - current_green[1])) # closest one
            expansion_row = int(np.mean([current_green[0], other_green[0]]))
            
            #seed to the right
            seed = find_closest_azure_seed(input_grid, expansion_row, current_green[1], direction = 1)
            
      else:  # no other green
        expansion_row = current_green[0]
        seed = find_closest_azure_seed(input_grid, expansion_row, current_green[1], direction = 1)

      
      if seed is not None: # apply expansion

        if expansion_row == current_green[0]: # same line
          # expand to the left
          col = seed[1] - 1
          while col >= 0 and input_grid[expansion_row, col] != 8:
                output_grid[expansion_row, col] = 3
                col -= 1

        else: # different line

          # expand to the right
          col = seed[1] + 1
          while col < input_grid.shape[1] and input_grid[expansion_row, col] != 8:
            output_grid[expansion_row, col] = 3
            col += 1

      processed_greens.append((current_green[0],current_green[1]))
      if 'other_green' in locals():
        processed_greens.append((other_green[0],other_green[1]))



    return output_grid