# 25.045.0717 • 1-3aa6fb7a • 003 Response

---

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
