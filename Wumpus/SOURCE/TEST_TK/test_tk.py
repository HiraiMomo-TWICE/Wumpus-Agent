from tkinter import *
from PIL import ImageTk, Image

windows = Tk(classname = 'Test tKinter')  # Create GUI
windos.title('Wumpus-Agent')
windows.geometry("600x600")  # Change resolution

quit_button = Button(windows, text = 'EXIT', command = windows.quit)
quit_button.pack()

windows.mainloop()
