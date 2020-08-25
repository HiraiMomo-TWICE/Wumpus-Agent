from tkinter import *
# from PIL import ImageTk, Image

windows = Tk()  # Create GUI
windows.title('Wumpus-Agent')
windows.geometry("1280x720")  # Change resolution

quit_button = Button(None, text = 'EXIT', command = windows.quit)
quit_button.pack()

windows.mainloop()
