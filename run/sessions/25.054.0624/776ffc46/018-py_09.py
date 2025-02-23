"""
1.  Identify Blue Clusters: Locate all contiguous clusters of blue (1) pixels in the input grid.

2.  Conditional Color Change: If a blue cluster is *not* directly adjacent (horizontally or vertically, not diagonally) to any other non-black, non-blue colors, change all pixels in that blue cluster to red (2).

3.  Expansion and Merging near Other Colors: If a blue cluster *is* adjacent to a non-black, non-blue color, the blue color expands. Pixels of other colors adjacent to this originally blue object now become the same color as the transformed object (red, value of 2).

4.  Preserve Other Colors: All pixels that are not part of the identified blue clusters, and not adjacent to changed blue clusters, retain their original colors. The overall grid dimensions remain unchanged.
"""

import numpy as np
from scipy.ndimage import label

def find_clusters(grid, color):
    """Finds clusters of a specific color in the grid."""
    colored_pixels = (grid == color)
    labeled_array, num_features = label(colored_pixels)
    return labeled_array, num_features

def get_adjacent_colors(grid, labeled_array, cluster_id):
    """Gets the set of colors adjacent to a specific cluster."""
    cluster_pixels = (labeled_array == cluster_id)
    rows, cols = grid.shape
    adjacent_colors = set()

    for r in range(rows):
        for c in range(cols):
            if cluster_pixels[r, c]:
                # Check neighbors (up, down, left, right)
                neighbors = []
                if r > 0:
                    neighbors.append((r - 1, c))
                if r < rows - 1:
                    neighbors.append((r + 1, c))
                if c > 0:
                    neighbors.append((r, c - 1))
                if c < cols - 1:
                    neighbors.append((r, c + 1))

                for nr, nc in neighbors:
                    if not cluster_pixels[nr, nc]:
                        adjacent_colors.add(grid[nr, nc])
    return adjacent_colors

def expand_cluster(grid, labeled_array, cluster_id, new_color):
    """Expands a cluster to include adjacent pixels of any color"""
    output_grid = np.copy(grid)
    cluster_pixels = (labeled_array == cluster_id)
    rows, cols = grid.shape
    
    for r in range(rows):
        for c in range(cols):
            if cluster_pixels[r,c]:
                #output_grid[r,c] = new_color # set the blue pixel
                neighbors = []
                if r > 0:
                    neighbors.append((r - 1, c))
                if r < rows - 1:
                    neighbors.append((r + 1, c))
                if c > 0:
                    neighbors.append((r, c - 1))
                if c < cols - 1:
                    neighbors.append((r, c + 1))
                for nr, nc in neighbors:
                    #if not cluster_pixels[nr, nc]: # do not expand to self
                    output_grid[nr,nc] = new_color
    return output_grid

def transform(input_grid):
    """Transforms the input grid based on blue cluster adjacency and expansion."""
    output_grid = np.copy(input_grid)
    labeled_array, num_blue_clusters = find_clusters(input_grid, 1)  # Find blue clusters

    for cluster_id in range(1, num_blue_clusters + 1):
        adjacent_colors = get_adjacent_colors(input_grid, labeled_array, cluster_id)
        cluster_pixels = (labeled_array == cluster_id)

        if any(color not in {0, 1} for color in adjacent_colors):
             # Expansion and change to red (2)
            output_grid = expand_cluster(output_grid, labeled_array, cluster_id, 2)
            # then set ALL blue pixels of this object to 2
            output_grid[cluster_pixels] = 2

        else:
            # Simple color change (blue to red)
           
            output_grid[cluster_pixels] = 2

    return output_grid