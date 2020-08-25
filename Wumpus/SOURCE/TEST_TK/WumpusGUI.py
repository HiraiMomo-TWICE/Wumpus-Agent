try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from PIL import ImageTk, Image
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class Layout(tk.Tk):
    def __init__(self,master):
       self.master = master
       self.rootgeometry()
       self.canvas = tk.Canvas(self.master)
       self.canvas.pack()
       self.background_image = Image.open('../../ASSET/background.jpg') 
       self.image_copy = self.background_image.copy()
       self.background = ImageTk.PhotoImage(self.background_image)
       self.loadbackground()

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

class WumpusWorld(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.iconphoto(False, ImageTk.PhotoImage(Image.open('../../ASSET/Wumpus-Icon.png')))

        self.title('WUMPUS WORLD AGENT')
        self.title_font = tkfont.Font(family='Helvetica', size=50, weight="bold")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for each_frame in (StartMenu, MapSelection):
            page_name = each_frame.__name__
            frame = each_frame(parent = container, controller = self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "WUMPUS WORLD AGENT", font=controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)

        StartGameButton = tk.Button(self, text = "START", command = lambda: controller.show_frame("MapSelection"))
        QuitGameButton = tk.Button(self, text = "QUIT", command = controller.destroy)
        StartGameButton.pack()
        QuitGameButton.pack()

class MapSelection(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "SELECT YOUR MAP", font=controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)

if __name__ == "__main__":
    wumpus = WumpusWorld()
    a = Layout(wumpus)
    wumpus.mainloop()
        
        
