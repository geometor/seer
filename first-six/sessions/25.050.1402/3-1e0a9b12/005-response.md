# 3-1e0a9b12 • 005 • example_3 - NLP

---
**Natural Language Program:**

The transformation rule operates on each column of the grid independently. For each column, the goal is to rearrange the numbers such that all non-zero numbers are moved to the bottom of the column, while the top positions are filled with zeros. The relative vertical order of the non-zero numbers within each column is maintained.

**Step-by-step transformation:**

1. **Process each column:** Iterate through the input grid column by column, starting from the leftmost column and moving to the right.

2. **Identify non-zero objects in the column:** Within the current column, locate all cells containing non-zero numbers. These are the "objects" we are interested in.

3. **Preserve and extract non-zero objects:**  As you scan the column from top to bottom, collect all the non-zero number objects in the order they appear. Imagine you are picking up the non-zero numbers from top to bottom in the column.

4. **Count the non-zero objects:** Determine the total count of non-zero objects you've extracted from the current column. Let's say this count is 'N'.

5. **Reposition non-zero objects at the bottom:** In the output grid's corresponding column, start from the bottom row and fill the bottom 'N' rows with the extracted non-zero objects, maintaining the order in which you collected them.

6. **Fill top positions with zero objects:** For the remaining rows in the output column, above the positioned non-zero objects, fill them with zeros. These become "zero objects".

7. **Repeat for all columns:** Continue steps 2-6 for every column in the input grid.

By applying this process to each column, we effectively "push" all the non-zero number objects in each column downwards to the bottom, stacking them up and filling the space above with zero objects. The original vertical order of the non-zero objects within each column is preserved during this transformation.
