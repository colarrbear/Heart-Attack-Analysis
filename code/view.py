"""handles the User interface of the application"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from model import *  # Assuming this imports your model logic
import time


class HeartDiseaseView(ThemedTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Explorer")
        self.init_components()
        # self.init_home_page()
        self.geometry("800x600")
        self.set_theme("winxpblue")
        self.create_quit_button()

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

            "Black Mode": "black",
            "Equilux Mode": "equilux",
        }
        # "WinXPBlue Mode": "winxpblue",

        for theme_name, theme_value in themes.items():
            self.theme_menu.add_command(label=theme_name, command=lambda t=theme_value: self.change_theme(t))

        self.theme_menu.add_command(label="Default Mode", command=self.set_default_theme)

        # Feature Tabs
        self.feature_tabs = ttk.Notebook(self)
        self.feature_tabs.configure(padding=10)
        # self.feature_tabs.pack(side=tk.TOP,expand=True, fill=tk.BOTH)
        # self.feature_tabs.pack(expand=True, fill=tk.BOTH)
        self.feature_tabs.pack(fill=tk.BOTH, expand=True)
        self.tabs()

    def tabs(self):
        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab, text="Data Information")
        # self.configure(anchor=tk.CENTER)

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")

        # Graph Tab
        self.graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.graph_tab, text="Graph")

    def change_theme(self, theme_value):
        self.set_theme(theme_value)

        # Create a list to hold references to child widgets to be destroyed
        widgets_to_destroy = []
        for child in self.winfo_children():
            if child != self.menu_bar and child != self.quit_button:
                widgets_to_destroy.append(child)

        # Destroy the child widgets in the list
        for widget in widgets_to_destroy:
            widget.destroy()

        # Reinitialize components to reflect the new theme
        self.feature_tabs.destroy()
        self.init_components()

        # Show pop-up box after theme change
        self.show_theme_change_popup(theme_value)
        # self.bind("<Configure>", self.show_theme_change_popup(theme_value))

    def show_theme_change_popup(self, new_theme):
        popup_message = f"Theme changed to {new_theme}"
        self.pop_up = Toast(self, popup_message, duration=2000)

    def set_default_theme(self):
        # self.set_theme("aqua")
        # # set to be centered
        # self.geometry("800x600")
        #
        # # Create a list to hold references to child widgets to be destroyed
        # widgets_to_destroy = []
        # for child in self.winfo_children():
        #     if child != self.menu_bar and child != self.quit_button:
        #         widgets_to_destroy.append(child)
        #
        # # Destroy the child widgets in the list
        # for widget in widgets_to_destroy:
        #     widget.destroy()
        #
        # # Reinitialize components to reflect the default theme
        # self.init_components()
        # Disable the default theme

        # Set new default theme to winxpblue
        self.set_theme("winxpblue")
        # self.bind("<Configure>", self.show_theme_change_popup("Default Theme Set"))
        # time.sleep(2)

        # Destroy and reinitialize components to reflect the default theme
        widgets_to_destroy = [child for child in self.winfo_children() if
                              child not in [self.menu_bar, self.quit_button]]
        for widget in widgets_to_destroy:
            widget.destroy()
        self.init_components()
        self.show_theme_change_popup("Default Theme Set")

    def create_quit_button(self):
        # Button to gracefully exit
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def init_home_page(self):
        # This function can be expanded for additional content on the home page
        pass

    def run(self):
        self.mainloop()


class Toast(tk.Toplevel):
    def __init__(self, parent, message, duration=2000):
        tk.Toplevel.__init__(self, parent)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.parent = parent
        self.message = message
        self.duration = duration
        self.label = tk.Label(self, text=self.message, bg="black", fg="white", padx=10, pady=5)
        self.label.pack()
        self.update_idletasks()
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self.x = self.parent.winfo_x() + self.parent.winfo_width() - self.width - 20  # Adjust the offset as needed
        self.y = self.parent.winfo_y() + 20  # Adjust the offset as needed
        self.geometry("+{}+{}".format(self.x, self.y))
        self.deiconify()
        self.after(self.duration, self.destroy)
# class Toast(tk.Toplevel):
#     def __init__(self, parent, message, duration=2000):
#         tk.Toplevel.__init__(self, parent)
#         self.overrideredirect(True)
#         self.attributes("-topmost", True)
#         self.parent = parent
#         self.message = message
#         self.duration = duration
#         self.label = tk.Label(self, text=self.message, bg="black", fg="white", padx=10, pady=5)
#         self.label.pack()
#         self.update_idletasks()
#         self.width = self.winfo_width()
#         self.height = self.winfo_height()
#         self.x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (self.width // 2)
#         self.y = self.parent.winfo_y() + self.parent.winfo_height() - self.height - 20
#         self.geometry("+{}+{}".format(self.x, self.y))
#         self.deiconify()
#         self.after(self.duration, self.destroy)


if __name__ == "__main__":
    controller = ...  # Initialize your controller object
    window = HeartDiseaseView(controller)
    window.mainloop()
