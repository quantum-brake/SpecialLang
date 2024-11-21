from colorama import Fore, Style, init


class ColorHandler:
    def __init__(self):
        init(autoreset=True)

        self.COLORS = {
            "red": Fore.RED,
            "green": Fore.GREEN,
            "blue": Fore.BLUE,
            "yellow": Fore.YELLOW,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE
        }

    def color_text(self, ascii_art, color):
        color_code = self.COLORS.get(color, Fore.WHITE)
        return f"{color_code}{ascii_art}{Style.RESET_ALL}"
