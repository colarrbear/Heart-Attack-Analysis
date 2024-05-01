# archive: for consider later
import customtkinter

# Define a variable to keep track of the current appearance mode
current_mode = "System"  # Start with the system mode

# Toggle between light and dark modes
def toggle_mode():
    global current_mode
    if current_mode == "System":
        customtkinter.set_appearance_mode("light")
        current_mode = "Light"
        print("Light mode")
    elif current_mode == "Light":
        customtkinter.set_appearance_mode("dark")
        current_mode = "Dark"
        print("Dark mode")
    else:
        customtkinter.set_appearance_mode("System")
        current_mode = "System"
        print("System mode")

app = customtkinter.CTk()
app.geometry("400x240")

button = customtkinter.CTkButton(master=app, text="Toggle Mode", command=toggle_mode)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
