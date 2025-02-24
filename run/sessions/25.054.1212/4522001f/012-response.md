# 4522001f • 012 • refine_coder

---
```python
"""
1.  **Identify the Seed Region:** Find the largest contiguous region of pixels in the input grid. Contiguous means pixels are connected horizontally or vertically (not diagonally). It does *not* depend on a single color; the region can contain multiple colors.

2.  **Determine the Bounding Box:** Calculate the smallest rectangle (bounding box) that completely encloses the seed region. This is defined by the top-left (min_row, min_col) and bottom-right (max_row, max_col) coordinates of the seed region.

3.  **Replicate:** Create a 3x3 grid of copies of this bounding box. The copies are placed without overlap. The output will therefore have 9 times the area of the seed area. The dimensions of the output is three times the height and width of the seed box.

4. **Preserve**: the relative positioning of each pixel within the seed region.
"""

import numpy as np

def find_largest_contiguous_region(grid):
    """
    Finds the largest contiguous region in a grid, regardless of color.
    """
    rows, cols = grid.shape
    visited = set()
    largest_region = set()

    def _explore_region(row, col, current_region):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols):
            return
        visited.add((row, col))
        current_region.add((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            _explore_region(row + dr, col + dc, current_region)


    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                current_region = set()
                _explore_region(r, c, current_region)
                if len(current_region) > len(largest_region):
                    largest_region = current_region
    return largest_region

def find_bounding_box(region):
    """
    Finds the bounding box of a set of points.
    """
    if not region:
        return None

    min_row = min(r for r, _ in region)
    min_col = min(c for _, c in region)
    max_row = max(r for r, _ in region)
    max_col = max(c for _, c in region)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    """
    Transforms the input grid by finding the largest contiguous region and replicating it 3x3.
    """
    # 1. Find the largest contiguous region.
    largest_region = find_largest_contiguous_region(input_grid)

    # 2. Determine the bounding box.
    if not largest_region:  # Handle empty input grids
        return np.zeros((1,1), dtype=int) # Return smallest grid
    (min_row, min_col), (max_row, max_col) = find_bounding_box(largest_region)
    seed_height = max_row - min_row + 1
    seed_width = max_col - min_col + 1

    # 3. Create the output grid (3x the size of the seed box).
    output_grid = np.zeros((seed_height * 3, seed_width * 3), dtype=int)

    # 4. Replicate the seed region into the output grid.
    for i in range(3):
        for j in range(3):
            row_offset = i * seed_height
            col_offset = j * seed_width
            for r in range(min_row, max_row + 1):
                for c in range(min_col, max_col + 1):
                    output_row = row_offset + (r - min_row)
                    output_col = col_offset + (c - min_col)
                    output_grid[output_row, output_col] = input_grid[r, c]

    return output_grid
```

