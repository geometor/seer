"""
The transformation rule takes each number (representing a color) in the input grid and decrements it by one. This decrement operation is modular, meaning it wraps around. Specifically, when the number 0 is decremented, it becomes 9. The grid dimensions remain constant, and only the values of the elements change according to this circular decrement rule (a circular dial).

Example:
- 0 becomes 9
- 1 becomes 0
- 2 becomes 1
- 3 becomes 2
- 4 becomes 3
- 5 becomes 4
- 6 becomes 5
- 7 becomes 6
- 8 becomes 7
- 9 becomes 8
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Apply the modular decrement rule: (x - 1) % 10
    output_grid = (output_grid - 1) % 10

    return output_grid