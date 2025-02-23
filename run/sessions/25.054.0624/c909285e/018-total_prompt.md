# c909285e • 018 • refine_coder

---

Previous Code:
```python
"""
1.  **Find the Border:** Scan the input grid to identify a rectangular border. The border is defined as a contiguous region of a single color that completely encloses an inner rectangular area. The border may have different colors on the inner and outer edges, or have more than one row or column making it thicker.
2.  **Extract Inner Region:** Once the border is identified, extract the rectangular region located *inside* the border. This inner region is the area of interest.
3.  **Conditional Color Substitution:** Examine the *input* grid. If color 5 is adjacent to the *outer* border color anywhere, replace all instances of color 5 with color 6 *within the extracted inner region*.
4. **Output:** The transformed "inner region" from step 3 becomes the output grid.
"""

import numpy as np

def find_border(grid):
    """Finds the rectangular border and returns its boundaries."""
    rows, cols = grid.shape
    
    # Find top-left corner of the border
    for top in range(rows):
        for left in range(cols):
            border_color = grid[top, left]
            
            # Check for rectangular shape and complete enclosure
            if is_valid_border(grid, top, left, border_color):
                bottom, right = find_bottom_right(grid, top, left, border_color)
                return top, left, bottom, right, border_color
    return None, None, None, None, None

def is_valid_border(grid, top, left, border_color):
    """Checks if the border at (top, left) is valid."""
    rows, cols = grid.shape

    # Check for minimum border thickness (at least 1)
    if top >= rows - 1 or left >= cols - 1:
        return False
    
    #Check to see if there is a bottom right corner
    bottom, right = find_bottom_right(grid, top, left, border_color)
    if bottom == -1:
        return False
    
    #check to make sure all pixels are the same color on the border.
    for row in range(top, bottom + 1):
        if grid[row, left] != border_color or grid[row, right] != border_color:
            return False
    for col in range(left, right+1):
        if grid[top, col] != border_color or grid[bottom, col] != border_color:
            return False
    
    #now check to make sure there is no border color inside.
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            if grid[row, col] == border_color:
                return False
    
    return True
    
def find_bottom_right(grid, top, left, border_color):
    rows, cols = grid.shape

    # Find bottom-right corner of the border
    bottom = top
    while bottom + 1 < rows and grid[bottom + 1, left] == border_color:
        bottom += 1

    right = left
    while right + 1 < cols and grid[top, right + 1] == border_color:
        right += 1
        
    #check corner
    if grid[bottom, right] != border_color:
        return -1, -1 #invalid corner

    return bottom, right

def extract_inner_region(grid, top, left, bottom, right):
    """Extracts the inner region of the border."""
    return grid[top+1:bottom, left+1:right]

def conditional_color_substitution(grid, inner_region, border_color):
    """Performs color substitution if 5 is adjacent to the border."""
    rows, cols = grid.shape
    
    # Check for adjacency of 5 to the border_color in the original grid
    substitution_needed = False
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 5:
                # Check neighbors for border_color
                neighbors = []
                if r > 0: neighbors.append(grid[r-1, c])
                if r < rows - 1: neighbors.append(grid[r+1, c])
                if c > 0: neighbors.append(grid[r, c-1])
                if c < cols - 1: neighbors.append(grid[r, c+1])
                
                if border_color in neighbors:
                    substitution_needed = True
                    break
        if substitution_needed:
            break
            
    if substitution_needed:
         return np.where(inner_region == 5, 6, inner_region)
    else:
        return inner_region

def transform(input_grid):
    # Convert input grid to a NumPy array
    grid = np.array(input_grid)

    # 1. Find the Border
    top, left, bottom, right, border_color = find_border(grid)
    
    if top is None:  # No border found
        return None

    # 2. Extract Inner Region
    inner_region = extract_inner_region(grid, top, left, bottom, right)

    # 3. Conditional Color Substitution
    transformed_inner_region = conditional_color_substitution(grid, inner_region, border_color)
    
    # 4. Output
    return transformed_inner_region.tolist()
```

Train Set Results:

## Example 1:

Input:
```
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
2 2 2 4 2 5 2 4 2 2 2 5 2 2 2 4 2 5 2 4 2 2 2 5
4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5
8 8 2 4 8 5 8 4 2 8 8 5 8 8 2 4 8 5 8 4 2 8 8 5
5 5 5 5 5 3 3 3 3 3 3 3 5 5 5 5 5 5 5 5 5 5 5 5
0 0 2 4 8 3 0 4 2 8 0 3 0 0 2 4 0 5 0 4 2 0 0 5
4 4 4 4 4 3 4 4 4 4 4 3 4 4 4 4 4 5 4 4 4 4 4 5
2 2 2 4 2 3 2 4 2 2 2 3 2 2 2 4 2 5 2 4 2 2 2 5
8 8 2 4 8 3 8 4 2 8 8 3 8 8 2 4 8 5 8 4 2 8 8 5
0 0 2 4 8 3 0 4 2 8 0 3 0 0 2 4 0 5 0 4 2 0 0 5
5 5 5 5 5 3 3 3 3 3 3 3 5 5 5 5 5 5 5 5 5 5 5 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
2 2 2 4 2 5 2 4 2 2 2 5 2 2 2 4 2 5 2 4 2 2 2 5
4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5 4 4 4 4 4 5
2 2 2 4 2 5 2 4 2 2 2 5 2 2 2 4 2 5 2 4 2 2 2 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
0 0 2 4 8 5 0 4 2 8 0 5 0 0 2 4 0 5 0 4 2 0 0 5
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
```
Expected Output:
```
3 3 3 3 3 3 3
3 0 4 2 8 0 3
3 4 4 4 4 4 3
3 2 4 2 2 2 3
3 8 4 2 8 8 3
3 0 4 2 8 0 3
3 3 3 3 3 3 3
```
Transformed Output:
```

```
![Transformed Image](016-py_09-train-example_1.png)
match: False
pixels_off: None
size_correct: False
color_palette_correct: True
correct_pixel_counts: False

## Example 2:

Input:
```
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
8 8 2 2 2 2 2 2 2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
3 3 2 3 3 8 3 3 2 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3
1 1 2 3 1 8 1 3 2 1 1 8 1 1 8 3 1 8 1 3 8 1 1 8 1 1
8 8 2 8 8 8 8 8 2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
0 0 2 3 1 8 0 3 2 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
3 3 2 3 3 8 3 3 2 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3
8 8 2 2 2 2 2 2 2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
1 1 8 3 1 8 1 3 8 1 1 8 1 1 8 3 1 8 1 3 8 1 1 8 1 1
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3 8 3 3
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
1 1 8 3 1 8 1 3 8 1 1 8 1 1 8 3 1 8 1 3 8 1 1 8 1 1
0 0 8 3 1 8 0 3 8 1 0 8 0 0 8 3 0 8 0 3 8 0 0 8 1 0
```
Expected Output:
```
2 2 2 2 2 2 2
2 3 3 8 3 3 2
2 3 1 8 1 3 2
2 8 8 8 8 8 2
2 3 1 8 0 3 2
2 3 3 8 3 3 2
2 2 2 2 2 2 2
```
Transformed Output:
```

```
![Transformed Image](016-py_09-train-example_2.png)
match: False
pixels_off: None
size_correct: False
color_palette_correct: True
correct_pixel_counts: False

## Example 3:

Input:
```
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3
1 1 3 1 8 5 1 1 3 8 1 5 1 1 3 1 1 5 1 8 3 1 1 5 8 1 3 1
8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
1 1 3 1 8 5 1 1 3 8 1 5 1 1 3 1 1 5 1 8 3 1 1 5 8 1 3 1
3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3
8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3
1 1 3 1 8 5 1 1 3 8 1 5 1 1 3 1 1 5 1 8 3 1 1 5 8 1 3 1
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
5 5 5 5 5 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
0 0 3 1 8 6 0 1 3 8 0 6 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
8 8 3 8 8 6 8 8 3 8 8 6 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8
3 3 3 3 3 6 3 3 3 3 3 6 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3
0 0 3 1 8 6 0 1 3 8 0 6 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
0 0 3 1 8 6 0 1 3 8 0 6 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
5 5 5 5 5 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8 8 5 8 8 3 8
0 0 3 1 8 5 0 1 3 8 0 5 0 0 3 1 0 5 0 8 3 0 0 5 8 0 3 1
3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3 3 5 3 3 3 3
1 1 3 1 8 5 1 1 3 8 1 5 1 1 3 1 1 5 1 8 3 1 1 5 8 1 3 1
```
Expected Output:
```
6 6 6 6 6 6 6
6 0 1 3 8 0 6
6 8 8 3 8 8 6
6 3 3 3 3 3 6
6 0 1 3 8 0 6
6 0 1 3 8 0 6
6 6 6 6 6 6 6
```
Transformed Output:
```

```
![Transformed Image](016-py_09-train-example_3.png)
match: False
pixels_off: None
size_correct: False
color_palette_correct: True
correct_pixel_counts: False
Here's a breakdown of the provided information, an analysis of the errors, and a revised natural language program:

**General Assessment and Strategy**

The initial natural language program and the corresponding code have fundamental flaws. While the concept of identifying a border and extracting an inner region is partially correct, the border identification logic and, crucially, the conditional color substitution are incorrect. The existing code seems to find borders, but not on every image and it does not always find the entire border when it identifies a region. The color substitution logic is applied too broadly and depends on the original grid, not the extracted region. The code also appears to try to change colors outside the region, causing errors. The code does not always identify a border on all of the provided examples.

The strategy to resolve these errors involves:

1.  **Improving Border Detection:** The `find_border` and related functions need to reliably detect the *outermost* border of a consistent color, regardless of "noise" or other colored pixels *inside* the border.  It must also handle cases where the border is on the very edge of the image.
2.  **Correcting Inner Region Extraction:** Once the correct border is found, `extract_inner_region` should correctly extract the area *inside* that border.
3. **Correcting Conditional Color Substitution**: The main logic of color substitution should be made simpler. Based on the example outputs, if an inner region contains the color `5`, then all instances of color `5` in the input *becomes* color `6` in the output.

**Metrics and Observations (using code execution for verification)**

```python
import numpy as np
from collections import Counter

def analyze_results(input_grid, expected_output, transformed_output):
    """Analyzes the results and returns a report."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    
    #convert empty lists to empty arrays
    if transformed_output == []:
        transformed_output = np.array([])
    else:
        transformed_output = np.array(transformed_output)

    report = {
        "match": np.array_equal(expected_output, transformed_output),
        "size_correct": expected_output.shape == transformed_output.shape if transformed_output.size>0 else False,
        "color_palette_correct": True,  # Placeholder, needs detailed check
        "correct_pixel_counts": True,  # Placeholder, needs detailed check
        "pixels_off": [],
    }
    
    if report["size_correct"] and not report["match"]:
      report["pixels_off"] = np.where(expected_output != transformed_output)

    # --- Detailed Color Palette and Pixel Count Checks ---
    if report["size_correct"]:
      expected_colors = Counter(expected_output.flatten())
      transformed_colors = Counter(transformed_output.flatten())
      
      all_colors = set(expected_colors.keys()).union(transformed_colors.keys())

      for color in all_colors:
        if expected_colors[color] != transformed_colors[color]:
          report["correct_pixel_counts"] = False
          break
        
      if set(expected_colors.keys()) != set(transformed_colors.keys()):
        report["color_palette_correct"] = False

    return report

#Example usage with provided data:
inputs = [
    # [Example 1 Input...],
    # [Example 2 Input...],
    # [Example 3 Input...],
    [
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5, 2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5],
[4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5],
[8, 8, 2, 4, 8, 5, 8, 4, 2, 8, 8, 5, 8, 8, 2, 4, 8, 5, 8, 4, 2, 8, 8, 5],
[5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 2, 4, 8, 3, 0, 4, 2, 8, 0, 3, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5],
[2, 2, 2, 4, 2, 3, 2, 4, 2, 2, 2, 3, 2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5],
[8, 8, 2, 4, 8, 3, 8, 4, 2, 8, 8, 3, 8, 8, 2, 4, 8, 5, 8, 4, 2, 8, 8, 5],
[0, 0, 2, 4, 8, 3, 0, 4, 2, 8, 0, 3, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5, 2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5],
[4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 5],
[2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5, 2, 2, 2, 4, 2, 5, 2, 4, 2, 2, 2, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[0, 0, 2, 4, 8, 5, 0, 4, 2, 8, 0, 5, 0, 0, 2, 4, 0, 5, 0, 4, 2, 0, 0, 5],
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
],
    # [Example 2 Input...],
    [
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[8, 8, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[3, 3, 2, 3, 3, 8, 3, 3, 2, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3],
[1, 1, 2, 3, 1, 8, 1, 3, 2, 1, 1, 8, 1, 1, 8, 3, 1, 8, 1, 3, 8, 1, 1, 8, 1, 1],
[8, 8, 2, 8, 8, 8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[0, 0, 2, 3, 1, 8, 0, 3, 2, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[3, 3, 2, 3, 3, 8, 3, 3, 2, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3],
[8, 8, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[1, 1, 8, 3, 1, 8, 1, 3, 8, 1, 1, 8, 1, 1, 8, 3, 1, 8, 1, 3, 8, 1, 1, 8, 1, 1],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3, 8, 3, 3],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[1, 1, 8, 3, 1, 8, 1, 3, 8, 1, 1, 8, 1, 1, 8, 3, 1, 8, 1, 3, 8, 1, 1, 8, 1, 1],
[0, 0, 8, 3, 1, 8, 0, 3, 8, 1, 0, 8, 0, 0, 8, 3, 0, 8, 0, 3, 8, 0, 0, 8, 1, 0]
],
    # [Example 3 Input...],
    [
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
[1, 1, 3, 1, 8, 5, 1, 1, 3, 8, 1, 5, 1, 1, 3, 1, 1, 5, 1, 8, 3, 1, 1, 5, 8, 1, 3, 1],
[8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8],
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[1, 1, 3, 1, 8, 5, 1, 1, 3, 8, 1, 5, 1, 1, 3, 1, 1, 5, 1, 8, 3, 1, 1, 5, 8, 1, 3, 1],
[3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
[8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
[1, 1, 3, 1, 8, 5, 1, 1, 3, 8, 1, 5, 1, 1, 3, 1, 1, 5, 1, 8, 3, 1, 1, 5, 8, 1, 3, 1],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[0, 0, 3, 1, 8, 6, 0, 1, 3, 8, 0, 6, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[8, 8, 3, 8, 8, 6, 8, 8, 3, 8, 8, 6, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8],
[3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
[0, 0, 3, 1, 8, 6, 0, 1, 3, 8, 0, 6, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[0, 0, 3, 1, 8, 6, 0, 1, 3, 8, 0, 6, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
[8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8, 8, 5, 8, 8, 3, 8],
[0, 0, 3, 1, 8, 5, 0, 1, 3, 8, 0, 5, 0, 0, 3, 1, 0, 5, 0, 8, 3, 0, 0, 5, 8, 0, 3, 1],
[3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
[1, 1, 3, 1, 8, 5, 1, 1, 3, 8, 1, 5, 1, 1, 3, 1, 1, 5, 1, 8, 3, 1, 1, 5, 8, 1, 3, 1]
],
]

expected_outputs = [
    # [Example 1 Expected Output...],
    # [Example 2 Expected Output...],
    # [Example 3 Expected Output...],
    [
[3, 3, 3, 3, 3, 3, 3],
[3, 0, 4, 2, 8, 0, 3],
[3, 4, 4, 4, 4, 4, 3],
[3, 2, 4, 2, 2, 2, 3],
[3, 8, 4, 2, 8, 8, 3],
[3, 0, 4, 2, 8, 0, 3],
[3, 3, 3, 3, 3, 3, 3]
],
    [
[2, 2, 2, 2, 2, 2, 2],
[2, 3, 3, 8, 3, 3, 2],
[2, 3, 1, 8, 1, 3, 2],
[2, 8, 8, 8, 8, 8, 2],
[2, 3, 1, 8, 0, 3, 2],
[2, 3, 3, 8, 3, 3, 2],
[2, 2, 2, 2, 2, 2, 2]
],
    [
[6, 6, 6, 6, 6, 6, 6],
[6, 0, 1, 3, 8, 0, 6],
[6, 8, 8, 3, 8, 8, 6],
[6, 3, 3, 3, 3, 3, 6],
[6, 0, 1, 3, 8, 0, 6],
[6, 0, 1, 3, 8, 0, 6],
[6, 6, 6, 6, 6, 6, 6]
]
]

transformed_outputs = [
    # [Example 1 Transformed Output...],
    # [Example 2 Transformed Output...],
    # [Example 3 Transformed Output...],
    [],
    [],
    [],
]


for i, (inp, exp, trans) in enumerate(zip(inputs, expected_outputs, transformed_outputs)):
    report = analyze_results(inp, exp, trans)
    print(f"## Example {i+1}:")
    print(f"match: {report['match']}")
    print(f"pixels_off: {report['pixels_off']}")
    print(f"size_correct: {report['size_correct']}")
    print(f"color_palette_correct: {report['color_palette_correct']}")
    print(f"correct_pixel_counts: {report['correct_pixel_counts']}")
    print("-" * 20)
```

```
## Example 1:
match: False
pixels_off: []
size_correct: False
color_palette_correct: True
correct_pixel_counts: True
--------------------
## Example 2:
match: False
pixels_off: []
size_correct: False
color_palette_correct: True
correct_pixel_counts: True
--------------------
## Example 3:
match: False
pixels_off: []
size_correct: False
color_palette_correct: True
correct_pixel_counts: True
--------------------
```
As expected, all examples fail because the function returns `None`.  The `find_border` function is not correctly identifying a border, so the rest of the transformation cannot proceed.

**YAML Facts**

```yaml
- task: 016
  example_1:
    input:
      objects:
        - type: grid
          properties:
            colors: [0, 2, 4, 8, 5, 3]
            has_border: true
            border_color: varies # Border changes within the same input!
        - type: border
          properties:
              color: varies
        - type: inner_region
          properties:
            contains_color_5: true
    output:
      objects:
        - type: grid
          properties:
            colors: [3, 0, 4, 2, 8]
        - type: transformed_inner_region # Inner region is the complete output.

  example_2:
    input:
      objects:
        - type: grid
          properties:
            colors: [0, 8, 3, 1, 2]
            has_border: true
            border_color: varies  # Again, changing border.
        - type: inner_region
           properties:
              contains_color_5: false
    output:
      objects:
        - type: grid
          properties:
              colors: [2, 3, 8, 1,
**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
