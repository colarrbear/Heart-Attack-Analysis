"""handles the GUI"""

import tkinter as tk
from tkinter import ttk


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Explorer")
        self.init_components()

    def init_components(self):
        self.summary_button = ttk.Button(self, text="Show Summary Statistics",
                                         command=self.show_summary)
        self.summary_button.pack(pady=10)

        self.correlation_button = ttk.Button(self, text="Show Correlations",
                                             command=self.show_correlations)
        self.correlation_button.pack(pady=10)

        self.filter_label = ttk.Label(self, text="Filter by Age:")
        self.filter_label.pack()
        self.filter_entry = ttk.Entry(self)
        self.filter_entry.pack()
        self.filter_button = ttk.Button(self, text="Apply Filter",
                                        command=self.apply_filter)
        self.filter_button.pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def show_summary(self):
        summary = self.controller.get_summary()
        self.result_label.config(text=summary)

    def show_correlations(self):
        correlations = self.controller.get_correlations()
        self.result_label.config(text=correlations)

    def apply_filter(self):
        age_filter = self.filter_entry.get()
        filtered_data = self.controller.filter_data({'age': int(age_filter)})
        self.result_label.config(text=filtered_data)

    def run(self):
        self.mainloop()
