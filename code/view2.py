import customtkinter
import tkinter as tk
from tkinter import ttk


# Define a variable to keep track of the current appearance mode
current_mode = "System"  # Start with the system mode


class HeartDiseaseView(customtkinter.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Heart Disease Analysis")
        self.geometry("800x600")
        self.init_components()

    def init_components(self):
        # Menu Bar for Selecting theme
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(label="System", command=self.set_system_theme)
        self.theme_menu.add_command(label="Light", command=self.set_light_theme)
        self.theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
        self.menu_bar.add_command(label="Quit", command=self.quit)
        self.menu_bar.bind("<Control-q>", lambda e: self.quit())

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

        # Button to gracefully exit
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    @staticmethod
    def set_system_theme():
        customtkinter.set_appearance_mode("System")
        show_toast("Changed theme color to System")

    @staticmethod
    def set_light_theme():
        customtkinter.set_appearance_mode("light")
        show_toast("Changed theme color to Light")

    @staticmethod
    def set_dark_theme():
        customtkinter.set_appearance_mode("dark")
        show_toast("Changed theme color to Dark")


def show_toast(message):
    toast = tk.Toplevel()
    toast.geometry("200x100+400+300")  # Adjust position and size as needed
    toast.title("Notification")
    toast.attributes("-topmost", True)  # Make the toast appear on top of other windows
    label = tk.Label(toast, text=message)
    label.pack(pady=20)
    # After 3 seconds, destroy the toast window
    toast.after(3000, toast.destroy)
    toast.mainloop()


# def set_system_theme():
#     customtkinter.set_appearance_mode("System")
#
# def set_light_theme():
#     customtkinter.set_appearance_mode("light")
#
# def set_dark_theme():
#     customtkinter.set_appearance_mode("dark")
# def toggle_mode():
#     global current_mode
#     if current_mode == "System":
#         customtkinter.set_appearance_mode("light")
#         current_mode = "Light"
#         print("Light mode")
#     elif current_mode == "Light":
#         customtkinter.set_appearance_mode("dark")
#         current_mode = "Dark"
#         print("Dark mode")
#     else:
#         customtkinter.set_appearance_mode("System")
#         current_mode = "System"
#         print("System mode")

# app = customtkinter.CTk()
# app.geometry("400x240")
#
# button = customtkinter.CTkButton(master=app, text="Toggle Mode", command=toggle_mode)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
app = HeartDiseaseView(None)
app.mainloop()
