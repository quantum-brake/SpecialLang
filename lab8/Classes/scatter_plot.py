from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt


class ScatterPlot(DataVisualizer):
    def visualize(self, save_as=None):
        if self.data is not None:
            plt.figure(figsize=(10, 6))

            x_column = self.data.columns[0]
            y_columns = self.data.columns[1:]

            x_labels = self.data[x_column]
            x_positions = range(len(x_labels))

            colors = ['blue', 'green', 'red']
            for y_column, color in zip(y_columns, colors):
                plt.scatter(x_positions, self.data[y_column], label=y_column, color=color)

            plt.xlabel(x_column)
            plt.ylabel("Значення")
            plt.title("Діаграма розсіювання (Expenses, Sales, Profit)")

            plt.xticks(ticks=x_positions, labels=x_labels, rotation=45)

            plt.legend()

            if save_as:
                self.save_plot(save_as)
            else:
                plt.show()
        else:
            print("Дані ще не завантажені!")