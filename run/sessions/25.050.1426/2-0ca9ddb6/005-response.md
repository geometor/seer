# 2-0ca9ddb6 • 005 • example_3 - NLP

---
**Natural Language Program: Transformation Rule**

1. **Initialization:** Create a new output grid, initially identical to the input grid.
2. **Iterate through Input Grid:** Process each cell of the input grid, row by row, and column by column.
3. **Identify Red Pixels:** If a cell in the input grid is red (color code 2):
    - Examine its diagonal neighbors: top-left, top-right, bottom-left, and bottom-right.
    - For each diagonal neighbor, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a diagonal neighbor in the input grid is white, change the color of the same diagonal neighbor cell in the *output* grid to yellow (color code 4).
4. **Identify Blue Pixels:** If a cell in the input grid is blue (color code 1):
    - Consider all eight neighbors: top, bottom, left, right, top-left, top-right, bottom-left, and bottom-right.
    - For each neighbor, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor in the input grid is white, change the color of the same neighbor cell in the *output* grid to orange (color code 7).
5. **Maintain Original Pixels:** The original red and blue pixels in the input grid remain unchanged in the output grid. Pixels that are not neighbors of red or blue pixels, or whose neighbors in the input were not white, are also unchanged.
6. **Unaffected Magenta Pixels:** Pixels of magenta color (color code 6) and their neighbors are not affected by this transformation and remain as they were in the input grid.
7. **Output:** The final output grid is the result of applying these transformations.
