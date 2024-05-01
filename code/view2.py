# archive: for consider later
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
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.pack(side="left", fill="both", expand=True)
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0,
                                                            weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        # Menu Bar for Selecting theme
        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            self.tabview.tab("CTkTabview"), dynamic_resizing=False,
            values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(
            self.tabview.tab("CTkTabview"),
            values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))

        # self.menu_bar = customtkinter.CTkOptionMenu(self, values=["System", "Light", "Dark"],
        #                                             command=lambda mode: customtkinter.set_appearance_mode(mode))
        # self.optionmenu.configure(menu=self.menu_bar)
        # self.config(menu=self.menu_bar)
        # self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        # self.theme_menu.add_command(label="System", command=self.set_system_theme)
        # self.theme_menu.add_command(label="Light", command=self.set_light_theme)
        # self.theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        # self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
        # self.menu_bar.add_command(label="Quit", command=self.quit)
        # self.menu_bar.bind("<Control-q>", lambda e: self.quit())

        # Feature Tabs
    #     self.feature_tabs = ttk.Notebook(self)
    #     self.feature_tabs.pack(expand=True, fill=tk.BOTH)
    #
    #     # Data Information Tab
    #     self.data_information_tab = ttk.Frame(self.feature_tabs)
    #     self.feature_tabs.add(self.data_information_tab,
    #                           text="Data Information")
    #
    #     # Statistics Tab
    #     self.statistics_tab = ttk.Frame(self.feature_tabs)
    #     self.feature_tabs.add(self.statistics_tab, text="Statistics")
    #
    #     # Graph Tab
    #     self.graph_tab = ttk.Frame(self.feature_tabs)
    #     self.feature_tabs.add(self.graph_tab, text="Graph")
    #
    #     # Button to gracefully exit
    #     self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
    #     self.quit_button.pack()
    #
    # @staticmethod
    # def set_system_theme():
    #     customtkinter.set_appearance_mode("System")
    #     show_toast("Changed theme color to System")
    #
    # @staticmethod
    # def set_light_theme():
    #     customtkinter.set_appearance_mode("light")
    #     show_toast("Changed theme color to Light")
    #
    # @staticmethod
    # def set_dark_theme():
    #     customtkinter.set_appearance_mode("dark")
    #     show_toast("Changed theme color to Dark")


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

# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# def darkstyle(root):
#     """Return a dark style to the window"""
#     style = ttk.Style(root)
#     # root.tk.call('source', 'azure dark/azure dark.tcl')
#     # style.theme_use('azure')
#     style.theme_use('clam')
#     style.configure('.', background='black')
#     style.configure("Accentbutton", foreground='white')
#     style.configure("Togglebutton", foreground='white')
#     return style
#
#
# def main_window():
#     """ The window with the darkstyle """
#     root = tk.Tk()
#     root.title("My App")
#     root.resizable(False, False)
#     img = tk.PhotoImage(file="select.png")
#
#     style = darkstyle(root)
#
#     lab = ttk.Label(
#         root,
#         text="Hello World",
#         compound="center",
#         font="arial 50",
#         image=img)
#     lab.pack(fill="both", expand=1)
#
#     button = ttk.Button(
#         root,
#         text="Click me"
#     )
#
#     button.place(relx=0.43, rely=0.7, width=100, height=30)
#
#     root.mainloop()
#
#
# main_window()