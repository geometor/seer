"""
Reduces a large grid to a smaller representation. The output represents the colors of the nested regions of the input, maintaining their relative positioning and centered.
"""

import numpy as np

def get_border_color(grid):
    # Return color of the top-left pixel.  Assumes a filled rectangle.
    return grid[0, 0]

def find_nested_regions(grid):
    """
    Finds the nested regions within the grid, starting from the border.
    Returns a list of dictionaries, each containing the color, height, and width of a region.
    """
    regions = []
    current_grid = grid
    while True:
        border_color = get_border_color(current_grid)
        height, width = current_grid.shape
        regions.append({'color': border_color, 'height': height, 'width': width})

        # Find the inner region by checking for a different color
        inner_grid = None
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                if current_grid[i, j] != border_color:
                    # Extract the inner grid
                    inner_grid = current_grid[i:, j:]

                    #find end of different colors
                    end_i = 0
                    while i + end_i < height and inner_grid[end_i,0] == inner_grid[0,0]:
                        end_i += 1
                    end_j = 0
                    while j + end_j < width and inner_grid[0,end_j] == inner_grid[0,0]:
                        end_j += 1                   
                    inner_grid = inner_grid[:end_i, :end_j]
                    break
            if inner_grid is not None:
                break
        
        if inner_grid is None:
          break
        else:
            current_grid = inner_grid


    return regions

def transform(input_grid):
    # Identify nested regions.
    regions = find_nested_regions(input_grid)

    # Determine output size.
    outer_region = regions[0]
    output_height = outer_region['height']
    output_width = outer_region['width']
    if output_height % 2 == 0:
        output_height = output_height // 2 + (output_height // 2) % 2 + 1 # make odd and scale
    else:
        output_height = output_height // 2 + 1
    
    if output_width % 2 == 0:
      output_width = output_width // 2 + (output_width // 2) % 2 + 1 # make odd and scale
    else:
        output_width = output_width // 2 + 1
    
    # if len(regions) > 1:
    #     inner_region = regions[1]
    #     output_height = inner_region['height'] if inner_region['height'] %2 != 0 else inner_region['height'] + 1
    #     output_width = inner_region['width'] if inner_region['width'] % 2 != 0 else inner_region['width'] + 1
    # else: # single region
    #     output_height = 1
    #     output_width = 1

    # Create an output grid filled with the border color.
    output_grid = np.full((output_height, output_width), outer_region['color'], dtype=int)

    # fill in layers from center outward
    center_y = output_height // 2
    center_x = output_width // 2

    for i in range(len(regions) -1, -1, -1):
        region = regions[i]
        region_h = region['height']
        if region_h % 2 == 0:
            region_h +=1
        region_w = region['width']
        if region_w % 2 == 0:
            region_w += 1
        
        start_y = center_y - region_h // 2
        start_x = center_x - region_w // 2

        end_y = start_y + min(region_h, output_height) # prevent out of bounds
        end_x = start_x + min(region_w, output_width)

        output_grid[start_y:end_y, start_x:end_x] = region['color']


    return output_grid