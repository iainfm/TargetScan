# TargetScore shooting target scoring system
# Author: Iain McLaren

print('TargetScore initialising...')

# Import modules
import tkinter as tkinter
# from PIL import ImageTk, Image
from PIL import Image, ImageTk

# # Static variables and function definitions
# from config import *
# from splatt_functions import *

# root = Tk()
# root.title('TargetScore')
# root.geometry('800x600')

# # Load the target image
# TargetImage = ImageTk.PhotoImage(Image.open('TestScan.jpg'))

# canvas = Canvas(root, width=800, height=600)
# canvas.create_image(0, 0, anchor=NW, image=TargetImage)
# canvas.config(scrollregion=canvas.bbox(ALL))

# canvas.grid(row=0, column=0, columnspan=3)

# # label = Label(image=TargetImage)
# # label.grid(row=1, column=0, columnspan=3)
# button_exit = Button(root, text='Exit', command=root.quit)
# button_exit.grid(row=5, column=1)
# root.mainloop()

def updateRoot(imagen):
    # resize the image to fill the whole screen
    pilImage = Image.open(imagen)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    image = ImageTk.PhotoImage(pilImage.resize((w,h)))
    # update the image
    canvas.itemconfig(imgbox, image=image)
    # need to keep a reference of the image, otherwise it will be garbage collected
    canvas.image = image

root = tkinter.Tk()
root.attributes('-fullscreen', 1)
root.bind('<Escape>', lambda _: root.destroy())

canvas = tkinter.Canvas(root, highlightthickness=0)
canvas.pack(fill=tkinter.BOTH, expand=1)
imgbox = canvas.create_image(0, 0, image=None, anchor='nw')

# show the first image
updateRoot('TestScan.jpg')
# change the image 5 seconds later
root.after(5000, updateRoot, 'TestScan1.jpg')

root.mainloop()