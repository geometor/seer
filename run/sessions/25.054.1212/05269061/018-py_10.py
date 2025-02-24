"""
The transformation rule is to create an output grid of the same size as the input grid. The output grid is filled with a repeating diagonal pattern of colors. The specific color sequence is derived from the first three non-zero values found in the input grid, starting from the top-left.
"""

import numpy as np

def get_sequence(input_grid):
    """Extracts the repeating color sequence from the input grid."""
    sequence = []
    rows, cols = input_grid.shape
    for i in range(rows):
      for j in range(cols):
        if input_grid[i,j] != 0:
          sequence.append(input_grid[i,j])
        if len(sequence) == 3:
          return sequence
    return sequence

def transform(input_grid):
    # initialize output_grid with the same dimensions as the input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Infer the color sequence
    sequence = get_sequence(input_grid)
    if not sequence:  # If sequence is empty, return a zero-filled grid
        return output_grid

    # Fill the output grid with the repeating sequence
    for i in range(rows):
        for j in range(cols):
            # Calculate the index in the sequence based on row and column
            seq_index = (i + j) % len(sequence)
            output_grid[i, j] = sequence[seq_index]

    return output_grid