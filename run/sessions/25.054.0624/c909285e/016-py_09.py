"""
1.  **Find the Border:** Scan the input grid to identify a rectangular border. The border is defined as a contiguous region of a single color that completely encloses an inner rectangular area. The border may have different colors on the inner and outer edges, or have more than one row or column making it thicker.
2.  **Extract Inner Region:** Once the border is identified, extract the rectangular region located *inside* the border. This inner region is the area of interest.
3.  **Conditional Color Substitution:** Examine the *input* grid. If color 5 is adjacent to the *outer* border color anywhere, replace all instances of color 5 with color 6 *within the extracted inner region*.
4. **Output:** The transformed "inner region" from step 3 becomes the output grid.
"""

import numpy as np

def find_border(grid):
    """Finds the rectangular border and returns its boundaries."""
    rows, cols = grid.shape
    
    # Find top-left corner of the border
    for top in range(rows):
        for left in range(cols):
            border_color = grid[top, left]
            
            # Check for rectangular shape and complete enclosure
            if is_valid_border(grid, top, left, border_color):
                bottom, right = find_bottom_right(grid, top, left, border_color)
                return top, left, bottom, right, border_color
    return None, None, None, None, None

def is_valid_border(grid, top, left, border_color):
    """Checks if the border at (top, left) is valid."""
    rows, cols = grid.shape

    # Check for minimum border thickness (at least 1)
    if top >= rows - 1 or left >= cols - 1:
        return False
    
    #Check to see if there is a bottom right corner
    bottom, right = find_bottom_right(grid, top, left, border_color)
    if bottom == -1:
        return False
    
    #check to make sure all pixels are the same color on the border.
    for row in range(top, bottom + 1):
        if grid[row, left] != border_color or grid[row, right] != border_color:
            return False
    for col in range(left, right+1):
        if grid[top, col] != border_color or grid[bottom, col] != border_color:
            return False
    
    #now check to make sure there is no border color inside.
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            if grid[row, col] == border_color:
                return False
    
    return True
    
def find_bottom_right(grid, top, left, border_color):
    rows, cols = grid.shape

    # Find bottom-right corner of the border
    bottom = top
    while bottom + 1 < rows and grid[bottom + 1, left] == border_color:
        bottom += 1

    right = left
    while right + 1 < cols and grid[top, right + 1] == border_color:
        right += 1
        
    #check corner
    if grid[bottom, right] != border_color:
        return -1, -1 #invalid corner

    return bottom, right

def extract_inner_region(grid, top, left, bottom, right):
    """Extracts the inner region of the border."""
    return grid[top+1:bottom, left+1:right]

def conditional_color_substitution(grid, inner_region, border_color):
    """Performs color substitution if 5 is adjacent to the border."""
    rows, cols = grid.shape
    
    # Check for adjacency of 5 to the border_color in the original grid
    substitution_needed = False
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 5:
                # Check neighbors for border_color
                neighbors = []
                if r > 0: neighbors.append(grid[r-1, c])
                if r < rows - 1: neighbors.append(grid[r+1, c])
                if c > 0: neighbors.append(grid[r, c-1])
                if c < cols - 1: neighbors.append(grid[r, c+1])
                
                if border_color in neighbors:
                    substitution_needed = True
                    break
        if substitution_needed:
            break
            
    if substitution_needed:
         return np.where(inner_region == 5, 6, inner_region)
    else:
        return inner_region

def transform(input_grid):
    # Convert input grid to a NumPy array
    grid = np.array(input_grid)

    # 1. Find the Border
    top, left, bottom, right, border_color = find_border(grid)
    
    if top is None:  # No border found
        return None

    # 2. Extract Inner Region
    inner_region = extract_inner_region(grid, top, left, bottom, right)

    # 3. Conditional Color Substitution
    transformed_inner_region = conditional_color_substitution(grid, inner_region, border_color)
    
    # 4. Output
    return transformed_inner_region.tolist()