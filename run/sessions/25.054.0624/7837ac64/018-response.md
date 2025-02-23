# 7837ac64 • 018 • refine_coder

---
```python
"""
1.  **Section Division:** Divide the input grid into horizontal sections. A section is defined as the area between single-color, full-width, horizontal lines. The lines themselves are not part of any section.

2.  **Stripe Identification (Irrelevant for Output):** Within each section, identify the two colors that make up the striped pattern. One of these colors is always color `0`. This step is useful for *identifying* highlight colors, but not used in determining the output grid layout.

3.  **Highlight Color Identification:** Within each section, the "highlight" colors are any colors *not* part of the section's striped pattern.

4. **Output Palette and Color Presence**: Determine the set of unique highlight colors across all sections. These colors will be the only colors in the output.

5.  **Output Grid Construction (3x3):**
    *   The output is *always* a 3x3 grid.
    * Determine, for each highlight color, in *which* sections of the input grid it appears.
    * If a color appears in:
        - Only the first section of highlights, the top-left element of the output
          is that color
        - Sections 2 & 3 (but *not* 4+), that color appears in an "L" shape in the
          output.
        - Sections that include 4 and greater:
          - If the highlight appears in exactly 3 sections, put that color in the bottom
            right element.
    * Colors can overlap.
    * Fill the output grid using this color section mapping.

6. If there are locations in the 3x3 grid that have not been set by the rules
   above, set them to 0
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
    """Transforms the input grid according to the rules."""

    # 1. Section Division
    sections = get_sections(input_grid)
    separator_color = get_separator_color(input_grid)

    # 2 & 3. Stripe and Highlight Color Identification
    all_highlight_colors = set()
    section_highlights = []  # Store highlight colors for each section
    for section in sections:
        stripe_colors = get_stripe_colors(section)
        if stripe_colors:
            highlight_colors = get_highlight_colors(section, stripe_colors)
            all_highlight_colors.update(highlight_colors)
            section_highlights.append(highlight_colors)
        else:
            section_highlights.append([])  # No stripe, so no highlights

    # 4. Output Palette
    output_colors = sorted(list(all_highlight_colors))

    # 5. Output Grid Construction (3x3)
    output_grid = np.zeros((3, 3), dtype=int)

    # Build map of which sections contain colors
    color_section_map = {color: [] for color in output_colors}
    for i, highlights in enumerate(section_highlights):
        for color in highlights:
            color_section_map[color].append(i)

    # Populate Output Grid based on section presence
    for color, sections_present in color_section_map.items():
        if not sections_present:
            continue

        # Check the sections where the color appears
        if len(sections_present) == 1 and sections_present[0] == 0 :
            output_grid[0, 0] = color  # Top-left corner
        elif all(sec < 4 for sec in sections_present) and 1 in sections_present and 2 in sections_present:
            output_grid[0, 0:2] = color  # row
            output_grid[1:3, 1] = color # column
        elif 3 in sections_present and len(sections_present) == 3 :
            output_grid[2,2] = color
        elif len(sections_present)>=3 and 3 in sections_present:
            output_grid[2, 0:2] = color  #row
            output_grid[0, 0] = color  # diag
            output_grid[1, 1] = color

    return output_grid
```
