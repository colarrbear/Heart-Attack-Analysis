# """handles the GUI"""
# # from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
# # from ttkthemes import ThemedTk
#
# # window = ThemedTk(theme="blue")
# # ttk.Button(window, text="Quit", command=window.destroy).pack()
# # window.mainloop()
# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedTk
# from model import *
#
#
# class HeartDiseaseView(tk.Tk):
#     def __init__(self, controller):
#         super().__init__()
#         self.controller = controller
#         self.title("Heart Disease Explorer")
#         self.init_components()
#         self.init_home_page()
#
#     def init_components(self):
#         # self.configure(bg=self.bg)
#
#         # Menu Bar for selecting theme
#         self.menu_bar = tk.Menu(self)
#         self.config(menu=self.menu_bar)
#
#         self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
#         self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
#
#         pixmap_themes = [
#             "arc",
#             "blue",
#             "clearlooks",
#             "elegance",
#             "kroc",
#             "plastik",
#             "radiance",
#             "winxpblue"
#             ]
#
#         for theme in pixmap_themes:
#             self.theme_menu.add_command(label=theme.capitalize() + " Mode",
#                                         command=lambda
#                                             t=theme: self.change_theme(t))
#
#         self.feature_tabs = ttk.Notebook(self)
#         self.feature_tabs.pack(expand=True, fill=tk.BOTH)
#         # bind click event to the theme menu
#         # self.theme_menu.bind("<Button-1>", self.change_theme)
#         # # Button Widgets
#         # Def_Btn = tk.Button(self, text='Default Button')
#         # Def_Btn.pack()
#         # Themed_Btn = ttk.Button(self, text='Themed button')
#         # Themed_Btn.pack()
#         #
#         # # Scrollbar Widgets
#         # Def_Scrollbar = tk.Scrollbar(self)
#         # Def_Scrollbar.pack(side='right', fill='y')
#         # Themed_Scrollbar = ttk.Scrollbar(self, orient='horizontal')
#         # Themed_Scrollbar.pack(side='top', fill='x')
#
#
#         # Feature Tabs
#         self.feature_tabs = ttk.Notebook(self)
#         self.feature_tabs.pack(expand=True, fill=tk.BOTH)
#
#         # Data Information Tab
#         self.data_information_tab = ttk.Frame(self.feature_tabs)
#         self.feature_tabs.add(self.data_information_tab,
#                               text="Data Information")
#
#         # Statistics Tab
#         self.statistics_tab = ttk.Frame(self.feature_tabs)
#         self.feature_tabs.add(self.statistics_tab, text="Statistics")
#
#         # Graph Tab
#         self.graph_tab = ttk.Frame(self.feature_tabs)
#         self.feature_tabs.add(self.graph_tab, text="Graph")
#
#     def init_home_page(self):
#         # This function can be expanded for additional content on the home page
#         pass
#
#     # def color_scheme(self, mode):
#     #     if mode == 'dark':
#     #         self.bg, self.fg, self.ac1, self.ac2 = (
#     #         '#282828', 'white', '#404040y', '#B3B3B3')
#     #     if mode == 'light':
#     #         self.bg, self.fg, self.ac1, self.ac2 = (
#     #         '#FBF8F1', 'black', '#F7ECDE', '#E9DAC1')
#
#     # def theme_switch(self):
#         # window = ThemedTk(theme="arc")
#         # if self.bg == '#282828':
#         #     self.color_scheme('light')
#         #     # We change the text to match the opposite theme
#         #     self.theme_btn_text = 'Dark Theme'
#         # elif self.bg == '#FBF8F1':
#         #     self.color_scheme('dark')
#         #     self.theme_btn_text = 'Light Theme'
#         # if self.bg == '#282828':
#         #     self.change_theme("light")
#         # else:
#         #     self.change_theme("dark")
#         # self.restart_GUI()
#
#     def change_theme(self, theme):
#         """Function to change the theme"""
#         self.set_theme(theme)
#
#     def set_theme(self, theme):
#         """Function to set the theme"""
#         window = ThemedTk(theme=theme)
#
#     #     # Left Panel: Data Information
#     #     self.left_frame = ttk.Frame(self, width=200, height=400)
#     #     self.left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
#     #
#     #     self.data_information_label = ttk.Label(self.left_frame,
#     #                                             text="Data Information")
#     #     self.data_information_label.pack(pady=10)
#     #
#     #     # self.data_information_image = tk.PhotoImage(
#     #     #     file="data_information.png")
#     #     # self.data_information_button = ttk.Button(self.left_frame,
#     #     #                                           image=self.data_information_image,
#     #     #                                           command=self.show_data_information)
#     #     # self.data_information_button = ttk.Button(self.left_frame,
#     #     #                                           command=self.show_data_information)
#     #     self.data_information_cbb = ttk.Combobox(self.left_frame, values=["Summary Statistics", "Correlations"])
#     #     self.data_information_cbb.pack(pady=10)
#     #     # self.data_information_button.pack(pady=10)
#     #
#     #     # Middle Panel: Visualization
#     #     self.middle_frame = ttk.Frame(self, width=400, height=400)
#     #     # self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
#     #     self.middle_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)
#     #
#     #     # self.visualization_image = tk.PhotoImage(
#     #     #     file="data_information.png")
#     #     self.visualization_label = ttk.Label(self.middle_frame,
#     #                                          text="Visualization")
#     #     self.visualization_label.pack(pady=10)
#     #
#     #     self.distribution_graph_button = ttk.Button(self.middle_frame,
#     #                                                 text="Distribution Graph",
#     #                                                 command=self.show_distribution_graph)
#     #     self.distribution_graph_button.pack(pady=5, padx=10, fill=tk.X)
#     #
#     #     self.interactive_graph_button = ttk.Button(self.middle_frame,
#     #                                                text="Interactive Graph",
#     #                                                command=self.show_interactive_graph)
#     #     self.interactive_graph_button.pack(pady=5, padx=10, fill=tk.X)
#     #
#     #     self.filtering_options_button = ttk.Button(self.middle_frame,
#     #                                                text="Filtering Options",
#     #                                                command=self.show_filtering_options)
#     #     self.filtering_options_button.pack(pady=5, padx=10, fill=tk.X)
#     #
#     #     # Right Panel: Select
#     #     self.right_frame = ttk.Frame(self, width=200, height=400)
#     #     self.right_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)
#     #
#     #
#     #     self.select_label = ttk.Button(self.right_frame, text="More options")
#     #     self.select_label.pack(pady=10, padx=10, fill=tk.X)
#     #
#     #     # self.select_label = ttk.Label(self.right_frame, text="Select")
#     #     # self.select_label.pack()
#     #     #
#     #     # # self.select_image = tk.PhotoImage(file="select.png")
#     #     # # self.select_button = ttk.Button(self.right_frame,
#     #     # #                                 image=self.select_image,
#     #     # #                                 command=self.show_select)
#     #     # self.select_button = ttk.Button(self.right_frame,
#     #     #                                 command=self.show_select)
#     #     # self.select_button.pack(pady=10)
#     #     # self.select_options = ttk.Combobox(self.right_frame, values=["Option 1", "Option 2", "Option 3"])
#     #     # self.select_options.pack(pady=10)
#     #     # self.select_cbb = ttk.Combobox(self.right_frame, command=self.show_select)
#     #     # self.select_cbb.pack(pady=10)
#     #
#     # def show_data_information(self):
#     #     """Function to handle Data Information click
#     #     Show the options for Summary Statistics and Correlations"""
#     #     pass
#     #
#     # def show_distribution_graph(self):
#     #     """Function to display the default distribution graph
#     #     (using Matplotlib)"""
#     #     pass
#     #
#     # def show_interactive_graph(self):
#     #     """ Function to allow users to select different interactive graphs
#     #     Implement based on user's choice (e.g., scatter plots, boxplots)"""
#     #     pass
#     #
#     # def show_filtering_options(self):
#     #     """Function to allow users to apply filters to the data
#     #     Implement based on user's selection criteria"""
#     #     pass
#     #
#     # def show_select(self):
#     #     """Function to handle Select click
#     #     perform specific actions when Select is clicked"""
#     #     pass
#
#     def run(self):
#         self.mainloop()

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from model import *  # Assuming this imports your model logic


class HeartDiseaseView(ThemedTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Explorer")
        self.init_components()
        self.default_theme = 'clam'

    def init_components(self):
        # Menu Bar for selecting theme
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        themes = {
            "Arc Mode": "arc",
            "Blue Mode": "blue",
            "Clearlooks Mode": "clearlooks",
            "Elegance Mode": "elegance",
            "Kroc Mode": "kroc",
            "Plastik Mode": "plastik",
            "Radiance Mode": "radiance",
            "WinXPBlue Mode": "winxpblue",
        }

        for theme_name, theme_value in themes.items():
            self.theme_menu.add_command(label=theme_name, command=lambda t=theme_value: self.change_theme(t))

        self.theme_menu.add_command(label="Default Theme", command=self.set_default_theme)
        self.bind("<Control-t>", lambda e: self.theme_switch())

        # Feature Tabs
        self.feature_tabs = ttk.Notebook(self)
        self.feature_tabs.pack(expand=True, fill=tk.BOTH)

        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab, text="Data Information")

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")

        # Graph Tab
        self.graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.graph_tab, text="Graph")

        # Button to gracefully exit
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def change_theme(self, theme_value):
        self.set_theme(theme_value)

        for child in self.winfo_children():
            if child != self.menu_bar and child != self.quit_button:
                child.destroy()
        self.init_components()

    def set_default_theme(self):
        self.set_theme(self.default_theme)

        for child in self.winfo_children():
            if child != self.menu_bar and child != self.quit_button:
                child.destroy()
        self.init_components()

    def init_home_page(self):
        # This function can be expanded for additional content on the home page
        pass

    # def theme_switch(self):
    #     # Display current theme in a dialog (optional):
    #     current_theme = self.theme_get()
    #     message = f"Current Theme: {current_theme.capitalize()}"
    #     tk.messagebox.showinfo(title="Theme Information", message=message)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    controller = ...  # Initialize your controller object
    window = HeartDiseaseView(controller)
    window.mainloop()
