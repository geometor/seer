# 1-3aa6fb7a • 001 • example_1 - NLP

---
**Natural Language Program:**

1. **Identify Color-8 Regions:** Find all contiguous regions of color 8 in the input grid. Consider cells to be part of the same region if they are 8-connected (horizontally, vertically, or diagonally).

2. **Process Each Region:** For each identified region of color 8, perform the following steps:
   a. **Find Top-Most Cell:** Locate the cell within the region that has the smallest row index. If there are multiple cells with the same smallest row index, choose the one with the smallest column index among them.
   b. **Find Bottom-Most Cell:** Locate the cell within the region that has the largest row index. If there are multiple cells with the same largest row index, choose the one with the smallest column index among them.
   c. **Modify Right of Top-Most:** Check the cell immediately to the right of the identified "top-most" cell. If this cell is within the grid boundaries (not outside the grid) and its current color is not 8, change its color to 1.
   d. **Modify Left of Bottom-Most:** Check the cell immediately to the left of the identified "bottom-most" cell. If this cell is within the grid boundaries (not outside the grid) and its current color is not 8, change its color to 1.

3. **Output Result:** After processing all color-8 regions, the modified grid becomes the output grid.

**YAML Block:**

```yaml
task_context: "ARC puzzle transformation"
transformation_rule: "For each connected component of color 8, modify the cell to the right of the topmost cell and the cell to the left of the bottommost cell to color 1, if they are within grid boundaries and not already color 8."
objects:
  - color_8_regions: "Connected components of cells with color 8"
predicates:
  - top_most_cell: "Cell in a region with the smallest row index (and smallest column index in case of ties)"
  - bottom_most_cell: "Cell in a region with the largest row index (and smallest column index in case of ties)"
actions:
  - identify_regions: "Find connected regions of color 8"
  - find_top_bottom_cells: "Locate the top-most and bottom-most cells within each region"
  - modify_cell_right: "Change color of the cell to the right of the top-most cell to 1 if conditions are met"
  - modify_cell_left: "Change color of the cell to the left of the bottom-most cell to 1 if conditions are met"
```
