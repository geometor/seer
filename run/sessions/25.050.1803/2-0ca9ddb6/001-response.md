# 2-0ca9ddb6 • 001 • example_1 - NLP

---
```yaml
task_context: "The task is to transform an input grid into an output grid based on the colors of non-zero cells. Specific colors trigger different types of neighbor modifications."
natural_language_program: |
  1. Initialize the output grid as a direct copy of the input grid.
  2. Iterate through each cell of the input grid, identifying each cell by its row and column index.
  3. For each cell, check if its value is non-zero (greater than 0).
  4. If the cell's value is non-zero, determine its color.
  5. If the color of the cell is red (color code 2), then for each of the four diagonal neighbor positions (top-left, top-right, bottom-left, bottom-right) relative to the current cell, set the value of the cell at that position in the output grid to yellow (color code 4).
  6. If the color of the cell is blue (color code 1), then for each of the four orthogonal neighbor positions (up, down, left, right) relative to the current cell, set the value of the cell at that position in the output grid to orange (color code 7).
  7. After checking and potentially modifying neighbors for all non-zero cells, the output grid is considered complete.
  8. Note that the original non-zero cells in the input grid remain in their positions and with their original colors in the output grid.
  9. Cells that were zero in the input grid remain zero in the output grid unless they are modified by being neighbors of a non-zero cell according to steps 5 and 6.
```
