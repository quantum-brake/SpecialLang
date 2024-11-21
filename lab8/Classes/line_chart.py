from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt


class LineChart(DataVisualizer):
    def visualize(self, save_as=None):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            for column in self.data.columns[1:]:
                plt.plot(self.data[self.data.columns[0]], self.data[column], label=column)
            plt.xlabel(self.data.columns[0])
            plt.ylabel("Значення")
            plt.title("Лінійний графік")
            plt.legend()
            plt.grid(True)
            if save_as:
                self.save_plot(save_as)
            else:
                plt.show()
        else:
            print("Дані ще не завантажені!")