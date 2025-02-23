import numpy as np

def get_object_pixels(grid, color):
    return [(x,y) for x,row in enumerate(grid) for y, pixel in enumerate(row) if pixel == color]

def analyze_example(input_grid, output_grid, name):
    gray_pixels = get_object_pixels(input_grid, 5)
    if not gray_pixels:
      return {}
    
    x_coords, y_coords = zip(*gray_pixels)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    width = max_y - min_y + 1
    height = max_x - min_x + 1
    total_gray_pixels = len(gray_pixels)

    # Analyze output for splitting rule
    azure_pixels = get_object_pixels(output_grid, 8)
    red_pixels = get_object_pixels(output_grid, 2)
    
    analysis = {
        "name": name,
        "min_x": min_x,
        "max_x": max_x,
        "min_y": min_y,
        "max_y": max_y,
        "width": width,
        "height": height,
        "total_gray_pixels": total_gray_pixels,
        "gray_pixels": gray_pixels,
        "azure_pixels": azure_pixels,
        "red_pixels": red_pixels
    }
    return analysis
    
# Example Data
examples = [
  {
        "input": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0],
            [0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 5, 0, 0, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]),
        "output": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 8, 8, 2, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 8, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 8, 8, 8, 8, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
    },
    {
        "input": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
            [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 5, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]),
        "output": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
            [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        
    },
    {
        "input": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 5, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 5, 5, 0, 0, 0],
            [0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 5, 5, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]),
        "output": np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 2, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 8, 8, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 8, 8, 0, 0, 0],
            [0, 0, 0, 2, 8, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
    }
]
analysis_results = [analyze_example(example['input'], example['output'], f"example_{i+1}") for i, example in enumerate(examples)]
for result in analysis_results:
    print (result)