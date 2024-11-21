from Classes.ascii_art_colorizer import Colorizer


class ArtDisplayer:
    def __init__(self):
        self.colorizer = Colorizer()

    def display_ascii_art(self, shape, color):
        projection = shape.project_to_2d()
        for row in projection:
            projection_row = "".join(row)
            if color:
                projection_row = self.colorizer.colorize(projection_row, color)
            print(projection_row)

