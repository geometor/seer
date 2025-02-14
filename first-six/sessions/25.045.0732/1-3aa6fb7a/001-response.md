# 25.045.0732 • 1-3aa6fb7a • 001 Response

---

*text:*

**Natural Language Program:**

For each contiguous block of color 8 (azure) in the input grid:
1. Identify all cells belonging to the block.
2. Find the cell within this block that is located at the topmost row and then leftmost column (prioritizing rows, then columns in reading order). Let's call this the 'top-leftmost' cell of the block.
3. Calculate the sum of the row index and column index of this 'top-leftmost' cell.
4. If this sum is less than 5, then change the color of the cell immediately to the right of the 'top-leftmost' cell to color 1 (blue).
5. If this sum is greater than or equal to 5, then change the color of the cell immediately below the 'top-leftmost' cell to color 1 (blue).

This transformation is applied independently to each block of color 8 in the input grid. Cells that are not part of a color 8 block, or are adjacent to it but not selected by the transformation rule, remain unchanged.
