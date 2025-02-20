# 1-3aa6fb7a • 001 • example_1 - NLP

---
**Natural Language Program:**

1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Determine Leftmost Azure Block:** For each azure block, find its minimum column index (the smallest column index among all cells in the block). Identify the azure block with the overall smallest minimum column index. Let's call this the "leftmost block".
3. **Locate First Cell in Leftmost Block:** Within the "leftmost block", find the cell that appears first in reading order, scanning from top to bottom and left to right. We'll refer to this as the "top-leftmost cell" of the leftmost block in reading order.
4. **Add Blue Cell to the Right of Leftmost Block's First Cell:**  In the output grid, place a cell of color 1 (blue) immediately to the right of the "top-leftmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "top-leftmost cell" is already in the rightmost column).
5. **Determine Rightmost Azure Block:**  For each azure block, again consider its minimum column index. Identify the azure block with the overall largest minimum column index. Let's call this the "rightmost block".
6. **Locate Last Cell in Rightmost Block:** Within the "rightmost block", find the cell that appears last in reading order, scanning from top to bottom and left to right. This can be seen as the "bottom-rightmost cell" of the rightmost block in reading order.
7. **Add Blue Cell to the Left of Rightmost Block's Last Cell:** In the output grid, place a cell of color 1 (blue) immediately to the left of the "bottom-rightmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "bottom-rightmost cell" is already in the leftmost column).
8. **Result:** The resulting grid, after applying these steps, is the final output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify leftmost and rightmost blocks of azure color. Add a blue cell to the right of the first cell (reading order) of the leftmost block and to the left of the last cell (reading order) of the rightmost block."
objects:
  - type: "azure block"
    color: 8
    properties:
      - "contiguous region"
      - "minimum column index"
      - "first cell (reading order)"
      - "last cell (reading order)"
  - type: "blue cell"
    color: 1
    actions:
      - "add to the right of first cell of leftmost azure block"
      - "add to the left of last cell of rightmost azure block"
predicates:
  - "is_leftmost_block(azure_block)"
  - "is_rightmost_block(azure_block)"
  - "first_cell_in_reading_order(azure_block) -> cell"
  - "last_cell_in_reading_order(azure_block) -> cell"
actions:
  - "add_cell_to_right(cell, color=1)"
  - "add_cell_to_left(cell, color=1)"
```
