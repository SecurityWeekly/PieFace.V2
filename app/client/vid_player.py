# from subprocess import Popen

# movie1 = '/home/kyle/Desktop/vids/vid.mp4'
# omxc = Popen(['omxplayer', '-b', movie1])






from tkinter import Tk, Canvas
from PIL import ImageTk, Image


# root = tkinter.Tk()
#
# photo = tkinter.PhotoImage(file="image.gif")
# img1 = tkinter.Label(root, image = photo)
# img1.pack()
# root.mainloop()




root = Tk()
root.attributes("-fullscreen", True)

# Create a canvas
canvas = Canvas(root, width=9000, height=300)
canvas.pack()

# Load the image file
im = Image.open('download.jpg')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
canvas.image = ImageTk.PhotoImage(im)
# Add the image to the canvas, and set the anchor to the top left / north west corner
canvas.create_image(0, 0, image=canvas.image, anchor='nw')

root.mainloop()

