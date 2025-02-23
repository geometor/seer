"""
1.  **Identify Objects:** Locate all 3x3 squares of yellow (4) and magenta (6).

2.  **Calculate Relative Shifts:**  For each magenta and yellow square:
    *   Find its top-left corner coordinates in the input grid.
    *   Find a corresponding square (same color) in the expected output grid.
    *   Calculate the shift vector (row difference, column difference) between the input and output positions.

3.  **Apply Shifts:** Create a copy of the input grid as the output grid.  For each identified square (magenta and yellow):
    * Apply the calculated shift to the square in the output grid.
    * Clear the original position, we will restore it after by copying from input.

4. **Restore Surrounding Pixels**:
    + iterate through the color squares that were identified and moved.
    + determine the dimensions of an affected area.
    + copy from input grid.

"""

import numpy as np

def find_squares(grid, color):
    """Finds the top-left corner coordinates of all 3x3 squares of a given color."""
    squares = []
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            if np.all(grid[r:r+3, c:c+3] == color):
                squares.append((r, c))
    return squares

def apply_shift(grid, square, shift):
    """Applies a shift to a 3x3 square within a grid, handling boundary conditions."""
    rows, cols = grid.shape
    r, c = square
    dr, dc = shift
    new_r, new_c = r + dr, c + dc

    # Check if the new position is within bounds
    if 0 <= new_r <= rows - 3 and 0 <= new_c <= cols - 3:
        return (new_r, new_c)
    else:
        return None  # Or handle out-of-bounds differently, e.g., clipping


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find objects
    magenta_squares_input = find_squares(input_grid, 6)
    yellow_squares_input = find_squares(input_grid, 4)
    
    all_squares_input = magenta_squares_input + yellow_squares_input
    
    #find the shifts
    shifts={}
    
    for square_in in all_squares_input:
      color = input_grid[square_in[0],square_in[1]]
      
      #clear original location of square in output_grid.
      output_grid[square_in[0]:square_in[0]+3, square_in[1]:square_in[1]+3] = 0

      # Find the place where to move the square.

      # calculate potential targets as positions relative to the original object
      potential_targets = []
      for r_offset in [-1,0,1]:
        for c_offset in [-1,0,1]:
            potential_targets.append((square_in[0]+r_offset,square_in[1]+c_offset))
      
      #check area around potential targets.
      for target in potential_targets:
        if(target[0] >=0 and target[0] < output_grid.shape[0] and target[1] >=0 and target[1] < output_grid.shape[1]):
            if(output_grid[target[0],target[1]] == color):
                #shift and store
                shift = (target[0]-square_in[0],target[1]-square_in[1])
                new_pos = apply_shift(output_grid,square_in,shift)
                if(new_pos != None):
                    output_grid[new_pos[0]:new_pos[0]+3, new_pos[1]:new_pos[1]+3] = color
                
    #restore area
    for square_in in all_squares_input:
       
        
        #determine affected area of the original location, 5x5
        r0 = max(0,square_in[0]-1)
        r1 = min(output_grid.shape[0],square_in[0]+3+1)
        
        c0 = max(0,square_in[1]-1)
        c1 = min(output_grid.shape[1],square_in[1]+3+1)        
        
        #restore original location
        output_grid[r0:r1, c0:c1] = input_grid[r0:r1, c0:c1]



    return output_grid