"""
1. **Divide into Sections:** Split the input grid into horizontal sections based on solid, single-color lines that span the entire width of the grid. The separator color is consistent within each example but can vary between examples.

2. **Identify Striped Pattern:** Within each section, identify the repeating striped pattern. The stripe consists of two alternating colors. One of the colors in the stripe is always '0'.

3. **Identify Highlight Colors**: Within each section, the "highlight" colors are those that *do not* belong to the striped pattern of that section.

4. **Determine Output Colors**: The output color palette consists of the distinct highlight colors from across all sections.

5. **Construct Output Grid (3x3):**
    *   The output grid is always 3x3.
    *   There are potentially several relationships between the layout of highlight colors and the layout of the output:
        * The number of sections in the input might determine layout
        * The number of highlights of a color in a section might influence output

6. **Populate output**:
    * For each highlight color:
       * The sections that *contain* highlights determine which rows/cols will have
         that color.
       * Count the number of highlight sections - use this to determine how to fill
         the 3x3 output with that color
       * if the number of sections is less than 3, there will be empty (0) rows or
         columns in the output
"""

import numpy as np

def get_sections(grid):
    """Splits the grid into sections based on separator lines."""
    rows, cols = grid.shape
    separator_rows = []
    for i in range(rows):
        if len(np.unique(grid[i, :])) == 1:
            separator_rows.append(i)

    sections = []
    start = 0
    for i in separator_rows:
        sections.append(grid[start:i, :])
        start = i + 1
    sections.append(grid[start:, :])  # Add the last section
    return sections

def get_separator_color(grid):
    """Finds the color of the separator lines."""
    for i in range(grid.shape[0]):
        unique_colors = np.unique(grid[i,:])
        if len(unique_colors) == 1:
            return unique_colors[0]
    return None # should never happen

def get_stripe_colors(section):
    """Identifies the two colors forming the striped pattern within a section."""
    #  get rows that are not the separator
    rows = [row for row in section if len(np.unique(row)) > 1]

    # get all unique color values
    colors = set()

    # add colors in if not separator
    for row in rows:
        colors.update(np.unique(row))

    colors = list(colors)

    # return the colors if 0 is one of them
    if 0 in colors and len(colors) == 2:
        return colors
    elif len(colors)>2:
        return [c for c in colors if 0 in colors]
    else:
      return None


def get_highlight_colors(section, stripe_colors):
    """Identifies the highlight colors within a section."""
    unique_colors = np.unique(section)
    highlight_colors = [color for color in unique_colors if color not in stripe_colors]
    return highlight_colors

def transform(input_grid):
    """Transforms the input grid to the output grid based on the defined rules."""

    # 1. Divide into Sections
    sections = get_sections(input_grid)
    separator_color = get_separator_color(input_grid)

    # 2 & 3. Identify Striped and Highlight Colors for each section
    all_highlight_colors = set()
    section_highlights = []  # Store highlight colors for each section
    for section in sections:
        stripe_colors = get_stripe_colors(section)
        if stripe_colors:
          highlight_colors = get_highlight_colors(section, stripe_colors)
          all_highlight_colors.update(highlight_colors)
          section_highlights.append(highlight_colors)
        else:
          section_highlights.append([]) # no stripe, so no highlights

    # 4. Determine Output Colors
    output_colors = sorted(list(all_highlight_colors))

    # 5. Construct Output Grid (3x3)
    output_grid = np.zeros((3, 3), dtype=int)

    # 6. Populate Output Grid
    # build map of which sections contain colors
    color_section_map = {color:[] for color in output_colors}

    # build section map
    for i, highlights in enumerate(section_highlights):
      for color in highlights:
        color_section_map[color].append(i)

    # now use map to populate output grid
    for color, sections_present in color_section_map.items():
      if len(sections_present) > 0 :

        if len(output_colors) == 1: # one output color
          if len(sections_present) == 1:
            output_grid[1,1] = color
          elif len(sections_present) == 2:
            output_grid[0,:] = color
            output_grid[2,:] = color
          else:
            output_grid[:,:] = color
        elif len(output_colors) == 2:  # 2 colors
            if len(sections_present) == 1:
              output_grid[sections_present[0],sections_present[0]] = color
            if len(sections_present) == 2:
              # use sections to create L shape
              output_grid[sections_present[0],:] = color
              output_grid[sections_present[1],sections_present[1]] = color
            elif len(sections_present) >= 3: # use all sections
              # use sections to create L shape
              output_grid[0,:] = color
              output_grid[1,1] = color
              output_grid[2,:] = color
        elif len(output_colors) >= 3: # use sections_present to fill grid
          for section_idx in sections_present:
            if section_idx < 3: # protect from index out of bounds
              output_grid[section_idx,:] = color

    return output_grid