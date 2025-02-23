# 00d62c1b • 007 • example_2 - NLP

---
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a grid of colored pixels. The primary colors observed are white (0), green (3), and yellow (4). The transformation appears to involve a local operation around a specific color, namely yellow (4). It seems that green pixels adjacent to a yellow pixel get a priority.

**YAML Fact Block:**



```yaml
facts:
  - object: grid
    description: 2D array of pixels
    properties:
      - width: 10
      - height: 10
      - values: [0, 3, 4]

  - object: pixel
    properties:
      - color:
        - white: 0
        - green: 3
        - yellow: 4
      - position: [row, column]

  - relation: adjacency
    description: Pixels are considered adjacent if they share a side (not diagonal).

  - action: change_color
    description: A pixel's color changes based on its neighbors.
    parameters:
      - from: 4
      - to: 3
    conditions:
      neighbor: yellow
```



**Natural Language Program:**

1.  **Identify Target Pixels:** Locate all yellow (4) pixels within the input grid.

2.  **Check Neighbors** For each green pixel, iterate through all the direct neighbors.

3.  **Conditional Modification:** Find green pixels that are next to yellow pixel.

4.  **Apply Rule universally:** Change all yellow cells to Green.


