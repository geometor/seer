# 25.044.1417 • 1-3aa6fb7a • 003 Response

---

*text:*

**Natural Language Program:**

For each row in the input grid, perform the following steps:

1. **Locate the First '8':** Identify the index of the first occurrence of the number 8 in the current row, scanning from left to right.
2. **Modify Right Cell (if applicable):** If an '8' is found, examine the cell immediately to its right within the same row. If this cell exists within the row boundaries and its value is 0, change its value to 1 in the output grid.
3. **Locate the Last '8':** Identify the index of the last occurrence of the number 8 in the same row, scanning from right to left.
4. **Modify Left Cell (if applicable):** If an '8' is found, examine the cell immediately to its left within the same row. If this cell exists within the row boundaries and its value is 0, change its value to 1 in the output grid.
5. **Unchanged Rows:** If no '8' is found in the current row, leave the entire row unchanged in the output grid.

Repeat these steps for every row in the input grid to generate the complete output grid.
