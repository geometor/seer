"""
1.  **Identify Key Pixels:** Locate all 'blue' (1) and 'azure' (8) pixels within the input grid. Also compute their mirrored positions across both the horizontal and vertical center lines of the grid.
2.  **Horizontal Expansion:** For every original and mirrored blue/azure pixel, expand it horizontally into a 3x1 block of the same color centered on the original pixel's column.
3.  **Vertical Expansion:** Expand each 3x1 block (both original and mirrored) into a 3x3 block of the same color, centered on the original 3x1 block.
4. **Color Swap:**  Within each 3x3 block (original and mirrored), swap all the 'blue' pixels with 'azure' pixels and vice-versa.
5.  **Add Gray Separators (Horizontal):** Add a horizontal line of 'gray' (5) pixels between the expanded blocks, along the center row of the expanded blocks.
6.  **Add Gray Separators (Vertical):** If there are any empty spaces ('white' (0)) vertically adjacent to the central expanded pixels, fill these with 'gray' (5).
7. Check the existance of blue and azure colors before operating on their pixel positions.

"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    return np.array(np.where(grid == color)).T.tolist()

def mirror_position(coord, grid_shape):
    """Calculates the mirrored position of a coordinate."""
    row, col = coord
    return [grid_shape[0] - 1 - row, grid_shape[1] - 1 - col]

def expand_horizontally(grid, coords, color):
    """Expands a pixel horizontally into a 3x1 block."""
    output_grid = np.copy(grid)
    row, col = coords
    for i in range(max(0, col - 1), min(grid.shape[1], col + 2)):
        output_grid[row, i] = color
    return output_grid

def expand_block_vertically(grid, row_start, col_start, color):
    """Expands a 3 x 1 block into a 3x3 block"""
    output_grid = np.copy(grid)
    for r in range(max(0, row_start - 1), min(grid.shape[0], row_start + 2)):
        for c in range(max(0, col_start -1), min(grid.shape[1], col_start + 2)):
          output_grid[r,c] = color
    return output_grid

def swap_colors_in_block(grid, row_start, col_start, color1, color2):
    """Swap color positions between two"""
    output_grid = np.copy(grid)
    coords1 = []
    coords2 = []

    #collect positions
    for r in range(max(0, row_start), min(grid.shape[0], row_start + 3)):
      for c in range(max(0, col_start), min(grid.shape[1], col_start+3)):
        if output_grid[r,c] == color1:
          coords1.append([r,c])
        elif output_grid[r,c] == color2:
          coords2.append([r,c])

    #swap
    for r,c in coords1:
      output_grid[r,c] = color2

    for r,c in coords2:
      output_grid[r,c] = color1

    return output_grid

def introduce_gray_pixels(grid, blue_coords, azure_coords):
    """Introduces gray pixels between and around the expanded blocks, considering mirrored positions."""
    output_grid = np.copy(grid)
    
    if blue_coords and azure_coords:
        
        #original
        row_blue, col_blue = blue_coords[0]
        row_azure, col_azure = azure_coords[0]
        
        # Between blocks horizontally
        if col_blue < col_azure:
            for r in range(max(0, row_blue -1), min(row_blue + 2, output_grid.shape[0])):
                output_grid[r, col_blue + 2] = 5
        else:
             for r in range(max(0, row_azure - 1), min(row_azure + 2, output_grid.shape[0])):
                output_grid[r, col_azure + 2] = 5
        
        #vertically adjacent
        if 0 <= row_blue - 2 < output_grid.shape[0]:
          output_grid[row_blue - 2, col_blue] = 5
          output_grid[row_blue - 2, col_blue + 1] = 5
          output_grid[row_blue - 2, col_blue + 2] = 5

        if 0 <= row_blue + 2 < output_grid.shape[0]:
            output_grid[row_blue + 2, col_blue] = 5
            output_grid[row_blue + 2, col_blue + 1] = 5
            output_grid[row_blue + 2, col_blue + 2] = 5
        
        if 0 <= row_azure -2 < output_grid.shape[0]:
          output_grid[row_azure - 2, col_azure] = 5
          output_grid[row_azure - 2, col_azure + 1] = 5
          output_grid[row_azure - 2, col_azure + 2] = 5
        
        if 0 <= row_azure + 2 < output_grid.shape[0] :
            output_grid[row_azure + 2, col_azure] = 5
            output_grid[row_azure + 2, col_azure + 1] = 5
            output_grid[row_azure + 2, col_azure + 2] = 5

    return output_grid

def transform(input_grid):
    # initialize output grid
    output_grid = np.copy(input_grid)
    grid_shape = input_grid.shape

    # Find initial blue and azure pixels
    blue_pixels = find_pixels_by_color(input_grid, 1)
    azure_pixels = find_pixels_by_color(input_grid, 8)

    #mirror locations
    blue_pixels_mirror = []
    if blue_pixels:
        blue_pixels_mirror = [mirror_position(coord, grid_shape) for coord in blue_pixels]
    azure_pixels_mirror = []
    if azure_pixels:
        azure_pixels_mirror = [mirror_position(coord, grid_shape) for coord in azure_pixels]

    # Expand horizontally - original
    if blue_pixels:
      for row, col in blue_pixels:
        output_grid = expand_horizontally(output_grid, [row, col], 1)
    if azure_pixels:
      for row, col in azure_pixels:
        output_grid = expand_horizontally(output_grid, [row, col], 8)

    #Expand horizontally - mirror
    if blue_pixels_mirror:
        for row, col in blue_pixels_mirror:
            output_grid = expand_horizontally(output_grid, [row, col], 1)
    if azure_pixels_mirror:
        for row, col in azure_pixels_mirror:
            output_grid = expand_horizontally(output_grid, [row, col], 8)
    

    #Expand vertically and Swap Colors
    if blue_pixels:
        row, col = blue_pixels[0]
        output_grid = expand_block_vertically(output_grid, row, col -1, 1)
        output_grid = swap_colors_in_block(output_grid, row-1, col-1, 1, 8 )
    if azure_pixels:
        row, col = azure_pixels[0]
        output_grid = expand_block_vertically(output_grid, row, col-1, 8)
        output_grid = swap_colors_in_block(output_grid, row-1, col-1, 1, 8)

    if blue_pixels_mirror:
        row, col = blue_pixels_mirror[0]
        output_grid = expand_block_vertically(output_grid, row, col - 1, 1)
        output_grid = swap_colors_in_block(output_grid, row - 1, col - 1, 1, 8)
    if azure_pixels_mirror:
        row, col = azure_pixels_mirror[0]
        output_grid = expand_block_vertically(output_grid, row, col - 1, 8)    
        output_grid = swap_colors_in_block(output_grid, row - 1, col - 1, 1, 8)
    
    # Introduce gray pixels - original
    output_grid = introduce_gray_pixels(output_grid, blue_pixels, azure_pixels)
    # Introduce gray pixels - mirrored
    output_grid = introduce_gray_pixels(output_grid, blue_pixels_mirror, azure_pixels_mirror)
    
    return output_grid