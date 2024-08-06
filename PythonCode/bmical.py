import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        result_label.config(text=f"Your BMI: {bmi}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x200")  # Set window size

# Custom font
title_font = tkfont.Font(family="Arial", size=16, weight="bold")

# Create labels
weight_label = tk.Label(window, text="Weight (in kg):", font=title_font)
weight_label.pack(pady=10)

height_label = tk.Label(window, text="Height (in meters):", font=title_font)
height_label.pack(pady=10)

result_label = tk.Label(window, text="Your BMI: ", font=title_font)
result_label.pack(pady=10)

# Create entry widgets
weight_entry = tk.Entry(window, font=title_font)
weight_entry.pack()

height_entry = tk.Entry(window, font=title_font)
height_entry.pack()

# Create a button
calculate_button = tk.Button(window, text="Calculate", font=title_font, command=calculate_bmi)
calculate_button.pack(pady=10)

# Configure background and foreground colors
window.configure(bg="#f0f0f0")
weight_label.configure(bg="#f0f0f0")
height_label.configure(bg="#f0f0f0")
result_label.configure(bg="#f0f0f0")

# Start the main loop
window.mainloop()
