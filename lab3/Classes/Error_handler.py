import os


class ErrorHandler:
    def __init__(self, log_file=os.path.join(os.path.dirname(__file__), '../Data/error.log')):
        self.log_file = log_file
        if not os.path.exists(log_file):
            with open(log_file, 'w', encoding="ascii"):
                pass

    def log_error(self, error_message):
        with open(self.log_file, 'a', encoding="ascii") as f:
            f.write(error_message + '\n')

    def validate_text_input(self, text):
        if not text:
            self.log_error("Empty input provided.")
            raise ValueError("Input cannot be empty.")