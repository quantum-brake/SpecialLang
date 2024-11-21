from Classes.ASCIIArt_generator import ASCIIGenerator


class UserInputManager:
    def __init__(self):
        self.ascii_generator = ASCIIGenerator()

    def update_text(self):
        self.ascii_generator.set_text(input("Введіть слово або фразу, яку хочете перетворити у ASCII art: "))

    def update_width(self):
        width = input("Введіть ширину (стандартно 10): ") or 10
        if width.isnumeric():
            self.ascii_generator.set_width(width)
        else:
            raise ValueError("Потрібно ввести число")

    def update_height(self):
        height = input("Введіть висоту (стандартно is 8): ") or 8
        if height.isnumeric():
            self.ascii_generator.set_width(height)
        else:
            raise ValueError("Потрібно ввести число")

    def update_alignment(self):
        print("Виберіть розташування:")
        print("1. Ліво")
        print("2. Центр")
        print("3. Право")
        alignment_option = input("Виберіть варіант (1, 2, or 3): ").strip()

        if alignment_option == '1':
            self.ascii_generator.set_alignment('left')
        elif alignment_option == '2':
            self.ascii_generator.set_alignment('center')
        elif alignment_option == '3':
            self.ascii_generator.set_alignment('right')
        else:
            print("Неправильний вибір. Використовується значення по стандарту (Ліво).")
            self.ascii_generator.set_alignment('left')