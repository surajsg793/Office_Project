import csv
import tkinter as tk
from tkinter import filedialog

class TxtToCsvConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Txt to CSV Converter")

        self.file_path_label = tk.Label(master, text='Selected File: No file selected')
        self.file_path_label.pack(pady=10)

        self.import_button = tk.Button(master, text='Import Text File', command=self.import_file)
        self.import_button.pack(pady=5)

        self.convert_button = tk.Button(master, text='Convert to CSV', command=self.convert_to_csv)
        self.convert_button.pack(pady=5)

    def import_file(self):
        file_path = filedialog.askopenfilename(title="Import Text File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            self.file_path_label.config(text=f'Selected File: {file_path}')
            self.input_file_path = file_path

    def convert_to_csv(self):
        if hasattr(self, 'input_file_path'):
            output_file_path = filedialog.asksaveasfilename(title="Save CSV File", defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])

            if output_file_path:
                with open(self.input_file_path, 'r') as txt_file:
                    lines = txt_file.readlines()

                with open(output_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    for line in lines:
                        # Assuming the text file has tab-delimited values
                        values = line.strip().split('\t')
                        csv_writer.writerow(values)

                self.file_path_label.config(text=f'Conversion completed. CSV file saved at: {output_file_path}')

if __name__ == '__main__':
    root = tk.Tk()
    converter = TxtToCsvConverter(root)
    root.mainloop()
