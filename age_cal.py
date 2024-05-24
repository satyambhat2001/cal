import tkinter as tk
from datetime import datetime


def calculate_age():
    birth_date = datetime.strptime(entry_birth_date.get(), "%Y-%m-%d")
    current_date = datetime.now()
    age = (
        current_date.year
        - birth_date.year
        - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    )
    label_result.config(text=f"You are {age} years old.")


# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place widgets
label_birth_date = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):")
label_birth_date.pack()
entry_birth_date = tk.Entry(root)
entry_birth_date.pack()

button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Start the GUI event loop
root.mainloop()
