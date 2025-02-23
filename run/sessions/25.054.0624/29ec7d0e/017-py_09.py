"""
The transformation rule involves identifying regions in the input grid where colors alternate in a sequence and are adjacent to a region that's already white (0). These alternating color regions are then filled with white (0) in the output grid. The filling appears to happen "behind" or "under" existing white areas.

"""

import numpy as np
from typing import List, Tuple

def find_alternating_sequence(grid: np.ndarray, row: int, col: int) -> List[Tuple[int, int]]:
    """
    Finds an alternating sequence of colors starting from a given cell.
    Explores in all 8 directions.
    """
    rows, cols = grid.shape
    start_color = grid[row, col]
    sequence = [(row, col)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        current_row, current_col = row + dr, col + dc
        if 0 <= current_row < rows and 0 <= current_col < cols:
            next_color = grid[current_row, current_col]
            if next_color != start_color:
                alternating_sequence = [(row,col)]  # Always keep the start.
                last_color = next_color
                alternating_sequence.append( (current_row, current_col) )

                current_row += dr
                current_col += dc
                while 0 <= current_row < rows and 0 <= current_col < cols:
                    current_color = grid[current_row, current_col]
                    if current_color != last_color and current_color !=0:
                        alternating_sequence.append( (current_row, current_col) )
                        last_color = current_color
                        current_row += dr
                        current_col += dc
                    else:
                        break # sequence broken

                if len(alternating_sequence) > 1: # need at least 2 diff colors
                    return alternating_sequence
    return []  # no sequence

def is_adjacent_to_white(grid: np.ndarray, row: int, col:int )-> bool:
    """check if a cell is next to white"""
    rows, cols = grid.shape
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r,c] == 0:
            return True

    return False

def transform(input_grid: np.ndarray) -> np.ndarray:
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Iterate through the grid to find regions eligible for transformation.
    for row in range(rows):
        for col in range(cols):
            # if it is next to white, check sequences
            if output_grid[row,col] != 0 and is_adjacent_to_white(output_grid, row, col):
                sequence = find_alternating_sequence(output_grid, row, col)
                if sequence:
                    # Fill the sequence with white (0).
                    for seq_row, seq_col in sequence:
                        output_grid[seq_row, seq_col] = 0

    return output_grid