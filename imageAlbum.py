from tkinter import *
from PIL import ImageTk, Image
# set up the tkinter window
root = Tk()
root.title("MOO ICT Python/Tkinter Image Viewer")
root.geometry("610x430")
root.iconbitmap("images/icon.ico")
# set up the images
image1 = ImageTk.PhotoImage(Image.open("images/01.jpg").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open("images/02.jpg").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((600, 350)))
image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))
# add them to the list
image_list = [image1, image2, image3, image4, image5]
# counter integer
counter = 0
# change image function
def ChangeImage():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(image_list)))
# set up the components
imageLabel = Label(root, image=image1)
infoLabel = Label(root, text="Image 1 of 5", font="Helvetica, 20")
button = Button(root, text="Change", width=20, height=2, bg="purple", fg="white", command=ChangeImage)
# display the components
imageLabel.pack()
infoLabel.pack()
button.pack(side="bottom", pady=3)
# run the main loop
root.mainloop()