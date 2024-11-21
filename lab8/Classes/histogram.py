from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt


class Histogram(DataVisualizer):
    def visualize(self, save_as=None):
        if self.data is not None:
            self.data.hist(figsize=(10, 6))
            plt.suptitle("Гістограма")
            if save_as:
                self.save_plot(save_as)
            else:
                plt.show()
        else:
            print("Дані ще не завантажені!")