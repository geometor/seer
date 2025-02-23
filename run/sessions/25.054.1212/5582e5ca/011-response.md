# 5582e5ca • 011 • refine_coder

---
```python
"""
1.  **Analyze the Input Grid:** Examine the input grid and count the occurrences of each color (0-9).
2.  **Determine Output Color**: Select the output color by these rules:
    - Most frequent color is selected.
    - Ties are resolved by selecting the color that occurred first in the input.
3.  **Construct Output Grid:** Create a new grid with the same dimensions as the input grid. Fill every cell of this new grid with the selected output color.
"""

import numpy as np
from collections import Counter

def get_most_frequent_color(grid):
    # Count color occurrences
    counts = Counter(grid.flatten())
    # Find most frequent colors (could be multiple with same count)
    max_count = max(counts.values())
    most_frequent = [color for color, count in counts.items() if count == max_count]
    # If only one, return it
    if len(most_frequent) == 1:
        return most_frequent[0]
    # Resolve ties by first occurrence
    else:
        first_occurrence = {}
        rows, cols = grid.shape
        for r in range(rows):
            for c in range(cols):
                color = grid[r, c]
                if color in most_frequent and color not in first_occurrence:
                    first_occurrence[color] = (r, c)
        # Find the color among the most frequent that appeared first
        earliest_color = min(first_occurrence, key=first_occurrence.get)
        return earliest_color
        
def transform(input_grid):
    # Convert to numpy array for easier manipulation
    grid = np.array(input_grid)

    # Determine output color
    output_color = get_most_frequent_color(grid)

    # Create output grid filled with the selected color
    output_grid = np.full(grid.shape, output_color)

    return output_grid
```
