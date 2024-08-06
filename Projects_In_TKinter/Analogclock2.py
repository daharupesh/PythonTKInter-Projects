import tkinter as tk
import time
import math

def update_clock():
    current_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    canvas.delete('clock')
    draw_clock_face()
    draw_clock_hands()
    root.after(1000, update_clock)

def draw_clock_face():
    center_x = 150
    center_y = 150
    radius = 130

    canvas.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       width=4, outline='black', tags='clock')
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        canvas.create_text(x, y, text=str(i + 1), font=('Arial', 12, 'bold'), tags='clock')

def draw_clock_hands():
    center_x = 150
    center_y = 150
    radius = 100
    current_time = time.localtime()
    
    hour_angle = math.radians((current_time.tm_hour % 12) * 30 - 90)
    hour_x = center_x + int(radius * 0.4 * math.cos(hour_angle))
    hour_y = center_y + int(radius * 0.4 * math.sin(hour_angle))
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill='black', tags='clock')
    
    minute_angle = math.radians(current_time.tm_min * 6 - 90)
    minute_x = center_x + int(radius * 0.6 * math.cos(minute_angle))
    minute_y = center_y + int(radius * 0.6 * math.sin(minute_angle))
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill='black', tags='clock')
    
    second_angle = math.radians(current_time.tm_sec * 6 - 90)
    second_x = center_x + int(radius * 0.8 * math.cos(second_angle))
    second_y = center_y + int(radius * 0.8 * math.sin(second_angle))
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill='red', tags='clock')

root = tk.Tk()
root.title('Well-Designed Analog Clock')

clock_label = tk.Label(root, font=('Arial', 16))
clock_label.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

update_clock()

root.mainloop()
