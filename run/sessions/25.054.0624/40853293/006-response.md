# 40853293 • 006 • refine_coder

---
```python
"""
Transforms single colored pixels into vertical or horizontal lines based on their color, with special handling for interactions between Gray/Magenta and Azure/Maroon, and line stopping for other colors.
"""

import numpy as np

def get_single_pixels(grid):
    """Finds isolated pixels of a given color."""
    single_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0:
                is_single = True
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    single_pixels.append((r, c, color))
    return single_pixels

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    single_pixels = get_single_pixels(input_grid)

    # 1. Single Pixel Transformations
    for r, c, color in single_pixels:
        if color in [2, 3, 4, 7]:  # Red, Green, Blue, Orange: Vertical lines
            for i in range(r, rows):
                if output_grid[i,c] == 0:
                    output_grid[i,c] = color
                else:
                    break #stop at occupied
        elif color == 6:  # Magenta: Horizontal lines
             for j in range(cols):
                output_grid[r,j] = color
        elif color == 8: # Azure: Conditional Vertical Line
            is_adjacent_to_maroon = False
            for dc in [-1, 1]: # Check left/right
                nc = c + dc
                if 0 <= nc < cols and input_grid[r, nc] == 9:
                    is_adjacent_to_maroon = True
                    break
            if not is_adjacent_to_maroon:
                for i in range(r,rows):
                    if output_grid[i,c] == 0:
                        output_grid[i,c] = color
                    else:
                        break
            else:  #Azure-Maroon interaction, horizontal fill until maroon
                if c < cols -1 and input_grid[r, c+1] == 9:
                    output_grid[r,c] = 8
                elif c > 0 and input_grid[r,c-1] == 9:
                    for j in range(c-1, -1, -1):
                        if output_grid[r,j] == 9:
                            break
                        else:
                           output_grid[r,j] = 8

    # 2. Handle Gray(5) and Magenta(6) interaction:
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 5:
                if r > 0 and output_grid[r-1,c] == 6: #magenta above
                    for j in range(cols):
                        output_grid[r-1,j] = 5 #change whole line to gray
                if r < rows -1 and output_grid[r+1,c] == 6: #if magenta below
                    for j in range(cols):
                        output_grid[r+1,j] = 5 #change whole line to gray

    return output_grid
```
