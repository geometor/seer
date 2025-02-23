# 0ca9ddb6 • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Observation:**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 8
      position: (0,3)
      shape: 1x1
    - color: 2
      positions: [(2,6), (7,1)]
      shape: 1x1
    - color: 1
      positions: [(3,2), (6,6)]
      shape: 1x1
    - color: 0
      position: all other cells
      shape: background

output_grid:
  size: 9x9
  objects:
     - color: 8
       position: (0,3)
       shape: 1x1
     - color: 2
       positions: [(2,6), (7,1)]
       shape: 1x1
     - color: 1
       positions: [(3,2), (6,6)]
       shape: 1x1
     - color: 4
       positions: [(1,5),(1,7), (3,5),(3,7),(6,0),(6,2),(8,0),(8,2)]
       shape: 1x1
     - color: 7
       positions: [(2,2),(3,1),(3,3),(6,5), (6,7), (5,6), (7,6)]
       shape: 1x1
     - color: 0
       position: all other cells
       shape: background
```

**Natural Language Program:**

1.  **Identify Key Cells:** There are two red (color 2) cells and two blue (color 1) cells in the input. An azure cell (color 8) is also in the input, but remains unchanged in position and in the output. Red and blue cells remain unchanged in position and color.

2.  **Yellow Expansion:** A yellow (color 4) 1x1 "cross" or "+" shape appears centered on the row above and the row below *each* red cell.

3.  **Orange Expansion:** An orange (color 7) 1x1 "cross" or "+" shape appears centered on the column to the left and the column to the right of *each* blue cell.

**Step-by-step Transformation Description:**

1.  The azure (8) cell, the red (2) cells and the blue (1) cells in the input are copied to the same positions in the output.
2.  Yellow (4) cells are placed on the cells located at one row of distance from each red cell.
3.  Orange (7) cells are placed on the cells located at one column of distance of each blue cell.

This is essentially the same rule as in the first example, but applied to *multiple* red and blue cells instead of just one of each.

**Python Code**
The code provided works perfectly also for this case, because it does not assume there is one single object 2 or object 1, as it uses the function `find_object` that returns coordinates no matter if the objects are more than one.

