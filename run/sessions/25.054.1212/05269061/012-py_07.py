"""
Identifies non-zero sequences in the input grid, determines a repeating
subsequence, and then tiles the output grid with that subsequence.
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

def analyze_sequences(sequences):
    """Analyzes a list of sequences to find potential repeating patterns."""
    if not sequences:
        return None

    # Flatten the sequences into a single list of values, preserving order
    flat_sequence = [val for seq in sequences for _, _, val in seq]

    # Find the shortest repeating subsequence
    for length in range(1, len(flat_sequence) // 2 + 1):
        subsequence = flat_sequence[:length]
        if len(flat_sequence) % length == 0:  # Check if subsequence divides the whole sequence
             repeats = len(flat_sequence) // length
             if flat_sequence == subsequence * repeats:
                return subsequence  # found a repeat
    return flat_sequence

def transform(input_grid):
    # Initialize output_grid as an array of zeros with the same dimensions as the input.
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Get the non-zero sequences from the input grid.
    sequences = get_sequences(input_grid)

    # Find the repeating subsequence.
    repeating_subsequence = analyze_sequences(sequences)

    if repeating_subsequence:
        # Tile the output grid with the repeating subsequence.
        sub_len = len(repeating_subsequence)
        for r in range(rows):
            for c in range(cols):
                index = (r + c) % sub_len  # Diagonal tiling
                output_grid[r, c] = repeating_subsequence[index]
    
    return output_grid