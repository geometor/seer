# 1a07d186 • 016 • refine_coder

---
```python
"""
1. **Identify Solid Lines:** Find all horizontal lines that span the entire width of the grid and consist of a single color.
2. **Preserve Solid Lines:** Keep all pixels on these solid lines unchanged.
3. **Color Preservation Rule:** Keep pixels that share the same color as the existing rows that are not all one color.
4. **Remove other pixels.** Remove any pixel not part of a solid line and that doesn't follow the color preservation rule.
"""

import numpy as np

def find_solid_lines(grid):
    # Find rows that are entirely of one color.
    rows, cols = grid.shape
    solid_lines = []
    for r in range(rows):
        unique_colors = np.unique(grid[r, :])
        if len(unique_colors) == 1:
            solid_lines.append((r, unique_colors[0]))  # (row_index, color)
    return solid_lines

def get_non_solid_rows(grid):
     # Find rows that are not entirely of one color
    rows, cols = grid.shape
    non_solid_row_indices = []
    for r in range(rows):
        unique_colors = np.unique(grid[r,:])
        if len(unique_colors) > 1:
            non_solid_row_indices.append(r)
    return non_solid_row_indices
            

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find solid lines.
    solid_lines = find_solid_lines(output_grid)
    
    # Find non solid rows
    non_solid_rows = get_non_solid_rows(output_grid)
    
    # Get the colors in the non-solid rows
    allowed_colors = set()
    for row_index in non_solid_rows:
        for color in np.unique(input_grid[row_index,:]):
            allowed_colors.add(color)

    # Iterate through the grid and apply the rules.
    for r in range(rows):
        for c in range(cols):
            is_solid_line = False
            for line_row, line_color in solid_lines:
                if r == line_row:
                    is_solid_line = True
                    break
            if is_solid_line:
                continue  # Preserve solid lines
            
            if output_grid[r,c] not in allowed_colors:
                output_grid[r,c] = 0
            elif not (r in [line[0] for line in solid_lines]):
                # check for solid line colors in non-solid rows, and remove if present
                solid_line_colors = [line[1] for line in solid_lines]
                if output_grid[r,c] in solid_line_colors:
                    output_grid[r,c] = 0
            

    return output_grid
```
