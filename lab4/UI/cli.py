import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Classes.asciiArt_service import AsciiArtService


def user_input_interface():
    ascii_art_service = AsciiArtService()

    while True:
        ascii_art_service.display_ascii_art()

        print("\nМеню:")
        print("1. Ввести текст")
        print("2. Задати колір")
        print("3. Задати ширину")
        print("4. Задати висоту")
        print("5. Виставити розташування")
        print("6. Зберегти ASCII art у файл")
        print("7. Вийти")
        choice = input("Виберіть опцію: ").strip()
        match choice:
            case '1':
                ascii_art_service.update_text()
            case '2':
                ascii_art_service.update_color()
            case '3':
                try:
                    ascii_art_service.update_width()
                except ValueError as e:
                    print(e)
            case '4':
                try:
                    ascii_art_service.update_height()
                except ValueError as e:
                    print(e)
            case '5':
                ascii_art_service.update_alignment()
            case '6':
                ascii_art_service.save_ascii_art()
            case '7':
                print("Вихід з програми...")
                break
            case _:
                print("Не правильний варіант, виберіть зі списку.")
