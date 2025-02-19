# 1-3aa6fb7a • 001 • example_1 - NLP

---

*text:*

**Natural Language Program:**

The transformation rule operates on each row of the input grid independently. For each row, we count the number of occurrences of the color '8' (azure).

- **If a row contains exactly one '8':**
    - **If the row index is even (0, 2, 4, 6, ...):** Check the cell immediately to the left of the '8'. If this cell is color '0' (white), change its color to '1' (blue) in the output grid.
    - **If the row index is odd (1, 3, 5, ...):** Check the cell immediately to the right of the '8'. If this cell is color '0' (white), change its color to '1' (blue) in the output grid.

- **If a row contains zero or more than one '8':** No changes are made to that row in the output grid.


This rule applies to every row in the input grid to produce the output grid.

**YAML Block:**

```yaml
task_context: "Grid transformation based on color '8' count and row index parity."
transformation_rule: "For each row, count occurrences of color '8'. If count is 1, change adjacent '0' to '1' based on row index parity (even row: left, odd row: right)."
objects:
  - type: "color_block"
    color: 8
    role: "trigger_action"
  - type: "cell"
    color: 0
    role: "target_cell"
  - type: "cell"
    color: 1
    role: "output_color"
predicates:
  - "has_color_count_one"
  - "is_even_row_index"
  - "is_odd_row_index"
  - "is_adjacent_left_zero"
  - "is_adjacent_right_zero"
actions:
  - "change_cell_color_to_1"
```
