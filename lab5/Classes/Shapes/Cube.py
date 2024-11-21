from Classes.Shapes.Shape3D import Shape3D


class Cube(Shape3D):
    """Class for a cube."""

    def __init__(self, size):
        super().__init__(size)

    def project_to_2d(self):
        projection_height = self.size * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(int(projection_width * 2))] for _ in range(int(projection_height))]
        half = self.size // 2
        vertices = [
            (-half, -half, -half), (half, -half, -half),
            (half, half, -half), (-half, half, -half),
            (-half, -half, half), (half, -half, half),
            (half, half, half), (-half, half, half),
        ]

        rotated_vertices = [self.apply_rotation(x, y, z) for x, y, z in vertices]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Нижня грань
            (4, 5), (5, 6), (6, 7), (7, 4),  # Верхня грань
            (0, 4), (1, 5), (2, 6), (3, 7)  # Вертикальні ребра
        ]

        center_x = projection_width // 2 # Центрування по ширині

        min_y = min(v[1] for v in rotated_vertices)
        max_y = max(v[1] for v in rotated_vertices)
        vertical_offset = (projection_height // 2) - ((max_y + min_y) // 2) # Центрування по висоті

        # Рисувати ребра куба
        for start, end in edges:
            x1, y1, z1 = rotated_vertices[start]
            x2, y2, z2 = rotated_vertices[end]
            x1 += center_x
            y1 += vertical_offset
            x2 += center_x
            y2 += vertical_offset
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(x1 * 2, y1, x2 * 2, y2, projection, symbol)

        return projection
