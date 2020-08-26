import handle_input as handlein
from tkinter import *
from PIL import ImageTk, Image
from sys import argv

def DrawMap(canvas, maze, maze_size, asset_path):
    for each in maze:
        for room in each:
            if room == '-':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'terrain.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)
            elif room == 'A':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'agent_right.png'))
                canvas.create_image((10, 10), anchor = 'nw',image=image)
            elif room == 'P':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'pit.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)
            elif room == 'W':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'wumpus.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)
            elif room == 'B':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'terrain_breeze.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)
            elif room == 'S':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'terrain_stench.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)
            elif room == 'BS':
                image = ImageTk.PhotoImage(Image.open(asset_path + 'terrain_BS.png'))
                canvas.create_image((10, 10), anchor = 'nw', image=image)

if __name__ == '__main__':
    filename = argv[1]
    Map_path = '../../INPUT/MAP/'
    asset_path = '../../ASSET/'
    
    map_size, maze = handlein.read_file(filename)

    for each in maze:
        print(each)
    
    root = Tk()
    canvas = Canvas(root)
    canvas.pack()
    root.title("WUMPUS WORLD AI")
    icon = ImageTk.PhotoImage(Image.open(asset_path + 'Wumpus-Icon.png'))
    root.iconphoto(None, icon)
    DrawMap(canvas, maze, map_size, asset_path)
    root.mainloop()

    
