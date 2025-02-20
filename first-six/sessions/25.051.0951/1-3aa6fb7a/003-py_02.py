import numpy as np

def find_vertical_lines(grid, color, height, width):
    """
    Find vertical lines of specified color, height, and width in the grid.
    """
    lines = []
    rows, cols = grid.shape
    for r in range(rows - height + 1):
        for c in range(cols - width + 1):
            if all(grid[r+i, c] == color for i in range(height)):
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    1. Find 2x1 vertical lines of azure color.
    2. Add one blue pixel at the upper-right of each of these lines,
     except if there are adjacent azure lines.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all 2x1 vertical lines of color 8 (azure)
    azure_lines = find_vertical_lines(input_grid, 8, 2, 1)

    # For each azure line, place a blue pixel (color 1) to the right of the top pixel
    for i, line in enumerate(azure_lines):
        r, c = line
        if c + 1 < output_grid.shape[1]:  # Check bounds
          if (r+1, c) in azure_lines: # Check for vertically adjacent lines
            output_grid[r+1,c+1] = 1
          else:
            output_grid[r, c + 1] = 1

    return output_grid