# """handles the GUI"""
#
# import tkinter as tk
# from tkinter import ttk
#
#
# class HeartDiseaseView(tk.Tk):
#     def __init__(self, controller):
#         super().__init__()
#         self.controller = controller
#         self.title("Heart Disease Explorer")
#         self.init_components()
#
#     def init_components(self):
#         # Combobox for data choices
#         self.data_choice_label = ttk.Label(self, text="Select Data:")
#         self.data_choice_label.pack()
#         self.data_choice = ttk.Combobox(self, values=["Summary Statistics", "Correlations"])
#         self.data_choice.pack(pady=10)
#
#         # Button to show selected data
#         # self.show_data_button = ttk.Button(self, text="Show Data", command=self.show_data)
#         # self.show_data_button.pack(pady=10)
#
#         # Text widget to display results
#         self.result_text = tk.Text(self, height=20, width=80)
#         self.result_text.pack(pady=10)
#
#         # self.summary_button = ttk.Button(self, text="Show Summary Statistics",
#         #                                  command=self.show_summary)
#         # self.summary_button.pack(pady=10)
#         #
#         # self.correlation_button = ttk.Button(self, text="Show Correlations",
#         #                                      command=self.show_correlations)
#         # self.correlation_button.pack(pady=10)
#
#         self.filter_label = ttk.Label(self, text="Filter by Age:")
#         self.filter_label.pack()
#         self.filter_entry = ttk.Entry(self)
#         self.filter_entry.pack()
#         self.filter_button = ttk.Button(self, text="Apply Filter",
#                                         command=self.apply_filter)
#         self.filter_button.pack(pady=10)
#
#         self.result_label = ttk.Label(self, text="")
#         self.result_label.pack(pady=10)
#
#     # def show_data(self):
#     #     selected_data = self.data_choice.get()
#     #     if selected_data == "Summary Statistics":
#     #         summary = self.controller.get_summary_statistics()
#     #         self.result_text.delete(1.0, tk.END)
#     #         self.result_text.insert(tk.END, summary)
#     #     elif selected_data == "Correlations":
#     #         correlations = self.controller.get_correlations()
#     #         self.result_text.delete(1.0, tk.END)
#     #         self.result_text.insert(tk.END, correlations)
#
#     def show_summary(self):
#         summary = self.controller.get_summary()
#         self.result_label.config(text=summary)
#
#     def get_summary(self):
#         return self.model.summary_statistics()
#
#     def show_correlations(self):
#         correlations = self.controller.get_correlations()
#         self.result_label.config(text=correlations)
#
#     def apply_filter(self):
#         age_filter = self.filter_entry.get()
#         filtered_data = self.controller.filter_data({'age': int(age_filter)})
#         self.result_label.config(text=filtered_data)
#
#     def run(self):
#         self.mainloop()

import tkinter as tk
from tkinter import ttk


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Explorer")
        self.init_components()

    def init_components(self):
        # Left Panel: Data Information
        self.left_frame = ttk.Frame(self, width=200, height=400)
        self.left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

        self.data_information_label = ttk.Label(self.left_frame,
                                                text="Data Information")
        self.data_information_label.pack(pady=10)

        # self.data_information_image = tk.PhotoImage(
        #     file="data_information.png")
        # self.data_information_button = ttk.Button(self.left_frame,
        #                                           image=self.data_information_image,
        #                                           command=self.show_data_information)
        # self.data_information_button = ttk.Button(self.left_frame,
        #                                           command=self.show_data_information)
        self.data_information_cbb = ttk.Combobox(self.left_frame, values=["Summary Statistics", "Correlations"])
        self.data_information_cbb.pack(pady=10)
        # self.data_information_button.pack(pady=10)

        # Middle Panel: Visualization
        self.middle_frame = ttk.Frame(self, width=400, height=400)
        # self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
        self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        # self.visualization_image = tk.PhotoImage(
        #     file="data_information.png")
        self.visualization_label = ttk.Label(self.middle_frame,
                                             text="Visualization")
        self.visualization_label.pack(pady=10)

        self.distribution_graph_button = ttk.Button(self.middle_frame,
                                                    text="Distribution Graph",
                                                    command=self.show_distribution_graph)
        self.distribution_graph_button.pack(pady=5, padx=10, fill=tk.X)

        self.interactive_graph_button = ttk.Button(self.middle_frame,
                                                   text="Interactive Graph",
                                                   command=self.show_interactive_graph)
        self.interactive_graph_button.pack(pady=5, padx=10, fill=tk.X)

        self.filtering_options_button = ttk.Button(self.middle_frame,
                                                   text="Filtering Options",
                                                   command=self.show_filtering_options)
        self.filtering_options_button.pack(pady=5, padx=10, fill=tk.X)

        # Right Panel: Select
        self.right_frame = ttk.Frame(self, width=200, height=400)
        self.right_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)


        self.select_label = ttk.Button(self.right_frame, text="More options")
        self.select_label.pack(pady=10, padx=10, fill=tk.X)

        # self.select_label = ttk.Label(self.right_frame, text="Select")
        # self.select_label.pack()
        #
        # # self.select_image = tk.PhotoImage(file="select.png")
        # # self.select_button = ttk.Button(self.right_frame,
        # #                                 image=self.select_image,
        # #                                 command=self.show_select)
        # self.select_button = ttk.Button(self.right_frame,
        #                                 command=self.show_select)
        # self.select_button.pack(pady=10)
        # self.select_options = ttk.Combobox(self.right_frame, values=["Option 1", "Option 2", "Option 3"])
        # self.select_options.pack(pady=10)
        # self.select_cbb = ttk.Combobox(self.right_frame, command=self.show_select)
        # self.select_cbb.pack(pady=10)

    def show_data_information(self):
        """Function to handle Data Information click
        Show the options for Summary Statistics and Correlations"""
        pass

    def show_distribution_graph(self):
        """Function to display the default distribution graph
        (using Matplotlib)"""
        pass

    def show_interactive_graph(self):
        """ Function to allow users to select different interactive graphs
        Implement based on user's choice (e.g., scatter plots, boxplots)"""
        pass

    def show_filtering_options(self):
        """Function to allow users to apply filters to the data
        Implement based on user's selection criteria"""
        pass

    def show_select(self):
        """Function to handle Select click
        perform specific actions when Select is clicked"""
        pass

    def run(self):
        self.mainloop()
