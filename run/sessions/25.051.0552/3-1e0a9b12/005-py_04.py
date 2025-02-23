import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions and background color
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find objects and their topmost row
    objects = {}
    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:
                if color not in objects:
                    objects[color] = {'topmost_row': r, 'positions': []}
                objects[color]['positions'].append((r, c))

   # Apply transformation rules
    for color, obj in objects.items():
      for r,c in obj['positions']:
        if color == 1 and obj['topmost_row'] == 0:
           if input_grid[r+1,c] == 3:
            output_grid[r+1,c] = 3

        else:
            new_row = r + obj['topmost_row']
            if new_row < rows:
                output_grid[new_row, c] = color
            else:
                output_grid[r,c] = color

    return output_grid