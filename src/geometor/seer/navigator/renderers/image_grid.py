from geometor.seer.navigator.renderers.base_grid import *

class ImageGrid(BaseGrid):
    """
    Grid rendered using an image-based approach via rich-pixels.
    This mode creates a PIL image with grid lines separating the cells.
    """

    def on_mount(self):
        try:
            from PIL import Image
            from rich_pixels import Pixels
        except ImportError:
            self.update(
                "Image rendering requires 'Pillow' and 'rich-pixels' libraries."
            )
            return

        # Determine cell pixel size (without grid lines)
        cell_pixel_size = 100
        lw = GRID_LINE_WIDTH
        # Compute total image size including grid lines between cells and around edges.
        img_width = self.cols * cell_pixel_size + (self.cols + 1) * lw
        img_height = self.rows * cell_pixel_size + (self.rows + 1) * lw

        # Create a new image and fill it with the grid line color.
        image = Image.new("RGB", (img_width, img_height), GRID_LINE_COLOR)
        # Fill each cell: calculate its top-left offset including the grid line offset.
        for r in range(self.rows):
            for c in range(self.cols):
                color = self.get_color(self.grid[r][c]) # use get_color
                x0 = lw + c * (cell_pixel_size + lw)
                y0 = lw + r * (cell_pixel_size + lw)
                for y in range(y0, y0 + cell_pixel_size):
                    for x in range(x0, x0 + cell_pixel_size):
                        image.putpixel((x, y), color.rgb) # use .rgb
        pixels = Pixels.from_image(image)
        self.update(pixels)

    def on_resize(self, event):
        """Regenerate the image on resize so that cell sizes scale with available space."""
        try:
            from PIL import Image
            from rich_pixels import Pixels
        except ImportError:
            return

        if self.cols == 0 or self.rows == 0:
            return

        lw = GRID_LINE_WIDTH
        new_width, new_height = event.size  # in terminal cells (approximation)
        # Determine available cell size (simple heuristic)
        factor_x = max(1, new_width // (self.cols + self.cols + 1))
        factor_y = max(1, new_height // (self.rows + self.rows + 1))
        cell_pixel_size = (
            min(factor_x, factor_y) * 2
        )  # scale factor; adjust multiplier for detail

        img_width = self.cols * cell_pixel_size + (self.cols + 1) * lw
        img_height = self.rows * cell_pixel_size + (self.rows + 1) * lw

        image = Image.new("RGB", (img_width, img_height), GRID_LINE_COLOR)
        for r in range(self.rows):
            for c in range(self.cols):
                color = self.get_color(self.grid[r][c])  # use get_color
                x0 = lw + c * (cell_pixel_size + lw)
                y0 = lw + r * (cell_pixel_size + lw)
                for y in range(y0, y0 + cell_pixel_size):
                    for x in range(x0, x0 + cell_pixel_size):
                        image.putpixel((x, y), color.rgb) # use .rgb
        pixels = Pixels.from_image(image)
        self.update(pixels)
