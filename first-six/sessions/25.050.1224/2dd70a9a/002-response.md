# 2dd70a9a • 002 • example_1 - CODE

---
```python
"""
The transformation rule is as follows:
1.  **Identify Static Objects:** The two red cells (color 2) at positions (2,17) and (3,17) remain unchanged. The Azure (color 8) objects also remain in their initial configuration.
2.  **Green Object Transformation:** The two single green cells (color 3) are agents.
3.  **Expansion to the sides**: The green color expands to the left and right.
4.  **Limit of Expansion**: This expansion continues horizontally until an azure (color 8) object is encountered.
5.  **Row determination:** The expansion takes place in the row 6.
"""

import numpy as np

def get_object_positions(grid, color):
    """Finds the positions of all cells with a specific color."""
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    
    # 1. Keep red cells unchanged (already in output_grid)
    
    # 2 & 3. Find green cells and the row for expansion
    green_positions = get_object_positions(input_grid, 3)

    # Calculate average index of green cells.
    if len(green_positions) > 0 :
        row_indices = [pos[0] for pos in green_positions]
        expansion_row = int(np.mean(row_indices))
        
    # 4. Expand green horizontally
    # Expand to the left
        col = green_positions[0][1] -1
        while col >= 0 and input_grid[expansion_row, col] != 8:
            output_grid[expansion_row, col] = 3
            col -= 1
            
        # Expand to the Right
        col = green_positions[-1][1] + 1
        
        while col < input_grid.shape[1] and input_grid[expansion_row, col] != 8:
            output_grid[expansion_row, col] = 3
            col += 1


    return output_grid
```

