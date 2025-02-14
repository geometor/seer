# 25.045.0717 • 1-3aa6fb7a • 004 example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30D570>

**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30D900>

*text:*
**Natural Language Program:**

The task is to identify and modify cells within connected regions of color 8 (azure).
1. **Identify Connected Regions:** Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. **Order the Regions:**  For each connected region, find its "top-leftmost" cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions based on their top-leftmost cells, first by row index and then by column index in ascending order. Let's call the regions Region 1 and Region 2 based on this order.
3. **Modify Region 1:** In Region 1, locate its top-leftmost cell and change its color to 1 (blue).
4. **Modify Region 2:** In Region 2, locate its bottom-rightmost cell. The bottom-rightmost cell is defined as the cell with the largest row index, and among those with the same largest row index, the largest column index. Change the color of this bottom-rightmost cell to 1 (blue).

**YAML Block:**

```yaml
task_context: "Grid transformation"
transformation_rule: "Modify cells in connected regions of color 8. For the first region (ordered by top-leftmost cell), change its top-leftmost cell to color 1. For the second region, change its bottom-rightmost cell to color 1."
objects:
  - type: "connected region"
    color: 8
    properties:
      - "top-leftmost cell"
      - "bottom-rightmost cell"
actions:
  - "identify connected regions of color 8"
  - "order regions based on top-leftmost cell position"
  - "change color of top-leftmost cell of the first region to 1"
  - "change color of bottom-rightmost cell of the second region to 1"
predicates:
  - "connected"
  - "same color"
  - "top-leftmost"
  - "bottom-rightmost"
  - "first region"
  - "second region"
```

*text:*
```python
"""
The task is to identify and modify cells within connected regions of color 8 (azure).
1. Identify Connected Regions: Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. Order the Regions:  For each connected region, find its "top-leftmost" cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions based on their top-leftmost cells, first by row index and then by column index in ascending order. Let's call the regions Region 1 and Region 2 based on this order.
3. Modify Region 1: In Region 1, locate its top-leftmost cell and change its color to 1 (blue).
4. Modify Region 2: In Region 2, locate its bottom-rightmost cell. The bottom-rightmost cell is defined as the cell with the largest row index, and among those with the same largest row index, the largest column index. Change the color of this bottom-rightmost cell to 1 (blue).
"""

import copy

def find_connected_regions(grid, color):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def get_neighbors(r, c):
        return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

    def dfs(r, c, current_region):
        visited[r][c] = True
        current_region.append((r, c))
        for nr, nc in get_neighbors(r, c):
            if is_valid(nr, nc) and grid[nr][nc] == color and not visited[nr][nc]:
                dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                current_region = []
                dfs(r, c, current_region)
                regions.append(current_region)
    return regions

def get_top_leftmost_cell(region):
    top_leftmost_cell = region[0]
    for r, c in region:
        if r < top_leftmost_cell[0] or (r == top_leftmost_cell[0] and c < top_leftmost_cell[1]):
            top_leftmost_cell = (r, c)
    return top_leftmost_cell

def get_bottom_rightmost_cell(region):
    bottom_rightmost_cell = region[0]
    for r, c in region:
        if r > bottom_rightmost_cell[0] or (r == bottom_rightmost_cell[0] and c > bottom_rightmost_cell[1]):
            bottom_rightmost_cell = (r, c)
    return bottom_rightmost_cell

def transform(input_grid):
    output_grid = copy.deepcopy(input_grid)
    regions = find_connected_regions(input_grid, 8)

    if not regions:
        return output_grid

    regions.sort(key=lambda region: get_top_leftmost_cell(region))

    if len(regions) >= 1:
        region1 = regions[0]
        tl_r1, tl_c1 = get_top_leftmost_cell(region1)
        output_grid[tl_r1][tl_c1] = 1

    if len(regions) >= 2:
        region2 = regions[1]
        br_r2, br_c2 = get_bottom_rightmost_cell(region2)
        output_grid[br_r2][br_c2] = 1

    return output_grid


if __name__ == '__main__':

    input = [
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

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30DAE0>

**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30D300>

*text:*
**Natural Language Program:**

The task is to identify connected regions of color 8 and modify a single cell adjacent to one of these regions.
1. **Identify Connected Regions:** Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. **Order Regions:** Order these regions based on their top-leftmost cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions first by row index and then by column index in ascending order.
3. **Directions Cycle:** Define a cycle of directions in the order: Right, Down, Left, Up.
4. **Iterate and Modify:** For each region in the ordered list, starting from the first region:
   a. Determine the direction from the directions cycle based on the region's order (1st region uses 'Right', 2nd uses 'Down', 3rd uses 'Left', 4th uses 'Up', and then the cycle repeats for subsequent regions if any).
   b. Calculate the coordinates of the target cell by taking the top-leftmost cell of the current region and moving one step in the determined direction.
   c. Check if the target cell is within the grid boundaries and if its color is 0.
   d. If both conditions are true, change the color of the target cell to 1, and stop the entire process. Only one cell's color is changed in the output grid.

**YAML Block:**

```yaml
task_context: "Grid transformation with connected regions and directional modification"
transformation_rule: "Identify and order connected regions of color 8. Modify a single cell adjacent to the top-leftmost cell of the first region in the order for which a valid modification is possible, following a cycle of directions (Right, Down, Left, Up)."
objects:
  - type: "connected region"
    color: 8
    properties:
      - "top-leftmost cell"
      - "adjacent cell"
actions:
  - "identify connected regions of color 8"
  - "order regions based on top-leftmost cell position"
  - "iterate through regions in order"
  - "determine direction from cycle (Right, Down, Left, Up) based on region order"
  - "calculate target cell based on top-leftmost cell and direction"
  - "check if target cell is within bounds and color 0"
  - "if conditions met, change target cell color to 1 and stop"
predicates:
  - "connected"
  - "same color"
  - "top-leftmost"
  - "adjacent"
  - "within bounds"
  - "color 0"
  - "first region in order"
  - "direction (Right, Down, Left, Up)"
```
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- Follow the template below
- If your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Transform Template:**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

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
