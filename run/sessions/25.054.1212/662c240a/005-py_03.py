"""
The transformation extracts a 3x3 subgrid from a larger input grid.  The selection
of the correct subgrid is based on identifying all possible 3x3 subgrids and
choosing one according to a rule we are still refining. The initial rule
hypothesis will select the subgrid based on some combination of color frequency.
"""

import numpy as np

def find_3x3_subgrids(grid):
    """Finds all unique 3x3 subgrids within a given grid."""
    subgrids = []
    rows, cols = grid.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = grid[i:i+3, j:j+3]
            subgrids.append(subgrid)
    return subgrids

def select_subgrid_by_color_frequency(input_grid, subgrids):
    """
    Selects a subgrid based on color frequency analysis. This is a placeholder
    for the actual selection rule, which is still under development. We'll start
    by testing whether the subgrid with the most frequent colors in the *entire input*
    is the correct one.
    """
    # 1. Count color frequencies in the entire input grid.
    color_counts = {}
    for color in np.unique(input_grid):
        color_counts[color] = np.sum(input_grid == color)

    # 2. Score each subgrid based on the sum of its colors' frequencies.
    best_subgrid = None
    best_score = -1

    for subgrid in subgrids:
        score = 0
        for color in np.unique(subgrid):
            if color in color_counts:  # Ensure the color exists in the input
                score += color_counts[color]  * np.sum(subgrid == color)

        if score > best_score:
            best_score = score
            best_subgrid = subgrid

    return best_subgrid


def transform(input_grid):
    # Generate all 3x3 subgrids
    subgrids = find_3x3_subgrids(input_grid)

    # Select the subgrid based on color frequency criteria
    output_grid = select_subgrid_by_color_frequency(input_grid, subgrids)

    return output_grid