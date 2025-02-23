# AboveBelow4 • 006 • refine_coder

---
```python
"""
1.  **Identify Stripes:** Find all horizontal and vertical stripes. A stripe is a contiguous sequence of pixels of the same color along a row or column.

2.  **Find Intersections:** Identify all points where stripes of *different* colors intersect.

3.  **Determine Intersection Color:** At each intersection, change the color of the pixel to the color of the stripe that is not considered 'background'. The 'background' color at an intersection point is considered to be '0' (white) if it exists. If white does not exist, then look at the colors of the other stripes in the image. The color that appears in a horizontal stripe AND a vertical stripe will be considered the intersecting color.

4.  **Apply Changes:** Update the output grid with the new colors at the intersection points, keeping all other pixels unchanged.
"""

import numpy as np

def find_stripes(grid, orientation):
    stripes = []
    if orientation == "horizontal":
        for i, row in enumerate(grid):
            stripe_start = None
            current_color = None
            for j, pixel in enumerate(row):
                if stripe_start is None:
                    stripe_start = j
                    current_color = pixel
                elif pixel != current_color:
                    stripes.append((i, stripe_start, i, j - 1, current_color))
                    stripe_start = j
                    current_color = pixel
            if stripe_start is not None:
                stripes.append((i, stripe_start, i, len(row) - 1, current_color))
    elif orientation == "vertical":
        for j in range(grid.shape[1]):
            stripe_start = None
            current_color = None
            for i, pixel in enumerate(grid[:, j]):
                if stripe_start is None:
                    stripe_start = i
                    current_color = pixel
                elif pixel != current_color:
                    stripes.append((stripe_start, j, i - 1, j, current_color))
                    stripe_start = i
                    current_color = pixel
            if stripe_start is not None:
                stripes.append((stripe_start, j, grid.shape[0] - 1, j, current_color))
    return stripes

def find_all_stripes(grid):
    horizontal_stripes = find_stripes(grid, "horizontal")
    vertical_stripes = find_stripes(grid, "vertical")
    return horizontal_stripes + vertical_stripes

def find_intersections(stripes):
    intersections = []
    for i in range(len(stripes)):
        for j in range(i + 1, len(stripes)):
            s1_start_row, s1_start_col, s1_end_row, s1_end_col, s1_color = stripes[i]
            s2_start_row, s2_start_col, s2_end_row, s2_end_col, s2_color = stripes[j]

            if s1_color == s2_color:
                continue

            if s1_start_row == s1_end_row:  # s1 horizontal
                if s2_start_row == s2_end_row:  # s2 horizontal
                    pass
                else:  # s2 vertical
                    if s2_start_col >= s1_start_col and s2_start_col <= s1_end_col and s1_start_row >= s2_start_row and s1_start_row <= s2_end_row:
                        intersections.append(((s1_start_row, s2_start_col), s1_color, s2_color))
            else:  # s1 vertical
                if s2_start_row == s2_end_row:  # s2 horizontal
                    if s1_start_col >= s2_start_col and s1_start_col <= s2_end_col and s2_start_row >= s1_start_row and s2_start_row <= s1_end_row:
                         intersections.append(((s2_start_row, s1_start_col), s1_color, s2_color))
                else: #s2 vertical
                  pass
    return intersections

def determine_intersection_color(intersection, all_stripes):
    (row, col), color1, color2 = intersection

    # Prioritize white (0) as background
    if color1 == 0:
        return color2
    if color2 == 0:
        return color1

    # If white isn't present, find a color that's in both horizontal and vertical stripes
    horizontal_colors = set()
    vertical_colors = set()

    for stripe in all_stripes:
        s_row, s_col, _, _, s_color = stripe
        if s_row == row: # Horizontal
            horizontal_colors.add(s_color)
        if s_col == col: # Vertical
           vertical_colors.add(s_color)

    intersecting_colors = horizontal_colors.intersection(vertical_colors)

    if color1 in intersecting_colors:
       return color1
    elif color2 in intersecting_colors:
       return color2
    
    return color1 # default - use the first one


def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)
    output_grid = np.copy(grid)

    # Find all stripes
    all_stripes = find_all_stripes(grid)

    # Find intersection points
    intersections = find_intersections(all_stripes)

    # change output pixels
    for intersection in intersections:
        replacement_color = determine_intersection_color(intersection, all_stripes)
        (row, col), _, _ = intersection  # Corrected unpacking
        output_grid[row, col] = replacement_color

    return output_grid
```
