import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox
from pandastable import Table
import typing
class CSVLoader:
    def __init__(self,root):
        self.root = root
        self.root.title(CSVLoader)

        self.load_button = tk.Button(root, text="Load File", command=self.load_file)
        self.load_button.pack(pady=30)
        self.data_frame_table = None
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path, dtype = "object" )

                self.display_data_frame(df)
            except pd.error.EmptyDataError:
                messagebox.showerror("Error", "The Selected CSV file is empty")
            except Exception as e:
                messagebox.showerror("Error", f"An Error Occured: {str(e)}")
    def display_data_frame(self,df):
        if self.data_frame_table:
            self.data_frame_table.destroy()
        self.data_frame_table = Table(self.root, dataframe = df)
        self.data_frame_table.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVLoader(root)
    root.mainloop()
