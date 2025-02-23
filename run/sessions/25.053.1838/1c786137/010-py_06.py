def compare_analyses(analysis_in, analysis_out):
    """Compares the analyses of input and output grids."""

    comparison = {
        'input_shape': analysis_in['shape'],
        'output_shape': analysis_out['shape'],
        'input_unique_colors': list(analysis_in['unique_colors']), # Convert to list for YAML compatibility
        'output_unique_colors': list(analysis_out['unique_colors']),
        'input_color_counts': dict(analysis_in['color_counts']),  # Convert to dict for YAML
        'output_color_counts': dict(analysis_out['color_counts']),
        'input_objects': len(analysis_in['objects']),
        'output_objects': len(analysis_out['objects']),
    }

    # More detailed object comparisons can be added here as needed.

    return comparison
example1_comparison = compare_analyses(analysis1, analysis1_out)
example2_comparison = compare_analyses(analysis2, analysis2_out)
example3_comparison = compare_analyses(analysis3, analysis3_out)

print("Example 1 Comparison:", example1_comparison)
print("Example 2 Comparison:", example2_comparison)
print("Example 3 Comparison:", example3_comparison)
