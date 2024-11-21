import os
from Classes.bar_chart import BarChart
from Classes.histogram import Histogram
from Classes.line_chart import LineChart
from Classes.scatter_plot import ScatterPlot


class Service:
    def __init__(self):
        self._visualizer = None
        self._file_path = os.path.join(os.path.dirname(__file__), "../Config/dataset.csv")

    def select_file(self):
        file_path = input("Введіть шлях до CSV-файлу: ").strip()
        if os.path.isfile(file_path):
            self._file_path = file_path
            print("Файл успішно завантажено!")
        else:
            print("Файл не існує. Спробуйте ще раз.")

    def select_visualization(self):
        if not self._file_path:
            print("Спочатку виберіть файл!")
            return

        chart_type = input("Оберіть тип візуалізації (line/bar/histogram/scatter): ").strip().lower()
        match chart_type:
            case 'line':
                self._visualizer = LineChart(self._file_path)
            case 'bar':
                self._visualizer = BarChart(self._file_path)
            case 'histogram':
                self._visualizer = Histogram(self._file_path)
            case 'scatter':
                self._visualizer = ScatterPlot(self._file_path)
            case _:
                print("Невірний тип візуалізації. Спробуйте ще раз.")

    def display_data(self):
        if self._visualizer:
            self._visualizer.load_data()
            self._visualizer.explore_data()
            self._visualizer.visualize()
        else:
            print("Спочатку виберіть файл і тип візуалізації!")

    def save_to_file(self):
        if not self._visualizer:
            print("Спочатку виберіть файл і тип візуалізації!")
            return

        try:
            file_name = input("Введіть ім'я файлу з розширенням (наприклад, graph.png або graph.svg): ").strip()

            save_path = os.path.join("Data", file_name)

            self._visualizer.visualize(save_path)

        except ValueError as e:
            print(f"Помилка під час збереження файлу: {e}")
