# 2-0ca9ddb6 • 003 • example_2 - NLP

---
```yaml
task_context: "The task is to modify a grid by adding colored cells around existing non-zero colored cells based on their original color. Specifically, red cells get yellow diagonals, and blue cells get orange orthogonals, as seen in the previous example."
objects:
  - red_cell:
      color: 2
      action: surround with yellow diagonals
  - blue_cell:
      color: 1
      action: surround with orange orthogonals
predicates:
  - is_red: cell color is 2
  - is_blue: cell color is 1
actions:
  - add_yellow_diagonals: place yellow cells at the four diagonal positions of the red cell
  - add_orange_orthogonals: place orange cells at the four orthogonal positions of the blue cell
transformation_rule: "For each red cell in the input grid, place yellow cells at its diagonal positions in the output grid. For each blue cell in the input grid, place orange cells at its orthogonal positions in the output grid. Keep all other cells as they are from the input, except for the positions where new colors are placed."
```

**Natural Language Program:**

The process transforms the input grid by iterating through each cell.
If a cell in the input grid is red (color 2), then in the output grid, yellow cells (color 4) are placed at the four diagonal positions relative to this red cell.
If a cell in the input grid is blue (color 1), then in the output grid, orange cells (color 7) are placed at the four orthogonal positions (up, down, left, right) relative to this blue cell.
If a cell in the input grid is of any other color, it remains unchanged in the output grid, unless it is modified by the placement of new colors around red or blue cells.
The transformations for red and blue cells are independent and can overwrite each other if their affected areas overlap. In this specific example, overlaps are possible and do occur as seen in the top right area, and the bottom left area.
This process is applied to every cell in the input grid that is either red or blue.
