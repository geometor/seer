"""
Finds all 3x3 subgrids and selects the first unique one encountered 
when scanning from top-to-bottom, left-to-right.
"""

import numpy as np

def find_3x3_subgrids(grid):
    """Finds all 3x3 subgrids within a given grid."""
    subgrids = []
    rows, cols = grid.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = grid[i:i+3, j:j+3]
            subgrids.append(((i, j), subgrid))  # Store start position with subgrid
    return subgrids

def subgrid_to_tuple(subgrid):
    """Converts a subgrid to a tuple representation for hashing."""
    return tuple(subgrid.flatten())

def transform(input_grid):
    """
    Finds all 3x3 subgrids, selects the first unique one,
    and returns it.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The selected 3x3 subgrid.
    """
    subgrids = find_3x3_subgrids(input_grid)
    
    # Count occurrences of each subgrid
    subgrid_counts = {}
    for _, subgrid in subgrids:
        subgrid_tuple = subgrid_to_tuple(subgrid)
        subgrid_counts[subgrid_tuple] = subgrid_counts.get(subgrid_tuple, 0) + 1
    
    # Find unique subgrids and their starting positions
    unique_subgrids = []
    for (i, j), subgrid in subgrids:
        subgrid_tuple = subgrid_to_tuple(subgrid)
        if subgrid_counts[subgrid_tuple] == 1:
            unique_subgrids.append(((i, j), subgrid))
    
    # If there are unique subgrids, select the first one
    if unique_subgrids:
        unique_subgrids.sort(key=lambda x: x[0])  # Sort by starting position (row, col)
        return unique_subgrids[0][1]
    else:
  
        #if there are no unique subgrids, return the first one, sorted by position
        subgrids.sort(key=lambda x: x[0])
        return subgrids[0][1]