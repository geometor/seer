import numpy as np

def compare_grids(expected, transformed):
    expected_np = np.array(expected)
    transformed_np = np.array(transformed)
    equal = np.array_equal(expected_np,transformed_np)
    pixels_off = np.sum(expected_np != transformed_np)
    size_correct = expected_np.shape == transformed_np.shape

    unique_expected, counts_expected = np.unique(expected_np, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed_np, return_counts=True)

    color_palette_correct = set(unique_expected) == set(unique_transformed)
    correct_pixel_counts = all([counts_expected[list(unique_expected).index(i)] == counts_transformed[list(unique_transformed).index(i)] if i in unique_transformed else False for i in unique_expected])

    return {
        'match': equal,
        'pixels_off': int(pixels_off),
        'size_correct': size_correct,
        'color_palette_correct': color_palette_correct,
        'correct_pixel_counts': correct_pixel_counts
    }

examples = [
    {
        'input': [
            [1, 0, 0, 5, 0, 1, 0],
            [0, 1, 0, 5, 1, 1, 1],
            [1, 0, 0, 5, 0, 0, 0]
        ],
        'expected': [
            [0, 0, 0],
            [2, 0, 2],
            [0, 0, 0]
        ],
        'transformed': [
            [0, 0, 0],
            [0, 0, 2],
            [0, 0, 0]
        ]
    },
    {
        'input': [
            [1, 1, 0, 5, 0, 1, 0],
            [0, 0, 1, 5, 1, 1, 1],
            [1, 1, 0, 5, 0, 1, 0]
        ],
        'expected': [
            [2, 0, 0],
            [0, 0, 2],
            [2, 0, 0]
        ],
        'transformed': [
            [0, 0, 0],
            [2, 0, 2],
            [0, 0, 0]
        ]
    },
    {
        'input': [
            [0, 0, 1, 5, 0, 0, 0],
            [1, 1, 0, 5, 1, 0, 1],
            [0, 1, 1, 5, 1, 0, 1]
        ],
        'expected': [
            [0, 0, 0],
            [2, 0, 0],
            [0, 0, 2]
        ],
        'transformed': [
            [2, 0, 0],
            [0, 0, 2],
            [2, 0, 2]
        ]
    }
]

for i, example in enumerate(examples):
  print(f"Example {i+1}:")
  metrics = compare_grids(example['expected'], example['transformed'])
  print(metrics)
