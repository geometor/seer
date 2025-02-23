"""
1.  **Identify** all *horizontal sequences* of one or more contiguous azure pixels (value `8`) in the input grid.
2.  **Preserve** all azure pixels in these sequences in their original positions in the output grid.
3.  **Introduce** a *single* blue pixel (value `1`) immediately to the right of the *end* of each azure pixel sequence, if there is available space within the grid boundaries.
4.  **Introduce** a *single* blue pixel (value `1`) immediately to the left of the *start* of each azure pixel sequence, if there is available space within the grid boundaries.
5.  **Fill** all other positions in the output grid with `0` (white).
"""

import numpy as np

def get_horizontal_sequences(grid, value):
    sequences = []
    for row in range(grid.shape[0]):
        in_sequence = False
        start = -1
        for col in range(grid.shape[1]):
            if grid[row, col] == value:
                if not in_sequence:
                    in_sequence = True
                    start = col
            elif in_sequence:
                in_sequence = False
                sequences.append(((row, start), (row, col - 1)))
                start = -1
        if in_sequence:
            sequences.append(((row, start), (row, grid.shape[1] - 1)))
    return sequences

def transform(input_grid):
    # Initialize output_grid with zeros (white)
    output_grid = np.zeros_like(input_grid)
    
    # Get horizontal sequences of azure pixels (value 8)
    azure_sequences = get_horizontal_sequences(input_grid, 8)
    
    # Preserve azure pixels in the output grid
    for start, end in azure_sequences:
        for col in range(start[1], end[1] + 1):
            output_grid[start[0], col] = 8

    # Introduce blue pixels (value 1) at the boundaries of azure sequences
    for start, end in azure_sequences:
        # To the left of the start
        if start[1] - 1 >= 0:
            output_grid[start[0], start[1] - 1] = 1
        # To the right of the end
        if end[1] + 1 < output_grid.shape[1]:
            output_grid[end[0], end[1] + 1] = 1
    
    return output_grid