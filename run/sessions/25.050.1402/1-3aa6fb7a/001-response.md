# 1-3aa6fb7a • 001 • example_1 - NLP

---
**Natural Language Program:**

For each connected region of color 8 in the input grid:
1. Identify the cell within the region that has the largest row index. If there are multiple such cells, choose the one with the largest column index among them. Let's call the coordinates of this cell (R, C).
2. Check the cell directly above, at coordinates (R-1, C). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
3. If step 2 did not result in a change (either the cell above was not within bounds, not color 0, or already changed), then check the cell directly to the left, at coordinates (R, C-1). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
4. If neither step 2 nor step 3 resulted in a change, no modification is made for this region of color 8.

This process is applied independently to each connected region of color 8 in the input grid.
