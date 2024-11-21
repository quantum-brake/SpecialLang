from Classes.ascii_generator import ASCIIGenerator

class UserInputManager:
    def __init__(self):
        self.ascii_art_generator = ASCIIGenerator()

    def update_shape(self):
        try:
            shape_type = input("Виберіть фігуру (cube/pyramid): ").strip().lower()
            if shape_type not in ['cube', 'pyramid']:
                raise ValueError("Невідома фігура.")
            self.ascii_art_generator.set_shape_type(shape_type)
        except ValueError as e:
            print(e)

    def update_size(self):
        try:
            size = int(input(f"Введіть розмір фігури (7-50, поточний: {self.ascii_art_generator.get_size()} ): ") or self.ascii_art_generator.get_size())
            if 7 <= size <= 50:
                self.ascii_art_generator.set_size(size)
            else:
                print("Розмір має бути від 7 до 50.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    def update_x(self):
        try:
            angle_x = float(input(f"Введіть обертання по X° (-180° до 180°, поточний: {self.ascii_art_generator.get_x()}): ") or self.ascii_art_generator.get_x())
            if -180 <= angle_x <= 180:
                self.ascii_art_generator.set_x(angle_x)
            else:
                print("Кут обертання має бути від -180° до 180°.")
        except ValueError:
            print("Будь ласка, введіть число.")

    def update_y(self):
        try:
            angle_y = float(input(f"Введіть обертання по Y° (-180° до 180°, поточний: {self.ascii_art_generator.get_y()} ): ") or self.ascii_art_generator.get_y())
            if -180 <= angle_y <= 180:
                self.ascii_art_generator.set_y(angle_y)
            else:
                print("Кут обертання має бути від -180° до 180°.")
        except ValueError:
            print("Будь ласка, введіть число.")

    def update_z(self):
        try:
            angle_z = float(input(f"Введіть обертання по Z° (-180° до 180°, поточний: {self.ascii_art_generator.get_z()}): ") or self.ascii_art_generator.get_z())
            if -180 <= angle_z <= 180:
                self.ascii_art_generator.set_z(angle_z)
            else:
                print("Кут обертання має бути від -180° до 180°.")
        except ValueError:
            print("Будь ласка, введіть число.")
