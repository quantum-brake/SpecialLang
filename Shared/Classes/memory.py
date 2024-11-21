from Shared.Variables.calculator_variables import memory


class Memory:
    def __init__(self):
        self.memory = memory

    def set_memory(self, value):
        self.memory = value

    def get_memory(self):
        return self.memory
