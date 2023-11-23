# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import AnchoredText, DraggableOffsetBox
# from scipy import stats
# import statistics

# class YourClassName:  # Replace YourClassName with the actual class name
#     def your_method_name(self, fileName):
#         sns.set()
#         data = np.loadtxt(fileName[0], skiprows=1)

#         x1 = self.parameter1_list.currentIndex()
#         x = data[:, x1]

#         y1 = self.parameter2_list.currentIndex()
#         y = data[:, y1]

#         param1 = self.parameter1_list.currentText()
#         param2 = self.parameter2_list.currentText()

#         df = pd.DataFrame({f'{param1}': x, f'{param2}': y})
#         summary_stats = df.describe()

#         fig, axes = plt.subplots(2, 2, figsize=(10, 8))

#         for i, column in enumerate(df.columns):
#             sns.lineplot(x=df.index, y=df[column], ax=axes[i // 2, i % 2])
#             axes[i // 2, i % 2].set_title(f'Lineplot of {column}')

#         # Calculate statistics
#         mean_val = statistics.mean(y)
#         median_val = statistics.median(y)
#         std_dev = statistics.stdev(y)
#         mode_val = stats.mode(list(y))
#         variance_val = np.var(y)

#         # Display statistics
#         summary_text = f'Mean: {mean_val}\nMedian: {median_val}\nStd Dev: {std_dev}\nMode: {mode_val.mode[0]}\nVariance: {variance_val}'
#         anchored_text = AnchoredText(summary_text, loc='lower left', prop=dict(size=10), frameon=True,
#                                      bbox_to_anchor=(0., 1.), bbox_transform=axes[0, 0].transAxes)
#         anchored_text.patch.set_boxstyle("round, pad=0., rounding_size=0.2")
#         axes[0, 0].add_artist(anchored_text)

#         plt.tight_layout()
#         plt.show()



#         sns.set()
#         data = np.loadtxt(fileName[0], skiprows=1)

#         x1 = self.parameter1_list.currentIndex()
#         x = data[:, x1]

#         y1 = self.parameter2_list.currentIndex()
#         y = data[:, y1]

#         param1 = self.parameter1_list.currentText()
#         param2 = self.parameter2_list.currentText()

#         df = pd.DataFrame({f'{param1}': x, f'{param2}': y})
#         summary_stats = df.describe()

#         fig, axes = plt.subplots(2, 2, figsize=(10, 8))

#         for i, column in enumerate(df.columns):
#             sns.lineplot(x=df.index, y=df[column], ax=axes[i // 2, i % 2])
#             axes[i // 2, i % 2].set_title(f'Lineplot of {column}')

#         # Calculate statistics
#         mean_val = statistics.mean(y)
#         median_val = statistics.median(y)
#         std_dev = statistics.stdev(y)
#         mode_val = stats.mode(list(y))
#         variance_val = np.var(y)

#         # Display statistics
#         summary_text = f'Mean: {mean_val}\nMedian: {median_val}\nStd Dev: {std_dev}\nMode: {mode_val.mode[0]}\nVariance: {variance_val}'
#         anchored_text = AnchoredText(summary_text, loc='lower left', prop=dict(size=10), frameon=True,
#                                      bbox_to_anchor=(0., 1.), bbox_transform=axes[0, 0].transAxes)

#         # Make the anchored text movable
#         draggable_anchored_text = DraggableOffsetBox(anchored_text, transform=axes[0, 0].transAxes, pad=0.1)
#         axes[0, 0].add_artist(draggable_anchored_text)

#         plt.tight_layout()
#         plt.show()


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox, OffsetImage
from scipy import stats
import statistics

# class YourClassName:  # Replace YourClassName with the actual class name
#     def your_method_name(self, fileName):
        # sns.set()
        # data = np.loadtxt(fileName[0], skiprows=1)

        # x1 = self.parameter1_list.currentIndex()
        # x = data[:, x1]

        # y1 = self.parameter2_list.currentIndex()
        # y = data[:, y1]

        # param1 = self.parameter1_list.currentText()
        # param2 = self.parameter2_list.currentText()

        # df = pd.DataFrame({f'{param1}': x, f'{param2}': y})
        # summary_stats = df.describe()

        # fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        # for i, column in enumerate(df.columns):
        #     sns.lineplot(x=df.index, y=df[column], ax=axes[i // 2, i % 2])
        #     axes[i // 2, i % 2].set_title(f'Lineplot of {column}')

        # # Calculate statistics
        # mean_val = statistics.mean(y)
        # median_val = statistics.median(y)
        # std_dev = statistics.stdev(y)
        # mode_val = stats.mode(list(y))
        # variance_val = np.var(y)

        # # Display statistics
        # summary_text = f'Mean: {mean_val}\nMedian: {median_val}\nStd Dev: {std_dev}\nMode: {mode_val.mode[0]}\nVariance: {variance_val}'

        # # Create an OffsetImage with the summary text
        # imagebox = OffsetImage(summary_text, pad=0.1, bbox=dict(facecolor='white', alpha=0.9, edgecolor='white'))

        # # Create an AnchoredOffsetbox with the OffsetImage
        # anchored_text = AnchoredOffsetbox(loc='lower left', child=imagebox, frameon=True, bbox_to_anchor=(0., 1.),
        #                                   bbox_transform=axes[0, 0].transAxes)

        # axes[0, 0].add_artist(anchored_text)

        # # Function to handle dragging events
        # def on_click(event):
        #     if event.inaxes == axes[0, 0]:
        #         anchored_text.set_offset((event.xdata, event.ydata))
        #         plt.draw()

        # # Connect the dragging event to the figure
        # fig.canvas.mpl_connect('button_press_event', on_click)

        # plt.tight_layout()
        # plt.show()
import plotly.graph_objects as go

# fig = go.Figure(go.Indicator(
#     mode = "number+gauge+delta",
#     gauge = {'shape': "bullet"},
#     delta = {'reference': 300},
#     value = 220,
#     domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
#     title = {'text': "Avg order size"}))

# fig.show()

# fig = go.Figure(go.Indicator(
#     mode = "number+delta",
#     value = 492,
#     number = {"prefix": "$", "suffix": "m"},
#     delta = {"reference": 512, "valueformat": ".0f", "prefix": "$", "suffix": "m"},
#     title = {"text": "Profit"},
#     domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

# fig.add_trace(go.Scatter(
#     y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

# fig.update_layout(xaxis = {'range': [0, 62]})
# fig.show()


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
