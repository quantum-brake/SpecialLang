from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt


class BarChart(DataVisualizer):
    def visualize(self, save_as=None):
        if self.data is not None:
            ax = self.data.plot(kind='bar', figsize=(10, 6))
            plt.title("Стовпчикова діаграма")
            plt.xlabel("Індекси")
            plt.ylabel("Значення")
            plt.grid(axis='y')
            if save_as:
                self.save_plot(save_as)
            else:
                plt.show()
        else:
            print("Дані ще не завантажені!")