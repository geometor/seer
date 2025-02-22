import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on a color-specific rule.
    """
    output_grid = np.copy(input_grid)
    transformation_rules = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8
    }

    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            original_color = input_grid[x, y]
            if original_color in transformation_rules:
              output_grid[x, y] = transformation_rules[original_color]

    return output_grid