# 5-150deff5 • 005 • example_3 - NLP

---
Okay, let's analyze the transformation between the input and output grids for this third example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position: centered
      size: 10
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells
output_grid:
  objects:
    - color: 8
      shape: partial copy of color 5 object.
      position: some positions from the original object.
      size: Less than input object.
    - color: 2
      shape: partial negative of the input object with color 5.
      position: inside the original positions of object 5.
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Object:** Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.

2.  **Substitution 1:** Every cell to the rigth of the central vertical axis of the object, that have color 5 is transformed to color 8.

3. **Substitution 2**: Every cell to the left of the central vertical axis of the object, that have color 5 is transformed to color 2.

**Explanation and Justification**

This time, the transformation uses the central vertical axis of object 5 as reference. Every cell in object 5 at each side of the central axis is changed to a different color. The cells at the right are changed to 8 and the cells to the left are changed to 2.

