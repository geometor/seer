"""
Copies non-zero pixels from the input grid to the output grid,
then fills zero-valued pixels by repeating nearby non-zero color sequences.
"""

import numpy as np

def get_sequences(input_grid):
    """
    Identifies sequences of non-zero pixels in the input grid.
    """
    rows, cols = input_grid.shape
    sequences = []

    # Horizontal sequences
    for r in range(rows):
        current_sequence = []
        for c in range(cols):
            if input_grid[r, c] != 0:
                current_sequence.append((r, c, input_grid[r, c]))
            elif current_sequence:
                sequences.append(current_sequence)
                current_sequence = []
        if current_sequence:  # Handle sequences at the end of rows
            sequences.append(current_sequence)

    # Vertical sequences
    for c in range(cols):
        current_sequence = []
        for r in range(rows):
            if input_grid[r, c] != 0:
                current_sequence.append((r, c, input_grid[r, c]))
            elif current_sequence:
                sequences.append(current_sequence)
                current_sequence = []
        if current_sequence: # Handle sequences at the end of columns.
            sequences.append(current_sequence)
    return sequences

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Get the initial sequences
    sequences = get_sequences(input_grid)
    
    # Fill the 0 pixels
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 0:
                #find closest sequence and continue it

                best_sequence = None
                min_dist = float('inf')

                for seq in sequences:
                    for r_seq, c_seq, val_seq in seq:
                        dist = abs(r - r_seq) + abs(c-c_seq)
                        if dist < min_dist:
                            min_dist = dist
                            best_sequence = seq

                if best_sequence:
                    #calculate index in sequence
                    seq_len = len(best_sequence)

                    #find closest element index
                    closest_index = -1
                    min_seq_dist = float('inf')
                    for i in range(seq_len):
                        r_seq, c_seq, _ = best_sequence[i]

                        dist =  abs(r-r_seq) + abs(c-c_seq)

                        if dist < min_seq_dist:
                            min_seq_dist = dist
                            closest_index = i
                    
                    # extend based on direction, calculate offset
                    r_seq_start, c_seq_start, _ = best_sequence[0]
                    
                    if r_seq_start == best_sequence[-1][0]: #horizontal
                        offset = c - c_seq_start
                    elif c_seq_start == best_sequence[-1][1]: #vertical
                        offset = r - r_seq_start
                    else: # single element, repeat value
                        offset = 0


                    index = (closest_index + offset) % seq_len
                    output_grid[r,c] = best_sequence[abs(index)][2]


    return output_grid