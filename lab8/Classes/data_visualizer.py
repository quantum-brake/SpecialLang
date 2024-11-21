from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd


class DataVisualizer(ABC):
    _instance = None

    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super(DataVisualizer, cls).__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.data = None
        return cls._instance

    def load_data(self):
        if self.file_path:
            self.data = pd.read_csv(self.file_path)
            print("Дані успішно завантажені!")
        else:
            print("Шлях до файлу не вказаний!")

    def explore_data(self):
        if self.data is not None:
            print("Екстремальні значення:")
            print(self.data.describe())
        else:
            print("Дані ще не завантажені!")

    @abstractmethod
    def visualize(self, save_as=None):
        pass

    def save_plot(self, save_as):
        if save_as:
            plt.savefig(save_as, format=save_as.split('.')[-1])
            print(f"Графік збережено у файл: {save_as}")