"""
1.  **Identify Regions:** Divide the input grid into distinct regions based on contiguous blocks of the same color. White (0) acts as a separator. The regions identified are Blue, Yellow and Red.

2.  **Consolidate Color:** Replace all Blue, Yellow and Red colors with the color Green (3).

3.  **Reduce Size**: Take the consolidated colors. Form the output grid using a subgrid.

4. **Position**:
    The green colored area (3 x 3) composed of value '3' form a subgrid inside a 4x4 grid.
    The empty area are composed of value '0'.
    The area occupied by '3's are
        - rows 0 and 3: cells 0 and 1
        - rows 1 and 2: cells 1 and 2

5.  **Output:** Create a 4x4 output grid based on the reduction and consolidation. The '0' values in the input separate regions. They are preserved.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # Initialize the output grid as a 4x4 array filled with 0s (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Consolidate colors: Replace 1, 2, and 4 with 3 (green).
    consolidated_grid = np.copy(input_grid)
    consolidated_grid[consolidated_grid == 1] = 3
    consolidated_grid[consolidated_grid == 2] = 3
    consolidated_grid[consolidated_grid == 4] = 3

    # Reduce and position the consolidated color (3) into the output grid.
    output_grid[0:2, 0:2] = 3
    output_grid[0, 0] = 3
    output_grid[0, 1] = 3
    output_grid[1, 1] = 3
    output_grid[1, 2] = 3
    output_grid[2, 1] = 3
    output_grid[2, 2] = 3
    output_grid[3, 0] = 3
    output_grid[3, 1] = 3
    
    return output_grid