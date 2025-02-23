# 1-3aa6fb7a • 003 • example_2 - NLP

---
**Natural Language Program:**

1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Order Azure Blocks by Minimum Column Index:** For each azure block, determine its minimum column index (the smallest column index among all cells in the block). Order all identified azure blocks based on their minimum column index, from smallest to largest.
3. **Process the First (Leftmost) Azure Block:** Take the first block in the ordered list (the one with the smallest minimum column index). Find the cell within this block that comes first in reading order (top to bottom, left to right). In the output grid, place a cell of color 1 (blue) immediately to the right of this first cell. Ensure that the placement is within grid boundaries.
4. **Process the Last (Rightmost) Azure Block:** Take the last block in the ordered list (the one with the largest minimum column index). Find the cell within this block that comes last in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this last cell. Ensure that the placement is within grid boundaries.
5. **Process Middle Azure Blocks (if any):** For any azure blocks that are positioned between the first and the last in the ordered list, process each of them. For each such block, find its first cell in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this first cell. Ensure that the placement is within grid boundaries.
6. **Result:** The resulting grid, after applying these steps, is the final output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify and order azure blocks by minimum column index. Add blue cells to the right of the first cell of the leftmost block, to the left of the last cell of the rightmost block, and to the left of the first cell of any middle blocks."
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
      - "add to the right of first cell of the first (leftmost) azure block"
      - "add to the left of last cell of the last (rightmost) azure block"
      - "add to the left of first cell of any middle azure block"
predicates:
  - "is_first_block_in_order(azure_block)"
  - "is_last_block_in_order(azure_block)"
  - "is_middle_block_in_order(azure_block)"
  - "first_cell_in_reading_order(azure_block) -> cell"
  - "last_cell_in_reading_order(azure_block) -> cell"
actions:
  - "add_cell_to_right(cell, color=1)"
  - "add_cell_to_left(cell, color=1)"
```
