# 5-150deff5 • 001 • example_1 - NLP

---
**Natural Language Program:**

The transformation applied to the input grid involves the following steps:

1. **Identify the gray object:** Locate the contiguous region of cells with color 5 (gray) in the input grid. This region constitutes the object to be transformed.

2. **Determine boundary and interior cells:** For each cell within the identified gray object, determine if it is a boundary cell or an interior cell.
    - A cell is considered a **boundary cell** if at least one of its immediate neighbors (up, down, left, right) is not part of the gray object (i.e., is color 0 or white).
    - A cell is considered an **interior cell** if all of its immediate neighbors (up, down, left, right) that are within the grid boundaries are also part of the gray object.

3. **Recolor boundary cells:** Change the color of all boundary cells of the gray object from gray (color 5) to azure (color 8).

4. **Recolor interior cells:** Change the color of all interior cells of the gray object from gray (color 5) to red (color 2).

5. **Maintain background:** All cells in the grid that are not part of the original gray object (i.e., cells with color 0 or white) remain unchanged.

In essence, the transformation outlines the gray shape with azure and fills its interior with red, while leaving the surrounding white background untouched.
