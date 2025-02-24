"""
The output is a 3x3 grid. The grid is composed of only magenta and white pixels.
The position of the magenta and white pixels is determined by the input grid.
The input grid is interpreted as a 1-dimensional sequence by reading rows
left-to-right, top-to-bottom. The sequence of pixels, excluding zeros, from the
input becomes the sequence of output pixels, starting in the top-left and
reading left-to-right, top-to-bottom, and replacing the values with 6. The
remaining pixels are set to zero. The position is determined by wrapping the
index of the non-zero elements.
"""

import numpy as np

def transform(input_grid):
    # Flatten the input grid into a 1D sequence.
    flattened_input = input_grid.flatten()

    # Remove zeros from the sequence.
    filtered_sequence = flattened_input[flattened_input != 0]
    filtered_indices = np.where(flattened_input != 0)[0]

    # Initialize a 3x3 output grid filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)
    output_size = output_grid.size
    
    # Replace elements in the flattened output grid with 6 (magenta)
    output_grid_flat = output_grid.flatten()

    for i in range(len(filtered_indices)):
        output_index = filtered_indices[i] % output_size
        output_grid_flat[output_index] = 6
    
    # Reshape back into 3 x 3
    output_grid = output_grid_flat.reshape((3,3))

    return output_grid