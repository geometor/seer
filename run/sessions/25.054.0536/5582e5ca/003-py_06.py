import numpy as np
from collections import Counter

def get_grid_properties(grid_str):
    grid = np.array(eval(grid_str))
    height, width = grid.shape
    unique_colors = np.unique(grid)
    color_counts = Counter(grid.flatten())

    
    
    return {
        'height': height,
        'width': width,
        'unique_colors': unique_colors.tolist(),
        'color_counts':  [(color,count) for color, count in color_counts.items()]
    }
    

examples = [
    {
        'input': '[[4, 4, 8], [6, 4, 3], [6, 3, 0]]',
        'expected_output': '[[4, 4, 4], [4, 4, 4], [4, 4, 4]]',
    },
    {
        'input': '[[6, 8, 9], [1, 8, 1], [9, 4, 9]]',
        'expected_output': '[[9, 9, 9], [9, 9, 9], [9, 9, 9]]',
    },
    {
        'input': '[[4, 6, 9], [6, 4, 1], [8, 8, 6]]',
        'expected_output': '[[6, 6, 6], [6, 6, 6], [6, 6, 6]]',
    }
]

results = []
for example in examples:
    input_props = get_grid_properties(example['input'])
    output_props = get_grid_properties(example['expected_output'])
    output_color = output_props['unique_colors'][0]
    
    if output_color in input_props['unique_colors']:
        fill_color_match = True
        
    else: 
        fill_color_match = False
    results.append({
        'input_properties': input_props,
        'output_properties': output_props,
        'fill_color_match': fill_color_match,
        'output_color': output_color
    })

for idx, result in enumerate(results):
    print(f"Example {idx + 1}:")
    print(f"  Input Properties: {result['input_properties']}")
    print(f"  Output Properties: {result['output_properties']}")
    print(f"  Fill Color Match: {result['fill_color_match']}")
    print(f"  Output Color: {result['output_color']}")