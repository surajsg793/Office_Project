import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
import seaborn as sns
import sys
from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft, fftfreq
from scipy.signal import find_peaks, butter, lfilter, freqz
from peakdetect import peakdetect
from matplotlib.offsetbox import AnchoredText
import mplcursors
import re
import pandas as pd
import seaborn as sns
from scipy.fft import fft, fftfreq, ifft, fftshift
from scipy import fftpack, stats, signal
import statistics
from scipy.stats import norm
import scipy.stats
from scipy import stats
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QLabel,
    QDialog,
    QCheckBox,
    QComboBox,
    QDialogButtonBox, 
    QVBoxLayout,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QGridLayout,
)
import mplcursors
import matplotlib.pyplot as plt
import statistics
from scipy import stats, signal
from matplotlib.offsetbox import AnchoredText
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd

class DataViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Viewer')
        self.resize(800, 600)

        button_style = """
            QPushButton {
                background-color: #007BFF;
                color: black;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton[data-type="special"] {
                background-color: darkorange;
            }
            QPushButton[data-type="special"]:hover {
                background-color: #ff8c00;
            }
        """
        bold_font = QFont()
        bold_font.setBold(True)

        self.setStyleSheet(f"""
            QMainWindow {{ background-color: skyblue; border: 2px solid skyblue; }}
            QTableWidget {{ background-color: lightgray; }}
            {button_style}
        """)


        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.search_layout = QHBoxLayout()
        self.search_edit = QLineEdit(self)
        self.search_edit.setPlaceholderText('Search...')
        self.search_layout.addWidget(self.search_edit)

        self.search_edit.returnPressed.connect(self.search_value)

        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.search_value)
        self.search_layout.addWidget(self.search_button)

        top_layout = QVBoxLayout()
        top_layout.addLayout(self.search_layout)
        self.layout.addLayout(top_layout)

        # Add QSplitter for adjustable table and plot
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.layout.addWidget(splitter)

        self.table_widget = QTableWidget(self)
        splitter.addWidget(self.table_widget)

        self.canvas = FigureCanvas(plt.Figure(figsize=(5, 3)))
        splitter.addWidget(self.canvas)

        bold_font = QFont()
        bold_font.setBold(True)

        # Create a horizontal layout for sampling rate, cutoff frequency, and stats checkbox
        self.horizontal_layout = QHBoxLayout()

        # Sampling Rate Label and Edit
        self.sampling_rate_label = QLabel('Sampling Rate (steps/sec):', self)
        self.sampling_rate_label.setFont(bold_font)
        self.horizontal_layout.addWidget(self.sampling_rate_label)

        self.sampling_rate_edit = QLineEdit(self)
        self.sampling_rate_edit.setPlaceholderText('Enter sampling rate')
        self.horizontal_layout.addWidget(self.sampling_rate_edit)

        # CutOff Frequency Label and Edit
        self.cutoff_frequency_label = QLabel('CutOff Frequency (Hz):', self)
        self.cutoff_frequency_label.setFont(bold_font)
        self.horizontal_layout.addWidget(self.cutoff_frequency_label)

        self.cutoff_frequency_edit = QLineEdit(self)
        self.cutoff_frequency_edit.setPlaceholderText('Enter cutoff frequency')
        self.horizontal_layout.addWidget(self.cutoff_frequency_edit)

        # Stats Checkbox
        self.stats_checkbox = QCheckBox('Show Statistics Report', self)
        self.stats_checkbox.setFont(bold_font)
        self.stats_checkbox.stateChanged.connect(self.toggle_stats_report) 
        self.horizontal_layout.addWidget(self.stats_checkbox)

        # Add the horizontal layout to the main layout
        self.layout.addLayout(self.horizontal_layout)

        # Connect the text boxes to their respective update methods
        self.sampling_rate_edit.textChanged.connect(self.update_sampling_rate)
        self.cutoff_frequency_edit.textChanged.connect(self.update_cutoff_frequency)

        self.grid_layout = QGridLayout(self.central_widget)
        self.layout.addLayout(self.grid_layout)

        buttons = [
            ('Load Data', self.load_data),
            ('Data Plot', self.plot_data),
            ('Compare File Data', self.compare_data),
            ('Cross-Correlation', self.cross_correlation),
            ('Interpolation', self.interpolation),
            ('Auto-Correlation', self.auto_correlation),
            ('Transfer-Function', self.transfer_function),
            ('Phase-Spectrum', self.phase_spectrum),
            ('FFT', self.fft),
            ('Linear Regression', self.linear_regression),
            ('Low-Pass-Filter', self.low_pass_filter),
            ('High-Pass-Filter', self.high_pass_filter),  
            ('Inter-Channel Averages', self.inter_channel_averages),
            ('Inter-Correlation', self.inter_correlation),
            ('Power-Spectrum', self.power_spectrum),
            ('Smoothing', self.smoothing),
            ('Coherence', self.coherence),
            ('Magnitude-Spectrum', self.magnitude_spectrum),
        ]

        for i, (button_text, button_callback) in enumerate(buttons):
            button = QPushButton(button_text, self)
            button.clicked.connect(button_callback)
            if button_text in ["Load Data", "Compare Data", "Plot Data"]:
                button.setProperty("data-type", "special")
            button.setStyleSheet(button_style)
            row, col = divmod(i, 4)
            self.grid_layout.addWidget(button, row, col)

        self.data_frames = []
        self.filtered_data = None
        self.show_stats_report = False

        self.set_search_options_enabled(False)

        self.show()
    
    def select_parameters(self, parameter1_required=True, parameter2_required=True):
    # def select_parameters(self):
        parameter_dialog = QDialog(self)
        parameter_dialog.setWindowTitle('Select Parameters')

        parameter_layout = QVBoxLayout(parameter_dialog)

        label_1 = QLabel('Select Parameter 1:')
        combo_1 = QComboBox(parameter_dialog)

        label_2 = QLabel('Select Parameter 2:')
        combo_2 = QComboBox(parameter_dialog)

        column_names = [self.table_widget.item(0, col).text() for col in range(self.table_widget.columnCount())]

        combo_1.addItems(column_names)
        combo_2.addItems(column_names)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(parameter_dialog.accept)
        button_box.rejected.connect(parameter_dialog.reject)

        parameter_layout.addWidget(label_1)
        parameter_layout.addWidget(combo_1)
        parameter_layout.addWidget(label_2)
        parameter_layout.addWidget(combo_2)
        parameter_layout.addWidget(button_box)

        result = parameter_dialog.exec_()

        if result == QDialog.Accepted:
            selected_column_1 = combo_1.currentIndex()
            selected_column_2 = combo_2.currentIndex()
            return selected_column_1, selected_column_2
        else:
            return None, None

    def update_sampling_rate(self, text):
        try:
            self.sampling_rate = float(text)
        except ValueError:
            self.sampling_rate = None

    def update_cutoff_frequency(self, text):
        try:
            self.cutoff_frequency = float(text)
        except ValueError:
            self.cutoff_frequency = None

    def set_search_options_enabled(self, enabled):
        self.search_edit.setEnabled(enabled)
        self.search_button.setEnabled(enabled)

    def toggle_stats_report(self, state):
        self.show_stats_report = state == Qt.Checked

    def load_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog
        global file_names
        file_names, _ = QFileDialog.getOpenFileNames(
            self, 'Open Data Files', '', 'CSV Files (*.csv *.txt);;All Files (*)', options=options
        )

        
        if file_names:
            self.load_data_to_table(file_names)
            # self.interpolation(file_names)

    def load_data_to_table(self, file_names):
        self.data_frames = []
        for file_name in file_names:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                data = [line.strip().split(',') for line in lines]
                df = pd.DataFrame(data[0:], columns=data[0])
                self.data_frames.append(df)

        self.display_data_in_table(self.data_frames[0])
        self.set_search_options_enabled(True)

    def display_data_in_table(self, df):
        self.table_widget.setRowCount(len(df))
        self.table_widget.setColumnCount(len(df.columns))

        for row_index, (_, row_data) in enumerate(df.iterrows()):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_index, col_index, item)
        self.table_widget.resizeColumnsToContents()

    def compare_data(self):
        if len(self.data_frames) < 2:
            QMessageBox.warning(self, 'Error', 'Please load at least two files for comparison.')
            return

        first_df = self.data_frames[0]
        for df in self.data_frames[1:]:
            if not first_df.equals(df):
                QMessageBox.warning(self, 'Error', 'Data structures are not the same in all files.')
                return

        QMessageBox.information(self, 'Comparison', 'All files have the same data structure. Comparison can proceed.')

    def plot_data(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]

            if data:
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(data)
                if self.show_stats_report:
                    mean = statistics.mean(data)
                    median = statistics.median(data)
                    std = statistics.stdev(data)
                    mode = stats.mode(list(data))
                    variance = np.var(data)
                    stat_res = (
                        'Statistics Report:'
                        + '\n'
                        + f'  => Mean is {float(mean)}'
                        + '\n'
                        + f'  => Median is {float(median)}'
                        + '\n'
                        + f'  => Mode is {float(np.array(mode)[0])}'
                        + '\n'
                        + f'  => Standard Deviation is {float(std)}'
                        + '\n'
                        + f'  => Variance is {float(variance)}'
                    )

                    anchored_txt = AnchoredText(
                        stat_res, loc='lower left', prop=dict(size=8), frameon=True, bbox_to_anchor=(0.0, 1.0),picker=True, bbox_transform=ax.transAxes
                    )
                    anchored_txt.patch.set_boxstyle('round, pad=0.2, rounding_size=0.2')
                    ax.add_artist(anchored_txt)

                ax.set_title(f"Column {selected_column + 1} - Parameter Name: {first_value}")
                mplcursors.cursor(hover=True)
                fig.legend()
                fig = plt.gcf()
                fig.canvas.manager.set_window_title(f'{first_value}')
                ax.set_xlabel("Row Index")
                ax.set_ylabel("Value")

                if self.show_stats_report:
                    ax.legend()

                self.canvas.figure = fig
                self.canvas.draw()
                plt.show()
            else:
                QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')

    def extract_data_from_column(self, column_index):
        data = []

        for df in self.data_frames:
            for row_index, (_, row_data) in enumerate(df.iterrows()):
                item = self.table_widget.item(row_index, column_index)
                try:
                    if item is not None and item.text().replace('.', '', 1).isdigit():
                        data.append(float(item.text()))
                    else:
                        data.append(None)
                except ValueError:
                    data.append(None)
        return [value for value in data if value is not None]

    def search_value(self):
        search_text = self.search_edit.text().strip().lower()

        if not search_text:
            return

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

        for df_index, df in enumerate(data_frames):
            for row_index, (_, row_data) in enumerate(df.iterrows()):
                for col_index, col_data in enumerate(row_data):
                    item = self.table_widget.item(row_index, col_index)

                    if item and search_text in str(col_data).lower():
                        item.setBackground(Qt.yellow)
                    else:
                        item.setBackground(Qt.white)
    
    def fft(self):
        selected_column = self.table_widget.currentColumn()

        if selected_column < 0:
            return        

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

            data = []
        first_value = None
        for df in data_frames:
            item = self.table_widget.item(0, selected_column)
            if item is not None:
                first_value = str(item.text())
                break

        if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

        data = self.extract_data_from_column(selected_column)

        if not data:
            QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')
            return

        sns.set()

        sampling_freq = self.sampling_rate_edit.text()

        if (data == 0 or sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the Sampling Rate")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()
            return

        fig, ax = plt.subplots()
        fft_plt = fft(data[1:])
        sampling_freq1 = float(sampling_freq)
        fft_lenth = len(fft_plt[1:])
        y_smapleLen = len(data)
        n = np.arange(fft_lenth)
        T = y_smapleLen / sampling_freq1  # time period
        freq = n / T  # FFT frequency
        f1 = freq[: fft_lenth]
        plt.plot(f1, abs(fft_plt[1:len(fft_plt)]))
        freqs = f1

        y_abs = np.abs(fft_plt)
        Peaks_indices, properties = find_peaks(y_abs,0)

        pks_values = y_abs[Peaks_indices]
        pks_values=set(pks_values)

        if(len(Peaks_indices) < 5):
            y_abs = np.abs(fft_plt)
            Peaks_indices, properties = find_peaks(y_abs, 0)

            pks_values = y_abs[Peaks_indices]
            pks_values = set(pks_values)
            first_5_max_peasks = np.argpartition(properties['peak_heights'], -len(Peaks_indices))[-len(Peaks_indices):]
            res2 = "Magnitude"+ "           " +"Frequency\n"
            for x in first_5_max_peasks:
                ferq = freqs[Peaks_indices[x]]
                res2=res2+str("{:.3f}".format(y_abs[Peaks_indices[x]])) + "         " +str("{:.3f}".format(ferq)) + "\n"
        else:
            first_5_max_peasks = np.argpartition(properties['peak_heights'], -5)[-5:]
            res2 = "Magnitude"+"                "+"Frequency\n"
            for x in first_5_max_peasks:
                ferq = freqs[Peaks_indices[x]]
                res2 = res2 + str("{:.3f}".format(y_abs[Peaks_indices[x]])) +"          "+ str("{:.3f}".format(ferq)) + "\n"

        anchored_txt1 = AnchoredText(res2, loc='lower left', prop=dict(size=9.5), frameon=True,
                                     bbox_to_anchor=(0., 1.),
                                     bbox_transform=ax.transAxes)
        anchored_txt1.patch.set_boxstyle("round, pad = 0., rounding_size = 0.2")
        ax.add_artist(anchored_txt1)

        mplcursors.cursor(hover=True)
        plt.xlabel("Frequency(Hz)")
        plt.ylabel("FFT of the Signal(Magnitude)")
        str1 = first_value
        plt.title("FFT result of " + str1, loc='right')
        # fig.tight_layout()
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('FFT Plot')
        plt.show()

    def phase_spectrum(self):
        selected_column = self.table_widget.currentColumn()

        if selected_column < 0:
            return        

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

            data = []
        first_value = None
        for df in data_frames:
            item = self.table_widget.item(0, selected_column)
            if item is not None:
                first_value = str(item.text())
                break

        if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

        data = self.extract_data_from_column(selected_column)

        if not data:
            QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')
            return
        sns.set()
        plt.phase_spectrum(data, color = 'blue')
        fig = plt.gcf()
        fig.canvas.manager.set_window_title(f'Phase Spectrum of {first_value}')
        plt.title(f'Phase Spectrum of {first_value}')
        mplcursors.cursor(hover = True)
        plt.show()

    def cross_correlation(self):
        selected_column_1, selected_column_2 = self.select_parameters(parameter1_required=True, parameter2_required=True)
        # , sampling_frequency, cutoff_frequency


        # Validate that both columns are selected and different
        if selected_column_1 is not None and selected_column_2 is not None and selected_column_1 != selected_column_2:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data_1 = []
            data_2 = []
            first_value_1 = None
            first_value_2 = None

            for df in data_frames:
                item_1 = self.table_widget.item(0, selected_column_1)
                item_2 = self.table_widget.item(0, selected_column_2)

                if item_1 is not None:
                    first_value_1 = str(item_1.text())

                if item_2 is not None:
                    first_value_2 = str(item_2.text())

            if first_value_1 is None or first_value_2 is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected columns.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item_1 = self.table_widget.item(row_index, selected_column_1)
                    item_2 = self.table_widget.item(row_index, selected_column_2)

                    try:
                        if item_1 is not None and item_2 is not None and \
                           item_1.text().replace('.', '', 1).isdigit() and item_2.text().replace('.', '', 1).isdigit():
                            data_1.append(float(item_1.text()))
                            data_2.append(float(item_2.text()))
                        else:
                            data_1.append(None)
                            data_2.append(None)
                    except ValueError:
                        data_1.append(None)
                        data_2.append(None)

            data_1 = [value for value in data_1 if value is not None]
            data_2 = [value for value in data_2 if value is not None]

            if data_1 and data_2:
                # Perform cross-correlation plot
                cross_correlation = np.correlate(data_1, data_2, mode='full')
                lags = np.arange(-len(data_1) + 1, len(data_1))

                fig, ax = plt.subplots()
                ax.plot(lags, cross_correlation)
                ax.set_title(f"Cross-Correlation - Parameters: {first_value_1} and {first_value_2}")
                mplcursors.cursor(hover=True)
                fig = plt.gcf()
                fig.canvas.manager.set_window_title(f'Cross-Correlation - {first_value_1} and {first_value_2}')
                ax.set_xlabel("Lag")
                ax.set_ylabel("Cross-Correlation Value")

                self.canvas.figure = fig
                self.canvas.draw()
                plt.show()
            else:
                QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected columns.')
        else:
            QMessageBox.warning(self, 'Error', 'Please select two different columns for cross-correlation.')

    def transfer_function(self):
        selected_column_1, selected_column_2 = self.select_parameters(parameter1_required=True, parameter2_required=True)

        # Validate that both columns are selected and different
        if selected_column_1 is None or selected_column_2 is None or selected_column_1 == selected_column_2:
            QMessageBox.warning(self, "Error", "Please select different valid columns for Parameter 1 and Parameter 2.")
            return

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

        data_1 = []
        data_2 = []
        first_value_1 = None

        # Extracting data from the first row
        for df in data_frames:
            item_1 = self.table_widget.item(0, selected_column_1)
            item_2 = self.table_widget.item(0, selected_column_2)

            if item_1 is not None:
                first_value_1 = str(item_1.text())

            if item_2 is not None:
                try:
                    data_2.append(float(item_2.text()))
                except ValueError:
                    data_2.append(None)
                    # Handle the case where the text cannot be converted to a float
                    QMessageBox.warning(self, "Error", f"Invalid data in {selected_column_2}. Could not convert to float.")
            else:
                QMessageBox.warning(self, "Error", "No valid data in the selected columns.")
                return

        for df in data_frames:
            for row_index, (_, row_data) in enumerate(df.iterrows()):
                item_1 = self.table_widget.item(row_index, selected_column_1)
                item_2 = self.table_widget.item(row_index, selected_column_2)

                try:
                    if item_1 is not None and item_2 is not None and \
                       item_1.text().replace('.', '', 1).isdigit() and item_2.text().replace('.', '', 1).isdigit():
                        data_1.append(float(item_1.text()))
                    else:
                        data_1.append(None)
                except ValueError:
                    data_1.append(None)

        input_data = [value for value in data_1 if value is not None]
        output_data = [value for value in data_2 if value is not None]

        if not input_data or not output_data:
            QMessageBox.warning(self, "Error", "No valid data in the selected columns.")
            return

        sys = signal.TransferFunction(input_data, output_data)

        try:
            time, response = signal.step(sys)
        except MemoryError:
            QMessageBox.warning(self, "Error", "Memory error!!! Please select fewer samples and try again.")
            return

        plt.plot(time, response)
        mplcursors.cursor(hover=True)
        plt.title(f"Transfer Function result of {first_value_1}")
        plt.xlabel("Time (sec)")
        plt.ylabel("Amplitude")
        plt.show()

    def auto_correlation(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]


        sns.set()
        fig, ax = plt.subplots(figsize=(8, 5))
        str1 = first_value
        plt.acorr(data, maxlags=10) 

        time_delay_str = "Autocorrelation Coeffecient ranges from +1 to -1" + "\n" + "If Autocorrelation Coeffecient:" + "\n" + " => +1, if Time Series 1 increase in value then " + "\n" + "  Time Series 2 also increase in propotion to change in Time Series 1" + "\n" + " => -1, if Time Series 1 increase in value then" + "\n" + "  Time Series 2  decrease in propotion to change in Time Series 1"
        anchored_txt1 = AnchoredText(time_delay_str, loc='lower left', prop=dict(size=11), frameon=True,
                                     bbox_to_anchor=(0., 1.),
                                     bbox_transform=ax.transAxes)
        anchored_txt1.patch.set_boxstyle("round, pad = 0., rounding_size = 0.2")
        ax.add_artist(anchored_txt1)

        plt.title("Result of Autocorrelation of " + str1)
        plt.xlabel("Lag(Sec)")
        plt.ylabel("Autocorrelation Coeffecient")
        mplcursors.cursor(hover=True)
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Autocorelation Plot')
        plt.show()

    def interpolation(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]


            sns.set()
            fig, (ax1, ax2) = plt.subplots(2, 1)
            # Convert the data list to a numeric numpy array
            numpy_array = np.array(data, dtype=np.float64)

            # Create a DataFrame with the numeric data
            df = pd.DataFrame({f'col_{selected_column}': numpy_array})

            # Perform interpolation
            interp_res = df.interpolate(method='linear', limit_direction='forward')
            df1 = pd.DataFrame(interp_res)


        numpy_array1 = df.to_numpy()
        x = numpy_array1[:, 0]
        y = numpy_array1[:, 0]
        ax1.plot(x, y, c='b', label='Original Data')
        ax1.set_title("Time Series Data")
        ax1.set_ylabel("Amplitude (V)")
        ax1.set_xlabel("Time(Sec)")

        numpy_array2 = df1.to_numpy()
        p = numpy_array2[:, 0]
        q = numpy_array2[:, 0]

        mplcursors.cursor(hover=True)
        fig.legend(loc='upper right')


        plt.xlabel("Time (Sec)")
        ax2.set_title("Result of Interpolation")
        ax2.plot(x, q, c = 'k', label = 'Data after Interpolation')
        fig.legend(loc='upper right')
        ax2.set_xlabel("Time(Sec)")
        ax2.set_ylabel("Amplitude(V)")
        plt.show()


    def linear_regression(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]

            if data:
                slope, intercept, r_value, p_value, std_err = stats.linregress(np.arange(len(data)), data)

                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(data, label='Actual Data')
                ax.plot(np.arange(len(data)), slope * np.arange(len(data)) + intercept, label='Linear Regression', linestyle='--')

                ax.set_title(f"Linear Regression - Parameter: {first_value}")
                mplcursors.cursor(hover=True)
                fig.legend()
                fig = plt.gcf()
                fig.canvas.manager.set_window_title(f'Linear Regression - {first_value}')
                ax.set_xlabel("Row Index")
                ax.set_ylabel("Value")

                self.canvas.figure = fig
                self.canvas.draw()
                plt.show()
            else:
                QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')

    def low_pass_filter(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]

        sns.set()
        fig, (ax1, ax2) = plt.subplots(2)
        dat = pd.read_csv(file_names[0], sep = '\t', header = 0)
        x = pd.DataFrame(dat)
        numpy_array1 = x.to_numpy()  # converting dataframe into numpy array
        # print(numpy_array1)
        x = numpy_array1[:, 0]
        
        y = data
        sampling_freq = self.sampling_rate_edit.text()
        cutoff_freq1 = self.cutoff_frequency_edit.text()
        
        if(y == 0 or cutoff_freq1 == "" or sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the Sampling frequency, Cutoff frequency ")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif(y and cutoff_freq1 and sampling_freq):
            cutoff_freq2 = float(cutoff_freq1)
            global sampling_freq1
            sampling_freq1 = float(sampling_freq)
            def butter_lowpass(cutoff_freq2, fs, order=5):
                nyq = 0.5 * fs
                normal_cutoff = cutoff_freq2 / nyq
                b, a = butter(order, normal_cutoff, btype='low',
                              analog=False) 
                return b, a

            def butter_lowpass_filter(data, cutoff_freq2, fs, order=5):
                b, a = butter_lowpass(cutoff_freq2, fs, order=order)
                y = lfilter(b, a, data)  
                return y
            
            Nyq = 0.5 * sampling_freq1  
            order = 2
            b, a = butter_lowpass(cutoff_freq2, sampling_freq1, order)

            w, h = freqz(b, a, worN=512)
            ax2.plot(0.5 * sampling_freq1 * w / np.pi, np.abs(h), 'b')
            ax2.plot(cutoff_freq2, 0.5 * np.sqrt(2), 'ko')
            ax2.axvline(cutoff_freq2, c='k', label='Cutoff frequency')
            ax2.set_xlabel("Frequency(Hz)")
            ax2.set_ylabel("Gain")
            ax2.set_title("Lowpass Butterworth Filter Frequency Response")

            new_sig = y
            y1 = butter_lowpass_filter(new_sig, cutoff_freq2, sampling_freq1, order)

            T = 5.0  # Sample Period
            T1 = len(y) / sampling_freq1  # sample timeperiod

            nyq = 0.5 * sampling_freq1  # Nyquist freq
            order = 2
            n = int(T1 * sampling_freq1)  # total no of samples
            time = np.linspace(0, T1, n, endpoint='False')
            normalized_cutoff_freq = 2 * cutoff_freq2 / sampling_freq1

            numer_coeff_low, denom_coeff_low = signal.butter(order, normalized_cutoff_freq, btype='lowpass', analog=False)
            filtered_sig_low = signal.lfilter(numer_coeff_low, denom_coeff_low, new_sig)

            ax1.plot(x, new_sig, 'b-', label='Data')
            ax1.plot(x, filtered_sig_low, 'r-', label='Filtered Data')
            fig.legend(loc='upper right')
            ax1.set_xlabel("Time(Sec)")
            ax1.set_ylabel("Magnitude")
            ax1.set_title("Result of Lowpass Butterworth Filter")
            mplcursors.cursor(hover=True)
            plt.tight_layout()
            fig = plt.gcf()
            fig.canvas.manager.set_window_title('Highpass Filter Plot')
            plt.show()

    def high_pass_filter(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]
        sns.set()
        fig, (ax1, ax2) = plt.subplots(2)
        dat = pd.read_csv(file_names[0], sep = '\t', header = 0)
        x = pd.DataFrame(dat)
        numpy_array1 = x.to_numpy()  
        x = numpy_array1[:, 0]

        y = data
        sampling_freq = self.sampling_rate_edit.text()
        global sampling_freq1
        sampling_freq1 = float(sampling_freq)

        def butter_highpass(cutoff_freq, fs, order=5):
            nyq = 0.5 * fs
            normal_cutoff = cutoff_freq / nyq
            b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
            return b, a

        def butter_highpass_filter(data, cutoff_freq, fs, order=5):
            b, a = butter_highpass(cutoff_freq, fs, order=order)
            y = signal.filtfilt(b, a, data) 
            return y

        order = 2
        cutoff_freq = self.cutoff_frequency_edit.text()
        cutoff_freq1 = float(cutoff_freq)
        b, a = butter_highpass(cutoff_freq1, sampling_freq1, order)

        w, h = freqz(b, a, worN=512)
        ax2.plot(0.5 * sampling_freq1 * w / np.pi, np.abs(h), 'b')
        ax2.plot(cutoff_freq1, 0.5 * np.sqrt(2), 'ko')
        ax2.axvline(cutoff_freq1, c='k', label='Cutoff Frequency')
        ax2.set_xlabel("Frequency(Hz)")
        ax2.set_ylabel("Gain")
        ax2.set_title("Highpass Butterworth Filter Frequency Response")

        noise = np.random.normal(np.mean(y), np.std(y), len(y))
        new_sig = y + noise
        y1 = butter_highpass_filter(new_sig, cutoff_freq1, sampling_freq1, order)

        T = 5.0  # Sample Period
        fs = 20  # sample rate Hz
        T1 = len(y) / sampling_freq1  # sample timeperiod

        nyq = 0.5 * fs  # Nyquist freq
        order = 2
        n = int(T1 * fs)  # total no of samples
        time = np.linspace(0, T1, n, endpoint='False')
        normalized_cutoff_freq = 2 * cutoff_freq1 / sampling_freq1

        numer_coeff_low, denom_coeff_low = signal.butter(order, normalized_cutoff_freq, btype='highpass', analog=False)
        filtered_sig_low = signal.lfilter(numer_coeff_low, denom_coeff_low, new_sig)

        ax1.plot(x, new_sig, 'b-', label='Data')
        ax1.plot(x, filtered_sig_low, 'r-', label='Filtered Data')
        fig.legend(loc='upper right')
        ax1.set_xlabel("Time(Sec)")
        ax1.set_ylabel("Magnitude")
        ax1.set_title("Result of Highpass Butterworth Filter")
        mplcursors.cursor(hover=True)
        plt.tight_layout()
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Highpass Filter Plot')
        plt.show()

    def inter_channel_averages(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]

            if data:
                inter_channel_avg_data = np.array(data).mean(axis=0)

                fig, ax = plt.subplots(figsize=(8, 5))
                plt.plot(inter_channel_avg_data, label=f'Inter-Channel Average of {first_value}')
                plt.title(f'Inter-Channel Average of {first_value}')
                plt.xlabel('Pixel')
                plt.ylabel('Average Value')
                fig.canvas.manager.set_window_title('Inter-Channel Averages')
                plt.legend()
                plt.grid(True)

                plt.show()
            else:
                QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')

    def inter_correlation (self):
            selected_column_1, selected_column_2 = self.select_parameters(parameter1_required=True, parameter2_required=True)
        # , sampling_frequency, cutoff_frequency


        # Validate that both columns are selected and different
            if selected_column_1 is not None and selected_column_2 is not None and selected_column_1 != selected_column_2:
                if self.filtered_data:
                    data_frames = self.filtered_data
                else:
                    data_frames = self.data_frames

                data_1 = []
                data_2 = []
                first_value_1 = None
                first_value_2 = None

                for df in data_frames:
                    item_1 = self.table_widget.item(0, selected_column_1)
                    item_2 = self.table_widget.item(0, selected_column_2)

                    if item_1 is not None:
                        first_value_1 = str(item_1.text())

                    if item_2 is not None:
                        first_value_2 = str(item_2.text())

                if first_value_1 is None or first_value_2 is None:
                    QMessageBox.warning(self, "Error", "No valid data in the selected columns.")
                    return

                for df in data_frames:
                    for row_index, (_, row_data) in enumerate(df.iterrows()):
                        item_1 = self.table_widget.item(row_index, selected_column_1)
                        item_2 = self.table_widget.item(row_index, selected_column_2)

                        try:
                            if item_1 is not None and item_2 is not None and \
                            item_1.text().replace('.', '', 1).isdigit() and item_2.text().replace('.', '', 1).isdigit():
                                data_1.append(float(item_1.text()))
                                data_2.append(float(item_2.text()))
                            else:
                                data_1.append(None)
                                data_2.append(None)
                        except ValueError:
                            data_1.append(None)
                            data_2.append(None)

                data_1 = [value for value in data_1 if value is not None]
                data_2 = [value for value in data_2 if value is not None]

                if data_1 and data_2:
                    # Perform cross-correlation plot
                    inter_correlation = np.correlate(data_1, data_2, mode='full')
                    lags = np.arange(-len(data_1) + 1, len(data_1))

                    fig, ax = plt.subplots()
                    ax.plot(lags, inter_correlation)
                    ax.set_title(f"Inter-Correlation - Parameters: {first_value_1} and {first_value_2}")
                    mplcursors.cursor(hover=True)
                    fig = plt.gcf()
                    fig.canvas.manager.set_window_title(f'Inter-Correlation - {first_value_1} and {first_value_2}')
                    ax.set_xlabel("Lag")
                    ax.set_ylabel("Inter-Correlation Value")

                    self.canvas.figure = fig
                    self.canvas.draw()
                    plt.show()
                else:
                    QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected columns.')
            else:
                QMessageBox.warning(self, 'Error', 'Please select two different columns for cross-correlation.')

    def  power_spectrum(self):
        selected_column = self.table_widget.currentColumn()

        if selected_column < 0:
            return        

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

            data = []
        first_value = None
        for df in data_frames:
            item = self.table_widget.item(0, selected_column)
            if item is not None:
                first_value = str(item.text())
                break

        if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

        data = self.extract_data_from_column(selected_column)

        if not data:
            QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')
            return
        sns.set()
        y = data
        sampling_freq = self.sampling_rate_edit.text()

        if (y == 0 or sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif (y ==0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif(sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif (y and sampling_freq):
            fig, ax = plt.subplots()
            yf = np.fft.fft(y)
            sampling_freq1 = float(sampling_freq)
            yf1 = np.fft.rfft(y)

            ps1 = 20 * np.log10(np.abs(yf1[1:]))
            
            str1 = first_value
            freq = np.linspace(0, sampling_freq1 / 2, len(ps1))
            res1 = "Maximum Power of " + str1 +" is " + str(float(max(list(ps1)))) + " dB"

            anchored_txt1 = AnchoredText(res1, loc='lower left', prop=dict(size=10), frameon=True,
                                         bbox_to_anchor=(0., 1.), bbox_transform=ax.transAxes)
            anchored_txt1.patch.set_boxstyle("round, pad = 0., rounding_size = 0.2")
            ax.add_artist(anchored_txt1)

            magnitude = np.abs(ps1)
            pks, _ = find_peaks(magnitude[:30000], height=400)
            plt.plot(freq, ps1)
            max_freq = list(freq)
            print("Max freq is ", max(max_freq))
            print(freq.mean())

            plt.title(" Powerspectrum result of " + str1, loc = 'right')
            plt.xlabel("Frequency (Hz)")
            plt.ylabel("Power (dB)")
            mplcursors.cursor(hover=True)
            fig = plt.gcf()
            fig.canvas.manager.set_window_title('Power Spectrum Plot')
            plt.show() 

    def smoothing(self):
        selected_column = self.table_widget.currentColumn()
        if selected_column >= 0:
            if self.filtered_data:
                data_frames = self.filtered_data
            else:
                data_frames = self.data_frames

            data = []
            first_value = None
            for df in data_frames:
                item = self.table_widget.item(0, selected_column)
                if item is not None:
                    first_value = str(item.text())
                    break

            if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

            for df in data_frames:
                for row_index, (_, row_data) in enumerate(df.iterrows()):
                    item = self.table_widget.item(row_index, selected_column)

                    try:
                        if item is not None and item.text().replace('.', '', 1).isdigit():
                            data.append(float(item.text()))
                        else:
                            data.append(None)
                    except ValueError:
                        data.append(None)

            data = [value for value in data if value is not None]

        sns.set()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        dat = pd.read_csv(file_names[0], sep = '\t', header = 0)
        x = pd.DataFrame(dat)
        numpy_array1 = x.to_numpy()  # converting dataframe into numpy array
        # print(numpy_array1)
        x = numpy_array1[:, 0]
        
        y = data
        new_sig = y

        str1 = first_value
        ax1.plot(x, y, label = str1)
        ax1.set_title("Origianl Signal")
        ax1.set_ylabel("Amplitude")
        ax1.set_xlabel("Time")
        yhat = signal.savgol_filter(new_sig, 21, 2)

        ax2.set_title("Result of Smoothing")
        ax2.plot(x, yhat, c='r', label= str1 + ' after Smoothing')
        fig.legend(loc='upper right')
        mplcursors.cursor(hover=True)
        ax2.set_ylabel("Amplitude")
        ax2.set_xlabel("Time")
        plt.title("Result of the Smoothed signal")

        new_sig_fft = fftpack.fft(new_sig)
        angle = np.angle(new_sig_fft) * 180 / np.pi
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Smoothing Plot')
        plt.show()


    def coherence(self):
            selected_column_1, selected_column_2 = self.select_parameters(parameter1_required=True, parameter2_required=True)
        # , sampling_frequency, cutoff_frequency
        # Validate that both columns are selected and different
            if selected_column_1 is not None and selected_column_2 is not None and selected_column_1 != selected_column_2:
                if self.filtered_data:
                    data_frames = self.filtered_data
                else:
                    data_frames = self.data_frames

                data_1 = []
                data_2 = []
                first_value_1 = None
                first_value_2 = None

                for df in data_frames:
                    item_1 = self.table_widget.item(0, selected_column_1)
                    item_2 = self.table_widget.item(0, selected_column_2)

                    if item_1 is not None:
                        first_value_1 = str(item_1.text())

                    if item_2 is not None:
                        first_value_2 = str(item_2.text())

                if first_value_1 is None or first_value_2 is None:
                    QMessageBox.warning(self, "Error", "No valid data in the selected columns.")
                    return

                for df in data_frames:
                    for row_index, (_, row_data) in enumerate(df.iterrows()):
                        item_1 = self.table_widget.item(row_index, selected_column_1)
                        item_2 = self.table_widget.item(row_index, selected_column_2)

                        try:
                            if item_1 is not None and item_2 is not None and \
                            item_1.text().replace('.', '', 1).isdigit() and item_2.text().replace('.', '', 1).isdigit():
                                data_1.append(float(item_1.text()))
                                data_2.append(float(item_2.text()))
                            else:
                                data_1.append(None)
                                data_2.append(None)
                        except ValueError:
                            data_1.append(None)
                            data_2.append(None)

                data_1 = [value for value in data_1 if value is not None]
                data_2 = [value for value in data_2 if value is not None]

            if data_1 and data_2:

                sns.set()
                dat = pd.read_csv(file_names[0], sep = '\t', header = 0)
                x = pd.DataFrame(dat)
                numpy_array1 = x.to_numpy()  # converting dataframe into numpy array
                # print(numpy_array1)
                x = numpy_array1[:, 0]
                # y1 = self.parameter1_list.currentIndex()
                y = data_1
                #  = self.parameter2_list.currentIndex()
                z = data_2
                sampling_freq = self.sampling_rate_edit.text()


                if (y == 0 or z == 0 or sampling_freq == ""):
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Error in selection of input")
                    msg.setWindowTitle("Warning")
                    msg.setDetailedText("Please select the Parameter 1, Parameter 2 and enter the sampling frequency")
                    res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    msg.exec_()
                    return

                fig, (ax1, ax2) = plt.subplots(2, 1)
                str1 = first_value_1
                str2 = first_value_2
                ax1.set_title("Time Series Plot representation of " + str1 + " and " + str2)
                ax1.plot(x, y, 'b', label=str1)
                ax1.plot(x, z, 'r', label=str2)
                # fig.legend()
                ax1.set_xlabel("Time(Sec)")
                ax1.set_ylabel("Amplitude(V)")
            
                coh= plt.cohere(y, z)
                cohArry=coh[0]
                freqArray=coh[1]
                indFreq=list(cohArry).index(max(list(cohArry)))
                FreqCorepndsToValue=list(freqArray)[indFreq]

                fig.legend()

                string_res1 = "=>If:" + "\n" + "   Coherence = 1.0 then two signals are Coherent" + "\n" + "   Coherence < 1.0 then two signals are Coherent with some Added Noise" + "\n" + "   Coherence = 0 then two signals are not Coherent"
                string_res = "=>Max coherence value is: " + str(float(max(list(cohArry)))) + " at Frequency of " + str(float(FreqCorepndsToValue)) + " Hz" + "\n" "=>Two Signals are Coherent if both are equal in Phase and Frequency" + "\n" + string_res1
                anchored_txt1 = AnchoredText(string_res, loc='lower left', prop=dict(size=11), frameon=True,bbox_to_anchor=(0., 1.), bbox_transform=ax1.transAxes)
                anchored_txt1.patch.set_boxstyle("round, pad = 0., rounding_size = 0.2")
                ax1.add_artist(anchored_txt1)

                plt.title("Coherence Spectrum between " + str1 + " and " + str2)


                plt.ylabel("Coherence")
                plt.xlabel("Frequency (Hz)")
                mplcursors.cursor(hover=True)
                plt.tight_layout()
                fig = plt.gcf()
                fig.canvas.manager.set_window_title('Coherence Plot')
                plt.show()


    def magnitude_spectrum(self):
        selected_column = self.table_widget.currentColumn()

        if selected_column < 0:
            return        

        if self.filtered_data:
            data_frames = self.filtered_data
        else:
            data_frames = self.data_frames

            data = []
        first_value = None
        for df in data_frames:
            item = self.table_widget.item(0, selected_column)
            if item is not None:
                first_value = str(item.text())
                break

        if first_value is None:
                QMessageBox.warning(self, "Error", "No valid data in the selected column.")
                return

        data = self.extract_data_from_column(selected_column)

        if not data:
            QMessageBox.warning(self, 'Error', 'No valid numeric data in the selected column.')
            return
        sns.set()
        y = data
        sampling_freq = self.sampling_rate_edit.text()
        fig, ax = plt.subplots()
       
        if (y == 0 or sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif (y ==0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif(sampling_freq == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Error in selection of input")
            msg.setWindowTitle("Warning")
            msg.setDetailedText("Please select the Parameter 1 and enter the sampling frequency")
            res = msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.exec_()

        elif( y and sampling_freq):

            str1 = self.parameter1_list.currentText()
            sampling_freq1 = float(sampling_freq)
            plt.magnitude_spectrum(y, Fs=sampling_freq1)
            plt.xlabel("Frequency (Hz)")
            plt.title("Magnitude Spectrum of " + str1)   
            mplcursors.cursor(hover=True)
            fig = plt.gcf()
            fig.canvas.manager.set_window_title('Magnitude Spectrum Plot')
            plt.show()     



def main():
    app = QApplication(sys.argv)
    viewer = DataViewer()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()