# 1-3aa6fb7a • 001 • example_1 - NLP

---

*text:*

**Natural Language Program:**

1. **Identify '8' Objects:** Detect all contiguous regions of color '8' in the input grid. Consider each region as a distinct object.
2. **Bounding Box Calculation:** For each identified '8' object, determine its bounding box. This box is defined by the minimum and maximum row and column indices that enclose the object.
3. **Object Sorting:** Sort the '8' objects based on the row index of the top boundary of their bounding boxes in ascending order. If row indices are the same, sort by the column index of the left boundary.
4. **Transformation - First Object:** For the first object in the sorted list:
    - Locate the top-right corner of its bounding box.
    - Check the cell immediately to the right of this corner.
    - If this cell is within the grid boundaries and its color is '0', change its color to '1'.
5. **Transformation - Second Object:** For the second object in the sorted list:
    - Locate the bottom-left corner of its bounding box.
    - Check the cell immediately below this corner.
    - If this cell is within the grid boundaries and its color is '0', change its color to '1'.

This program describes how to transform the input grid into the output grid by identifying and modifying cells adjacent to regions of color '8' based on their sorted order and bounding box properties.
