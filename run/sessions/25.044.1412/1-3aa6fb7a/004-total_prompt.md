# 25.044.1412 • 1-3aa6fb7a • 004 example_2 - CODE

---

**input**
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x76B93F2115A0>
**output**
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x76B93F211930>

*text:*
**Natural Language Program:**

1. **Identify Connected Regions:** Detect the two distinct, connected regions formed by cells with value '8' in the input grid.
2. **Determine Bounding Boxes:** For each of these regions, calculate the smallest bounding box that encloses all cells of the region. This box is defined by its top row, bottom row, left column, and right column.
3. **Order Regions:** Compare the bounding boxes of the two regions. The region whose bounding box has a smaller top row index, or in case of a tie, a smaller left column index, is considered the "first" region. The other is the "second" region.
4. **Modify First Region:** For the "first" region, locate the cell at the intersection of the top row of its bounding box and the right column of its bounding box. Change the value of this cell to '1'.
5. **Modify Second Region:** For the "second" region, locate the cell at the intersection of the bottom row of its bounding box and the left column of its bounding box. Change the value of this cell to '1'.
6. **Preserve Unchanged Cells:** All cells in the grid that are not modified in steps 4 and 5 retain their original values from the input grid.

**Explanation of Objects, Properties, and Actions:**

* **Objects:**
    * **Grid:** The input and output 2D array of numbers.
    * **Regions of '8's:** Connected groups of cells with value '8'.
    * **Bounding Box:** Rectangular area defined by the minimum and maximum row and column indices of a region.
    * **Cell:** Individual element in the grid, identified by its row and column index.
* **Properties (Predicates):**
    * **Connected:** Property of cells being adjacent (horizontally or vertically) and having the same value ('8').
    * **Value '8':** Property of a cell having the value 8.
    * **Bounding Box Coordinates:** Top row, bottom row, left column, right column of a bounding box.
    * **Top-Left Corner:** The cell at the top-left of a bounding box, used for ordering.
    * **Top-Right Corner:** The cell at the top-right of a bounding box.
    * **Bottom-Left Corner:** The cell at the bottom-left of a bounding box.
* **Actions:**
    * **Identify:** Detect regions of '8's.
    * **Calculate:** Determine the bounding box for each region.
    * **Order:** Rank regions based on their bounding box top-left corner.
    * **Locate:** Find specific cells within the bounding box (top-right, bottom-left).
    * **Change Value:** Modify the value of a cell to '1'.
    * **Preserve:** Keep the value of cells unchanged.

*text:*
```python
"""
1. Identify Connected Regions: Detect the two distinct, connected regions formed by cells with value '8' in the input grid.
2. Determine Bounding Boxes: For each of these regions, calculate the smallest bounding box that encloses all cells of the region. This box is defined by its top row, bottom row, left column, and right column.
3. Order Regions: Compare the bounding boxes of the two regions. The region whose bounding box has a smaller top row index, or in case of a tie, a smaller left column index, is considered the "first" region. The other is the "second" region.
4. Modify First Region: For the "first" region, locate the cell at the intersection of the top row of its bounding box and the right column of its bounding box. Change the value of this cell to '1'.
5. Modify Second Region: For the "second" region, locate the cell at the intersection of the bottom row of its bounding box and the left column of its bounding box. Change the value of this cell to '1'.
6. Preserve Unchanged Cells: All cells in the grid that are not modified in steps 4 and 5 retain their original values from the input grid.
"""

import numpy as np
from collections import deque

input_grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

expected_output = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    grid = np.array(input_grid).copy() # Create a copy to avoid modifying the input

    regions = []
    visited = np.zeros_like(grid, dtype=bool)

    # Function to perform BFS for finding connected regions
    def find_region(r, c):
        region_cells = []
        q = deque([(r, c)])
        visited[r, c] = True
        while q:
            row, col = q.popleft()
            region_cells.append((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Explore neighbors
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 8 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    q.append((nr, nc))
        return region_cells

    # Identify all regions
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8 and not visited[r, c]:
                regions.append(find_region(r, c))

    region_bounding_boxes = []
    for region in regions:
        min_r = min(r for r, c in region)
        max_r = max(r for r, c in region)
        min_c = min(c for r, c in region)
        max_c = max(c for r, c in region)
        region_bounding_boxes.append(((min_r, min_c), (max_r, max_c), region)) # Store bounding box coordinates and region cells

    # Order regions
    def get_sort_key(bbox_data):
        (min_r, min_c), _, _ = bbox_data
        return (min_r, min_c)
    region_bounding_boxes.sort(key=get_sort_key)

    # Modify regions
    if len(region_bounding_boxes) >= 1:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[0]
        grid[min_r, max_c] = 1 # Top-right of first region

    if len(region_bounding_boxes) >= 2:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[1]
        grid[max_r, min_c] = 1 # Bottom-left of second region

    return grid.tolist()


if __name__ == '__main__':

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```

**input**
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x76B93F211B10>
**output**
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x76B93F211060>

*text:*
**Natural Language Program:**

1. **Identify Connected Regions:** Detect all distinct, connected regions formed by cells with value '8' in the input grid.
2. **Determine Bounding Boxes:** For each of these regions, calculate the smallest bounding box that encloses all cells of the region.
3. **Order Regions:** Order the regions based primarily on the top row index of their bounding boxes, and secondarily on the left column index in case of a tie in top row indices, to determine the first, second, and subsequent regions.
4. **Modify First Region:** For the first ordered region, locate the cell diagonally down and to the left from the top-right corner of its bounding box. Specifically, if the top-right corner is at row `r` and column `c`, examine the cell at `(r+1, c-1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
5. **Modify Second Region:** For the second ordered region, locate the cell diagonally up and to the right from the bottom-left corner of its bounding box. Specifically, if the bottom-left corner is at row `r` and column `c`, examine the cell at `(r-1, c+1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
6. **Modify Third Region:** For the third ordered region, locate the cell diagonally up and to the left from the bottom-right corner of its bounding box. Specifically, if the bottom-right corner is at row `r` and column `c`, examine the cell at `(r-1, c-1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
7. **Preserve Unchanged Cells:** All cells in the grid that are not modified in steps 4, 5, and 6 retain their original values from the input grid.

**Explanation of Objects, Properties, and Actions:**

* **Objects:**
    * **Grid:** The input and output 2D array of numbers.
    * **Regions of '8's:** Connected groups of cells with value '8'.
    * **Bounding Box:** Rectangular area defined by the minimum and maximum row and column indices of a region.
    * **Cell:** Individual element in the grid, identified by its row and column index.
    * **Corner Cells of Bounding Box:** Top-right, bottom-left, bottom-right corners of the bounding box.
    * **Diagonal Cells:** Cells located diagonally adjacent to the corner cells of the bounding boxes.
* **Properties (Predicates):**
    * **Connected:** Property of cells being adjacent (horizontally or vertically) and having the same value ('8').
    * **Value '8':** Property of a cell having the value 8.
    * **Value '0':** Property of a cell having the value 0.
    * **Bounding Box Coordinates:** Top row, bottom row, left column, right column of a bounding box.
    * **Top-Left Corner (of Bounding Box):** The cell at the top-left of a bounding box, used for ordering regions.
    * **Top-Right Corner (of Bounding Box):** The cell at the top-right of a bounding box.
    * **Bottom-Left Corner (of Bounding Box):** The cell at the bottom-left of a bounding box.
    * **Bottom-Right Corner (of Bounding Box):** The cell at the bottom-right of a bounding box.
    * **Diagonal Down-Left Cell:** Cell at (row+1, column-1) relative to a given cell.
    * **Diagonal Up-Right Cell:** Cell at (row-1, column+1) relative to a given cell.
    * **Diagonal Up-Left Cell:** Cell at (row-1, column-1) relative to a given cell.
    * **Within Grid Boundaries:** Property of a cell's coordinates being valid within the grid dimensions.
* **Actions:**
    * **Identify:** Detect regions of '8's.
    * **Calculate:** Determine the bounding box for each region.
    * **Order:** Rank regions based on their bounding box top-left corner.
    * **Locate:** Find specific corner cells of the bounding box (top-right, bottom-left, bottom-right).
    * **Examine:** Check the value of diagonal cells relative to the corner cells.
    * **Change Value:** Modify the value of a cell to '1'.
    * **Preserve:** Keep the value of cells unchanged.
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- The primary function should be named `transform`, which takes the input grid (represented as a Python list of lists) and returns the transformed output grid (also a Python list of lists).
- Include a docstring at the top of the module that contains the natural language description of the transformation rule.
- Use comments to describe the workflow.
- All major math, science and analysis libraries are available to you.
- Include an `if __name__ == '__main__':` block that:
    - Defines the input grid.
    - Defines the expected output grid.
    - Calls the `transform` function with the input grid.
    - Asserts that the transformed output matches the expected output. Print a clear message indicating success or failure.

- if your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Skeleton Template**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

input = 0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0

expected_output = 0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."

```
