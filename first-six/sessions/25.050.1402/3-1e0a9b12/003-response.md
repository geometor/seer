# 3-1e0a9b12 • 003 • example_2 - NLP

---
**Natural Language Program:**

The transformation rule involves processing each column of the input grid independently. For each column, the operation is to gather all non-zero numbers and reposition them at the bottom of the same column in the output grid, while filling the top portion of the column with zeros. The relative order of the non-zero numbers within each column is maintained during this process.

**Step-by-step transformation:**

1. **For each column** in the input grid, proceeding from the first column to the last:
    - **Identify all non-zero numbers** present in the current column.
    - **Extract these non-zero numbers**, maintaining their original top-to-bottom order within the column.  Think of collecting these numbers as if picking them up from top to bottom.
    - **Count the number of extracted non-zero numbers**. Let's call this count 'N'.
    - **Place these 'N' non-zero numbers** in the output grid's corresponding column, starting from the bottom-most rows and moving upwards for 'N' rows.  The order of placement should be the same as the extracted order.
    - **Fill the remaining positions** in the output grid's column, above the placed non-zero numbers, with zeros.

2. Repeat step 1 for every column in the input grid.

This procedure effectively "stacks" all the non-zero numbers in each column at the bottom, preserving their vertical order and padding the top with zeros.
