# 50846271 • 016 • refine_coder

---
```python
"""
Identify red (2) pixels and change them to azure (8).  For each changed red pixel, examine its immediate neighbors (including diagonals).  If a neighboring pixel is gray (5), apply a further condition (currently unknown - SEE NOTES) to determine if that gray pixel should also be changed to azure (8). Preserve the colors of all other pixels.

NOTES: The key to solving this task is determining the unknown condition.  The current code replaces *all* adjacent gray pixels, which is incorrect.  This version adds some debugging prints to help analyze the neighbors of changed red/azure pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing red pixels with azure and conditionally replacing adjacent gray pixels.
    """
    output_grid = np.copy(input_grid)
    red_pixels = np.argwhere(input_grid == 2)

    for r, c in red_pixels:
        output_grid[r,c] = 8  # Change red to azure
        # Check neighbors and conditionally replace gray with azure
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
            #Diagonals:
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c-1),
            (r+1, c+1)
        ]
        # print(f"--- Examining red pixel at ({r}, {c}) ---") # Debug print
        for nr, nc in neighbors:
            if 0 <= nr < output_grid.shape[0] and 0 <= nc < output_grid.shape[1]:
                neighbor_color = output_grid[nr, nc]
                # print(f"  Neighbor at ({nr}, {nc}) has color {neighbor_color}") # Debug Print
                if neighbor_color == 5:
                    # --- UNKNOWN CONDITION GOES HERE ---
                    # For now, let's try a simple condition:  Change gray to azure only if
                    # there are at LEAST two other azure neighbors already.  This is just a GUESS!
                    azure_neighbors = 0
                    for nnr, nnc in neighbors:
                        if (nnr, nnc) != (nr, nc) and 0 <= nnr < output_grid.shape[0] and 0 <= nnc < output_grid.shape[1] and output_grid[nnr, nnc] == 8:
                           azure_neighbors += 1

                    if azure_neighbors >= 2 :
                      output_grid[nr, nc] = 8 #Change based on condition


    return output_grid
```

