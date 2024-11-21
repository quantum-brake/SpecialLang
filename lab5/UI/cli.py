import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Classes.ascii_art_service import AsciiArtService


def user_input_interface():
    ascii_art_service = AsciiArtService()

    while True:
        ascii_art_service.display_ascii_art()

        print("\nМеню:")
        print("1. Вибрати фігуру (cube/pyramid)")
        print("2. Встановити розмір")
        print("3. Обновити колір")
        print("4. Кут X ")
        print("5. Кут Y")
        print("6. Кут Z")
        print("7. Зберегти у файл")
        print("9. Вийти")
        choice = input("Виберіть опцію: ").strip()
        match choice:
            case '1':
                ascii_art_service.update_shape()
            case '2':
                ascii_art_service.update_size()
            case '3':
                ascii_art_service.update_color()
            case '4':
                ascii_art_service.update_x()
            case '5':
                ascii_art_service.update_y()
            case '6':
                ascii_art_service.update_z()
            case '7':
                ascii_art_service.save_to_file()
            case '9':
                print("Вихід з програми...")
                break
            case _:
                print("Неправильний вибір.")
