"""
1.  **Identify Separators:** Find all vertical columns where *all* pixels are gray (value 5).
2.  **Copy Separators:** Copy all gray separator columns from the input to the output.
3.  **Segment:** Divide the input grid into sections. A section is a continuous block of columns between two separators, or between the edge of the grid and a separator.
4.  **Reflect Sections:** For each section:
    *   Iterate through each row of the current section.
    *   Within that row, identify any white regions (contiguous blocks of white pixels).
    *   For each white region, treat it as a horizontal "mirror".
    *   Swap the pixels to the left of the mirror with the pixels to the right of the mirror over the mirror, such as to reflect those portions of the image.
5. **Assemble Output** Recombine the reflected sections and separator columns to form the final output grid. The separators should remain unchanged.
"""

import numpy as np

def find_gray_columns(grid):
    """Finds the indices of columns that are entirely gray (value 5)."""
    gray_columns = []
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 5):
            gray_columns.append(j)
    return gray_columns

def reflect_row(row):
    """Reflects a single row based on white regions as mirrors."""
    new_row = np.copy(row)
    white_starts = []
    white_ends = []
    in_white = False
    for i, val in enumerate(row):
        if val == 0 and not in_white:
            in_white = True
            white_starts.append(i)
        elif val != 0 and in_white:
            in_white = False
            white_ends.append(i - 1)
    if in_white:
        white_ends.append(len(row) - 1)

    for start, end in zip(white_starts, white_ends):
        mirror_len = end - start + 1
        left = start - 1
        right = end + 1
        while left >= 0 and right < len(row):
            new_row[left], new_row[right] = new_row[right], new_row[left]
            left -= 1
            right += 1
    return new_row

def reflect_section(section):
    """Reflects each row of a section."""
    reflected_section = np.copy(section)
    for i in range(section.shape[0]):
        reflected_section[i, :] = reflect_row(section[i, :])
    return reflected_section

def transform(input_grid):
    """Transforms the input grid according to the reflection rules."""
    # Initialize output grid
    output_grid = np.zeros_like(input_grid)
    
    # Find and copy gray columns
    gray_columns = find_gray_columns(input_grid)
    for col in gray_columns:
        output_grid[:, col] = input_grid[:, col]

    # Define sections and reflect
    start = 0
    for end in gray_columns + [input_grid.shape[1]]:  # Include the end of the grid
        if start != end: # prevent empty sections
            section = input_grid[:, start:end]
            reflected_section = reflect_section(section)
            output_grid[:, start:end] = reflected_section
        start = end + 1  # Start of the next section

    return output_grid