# 3-1e0a9b12 • 005 • example_3 - NLP

---
**Natural Language Program:**

The transformation is column-based. For each column in the input grid:
1. **Identify objects:** The objects are the non-zero color values within the column.
2. **Action: Push to bottom:**  Move all identified non-zero color values to the bottom of the corresponding column in the output grid. Maintain the relative order of these non-zero values as they appeared from top to bottom in the input column.
3. **Fill with background:** Fill the empty cells in the upper part of the output column with the background color, which is white (0). This effectively shifts all colored objects in each column downwards, stacking them at the bottom.
