import handle_input as handlein
from tkinter import *
from PIL import ImageTk, Image
from sys import argv

def DrawMap(canvas, maze, maze_size, asset_path):

    background = {
        '-'     : ImageTk.PhotoImage(file=asset_path + '/terrain.png'),
        'P'     : ImageTk.PhotoImage(file=asset_path + '/pit.png'),
        'B'     : ImageTk.PhotoImage(file=asset_path + '/terrain_breeze.png'),
        'S'     : ImageTk.PhotoImage(file=asset_path + '/terrain_stench.png'),
        'BS'    : ImageTk.PhotoImage(file=asset_path + '/terrain_BS.png'),
        'A'     : ImageTk.PhotoImage(file=asset_path + '/agent_right.png'),
        'W'     : ImageTk.PhotoImage(file=asset_path + '/wumpus.png'),
        'G'     : ImageTk.PhotoImage(file=asset_path + '/gold.png'),
        'BG'    : ImageTk.PhotoImage(file=asset_path + '/gold_BG.png'),
        'GS'    : ImageTk.PhotoImage(file=asset_path + '/gold_GS.png'),
        'BGS'   : ImageTk.PhotoImage(file=asset_path + '/gold_BS.png')
    }

    # Draw Background
    for y, item in enumerate(maze):
        print(y, item)
        for x, tile in enumerate(item):
            print(x, tile, background[tile])
            photo = background[tile]
            canvas.image = photo
            canvas.create_image((x * background[tile].width(), y * background[tile].height()), anchor = 'nw', image=photo)
            #if 'S': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['S'])
            #elif 'A': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['A'])
            #elif 'P': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['P'])
            #elif '-': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['-'])
            #elif 'B': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['B'])
            #elif 'W': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['W'])
            #elif 'G': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['G'])
            #elif 'BS': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['BS'])
            #elif 'BG': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['BG'])
            #elif 'GS': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['GS'])
            #elif 'BGS': canvas.create_image(x * background[tile].width(), y * background[tile].height(), anchor = 'nw', image=background['BGS'])

if __name__ == '__main__':
    filename = argv[1]
    Map_path = '../../INPUT/MAP/'
    asset_path = '../../ASSET'
    
    map_size, maze = handlein.read_file(Map_path + filename)
    
    for each in maze:
        print(each)
    
    root = Tk()
    canvas = Canvas(root, width='400p', height='400p')
    canvas.pack(expand=YES, fill=BOTH)
    root.title("WUMPUS WORLD AI")
    icon = ImageTk.PhotoImage(Image.open(asset_path + '/Wumpus-Icon.png'))
    root.iconphoto(None, icon)
    DrawMap(canvas, maze, map_size, asset_path)
    root.mainloop()
