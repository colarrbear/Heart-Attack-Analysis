"""holds the data and calculations"""

import pandas as pd
import tkinter as tk


class HeartDiseaseModel:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        """for loading the data from a CSV file"""
        self.data = pd.read_csv('heart.csv')

    # def summary_statistics(self):
    #     return self.data.describe()
    #
    # def correlations(self):
    #     return self.data.corr()

    def summary_statistics(self):
        """returns summary statistics for the data"""
        summary_stats = self.data.describe()
        return summary_stats.to_string()

    def calculate_correlations(self):
        """returns correlation values for the data"""
        correlations = self.data.corr()
        return correlations.to_string()

    def filter_data(self, filters):
        """filters the data based on the given criteria"""
        filtered_data = self.data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data


class Toast(tk.Toplevel):
    def __init__(self, parent, message, duration=2000):
        tk.Toplevel.__init__(self, parent)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.withdraw()
        self.parent = parent
        self.message = message
        self.duration = duration
        self.label = tk.Label(self, text=self.message, bg="black", fg="white", padx=10, pady=5)
        self.label.pack()
        self.update_idletasks()
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (self.width // 2)
        self.y = self.parent.winfo_y() + self.parent.winfo_height() - self.height - 20
        self.geometry("+{}+{}".format(self.x, self.y))
        self.after(self.duration, self.destroy)
        self.deiconify()