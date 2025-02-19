# 2-0ca9ddb6 • 005 • example_3 - NLP

---
**Natural Language Program:**

The transformation process analyzes each cell in the input grid.
If a cell's color is red (2), then in the output grid, yellow cells (4) are added to the four diagonal positions adjacent to this red cell.
If a cell's color is blue (1), then in the output grid, orange cells (7) are added to the four orthogonal positions (up, down, left, right) adjacent to this blue cell.
Cells with any other color in the input grid remain unchanged in the output grid, unless they are modified by the addition of yellow or orange cells as described.
These modifications are independent, meaning if a location is targeted by both a red cell's diagonal modification and a blue cell's orthogonal modification, the last modification applied will take precedence. In this particular example, there is no overlap of modifications from different colored cells.
This process is applied for every cell in the input grid that is either red or blue.
