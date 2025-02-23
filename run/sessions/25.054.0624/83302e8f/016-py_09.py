import numpy as np

def compare_grids(grid1, grid2):
    """Compares two grids and returns a detailed report."""
    grid1 = np.array(grid1)
    grid2 = np.array(grid2)

    report = {
        'match': False,
        'pixels_off': None,
        'size_correct': False,
       'rows_grid1':None,
       'cols_grid1':None,
       'rows_grid2':None,
       'cols_grid2':None,        
        'color_palette_correct': False,
        'correct_pixel_counts': False
    }

    if grid1.shape == grid2.shape:
        report['size_correct'] = True
       
    report['rows_grid1'] = grid1.shape[0]
    report['cols_grid1'] = grid1.shape[1]
    report['rows_grid2'] = grid2.shape[0]
    report['cols_grid2'] = grid2.shape[1]

    if np.array_equal(grid1, grid2):
        report['match'] = True
        report['pixels_off'] = 0
    else:
      
        diff = grid1 != grid2
        report['pixels_off'] = np.sum(diff)

    colors_grid1 = set(np.unique(grid1))
    colors_grid2 = set(np.unique(grid2))

    if colors_grid1 == colors_grid2:
        report['color_palette_correct'] = True

    pixel_counts_grid1 = {color: np.sum(grid1 == color) for color in colors_grid1}
    pixel_counts_grid2 = {color: np.sum(grid2 == color) for color in colors_grid2}

    if pixel_counts_grid1 == pixel_counts_grid2:
        report['correct_pixel_counts'] = True
        

    return report