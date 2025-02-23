"""
Reduces a large grid to a smaller representation. The output represents the outlines of the nested regions of the input, maintaining their relative positioning and centered. The size of the output grid corresponds to the number of nested regions.
"""

import numpy as np

def get_border_color(grid):
    """Return color of the top-left pixel. Assumes a filled rectangle."""
    return grid[0, 0]

def find_nested_regions(grid):
    """
    Finds the nested regions within the grid, starting from the border.
    Returns a list of dictionaries, each containing the color and dimensions of a region.
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
    """Transforms the input grid into a smaller grid representing nested regions."""

    # Identify nested regions.
    regions = find_nested_regions(input_grid)
    num_layers = len(regions)

    # Create an output grid of size L x L, where L is the number of layers.
    output_grid = np.zeros((num_layers, num_layers), dtype=int)

    # Draw outlines for each layer.
    for i in range(num_layers):
        color = regions[i]['color']
        # Draw top and bottom borders.
        output_grid[i, i:num_layers-i] = color
        output_grid[num_layers-1-i, i:num_layers-i] = color
        # Draw left and right borders (excluding corners already filled).
        output_grid[i+1:num_layers-1-i, i] = color
        output_grid[i+1:num_layers-1-i, num_layers-1-i] = color

    return output_grid