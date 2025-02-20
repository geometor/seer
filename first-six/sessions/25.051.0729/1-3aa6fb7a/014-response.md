# 1-3aa6fb7a • 014 • refine_code - NLP

---
Okay, here's a natural language description of the transformation rule, based on the provided input and expected output grids, and taking into account the failures of the previous code:

**Natural Language Program:**

1.  **Identify Isolated Azure Objects:** Find all azure (color 8) objects that are comprised of a single cell.  An "isolated" azure cell is one that has no adjacent cells of the same color, including diagonals.

2.  **Sort by Position:** Sort the isolated azure cells. The sorting order prioritizes cells higher up in the grid (smaller row index). For cells in the same row, prioritize those further to the left (smaller column index).

3.  **Place Blue Cell to the Right of Topmost:** For the *topmost* isolated azure cell (the first one after sorting), place a blue cell (color 1) immediately to its *right*. If the azure cell is at the right edge of the grid, do nothing.

4. **Place Blue Cell to the Left all others:** For *all other* isolated azure cells (i.e., all except the topmost), place a blue (color 1) cell immediately to their *left*. If an azure cell is at the left edge, skip it.

**Why Previous Attempts Failed and Key Improvements:**

*   **Diagonal Adjacency:** The core issue was the correct identification of "isolated" cells. The description clearly stated "considering diagonal adjacency." The flood fill approach is a good, standard way to handle connected component analysis.
* **Sorting is Needed:** The sorting is explicit in the problem. The topmost azure cell by row, and the leftmost if there is a tie, takes precedence.
* **Right for Top, Left for Others:** The core logic specifies placement.

**YAML Summary (Conceptual):**

```yaml
objects:
  - name: azure_cell
    color: 8
    properties:
      - isolated: boolean  # True if no neighbors (including diagonals) of the same color
  - name: blue_cell
    color: 1
    properties: {}

actions:
  - find: azure_cell
    where: isolated == True
    store_as: isolated_azures
  - sort: isolated_azures
    by: [row_index, column_index]  # Ascending order for both
  - for_each: isolated_azures
    do:
      - if: index == 0  # First element (topmost)
        then: place blue_cell to_right_of current azure_cell
      - else:
        then: place blue_cell to_left_of current azure_cell
  - edge_cases:
      description: "Handle boundary checks before placing."
```

