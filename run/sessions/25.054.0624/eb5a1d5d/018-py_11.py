"""
1.  **Identify Rectangles:** Find all rectangles in the input grid. A rectangle is defined as a contiguous block of pixels of the same color.
2.  **Determine Nesting:** Determine the nesting order of the rectangles. A rectangle A is considered to contain rectangle B if B is fully enclosed within A's boundaries.
3.  **Find the Outermost Rectangle:** Identify the outermost rectangle. This rectangle contains all other rectangles.
4.  **Crop the Grid:** "Crop" or "inset" the grid to the boundaries of the outermost rectangle. The outermost rectangle will be the same size and position, but the background surrounding it will be removed. This determines the output grid's dimensions.
5.  **Set Background**: Fill the output grid with the color of the outermost rectangle.
6.  **Draw Outlines (Except Innermost):** For each nested rectangle *except* for the most deeply nested one, draw its outline in the output grid. The outline's position and size are relative to the cropped, outermost rectangle. Outlines are one pixel wide.
7.  **Fill Innermost:** For the most deeply nested rectangle, *fill* the rectangle with its original color.
"""

import numpy as np

def get_object_bounds(grid):
    # Find all unique colors, excluding white (0) by default, but the outermost can be 0.
    unique_colors = np.unique(grid)

    bounds = {}
    for color in unique_colors:
        rows, cols = np.where(grid == color)
        if len(rows) > 0:
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)
            bounds[color] = (min_row, max_row, min_col, max_col)
    return bounds

def find_outermost_rectangle(bounds):
    # Find the rectangle that encloses all others
    if not bounds:
        return None, None

    outermost_color = None
    outermost_bounds = None

    for color, (min_row, max_row, min_col, max_col) in bounds.items():
        if outermost_bounds is None:
            outermost_color = color
            outermost_bounds = (min_row, max_row, min_col, max_col)
        else:
            o_min_row, o_max_row, o_min_col, o_max_col = outermost_bounds
            if min_row <= o_min_row and max_row >= o_max_row and min_col <= o_min_col and max_col >= o_max_col:
                outermost_color = color
                outermost_bounds = (min_row, max_row, min_col, max_col)
    return outermost_color, outermost_bounds

def find_contained_rectangles(bounds, outer_bounds):
    #find rectangles within outer_bounds
    contained = []
    if not outer_bounds:
        return contained

    o_min_row, o_max_row, o_min_col, o_max_col = outer_bounds
    for color, (min_row, max_row, min_col, max_col) in bounds.items():
        if (min_row >= o_min_row and max_row <= o_max_row and
            min_col >= o_min_col and max_col <= o_max_col and
            (min_row, max_row, min_col, max_col) != outer_bounds):
            
            #calculate relative position and size
            rel_row = min_row - o_min_row
            rel_col = min_col - o_min_col
            height = max_row - min_row + 1
            width = max_col - min_col + 1
            
            contained.append((color, (rel_row, rel_col), (height, width)))

    return contained

def find_innermost_rectangle(bounds, contained):
    # Find the most deeply nested rectangle
    if not contained:
        return None, None

    innermost_color = None
    innermost_bounds = None

    for color, (rel_row, rel_col), (height, width) in contained:
      absolute_bounds = (rel_row, rel_row + height -1, rel_col, rel_col + width - 1)
      is_innermost = True
      for other_color, (other_rel_row, other_rel_col), (other_height, other_width) in contained:
        if (color, (rel_row, rel_col), (height, width)) == (other_color, (other_rel_row, other_rel_col), (other_height, other_width)):
          continue

        other_absolute_bounds = (other_rel_row, other_rel_row + other_height-1, other_rel_col, other_rel_col + other_width - 1)
        if (absolute_bounds[0] >= other_absolute_bounds[0] and
            absolute_bounds[1] <= other_absolute_bounds[1] and
            absolute_bounds[2] >= other_absolute_bounds[2] and
            absolute_bounds[3] <= other_absolute_bounds[3]
            ):
            is_innermost = False
            break
      if is_innermost:
        innermost_color = color
        innermost_bounds = (rel_row, rel_col, height, width) #relative bounds
        break #should only be one

    return innermost_color, innermost_bounds
            
def transform(input_grid):
    # Get bounds for all objects
    object_bounds = get_object_bounds(input_grid)

    # Find the outermost rectangle
    outermost_color, outermost_bounds = find_outermost_rectangle(object_bounds)

    if outermost_bounds is None:
        return np.array([[]]) #return empty if no objects
        
    o_min_row, o_max_row, o_min_col, o_max_col = outermost_bounds

    # Determine output grid size after cropping.
    output_height = o_max_row - o_min_row + 1
    output_width = o_max_col - o_min_col + 1
    output_grid = np.full((output_height, output_width), outermost_color)
    
    # Find contained rectangles
    contained_rectangles = find_contained_rectangles(object_bounds, outermost_bounds)

    #find innermost
    innermost_color, innermost_bounds = find_innermost_rectangle(object_bounds, contained_rectangles)
    if innermost_bounds:
      i_rel_row, i_rel_col, i_height, i_width = innermost_bounds
      output_grid[i_rel_row:i_rel_row + i_height, i_rel_col: i_rel_col + i_width] = innermost_color

    # Draw contained rectangles outlines
    for color, (rel_row, rel_col), (height, width) in contained_rectangles:
        if (color, (rel_row, rel_col, height, width)) == (innermost_color, innermost_bounds):
          continue
        output_grid[rel_row:rel_row + height, rel_col] = color  # Left border
        output_grid[rel_row:rel_row + height, rel_col + width - 1] = color  # Right border
        output_grid[rel_row, rel_col:rel_col + width] = color  # Top border
        output_grid[rel_row + height - 1, rel_col:rel_col + width] = color  # Bottom border

    return output_grid