import math


class Shape3D:
    """Base class for 3D shapes."""

    def __init__(self, size):
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def rotate(self, angle_x=0, angle_y=0, angle_z=0):
        """Sets rotation angles."""
        self.angle_x += math.radians(angle_x)
        self.angle_y += math.radians(angle_y)
        self.angle_z += math.radians(angle_z)

    def apply_rotation(self, x, y, z):
        """Applies rotation to a point (x, y, z) based on set angles."""
        # Rotate around X-axis
        y, z = (
            y * math.cos(self.angle_x) - z * math.sin(self.angle_x),
            y * math.sin(self.angle_x) + z * math.cos(self.angle_x)
        )
        # Rotate around Y-axis
        x, z = (
            x * math.cos(self.angle_y) + z * math.sin(self.angle_y),
            -x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
        )
        # Rotate around Z-axis
        x, y = (
            x * math.cos(self.angle_z) - y * math.sin(self.angle_z),
            x * math.sin(self.angle_z) + y * math.cos(self.angle_z)
        )
        return int(x), int(y), int(z)

    def draw_line(self, x1, y1, x2, y2, canvas, symbol):
        """Draws a line between two points on the canvas, skipping only for horizontal lines."""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        step_count = 0

        while True:
            # Skip symbols only for horizontal lines (y1 == y2)
            if not (y1 == y2 and step_count % 2 != 0):  # draw continuously for vertical and diagonal lines
                if 0 <= y1 < len(canvas) and 0 <= x1 < len(canvas[0]):
                    canvas[int(y1)][int(x1)] = symbol
            step_count += 1
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def project_to_2d(self):
        """Abstract method for projecting the shape from 3D to 2D."""
        raise NotImplementedError("The project_to_2d method must be implemented in a subclass.")

