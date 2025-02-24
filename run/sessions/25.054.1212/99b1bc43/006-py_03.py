"""
1.  **Input:** A 9x4 grid.
2.  **Output:** A 4x4 grid.
3.  **Sections:** Divide the input into five sections:
    *   Section 1: Rows 1-2
    *   Section 2: Rows 3-4
    *   Section 3: Row 5
    *   Section 4: Rows 6-7
    *   Section 5: Rows 8-9
4.  **Output Row 1:**
    *   If *any* pixel in Section 1 or Section 2 is *not* 0 or 1, the output row is all green (3).
    *   Otherwise, perform a modified XOR operation between Row 1 and Row 2.
5.  **Output Row 2:**
    *   If *any* pixel in Section 1 or Section 2 is *not* 0 or 1, the output row is all green (3).
    *   Otherwise, perform a modified XOR operation between Row 3 and Row 4.
6.  **Output Row 3:**
    *  If *all* pixels on Row 5 are the *same* non-zero color, the output row is all green (3).
    *   Otherwise, perform a modified XOR operation between row 5 and itself (which is equivalent to copy)
7.  **Output Row 4:**
    *   If *any* pixel in Section 4 or Section 5 is *not* 0 or 1, the output row is all green (3).
    *   Otherwise, perform a modified XOR operation between Row 6 and Row 7.
8.  **Modified XOR Operation:**
    *   If both pixels are the same, the result is 0.
    *   If one pixel is 0 and the other is 1, the result is 0.
    *   If one pixel is 0 and the other is not 0 or 1, the result is the non-zero pixel's value.
    * If both pixels have colors other than 0 or 1:
      * Collect all colors used in related section(s). For row 1 and 2, it is Section 1 and 2. For row 4, it is Section 4 and 5.
      * If the colors are different, cycle through the collected colors.

9. **Color cycling rule:**
    * the available color list is all colors that appear in the related section. For row 1 and 2, it is Section 1 and 2. For row 4, it is Section 4 and 5.
    * if two pixels requires using the color cycling rule, then pick the next color in the available colors. Wrap around when reach to the end.
"""

import numpy as np

def get_section_colors(section):
    # get section colors
    colors = []
    for c in np.unique(section):
        if c != 0 and c not in colors:
            colors.append(c)
    return colors

def modified_xor(row1, row2, section1=None, section2=None):
    # modified xor
    output_row = []
    colors = []
    if section1 is not None:
      colors.extend(get_section_colors(section1))
    if section2 is not None:
      colors.extend(get_section_colors(section2))
    
    colors = sorted(list(set(colors))) # unique and sorted
    color_index = 0

    for i in range(len(row1)):
        if row1[i] == row2[i]:
            output_row.append(0)
        elif (row1[i] == 0 and row2[i] == 1) or (row1[i] == 1 and row2[i] == 0):
            output_row.append(0)
        elif row1[i] == 0:
            output_row.append(row2[i])
        elif row2[i] == 0:
            output_row.append(row1[i])
        else:
            # both are not zero or one, and different
            if len(colors)>0:
                output_row.append(colors[color_index % len(colors)])
                color_index += 1
            else:
              output_row.append(0)

    return np.array(output_row)

def check_for_other_colors(section):
    # Check if any pixel in the section is not 0 or 1.
    for x in np.nditer(section):
        if x != 0 and x != 1:
            return True
    return False

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros((4, input_grid.shape[1]), dtype=int)

    # Section definitions
    section1 = input_grid[0:2, :]
    section2 = input_grid[2:4, :]
    section3 = input_grid[4:5, :]
    section4 = input_grid[5:7, :]
    section5 = input_grid[7:9, :]

    # Output Row 1
    if check_for_other_colors(section1) or check_for_other_colors(section2):
        output_grid[0, :] = 3
    else:
        output_grid[0, :] = modified_xor(input_grid[0, :], input_grid[1, :], section1, section2)

    # Output Row 2
    if check_for_other_colors(section1) or check_for_other_colors(section2):
        output_grid[1, :] = 3
    else:
        output_grid[1, :] = modified_xor(input_grid[2, :], input_grid[3, :], section1, section2)

    # Output Row 3
    unique_colors_row5 = np.unique(input_grid[4, :])
    if len(unique_colors_row5) == 1 and unique_colors_row5[0] != 0:
        output_grid[2, :] = 3
    else:
        output_grid[2,:] = modified_xor(input_grid[4,:], input_grid[4,:])

    # Output Row 4
    if check_for_other_colors(section4) or check_for_other_colors(section5):
        output_grid[3, :] = 3
    else:
        output_grid[3, :] = modified_xor(input_grid[5, :], input_grid[6, :], section4, section5)

    return output_grid.tolist()