# Imagined execution of a function to analyze example 1
# metrics_example_1 = analyze_example(input_grid_1, expected_output_1, transformed_output_1)
# print(metrics_example_1)
metrics_example_1 = {
    'input_dims': (6, 6),
    'output_dims': (6, 6),
    'core_cluster_found': True,
    'core_cluster_coords': (2, 2),
    'core_cluster_colors': [9, 3, 7, 8],
    'horizontal_mirror_offset_used': -2,
    'vertical_mirror_offset_used': 2,
     'expected_h_mirror_coords': [(0,2),(0,3)], #row, col of top left pixel
    'expected_v_mirror_coords': [(2,4),(3,4)],
}

# Imagined execution of a function to analyze example 2
# metrics_example_2 = analyze_example(input_grid_2, expected_output_2, transformed_output_2)
# print(metrics_example_2)
metrics_example_2 = {
'input_dims': (6, 6),
    'output_dims': (6, 6),
    'core_cluster_found': True,
    'core_cluster_coords': (1, 1),
    'core_cluster_colors': [4, 6, 2, 1],
    'horizontal_mirror_offset_used': 3,
    'vertical_mirror_offset_used': -1,
     'expected_h_mirror_coords': [(3,1),(3,2)], #row, col of top left pixel
    'expected_v_mirror_coords': [(1,-1),(2,-1)],
}
# Imagined execution of a function to analyze example 3
# metrics_example_3 = analyze_example(input_grid_3, expected_output_3, transformed_output_3)
# print(metrics_example_3)
metrics_example_3 = {
  'input_dims': (6, 6),
    'output_dims': (6, 6),
    'core_cluster_found': True,
    'core_cluster_coords': (2, 2),
    'core_cluster_colors': [3, 6, 5, 2],
    'horizontal_mirror_offset_used': -2,
    'vertical_mirror_offset_used': 2,
    'expected_h_mirror_coords': [(0,2),(0,3)], #row, col of top left pixel
    'expected_v_mirror_coords': [(2,4),(3,4)],
}