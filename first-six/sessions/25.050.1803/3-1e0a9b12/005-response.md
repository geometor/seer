# 3-1e0a9b12 • 005 • example_3 - NLP

---
**Natural Language Description of Transformation:**

The transformation rule is to move all non-zero colored objects in each column of the input grid to the bottom of the corresponding column in the output grid, while maintaining their vertical order within each column.  Any empty spaces created at the top of the columns in the output grid are filled with white color (0).

**Step-by-step transformation:**

1. **Column-wise Processing:**  The transformation operates on each column of the grid independently.
2. **Identify and Extract Objects:** For each column, locate and extract all non-zero colored cells. These are considered the "objects" in this transformation.
3. **Maintain Vertical Order:**  Note the original top-to-bottom sequence of these extracted objects within the column.
4. **Position Objects at Bottom:**  In the output grid, for the same column, place the extracted objects in the bottom-most rows, ensuring they retain the vertical order observed in the input.
5. **Fill with White Space:**  The remaining cells at the top of each column in the output grid, which are not occupied by the moved objects, are filled with the white color (represented by 0).
6. **Repeat for All Columns:**  Apply steps 2-5 to each column of the input grid to produce the complete output grid.

Essentially, this transformation simulates a "gravity" effect within each column, causing all colored objects to fall to the bottom, stacking upon one another in their original relative order, with empty space (white) filling in from the top.
