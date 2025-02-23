# 25.045.1150 • 1-3aa6fb7a • 003 Response

---

*text:*

**Natural Language Program: Transformation Rule**

1. **Identify 'Azure' (color 8) Objects:** Locate all contiguous blocks of cells containing the color 'azure' (8) in the input grid. These blocks are considered as objects.
2. **Examine Neighbors of 'Azure' Objects:** For each cell that is part of an 'azure' object, inspect its immediate neighboring cells (up, down, left, right).
3. **Conditional Color Change:** If a neighboring cell of an 'azure' object has the color 'white' (0), change the color of this neighboring cell to 'blue' (1) in the output grid.
4. **Maintain Unaffected Cells:**  All cells in the input grid that are not neighbors of an 'azure' object (and are 'white') or are already part of an 'azure' object, retain their original color in the output grid. In essence, only 'white' cells directly adjacent to 'azure' objects are transformed to 'blue'.
