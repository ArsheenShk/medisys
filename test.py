import tkinter as tk

def change_color(*args):
    color = choice_var.get()
    if color == "Red-22":
        root.configure(background="red")
    elif color == "Green-23":
        root.configure(background="green")
    elif color == "Blue":
        root.configure(background="blue")
    elif color == "Yellow":
        root.configure(background="yellow")
    elif color == "Purple":
        root.configure(background="purple")

root = tk.Tk()
root.title("Color Chooser")

# Define color options
colors = ["Red-22", "Green-23", "Blue", "Yellow", "Purple"]

# Create choicebox
choice_var = tk.StringVar(root)
choice_var.set(colors[-1])  # Set default value
choice_var.trace("w", change_color)  # Call change_color function when choice changes
choicebox = tk.OptionMenu(root, choice_var, *colors)
choicebox.pack(pady=10)

root.mainloop()
