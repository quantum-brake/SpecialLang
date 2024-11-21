import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Classes.Ascii_art_service import ASCIIArtService
from Classes.Fonts import FontManager


def user_input_interface():
    ascii_art_service = ASCIIArtService()
    font_manager = FontManager()

    text = "ASCII    Gen"
    font = "roman"
    color = "blue"
    custom_char = None
    width = 1
    height = 1

    while True:
        ascii_art, colored_art = ascii_art_service.generate_ascii_art(text, font, custom_char, width, height, color)

        print("\nПрев'ю згенерованого арту:\n")
        print(colored_art)

        print("\nMenu:")
        print("1. Встановити текст для арту")
        print("2. Вибрати шрифт")
        print("3. Вибрати колір")
        print("4. Встановити власний символ")
        print("5. Встановити ширину")
        print("6. Встановити висоту")
        print("7. Зберегти у файл")
        print("8. Вийти")

        choice = input("Оберіть дію (1-8): ")

        match choice:
            case "1":
                text = input("Введіть текст для ASCII art: ")
            case "2":
                font = font_manager.choose_font()
            case "3":
                color = input("Оберіть колір (red, green, blue, yellow, magenta, cyan, white): ").lower()
            case "4":
                custom_char = input("Введіть символ по якому генерувється ASCII art (необов'язково): ") or None
            case "5":
                width = ascii_art_service.set_dimensions("Введіть ширину ASCII art")
            case "6":
                height = ascii_art_service.set_dimensions("Введіть висоту ASCII art")
            case "7":
                filename = input("Введіть назву файлу: ")
                ascii_art_service.save_art(ascii_art, filename)
            case "8":
                print("Вхід...")
                break
            case _:
                print("Неправильний вибір, Спробуйте знову.")
