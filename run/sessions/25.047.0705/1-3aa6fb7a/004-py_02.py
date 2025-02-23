"""
The transformation identifies cells that have specific relations to the L-shape objects and changes the color of cells in the described location. The other elements of the grid remain the same. This description is very close with the previous one. The difference is that now we have three L-shapes.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the positions of the L-shaped objects
    l_shape_positions = []
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            if input_grid[r][c] == 8:
                l_shape_positions.append((r, c))

    # Group L-shape positions
    l_shapes = []
    
    #Helper Function
    def find_l_shape(start_pos, positions):

      
      r, c = start_pos
      
      l_shape = [start_pos]
      
      # Check right
      if (r, c+1) in positions:
        l_shape.append((r,c+1))
        if (r-1, c+1) in positions:
          l_shape.append((r-1, c+1))
        elif (r+1, c+1) in positions:
          l_shape.append((r+1, c+1))
        
      # Check left  
      elif (r, c-1) in positions:
          l_shape.append((r, c-1))
          if (r-1, c-1) in positions:
            l_shape.append((r-1, c-1))
          elif (r+1, c-1) in positions:
            l_shape.append((r+1, c-1))
      
      # Check down
      elif (r+1, c) in positions:
          l_shape.append((r+1, c))
          if (r+1, c-1) in positions:
              l_shape.append((r+1, c-1))
          elif (r+1, c+1) in positions:
              l_shape.append((r+1,c+1))

      # Check up
      elif (r-1, c) in positions:
          l_shape.append((r-1, c))
          if (r-1, c-1) in positions:
            l_shape.append((r-1, c-1))
          elif (r-1, c+1) in positions:
            l_shape.append((r-1, c+1))
            
      return sorted(l_shape)

    
    
    processed_positions = []
    for pos in l_shape_positions:
      if pos not in processed_positions:
        current_l = find_l_shape(pos, l_shape_positions)  
        l_shapes.append(current_l)
        processed_positions.extend(current_l)
    

    # Iterate through each L-shape
    for l_shape in l_shapes:
        # Find top cell
        top_cell = sorted(l_shape)[0]

        # Determine relative position to modify and modify it
        
        # If there is only one position at the top row within l_shape
        if len([pos for pos in l_shape if pos[0] == top_cell[0]])==2: # two cells in top row
          # then the top cell is the left most, so modify to the left.

            output_grid[top_cell[0]][top_cell[1] - 1] = 1

        # If there is a cell to the right of top_cell
        elif (top_cell[0], top_cell[1]+1) in l_shape:
          output_grid[top_cell[0]][top_cell[1] - 1] = 1

        # If there is a cell to the left of top_cell    
        else:
          output_grid[top_cell[0]][top_cell[1] + 1] = 1

    return output_grid


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]
    
    output_grid = transform(input_grid)

    if output_grid.tolist() == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid.tolist())

    print()
    assert output_grid.tolist() == expected_output_grid, "Transformed output does not match expected output."