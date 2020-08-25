import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class Layout:
    def __init__(self,master):
       self.master = master
       self.rootgeometry()
       self.canvas = tk.Canvas(self.master)
       self.canvas.pack()
       self.background_image = Image.open('../../ASSET/background.jpg') 
       self.image_copy = self.background_image.copy()
       self.background = ImageTk.PhotoImage(self.background_image)
       self.loadbackground()
       frame = Frame(root, height = "200", width = "200", bg = "red")
       frame.pack()
       quit_button = Button(frame, text = 'EXIT', command = root.quit)
       quit_button.pack(padx = "10", pady = "10")

    def loadbackground(self):
        self.label = tk.Label(self.canvas, image = self.background)
        self.label.bind('<Configure>',self.resizeimage)
        self.label.pack(fill='both', expand='yes')

    def rootgeometry(self):
       x=int(self.master.winfo_screenwidth()*0.7)
       y=int(self.master.winfo_screenheight()*0.7)
       z = str(x) + 'x' + str(y)
       self.master.geometry(z)

    def resizeimage(self,event):
       image = self.image_copy.resize((self.master.winfo_width(),self.master.winfo_height()))
       self.image1 = ImageTk.PhotoImage(image)
       self.label.config(image = self.image1)

#def resize_image(event):
    #new_witdth = event.width
    #new_height = event.height
    #image = copy_of_image.resize((new_width, new_height))
    #photo = ImageTk.PhotoImage(image)
    #label.config(image = photo)
    #label.image = photo

root = Tk()  # Create GUI
a = Layout(root)
root.title('Wumpus-Agent') # Game Title
root.geometry("1280x720")  # Change resolution

# Game Icon
root.iconphoto(False, ImageTk.PhotoImage(Image.open('../../ASSET/Wumpus-Icon.png')))

# Button
z = Label(root, text = "OUTSIDE")
z.pack()

root.mainloop()
