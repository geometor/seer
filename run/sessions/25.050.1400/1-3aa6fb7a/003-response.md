# 1-3aa6fb7a • 003 • example_2 - NLP

---
**Natural Language Program:**

1. **Identify Color-8 Regions:** Find all contiguous regions of color 8 in the input grid. Regions are considered contiguous if cells are 8-connected (horizontally, vertically, or diagonally).

2. **Process Each Region:** For every region of color 8 identified in the previous step, perform the following operations:
   a. **Locate Topmost Cell:** Determine the cell within the current region that has the minimum row index. In case of a tie in row indices, select the cell with the minimum column index among the tied cells. This cell is the "topmost cell" of the region.
   b. **Locate Bottommost Cell:** Determine the cell within the current region that has the maximum row index. In case of a tie in row indices, select the cell with the minimum column index among the tied cells. This cell is the "bottommost cell" of the region.
   c. **Modify Cell to the Right of Topmost:** Examine the cell immediately to the right of the "topmost cell". If this cell exists within the grid boundaries and its color is not 8, change its color to 1.
   d. **Modify Cell to the Left of Bottommost:** Examine the cell immediately to the left of the "bottommost cell". If this cell exists within the grid boundaries and its color is not 8, change its color to 1.

3. **Output Result:** After processing all regions of color 8, the resulting grid is the output grid.

**YAML Block:**

```yaml
task_context: "ARC puzzle transformation"
transformation_rule: "For each 8-connected region of color 8, change the color of the cell to the right of the topmost cell and to the left of the bottommost cell to color 1, provided they are within the grid and are not already color 8."
objects:
  - color_8_regions: "8-connected components of cells with color 8"
predicates:
  - topmost_cell: "The cell with the minimum row index (and minimum column index in case of row index ties) within a region"
  - bottommost_cell: "The cell with the maximum row index (and minimum column index in case of row index ties) within a region"
actions:
  - find_connected_regions: "Identify all 8-connected regions of color 8"
  - determine_topmost_cell: "Find the topmost cell within each region"
  - determine_bottommost_cell: "Find the bottommost cell within each region"
  - conditional_color_change_right: "If conditions are met, change the color of the cell to the right of the topmost cell to 1"
  - conditional_color_change_left: "If conditions are met, change the color of the cell to the left of the bottommost cell to 1"
```
