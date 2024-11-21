class FontManager:
    def __init__(self):
        self.fonts = ["roman", "block", "bubble", "ghost", "big", "standard", "dot", "charis", "banner", "starwars"]

    def display_fonts(self):
        print("Доступні шрифти:", ', '.join(self.fonts))

    def choose_font(self):
        self.display_fonts()
        font = input("Оберіть шрифт зі списку (стандартний 'roman'): ") or "roman"
        if font not in self.fonts:
            print(f"Шрифт '{font}' не доступний, обирається стандартний 'roman'")
            font = 'roman'
        return font
