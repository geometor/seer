# 6-0520fde7 • 024 • refine_coder

---
```python
"""
1.  **Initialize:** Create a 3x3 output grid filled with white (0).

2.  **Identify Separators:** Locate the grey (5) pixels in the input grid. These act as vertical separators, dividing the input grid into three vertical sections. If a grey separator is not found, the complete row or grid is considered a section.

3. **Sectioned Blue Counting:** Iterate through the sections in the input grid created by the vertical grey lines, starting at the left section and moving to the right.

4.  **Transformation:** For each section:
    * Count the number of blue pixels (1).
    * If a blue pixel is present in the section, turn the corresponding column in the *middle* row of the output grid red (2).
	* Map sections to the output grid sequentially:
        *   First section (left-most) maps to output column 0.
        *   Second section maps to output column 1.
        *   Third section (right-most) maps to output column 2.

5.  **Ignore other colors:** Pixels in the input grid that are not blue (1) or grey (5) do not directly affect the output.
"""

import numpy as np

def get_sections(input_grid):
    # Find the column indices of grey pixels (5) that act as separators
    grey_cols = np.where(input_grid == 5)[1]
    # Get unique separator column indices
    separator_cols = np.unique(grey_cols)

    # Determine section boundaries
    sections = []
    start = 0
    for col in separator_cols:
        sections.append((start, col))  # Store start and end column indices
        start = col + 1
    sections.append((start, input_grid.shape[1])) # Add the last section

    return sections


def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the sections defined by grey separators
    sections = get_sections(input_grid)

    # Iterate through sections and map to the output grid's middle row.
    for i, (start, end) in enumerate(sections):
        section_has_blue = False
        for row in range(input_grid.shape[0]):
            for col in range(start, end):
                 if input_grid[row, col] == 1:
                    section_has_blue = True
                    break  # Optimization: Stop checking once blue is found
            if section_has_blue:
                break       # exit out of rows when found
        if section_has_blue:
            if i < 3:  # Make sure we don't exceed output grid bounds
               output_grid[1, i] = 2  # Set middle row, corresponding column to red

    return output_grid
```
