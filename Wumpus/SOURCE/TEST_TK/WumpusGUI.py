try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from PIL import ImageTk, Image
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
    
class WumpusWorld(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.iconphoto(False, ImageTk.PhotoImage(Image.open('../../ASSET/Wumpus-Icon.png')))

        self.title('WUMPUS WORLD AGENT')
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for each_frame in (StartMenu, MapSelection, Map1, Map2, Map3,):
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

        Map1Button = tk.Button(self, text = "MAP 1", command = lambda: controller.show_frame("Map1"))
        Map1Button.pack()
        Map2Button = tk.Button(self, text = "MAP 2", command = lambda: controller.show_frame("Map2"))
        Map2Button.pack()
        Map3Button = tk.Button(self, text = "MAP 3", command = lambda: controller.show_frame("Map3"))
        Map3Button.pack()
        BackButton = tk.Button(self, text = "BACK", command = lambda: controller.show_frame("StartMenu"))
        BackButton.pack(side = "bottom")

class Map1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        StartMenuButton = tk.Button(self, text = "BACK TO START MENU", command = lambda:controller.show_frame("StartMenu"))
        StartMenuButton.pack()

class Map2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        StartMenuButton = tk.Button(self, text = "BACK TO START MENU", command = lambda:controller.show_frame("StartMenu"))
        StartMenuButton.pack()

class Map3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        StartMenuButton = tk.Button(self, text = "BACK TO START MENU", command = lambda:controller.show_frame("StartMenu"))
        StartMenuButton.pack()

if __name__ == "__main__":
    wumpus = WumpusWorld()
    wumpus.mainloop()
