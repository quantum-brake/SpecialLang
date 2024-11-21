from Classes.Shapes.Cube import Cube
from Classes.Shapes.Pyramid import Pyramid


class ASCIIGenerator:
    def __init__(self):
        self._shape = None
        self._shape_type = "cube"
        self._size = 20
        self._angle_x = 21
        self._angle_y = 10
        self._angle_z = 0

        self.set_shape(self._shape_type, self._size)
        self.rotate_shape(self._angle_x, self._angle_y, self._angle_z)

    def set_shape_type(self, shape_type):
        self._shape_type = shape_type

    def get_shape_type(self):
        return self._shape_type

    def set_shape(self, shape_type, size):
        self._shape_type = shape_type
        self._size = size
        if shape_type == "cube":
            self._shape = Cube(size)
        elif shape_type == "pyramid":
            self._shape = Pyramid(size)

    def get_shape(self):
        return self._shape

    def set_size(self, size):
        self._size = size

    def get_size(self):
        return self._size

    def rotate_shape(self, angle_x, angle_y, angle_z):
        if self._shape:
            self._shape.rotate(angle_x, angle_y, angle_z)

    def set_x(self, x):
        self._angle_x = x

    def set_y(self, y):
        self._angle_y = y

    def set_z(self, z):
        self._angle_z = z

    def get_x(self):
        return self._angle_x

    def get_y(self):
        return self._angle_y

    def get_z(self):
        return self._angle_z
