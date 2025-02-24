def analyze_results(examples):
    """Analyzes the results of the transformation, including object selection details."""
    analysis = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        expected_output = np.array(example['output'])
        transformed_output = np.array(transform(example['input']))

        # Object analysis
        objects = find_objects(input_grid)
        non_edge_objects = [(coords, color) for coords, color in objects if not is_edge_object(input_grid, coords)]

        analysis.append({
            'example': i + 1,
            'match': np.array_equal(transformed_output, expected_output),
            'num_objects': len(objects),
            'num_non_edge_objects': len(non_edge_objects),
            'selected_object_color': None if len(objects)==0 else (non_edge_objects[0][1] if len(non_edge_objects)>0 else objects[np.argmax([len(coords) for coords, _ in objects])][1] ), #color of the first one
            'expected_object_color': expected_output[0][0] if expected_output.size > 0 else None,
        })

    return analysis
examples = [
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "output": [
            [2, 2, 0],
            [0, 2, 0],
            [0, 2, 2],
            [2, 2, 2]
        ]
    },
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 6, 6, 0],
            [0, 3, 0, 0, 4, 4, 0, 0, 6, 0],
            [3, 3, 3, 0, 4, 4, 0, 0, 0, 0],
            [0, 3, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "output": [
            [4, 4],
            [4, 4],
            [4, 4]
        ]
    },
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 8, 0, 0, 0, 0, 7, 7, 0],
            [0, 0, 8, 0, 0, 0, 2, 0, 0, 7, 0],
            [0, 8, 8, 0, 0, 2, 2, 0, 0, 7, 0],
            [0, 8, 8, 0, 0, 0, 2, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "output": [
            [8, 8, 8],
            [0, 8, 0],
            [8, 8, 0],
            [8, 8, 0]
        ]
    },
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 0, 0, 2, 2, 2],
            [0, 0, 0, 7, 7, 0, 0, 2, 0],
            [0, 0, 0, 0, 7, 0, 2, 2, 2],
            [8, 8, 8, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        "output": [
            [2, 2, 2],
            [0, 2, 0],
            [2, 2, 2]
        ]
    }
]
analysis_results = analyze_results(examples)
print(analysis_results)