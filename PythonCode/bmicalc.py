import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
window.geometry("400x300")  # Set window size

# Load and resize the background image
background_image = Image.open("img.png")
background_image = background_image.resize((400, 300), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a background label and place it in the window
background_label = tk.Label(window, image=background_photo)
background_label.pack()

# Apply the image as the window background
window.configure(bg="#f0f0f0")
window.wm_attributes("-transparentcolor", "#f0f0f0")

# Create labels
weight_label = tk.Label(window, text="Weight (in kg):", font=("Arial", 16), bg="#f0f0f0")
weight_label.place(x=50, y=80)

height_label = tk.Label(window, text="Height (in meters):", font=("Arial", 16), bg="#f0f0f0")
height_label.place(x=50, y=120)

result_label = tk.Label(window, text="Your BMI: ", font=("Arial", 16), bg="#f0f0f0")
result_label.place(x=50, y=200)

# Create entry widgets
weight_entry = tk.Entry(window, font=("Arial", 16))
weight_entry.place(x=230, y=80)

height_entry = tk.Entry(window, font=("Arial", 16))
height_entry.place(x=230, y=120)

# Create a button
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 16), command=calculate_bmi)
calculate_button.place(x=150, y=160)

# Start the main loop
window.mainloop()
