import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Heart Disease Explorer")
root.geometry("1000x600")

s=ttk.Style()
s.theme_use('aqua')
# ('aqua', 'clam', 'alt', 'default', 'classic')
# aqua=default mac, clam=blue

# Modify the background color
# s.configure('.', background='lightblue')  # '.' is a wildcard selector, applies to all widgets

# Create some widgets
label = ttk.Label(root, text="Theme Test")
label.pack(padx=20, pady=20)

entry = ttk.Entry(root)
entry.pack(padx=20, pady=5)

button = ttk.Button(root, text="Submit")
button.pack(padx=20, pady=10)

root.mainloop()
