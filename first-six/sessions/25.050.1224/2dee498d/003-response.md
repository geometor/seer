# 2dee498d • 003 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  size: 4x12
  objects:
    color_0:
        - position: [0,1]
        - position: [0,2]
        - position: [0,5]
        - position: [0,6]
        - position: [0,9]
        - position: [0,10]
        - position: [3,1]
        - position: [3,2]
        - position: [3,5]
        - position: [3,6]
        - position: [3,9]
        - position: [3,10]
    color_1:
        - position: [0,3]
        - position: [0,7]
        - position: [0,11]
        - position: [1,2]
        - position: [1,6]
        - position: [1,10]
        - position: [2,1]
        - position: [2,5]
        - position: [2,9]
        - position: [3,0]
        - position: [3,4]
        - position: [3,8]
    color_2:
        - position: [0,0]
        - position: [0,4]
        - position: [0,8]
        - position: [1,1]
        - position: [1,5]
        - position: [1,9]
        - position: [2,2]
        - position: [2,6]
        - position: [2,10]
        - position: [3,3]
        - position: [3,7]
        - position: [3,11]
    color_4:
        - position: [1,0]
        - position: [1,3]
        - position: [1,4]
        - position: [1,7]
        - position: [1,8]
        - position: [1,11]
        - position: [2,0]
        - position: [2,3]
        - position: [2,4]
        - position: [2,7]
        - position: [2,8]
        - position: [2,11]
output_grid:
  size: 4x4
    objects:
        color_0:
            - position: [0,1]
            - position: [0,2]
            - position: [3,1]
            - position: [3,2]
        color_1:
            - position: [0,3]
            - position: [1,2]
            - position: [2,1]
            - position: [3,0]
        color_2:
            - position: [0,0]
            - position: [1,1]
            - position: [2,2]
            - position: [3,3]
        color_4:
            - position: [1,0]
            - position: [1,3]
            - position: [2,0]
            - position: [2,3]

```

**Natural Language Program:**

The transformation rule can be described as follows:

1.  **Identify Columns:** Examine the input grid, which is 4x12.
2.  **Select Columns:** Take every fourth column of the input grid starting from the first column. That is, consider column 0, column 4, column 8.
3. Remove other columns.
4.  **Construct Output:** Arrange the content of these selected columns to construct the output grid of size 4x4, preserving the original order of rows.

In other words, the output grid is formed by sampling specific columns from the input grid.

