#Displaying Images Using Label | Python Tkinter Gui Tutorial

from tkinter import *
# by default it support the png image but for other types of image like jpg
# we have to install pillow package... Pip install pillow
from PIL import Image, ImageTk


root = Tk()
root.geometry("1400x1100")
# photo = PhotoImage(file="image/img1.png")
image = Image.open("image/img.jpg")
photo = ImageTk.PhotoImage(image)

img_label = Label(image=photo)
img_label.pack()

root.mainloop()