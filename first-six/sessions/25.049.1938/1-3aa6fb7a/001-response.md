# 1-3aa6fb7a • 001 • example_1 - NLP

---
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
objects:
  - color: 8 (azure)
    description: Two separate azure colored structures, each made of three cells in an L-shape.
    
  - color: 1 (blue)
      description: single blue cells

transformation:
  - The transformation involves identifying specific cells within the azure structures and changing color of those cells to blue (1)
  - In the example, the two cells changed to blue are located in the corner of the object that is furthest away from other objects.
```

**Natural Language Program**

1.  **Identify Objects:** Locate all azure (8) colored objects. In this case, we have two L-shaped structures.

2.  **Action- Change single cell color:** For each azure object, the corner cell that forms the corner furthest away from all other shapes is recolored to blue (1).

This natural language program describes the "story" of the transformation: identifying particular azure shapes and recoloring the furthest away corner of each.

