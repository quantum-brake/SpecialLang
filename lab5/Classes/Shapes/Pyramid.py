from Classes.Shapes.Shape3D import Shape3D

class Pyramid(Shape3D):

    def __init__(self, size):
        super().__init__(size)

    def project_to_2d(self):
        projection_height = self.size * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(int(projection_width))] for _ in range(int(projection_height))]
        half = self.size // 2
        vertices = [
            (0, -half, half), (half, half, half),
            (-half, half, half), (0, 0, -half)
        ]

        # Обертання для кожної вершини
        rotated_vertices = [self.apply_rotation(x, y, z) for x, y, z in vertices]

        edges = [
            (0, 1), (1, 2), (2, 0),  # Основа піраміди
            (0, 3), (1, 3), (2, 3)  # Ребро до вершини
        ]

        center_x = projection_width // 2 # Центрування по ширині

        min_y = min(rotated_vertices, key=lambda v: v[1])[1]
        max_y = max(rotated_vertices, key=lambda v: v[1])[1]

        vertical_offset = (projection_height // 2) - ((max_y + min_y) // 2) # Центрування по висоті

        # Рисувати ребра піраміди
        for start, end in edges:
            x1, y1, z1 = rotated_vertices[start]
            x2, y2, z2 = rotated_vertices[end]
            x1 += center_x
            y1 += vertical_offset
            x2 += center_x
            y2 += vertical_offset
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(int(x1), int(y1), int(x2), int(y2), projection, symbol)

        return projection


