import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the defined rules:
    1. Copies azure (8), red (2), and blue (1) pixels, and all other colors.
    2. Adds yellow (4) pixels above and below each red pixel.
    3. Adds orange (7) pixels around each blue pixel.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 2:  # Red pixel
                if i > 0:
                    output_grid[i - 1, j] = 4  # Yellow above
                if i < rows - 1:
                    output_grid[i + 1, j] = 4  # Yellow below
            elif input_grid[i, j] == 1:  # Blue pixel
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        output_grid[x, y] = 7  # Orange around

    return output_grid