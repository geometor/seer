# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Description**

```yaml
objects:
  - color: 8 (azure)
    description: Three separate azure colored structures, each made of three cells in an L-shape.

  - color: 1 (blue)
    description: Single blue cells.

transformation:
  - The transformation involves identifying specific cells within the azure structures and changing the color of those cells to blue (1).
  - In the example, the cells changed to blue are located in the corner of the object that is furthest away from other objects.
```

**Natural Language Program**

1.  **Identify Objects:** Locate all azure (8) colored objects. In this case, we have three L-shaped structures.

2.  **Action - Change single cell color:** For each azure object, the corner cell that forms the corner furthest away from all other shapes is recolored to blue (1).

The program remains the same as in the first example. The only difference is that there are three L shaped objects in the second input grid, instead of two. The transformation rule, correctly, transforms the corner of each azure object that is furthest away from the other objects to blue.

