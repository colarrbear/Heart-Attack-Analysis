"""handles the User interface of the application"""

import tkinter as tk
from tkinter import ttk
from model import *


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.data_loader = controller.data
        self.title("Heart Disease Explorer")
        self.init_components()
        # self.init_home_page()
        self.configure_window()
        self.create_quit_button()

    def configure_window(self):
        """Configure the window settings."""
        self.resizable(True, True)

    def init_components(self):
        # Create the left panel frames
        self.left_panel1 = ttk.Frame(self, width=150,
                                     height=600)  # relief="solid",

        attributes_label = ttk.Label(self.left_panel1,
                                     text="Select Attribute:")
        attributes_label.pack(side="top", fill="x", padx=5, pady=5)

        # Add a combobox to select attributes
        self.attribute_combobox = ttk.Combobox(self.left_panel1,
                                               values=["Attribute 1",
                                                       "Attribute 2",
                                                       "Attribute 3"])
        self.attribute_combobox.pack(side="top", fill="x", padx=5, pady=5)
        self.attribute_combobox.set("Attribute 1")  # Set default value
        self.attribute_combobox.bind("<<ComboboxSelected>>", lambda
            event: self.handle_attribute_selection(
            self.attribute_combobox.get()))

        # Feature Tabs
        self.feature_tabs = ttk.Notebook(self)
        self.feature_tabs.configure(padding=10)
        self.feature_tabs.pack(fill=tk.BOTH, expand=True)
        self.tabs()

    def tabs(self):
        """Create tabs for the application."""
        # Home Tab
        self.home_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.home_tab, text="Home")

        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab,
                              text="Data Information")
        self.init_data_information_tab()

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")

        # Graph Tab
        self.graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.graph_tab, text="Graph")

    def init_data_information_tab(self):
        """Initialize the Data Information tab."""
        # Add a label for the combobox in Data Information tab
        attributes_label = ttk.Label(self.data_information_tab,
                                     text="Select Attribute:")
        attributes_label.pack(side="top", fill="x", padx=5, pady=5)

        column = self.data_loader.get_column_names

        # Add a combobox to select attributes in Data Information tab
        self.attribute_combobox = ttk.Combobox(self.data_information_tab,
                                               values=[i for i in column])
        self.attribute_combobox.pack(side="top", fill="x", padx=5, pady=5)
        self.attribute_combobox.set(column[0])  # Set default value
        self.attribute_combobox.bind("<<ComboboxSelected>>", lambda
            event: self.handle_attribute_selection(
            self.attribute_combobox.get()))

    def handle_attribute_selection(self, selected_attribute):
        """
        Handle the selection of an attribute in
        the combobox of the Data Information tab.
        """
        data_info = self.controller.summary_statistics()[selected_attribute]
        self.update_data_information_tab(data_info)

    def update_data_information_tab(self, data_info):
        """Update the Data Information tab with the given data information."""
        for stat, value in data_info.items():
            # Check if a label for this statistic already exists
            existing_label = None
            for child in self.data_information_tab.winfo_children():
                if isinstance(child, ttk.Label) and child.cget(
                        "text").startswith(stat + ":"):
                    existing_label = child
                    break

            # If an existing label exists, update its text
            if existing_label:
                existing_label.config(text=f"{stat}: {value}")
            # Otherwise, create a new label
            else:
                stat_label = ttk.Label(self.data_information_tab,
                                       text=f"{stat}: {value}")
                stat_label.pack(side="top", fill="x", padx=5, pady=2)

    # def tabs_left_panel1(self):
    #     """Create tabs for the application."""
    #     # Add widgets to the first left panel
    #     label_left_panel = tk.Label(self.left_panel, text="Left Panel",
    #                                 bg="white", padx=10, pady=5)
    #     label_left_panel.pack()

    def create_quit_button(self):
        # Button to gracefully exit
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def init_home_page(self):
        # This function can be expanded for additional content on the home page
        pass

    def run(self):
        self.mainloop()
