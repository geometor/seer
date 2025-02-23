# 9d9215db • 018 • refine_coder

---
```python
"""
1. **Identify Seed Pixels:** Locate all non-zero pixels in the input grid. These are the "seed" pixels.
2. **Horizontal Fill:** For each row containing seed pixels:
   a. Create an alternating color sequence based on the seed pixels in that row, starting from left to right.
   b. Fill the entire row with this alternating sequence.  Leftmost seed pixels determine the start of the sequence.
"""

import numpy as np

def get_seed_pixels(grid):
    """Finds the coordinates and colors of non-zero pixels (seed pixels) in a grid."""
    seed_pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                seed_pixels.append(((r, c), value))
    return seed_pixels

def generate_alternating_sequence(seed_pixels_row, cols):
    """Generates the alternating color sequence for a row."""
    sequence = []
    sorted_seeds = sorted(seed_pixels_row, key=lambda x: x[0][1])  # Sort by column

    if not sorted_seeds:
        return sequence
    
    current_color_index = 0
    for c in range(cols):
        sequence.append(sorted_seeds[current_color_index][1])
        current_color_index = (current_color_index + 1) % len(sorted_seeds)
    return sequence

def transform(input_grid):
    """Transforms the input grid according to the horizontal fill rule."""
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Get all seed pixels
    all_seed_pixels = get_seed_pixels(input_grid)

    # Group seed pixels by row
    seed_pixels_by_row = {}
    for (row, col), value in all_seed_pixels:
        if row not in seed_pixels_by_row:
            seed_pixels_by_row[row] = []
        seed_pixels_by_row[row].append(((row, col), value))

    # Horizontal Fill for each row with seed pixels
    for row, seed_pixels in seed_pixels_by_row.items():
        alternating_sequence = generate_alternating_sequence(seed_pixels, cols)
        for c in range(cols):
            output_grid[row, c] = alternating_sequence[c]

    return output_grid
```
