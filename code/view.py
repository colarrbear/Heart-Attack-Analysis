"""handles the GUI"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from model import *


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Explorer")
        self.theme = ttk.Style()
        # .theme_use("aqua")
        self.init_components()
        self.init_home_page()

    def init_components(self):
        # # theme
        # self.theme = ttk.Style(self)
        # self.theme.theme_use("aqua")
        # menu = [colour for colour in self.theme.theme_names()]
        #
        # # Menu Bar for selecting theme
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        #
        #
        # # self.theme_names = self.theme.theme_names()
        # # self.menu_bar.add_cascade(label="Themes", menu=self.menu_bar)
        #
        # for colors in self.theme_names:
        #     self.menu_bar.add_command(label=colors + " Mode",
        #                            command=lambda t=colors: self.change_theme(t))
        # # self.menu_bar.add_command(label="Exit", command=self.quit)
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        # Add theme options to the submenu
        themes = [colour for colour in self.theme.theme_names()]
        for theme in themes:
            self.theme_menu.add_command(label=theme.capitalize() + " Mode",
                                        command=lambda
                                            t=theme: self.change_theme(t))

        # Feature Tabs
        self.feature_tabs = ttk.Notebook(self)
        self.feature_tabs.pack(expand=True, fill=tk.BOTH)

        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab,
                              text="Data Information")

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")

        # Graph Tab
        self.graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.graph_tab, text="Graph")

    def init_home_page(self):
        # This function can be expanded for additional content on the home page
        pass

    def change_theme(self, theme="aqua"):
        """Function to change the theme"""
        self.theme.theme_use(theme)


    #     # Left Panel: Data Information
    #     self.left_frame = ttk.Frame(self, width=200, height=400)
    #     self.left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
    #
    #     self.data_information_label = ttk.Label(self.left_frame,
    #                                             text="Data Information")
    #     self.data_information_label.pack(pady=10)
    #
    #     # self.data_information_image = tk.PhotoImage(
    #     #     file="data_information.png")
    #     # self.data_information_button = ttk.Button(self.left_frame,
    #     #                                           image=self.data_information_image,
    #     #                                           command=self.show_data_information)
    #     # self.data_information_button = ttk.Button(self.left_frame,
    #     #                                           command=self.show_data_information)
    #     self.data_information_cbb = ttk.Combobox(self.left_frame, values=["Summary Statistics", "Correlations"])
    #     self.data_information_cbb.pack(pady=10)
    #     # self.data_information_button.pack(pady=10)
    #
    #     # Middle Panel: Visualization
    #     self.middle_frame = ttk.Frame(self, width=400, height=400)
    #     # self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
    #     self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)
    #
    #     # self.visualization_image = tk.PhotoImage(
    #     #     file="data_information.png")
    #     self.visualization_label = ttk.Label(self.middle_frame,
    #                                          text="Visualization")
    #     self.visualization_label.pack(pady=10)
    #
    #     self.distribution_graph_button = ttk.Button(self.middle_frame,
    #                                                 text="Distribution Graph",
    #                                                 command=self.show_distribution_graph)
    #     self.distribution_graph_button.pack(pady=5, padx=10, fill=tk.X)
    #
    #     self.interactive_graph_button = ttk.Button(self.middle_frame,
    #                                                text="Interactive Graph",
    #                                                command=self.show_interactive_graph)
    #     self.interactive_graph_button.pack(pady=5, padx=10, fill=tk.X)
    #
    #     self.filtering_options_button = ttk.Button(self.middle_frame,
    #                                                text="Filtering Options",
    #                                                command=self.show_filtering_options)
    #     self.filtering_options_button.pack(pady=5, padx=10, fill=tk.X)
    #
    #     # Right Panel: Select
    #     self.right_frame = ttk.Frame(self, width=200, height=400)
    #     self.right_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
    #
    #
    #     self.select_label = ttk.Button(self.right_frame, text="More options")
    #     self.select_label.pack(pady=10, padx=10, fill=tk.X)
    #
    #     # self.select_label = ttk.Label(self.right_frame, text="Select")
    #     # self.select_label.pack()
    #     #
    #     # # self.select_image = tk.PhotoImage(file="select.png")
    #     # # self.select_button = ttk.Button(self.right_frame,
    #     # #                                 image=self.select_image,
    #     # #                                 command=self.show_select)
    #     # self.select_button = ttk.Button(self.right_frame,
    #     #                                 command=self.show_select)
    #     # self.select_button.pack(pady=10)
    #     # self.select_options = ttk.Combobox(self.right_frame, values=["Option 1", "Option 2", "Option 3"])
    #     # self.select_options.pack(pady=10)
    #     # self.select_cbb = ttk.Combobox(self.right_frame, command=self.show_select)
    #     # self.select_cbb.pack(pady=10)
    #
    # def show_data_information(self):
    #     """Function to handle Data Information click
    #     Show the options for Summary Statistics and Correlations"""
    #     pass
    #
    # def show_distribution_graph(self):
    #     """Function to display the default distribution graph
    #     (using Matplotlib)"""
    #     pass
    #
    # def show_interactive_graph(self):
    #     """ Function to allow users to select different interactive graphs
    #     Implement based on user's choice (e.g., scatter plots, boxplots)"""
    #     pass
    #
    # def show_filtering_options(self):
    #     """Function to allow users to apply filters to the data
    #     Implement based on user's selection criteria"""
    #     pass
    #
    # def show_select(self):
    #     """Function to handle Select click
    #     perform specific actions when Select is clicked"""
    #     pass

    def run(self):
        self.mainloop()