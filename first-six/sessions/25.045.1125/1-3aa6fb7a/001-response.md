# 25.045.1125 • 1-3aa6fb7a • 001 Response

---

*text:*

**Natural Language Program:**

1. **Identify Objects:** Find all connected regions of color 8 (azure) in the input grid. We consider these regions as distinct objects.
2. **Locate Topmost Cell:** For each region of color 8, determine the cell with the smallest row index. If there are multiple cells with the same smallest row index, choose the one with the smallest column index among them. This cell is the "topmost" cell of the region.
3. **Locate Bottommost Cell:** For each region of color 8, determine the cell with the largest row index. If there are multiple cells with the same largest row index, choose the one with the smallest column index among them. This cell is the "bottommost" cell of the region.
4. **Transform Topmost Neighbor:** For each region, examine the cell immediately to the right of its "topmost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
5. **Transform Bottommost Neighbor:** For each region, examine the cell immediately to the left of its "bottommost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
6. **Output:** The grid modified after applying steps 4 and 5 for all regions of color 8 is the final output grid.

This program describes how to identify contiguous regions of color 8 as objects and then modify specific neighboring cells based on the topmost and bottommost cells within each object.
