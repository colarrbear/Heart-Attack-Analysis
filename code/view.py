"""handles the User interface of the application"""
#TODO:
# - nominal data (e.g. gender) must not compute in descriptive stat
# - (done) bar chart still received only one attribute. Not yet implemented for two attributes.
# - (done) correlation still not yet implemented for one attribute.
# - For "Graph" (superior graph) tab and Home tab is work in progress.

import tkinter as tk
from tkinter import ttk, messagebox
from model import *


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.data_loader = controller.data
        self.plotter = PlotGraphs(self.data_loader)
        self.title("Heart Disease Explorer")
        self.init_components()
        # self.init_home_page()
        self.create_quit_button()
        self.configure_window()

    def configure_window(self):
        """Configure the window settings."""
        self.resizable(True, True)

    def init_components(self):
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
        self.init_home_tab()

        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab,
                              text="Data Information")
        self.init_data_information_tab()

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")
        self.init_statistics_tab()

        # Graph Tab
        self.graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.graph_tab, text="Graph")
        self.init_advance_graph_tab()

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
            event: self.di_handle_attribute_selection(
            self.attribute_combobox.get()))

    def di_handle_attribute_selection(self, selected_attribute):
        """
        Handle the selection of an attribute in
        the combobox of the Data Information tab.
        """
        data_info = self.controller.summary_statistics()[selected_attribute]
        self.di_update_data_information_tab(data_info)

    def di_update_data_information_tab(self, data_info):
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

    def init_statistics_tab(self):
        """Initialize the Statistics tab."""
        # Create a frame for visual separation
        separator_frame = tk.Frame(self.statistics_tab, height=10)
        separator_frame.pack(side="bottom", pady=10)

        # Create another frame for the graph canvas
        self.graph_canvas_frame = tk.Frame(self.statistics_tab, width=800,
                                           height=400)
        self.graph_canvas_frame.pack(side="bottom", fill="both", expand=True)


        # Create the menu box
        menu_label = ttk.Label(self.statistics_tab, text="Select Visualization:")
        menu_label.pack(side="top", fill="x", padx=5, pady=5)

        menu_var = tk.StringVar()
        menu_var.set("Select Visualization")
        menu_combobox = ttk.Combobox(self.statistics_tab, textvariable=menu_var,
                                     values=["Bar Charts", "Histogram",
                                             "Correlations"])
        menu_combobox.pack(side="top", fill="x", padx=5, pady=5)
        menu_combobox.bind("<<ComboboxSelected>>", self.handle_menu_selection)

        # Create the label for the first attribute combobox
        left_label = ttk.Label(self.statistics_tab,
                               text="Select 1st attribute:")
        left_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        # Create the attribute comboboxes
        self.left_attribute_combobox = ttk.Combobox(self.statistics_tab,
                                                    state="disabled")
        self.left_attribute_combobox.pack(side="left", fill="x", padx=5,
                                          pady=5, expand=True)

        # Create the label for the second attribute combobox
        right_label = ttk.Label(self.statistics_tab,
                                text="Select 2nd attribute:")
        right_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        self.right_attribute_combobox = ttk.Combobox(self.statistics_tab,
                                                     state="disabled")
        self.right_attribute_combobox.pack(side="left", fill="x", padx=5,
                                           pady=5, expand=True)

        # Create the button to create the graph
        create_graph_button = ttk.Button(self.statistics_tab, text="Plot Graph",
                                            command=self.create_graph)
        create_graph_button.pack(side="right", padx=5, pady=5)

    def create_graph(self):
        """Create a graph based on the selected visualization."""
        selected = self.selected_visualization
        left = self.left_attribute_combobox.get()
        right = None

        # If the selected visualization is "Correlations", fetch the right attribute
        if selected == "Correlations" or selected == "Bar Charts":
            right = self.right_attribute_combobox.get()

        # Clear the existing graph canvas
        for widget in self.graph_canvas_frame.winfo_children():
            widget.destroy()

        # Plot the graph based on the selected visualization
        if selected == "Bar Charts":
            self.plotter.plot_bar_chart(left, right, self.graph_canvas_frame)
        elif selected == "Histogram":
            self.plotter.plot_histogram(left, self.graph_canvas_frame)
        elif selected == "Correlations":
            self.disable_comboboxes()
            self.plotter.plot_correlation(self.graph_canvas_frame)

    def enable_comboboxes(self):
        """Enable the comboboxes in the Statistics tab."""
        self.left_attribute_combobox["state"] = "normal"
        self.right_attribute_combobox["state"] = "normal"

    def disable_right_combobox(self):
        """Disable the right combobox in the Statistics tab."""
        self.right_attribute_combobox.set("")
        self.right_attribute_combobox["state"] = "disabled"

    def disable_comboboxes(self):
        """Disable all the comboboxes in the Statistics tab."""
        self.left_attribute_combobox.set("")
        self.right_attribute_combobox.set("")
        self.left_attribute_combobox["state"] = "disabled"
        self.right_attribute_combobox["state"] = "disabled"

    def handle_menu_selection(self, event):
        """Handle the selection of a visualization in the Statistics tab."""
        selected = event.widget.get()
        self.selected_visualization = selected

        if selected == "Histogram":
            self.enable_comboboxes()
            self.disable_right_combobox()

            column = self.data_loader.get_column_names
            self.left_attribute_combobox["values"] = column
            self.left_attribute_combobox.set(column[0])

        elif selected == "Bar Charts":
            self.enable_comboboxes()

            allowed_attributes = ["sex", "output", "fbs", "slp"]
            self.left_attribute_combobox["values"] = allowed_attributes
            self.left_attribute_combobox.set(allowed_attributes[0])
            self.left_attribute_combobox.bind("<<ComboboxSelected>>",
                                              self.validate_comboboxes)
            self.right_attribute_combobox["values"] = allowed_attributes
            self.right_attribute_combobox.bind("<<ComboboxSelected>>",
                                               self.validate_comboboxes)

        elif selected == "Correlations":
            pass

    def validate_comboboxes(self, event):
        """Validate the selected attributes in the comboboxes."""
        selected_left = self.left_attribute_combobox.get()
        selected_right = self.right_attribute_combobox.get()

        # Check if both comboboxes have selections
        if selected_left and selected_right:
            if selected_left == selected_right:
                messagebox.showerror("Error", "Select different attributes.")
                self.right_attribute_combobox.set("")
        elif not selected_left:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
        elif not selected_right:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")

    def create_quit_button(self):
        """ Button to gracefully exit"""
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def init_home_tab(self):
        """This function can be expanded for additional content on the home page"""
        label = ttk.Label(self.home_tab, text="WIP: Home Page, see other tabs for content.")
        label.pack()

    def init_advance_graph_tab(self):
        """This function can be expanded for additional content on the home page"""
        label = ttk.Label(self.graph_tab, text="WIP: Graph Page, see other tabs for content.")
        label.pack()

    def run(self):
        self.mainloop()