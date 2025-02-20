# 3-1e0a9b12 • 003 • example_2 - NLP

---
**Natural Language Program:**

The transformation is applied column by column. For each column, we identify the colored blocks (non-zero cells).  The action is to "push down" these colored blocks to the bottom of the column, maintaining their original order from top to bottom within that column.  Any empty spaces created at the top of the column after pushing the colored blocks down are filled with white (color 0).  This effectively sorts the colors in each column by placing all white blocks (0) at the top and all colored blocks at the bottom, preserving the relative order of the colored blocks.
