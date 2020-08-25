from tkinter import *
from PIL import ImageTk, Image

root = Tk()  # Create GUI
root.title('Wumpus-Agent') # Game Title
root.geometry("1280x720")  # Change resolution

# Game Icon
root.iconphoto(False, ImageTk.PhotoImage(Image.open('../../ASSET/Wumpus-Icon.png')))

# Background Image for Wumpus
C = Canvas(root, bg='blue', height=700, width=1280)
imagefile = ImageTk.PhotoImage(Image.open('../../ASSET/background.jpg'))
background_label = Label(root, image = imagefile)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
C.pack()

quit_button = Button(None, text = 'EXIT', command = root.quit)
quit_button.pack()

root.mainloop()
