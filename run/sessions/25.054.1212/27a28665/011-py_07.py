import numpy as np
from collections import Counter

def analyze_examples(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        output_value = example['output'][0][0]  # Extract single integer

        color_counts = Counter(input_grid.flatten())
        
        at_least_two = {color : count for color, count in color_counts.items() if count >= 2}
        
        results.append({
            'example': i + 1,
            'input_color_counts': dict(color_counts),
            'colors_with_at_least_two': dict(at_least_two),
            'output_value': output_value,
        })
    return results

examples = [
    {'input': [[5, 5, 0], [5, 0, 5], [0, 5, 0]], 'output': [[1]]},
    {'input': [[8, 0, 8], [0, 8, 0], [8, 0, 8]], 'output': [[2]]},
    {'input': [[5, 0, 5], [0, 5, 0], [5, 0, 5]], 'output': [[2]]},
    {'input': [[0, 1, 1], [0, 1, 1], [1, 0, 0]], 'output': [[3]]},
    {'input': [[0, 8, 8], [0, 8, 8], [8, 0, 0]], 'output': [[3]]},
    {'input': [[4, 4, 0], [4, 0, 4], [0, 4, 0]], 'output': [[1]]},
    {'input': [[0, 5, 0], [5, 5, 5], [0, 5, 0]], 'output': [[6]]}
]

analysis = analyze_examples(examples)

# Print the analysis in a readable format
for result in analysis:
    print(f"Example {result['example']}:")
    print(f"  Input Color Counts: {result['input_color_counts']}")
    print(f" Colors with at least two: {result['colors_with_at_least_two']}")
    print(f"  Output Value: {result['output_value']}")
    print("-" * 30)