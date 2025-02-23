# AboveBelow2 • 001 • example_1 • investigate_dreamer

---
Okay, here's a breakdown of my observations, documented facts, and a natural language program describing the transformation:

**Perception of Task Elements:**

The task involves identifying and potentially removing or retaining specific colored rectangular objects within a grid. The primary colors involved seem to be blue (1), red (2), green (3), and yellow (4). White (0) appears to act as a background or empty space. The output seems to retain some of the original colored rectangles while removing others. The decision of which to keep, and which to remove is not based on color, only the green and yellow remain.

**YAML Fact Documentation:**



```yaml
facts:
  - observation: |
      The input grid contains multiple rectangular objects of different colors (blue, red, green, yellow) on a white background.
  - object_types:
      - type: rectangle
        properties:
          - color: [blue, red, green, yellow, white]
          - shape: rectangular
          - size: varies
  - actions:
      - name: remove
        description: |
            Certain colored rectangles are completely removed from the grid, replaced by the background color (white).
      - name: retain
        description: |
           Other rectangles remain in the grid
  - selection_criteria: unknown
    - description:
      The criteria to keep specific objects is not obvious
  - relationships:
      - type: spatial
        description: |
            Objects are positioned in different locations within the grid, some are adjacent.
```



**Natural Language Program:**

1.  **Identify Rectangles:** Locate all rectangular shapes formed by contiguous blocks of pixels of the same color (excluding white/0).
2.  **Selective Retention:** Retain any Green and yellow rectangles.
3.  **Removal:** remove red and blue rectangles
4.  **Output:** Produce a new grid with the selected color areas retained and all others replaced with background (white/0).


