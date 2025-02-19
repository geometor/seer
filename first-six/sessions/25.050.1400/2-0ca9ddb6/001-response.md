# 2-0ca9ddb6 • 001 • example_1 - NLP

---
**Natural Language Program: Transformation Rule**

The transformation process operates on each non-white cell in the input grid independently. For every non-white cell, we identify its color. If the cell is red (color 2), its orthogonal neighbors (up, down, left, right) in the output grid are turned yellow (color 4). If the cell is blue (color 1), its orthogonal neighbors in the output grid are turned orange (color 7).  The original non-white cells and any white cells that are not neighbors of these colored cells remain unchanged in the output grid. Essentially, each colored cell in the input grid "emanates" a specific color to its immediate surroundings in the output grid, based on its own color.
