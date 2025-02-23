"""
Extracts the smallest repeating horizontal sequence from the input grid to form the output grid, ensuring the sequence can reconstruct the original row when repeated.
"""

import numpy as np

def find_repeating_unit(row):
    """Finds the repeating unit in a single row."""
    width = len(row)
    for unit_width in range(1, width // 2 + 1):
        unit = row[:unit_width]
        # Construct a hypothetical row by repeating the unit
        hypothetical_row = (unit * (width // unit_width + 1))[:width]
        if np.array_equal(hypothetical_row, row):
            return unit
    return row  # If no repeating unit found, return the entire row

def transform(input_grid):
    """
    Extracts the repeating horizontal unit from each row of the input grid.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The output grid, formed by the repeating units of each row.
    """
    output_grid = []
    for row in input_grid:
        # Find the repeating unit for each row
        repeating_unit = find_repeating_unit(row)
        output_grid.append(repeating_unit)

    return output_grid