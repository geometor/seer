"""
The transformation extracts columns and rows from the input grid that contain at least one green (3) cell, discarding others to construct the output grid.
"""

import numpy as np

def get_rows_with_value(grid, value):
    """
    Returns a list of row indices that contain at least one cell with the specified value.
    """
    rows = []
    for i, row in enumerate(grid):
        if value in row:
            rows.append(i)
    return rows

def get_cols_with_value(grid, value):
    """
    Returns a list of column indices that contain at least one cell with the specified value.
    """
    return get_rows_with_value(grid.T, value)

def extract_rows(grid, row_indices):
    """Extracts specific rows from a grid, based on row indices."""
    return grid[row_indices]


def extract_cols(grid, col_indices):
    """Extracts specific columns from a grid, based on column indices."""

    return grid[:, col_indices]

def transform(input_grid):
    """
    Transforms the input grid by extracting rows and columns that contain the value '3'.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # 1. Identify Columns with '3's
    cols_with_3 = get_cols_with_value(input_grid, 3)

    # 2. Extract those columns
    intermediate_grid = extract_cols(input_grid, cols_with_3)

    # 3. Identify rows with '3's in the modified grid
    rows_with_3 = get_rows_with_value(intermediate_grid, 3)

    # 4. Extract those rows.
    output_grid = extract_rows(intermediate_grid, rows_with_3)

    return output_grid.tolist()