# 662c240a • 010 • refine_coder

---
```python
"""
Extracts a 3x3 sub-grid from the input grid. The sub-grid is selected based on
the highest similarity score among all possible 3x3 sub-grids.  Similarity
is calculated by counting the number of adjacent, same-color pixel pairs
within the sub-grid. The top-most, left-most sub-grid is chosen in case
of ties.
"""

import numpy as np

def calculate_similarity(subgrid):
    """Calculates the similarity score of a 3x3 subgrid.

    Args:
        subgrid: A 3x3 NumPy array.

    Returns:
        An integer representing the similarity score.  Higher is more similar.
    """
    count = 0
    # Check horizontal adjacency
    for i in range(3):
        for j in range(2):
            if subgrid[i, j] == subgrid[i, j+1]:
                count += 1
    # Check vertical adjacency
    for i in range(2):
        for j in range(3):
            if subgrid[i, j] == subgrid[i+1, j]:
                count += 1
    return count

def transform(input_grid):
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Initialize variables to track the best subgrid and its score.
    best_subgrid = None
    max_similarity = -1

    # Iterate through all possible 3x3 subgrids.
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = input_array[i:i+3, j:j+3]
            similarity = calculate_similarity(subgrid)

            # Update best_subgrid if a higher similarity is found.
            if similarity > max_similarity:
                max_similarity = similarity
                best_subgrid = subgrid

    # Convert the NumPy array back to a list of lists.
    output_grid = best_subgrid.tolist()

    return output_grid
```
