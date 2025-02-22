# 2-0ca9ddb6 • 009 • example_3 - NLP

---
Okay, let's analyze the third example.

**Observations and Documentation**

```yaml
observations:
  input_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (2, 2)
        shape: single cell
      - color: 1 (blue)
        position: (7, 3)
        shape: single cell
      - color: 6 (magenta)
        position: (5,6)
        shape: single cell
    background_color: 0 (white)
  output_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (2, 2)
        shape: single cell
      - color: 1 (blue)
        position: (7, 3)
        shape: single cell
      - color: 6 (magenta)
        position: (5,6)
        shape: single cell
      - color: 4 (yellow)
        positions: [(1, 2), (3, 2), (2, 1), (2, 3)]
        shape: single cells forming a cross pattern centered on red cell
      - color: 7 (orange)
        positions: [(6,3), (7,2), (7,4), (8,3)]
        shape: single cells surrounding blue cell
    background_color: 0 (white)
```

**Determining the Transformation Rule**

This example further reinforces the established pattern, and shows that the transformation applies to blue and red cells only.

1.  **Identify Key Objects:** Locate all red (color 2) and blue (color 1) cells in the input grid. Ignore other color.
2.  **Yellow Cross Creation:** For *each* red cell, create a cross pattern using yellow (color 4) cells.  The cross extends one cell in each cardinal direction (up, down, left, and right) from the red cell.
3.  **Orange Surround:** For *each* blue cell, place orange (color 7) cells around it in each of the cardinal directions.
4.  **Preservation**: The magenta cell, and all red and blue cells remain in the same place.

**Natural Language Program**

The transformation rule remains consistent. We apply the "decoration" rule around every red and blue cell, and leave any other cells untouched.

1.  Copy all cells from the input to the output.

2.  For each red cell in the input grid:
    *   Place a yellow cell one position above, below, to the left, and to the right of the red cell's location.

3.  For each blue cell in the input grid:
    *   Place an orange cell one position above, below, to the left and to the right of the blue cell's location.

