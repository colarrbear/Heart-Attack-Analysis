# # archive: for consider later
# import tkinter as tk
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename, asksaveasfilename
#
#
# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# window = tk.Tk()
# window.title("Simple Text Editor")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# check_on = tk.IntVar()
#
#
# def toggle():
#     if check_on.get():
#         cb_on.config(text='I love Python ')
#         txt_edit.config(fg='white', bg="#26242f")
#         cb_on.config(text='Change To White-mode')
#     else:
#         txt_edit.config(fg='black', bg="white")
#         cb_on.config(text='Change To Dark-mode')
#
#
# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
# cb_on = ttk.Checkbutton(fr_buttons, text='Change To Dark-mode',
#                         variable=check_on, onvalue=1,
#                         offvalue=0, command=toggle)
#
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
# cb_on.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
#
# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")
#
# window.mainloop()

from ttkthemes import ThemedStyle, ThemedTk
import tkinter as tk
from tkinter import ttk

# app = tk.Tk()
# app.title('App')

# style = ThemedStyle(app)
# style.set_theme("black")
#
# tktext = tk.Label(app, text=" tk Label")
# tktext.pack()
# tkbutton = tk.Button(app, text="tk Button")
# tkbutton.pack()
#
# # text = ttk.Label(app, text=" ttk Label")
# # text.pack()
# button = ttk.Button(app, text="ttk Button")
# button.pack()
#
# app.geometry('200x200')

app = ThemedTk(theme="winxpblue")
ttk.Button(app, text="Quit", command=app.destroy).pack()
app.mainloop()