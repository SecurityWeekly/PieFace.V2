from itertools import cycle

import tkinter as tk
from PIL import ImageTk, Image


class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''

    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((ImageTk.PhotoImage(image), image)
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
        self.attributes("-fullscreen", True)

    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set milliseconds time between slides
delay = 3500
# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
image_files = [
    Image.open('download.jpg').resize((1920, 1080), Image.ANTIALIAS),
    Image.open('download2.png').resize((1920, 1080), Image.ANTIALIAS),
    Image.open('download3.jpg').resize((1920, 1080), Image.ANTIALIAS)
]
# upper left corner coordinates of app window
x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()
