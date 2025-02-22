import numpy as np

def find_objects(grid, color):
    """
    Find and return the positions of all 2x1 rectangles of the specified color.
    Also, distinguish between vertical and horizontal rectangles.
    """
    vertical_objects = []
    horizontal_objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            # Vertical 2x1 rectangle
            if r + 1 < rows and grid[r, c] == color and grid[r + 1, c] == color:
                vertical_objects.append((r, c))
            # Horizontal 1x2 rectangle
            if c + 1 < cols and grid[r, c] == color and grid[r, c + 1] == color:
                horizontal_objects.append((r, c))
    return vertical_objects, horizontal_objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    vertical_azure_objects, horizontal_azure_objects = find_objects(output_grid, 8)
    
    # Apply rules for vertical rectangles
    for obj in vertical_azure_objects:
        r, c = obj
        # Check if it's the top one (by checking above)
        if r > 0 and output_grid[r - 1, c] == 8:  # Part of a >2x1 vertical block
            output_grid[r, c-1] = 1
            
        elif c + 1 < output_grid.shape[1] and output_grid[r,c+1] != 1:  # Can insert at top-right
                output_grid[r, c + 1] = 1
           
        else:
            
            output_grid[r + 1, c] = 1 # Bottom-left insertion
    
    return output_grid