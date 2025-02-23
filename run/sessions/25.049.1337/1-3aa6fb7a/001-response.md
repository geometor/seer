# 1-3aa6fb7a • 001 • example_1 - NLP

---

*text:*

**Natural Language Description of the Transformation:**

The transformation rule operates on each row of the input grid independently. For each row, it identifies contiguous blocks of cells with color 8 (azure). If a block of color 8 has a length of exactly one cell, then the rule checks the row index of this block.

- If the row index is in the top half of the grid (row indices 0, 1, 2, or 3), and if the cell immediately to the right of this single-cell block of color 8 is within the grid boundaries and has color 0 (white), then change the color of that cell to 1 (blue).
- If the row index is in the bottom half of the grid (row indices 4, 5, or 6), and if the cell immediately to the left of this single-cell block of color 8 is within the grid boundaries and has color 0 (white), then change the color of that cell to 1 (blue).

If a block of color 8 in any row has a length greater than one cell, no changes are made in the vicinity of that block in that row. If there are no blocks of color 8 of length one in a row, no changes are made in that row.

**YAML Block:**

```yaml
task_context: "grid transformation"
transformation_rule: "conditional color change based on block of 8s length and row position"
objects:
  - type: "block of color 8"
    properties:
      - "length"
      - "position (row, column)"
predicates:
  - "is_length_one(block)"
  - "is_row_in_top_half(row_index)"
  - "is_row_in_bottom_half(row_index)"
  - "is_cell_to_right_color_0(block)"
  - "is_cell_to_left_color_0(block)"
actions:
  - "change_cell_to_color_1(cell)"
step_by_step_transformation:
  - "for each row in the grid:"
  - "  identify contiguous blocks of color 8"
  - "  for each block:"
  - "    determine block length"
  - "    if block length is 1:"
  - "      get row index of the block"
  - "      if row index < 4:"
  - "        check cell to the right; if color 0, change to 1"
  - "      else if row index >= 4:"
  - "        check cell to the left; if color 0, change to 1"
```
