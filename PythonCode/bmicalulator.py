import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text="BMI: {:.2f}".format(bmi))

root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for height and weight
height_label = tk.Label(root, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create a label to display the calculated BMI
bmi_label = tk.Label(root, text="")
bmi_label.pack()

root.mainloop()
