# 2-0ca9ddb6 • 003 • example_2 - NLP

---
```yaml
task_context: "The task is to transform an input grid into an output grid by modifying the neighbors of non-zero colored cells based on their color. Red cells affect diagonal neighbors and blue cells affect orthogonal neighbors."
natural_language_program: |
  1. Initialize the output grid as an exact copy of the input grid.
  2. Iterate through each cell in the input grid, considering both its row and column index.
  3. Check if the value of the current cell is greater than zero.
  4. If the cell's value is non-zero, identify its color.
  5. If the color of the cell is red (color code 2), then for each of its four diagonal neighbors (top-left, top-right, bottom-left, bottom-right), change the color of the corresponding cell in the output grid to yellow (color code 4). Ensure these neighbors are within the grid boundaries.
  6. If the color of the cell is blue (color code 1), then for each of its four orthogonal neighbors (up, down, left, right), change the color of the corresponding cell in the output grid to orange (color code 7). Ensure these neighbors are within the grid boundaries.
  7. After processing all cells in the input grid, the resulting output grid is the final transformed grid.
  8. Note that the cells in the output grid that correspond to the original non-zero cells in the input grid retain their original colors.
  9. Cells that were zero in the input grid remain zero in the output grid unless they are modified because they are neighbors of a red or blue cell as described in steps 5 and 6.
```
