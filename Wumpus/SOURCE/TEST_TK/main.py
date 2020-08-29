import handle_input as handlein
from tkinter import *
from PIL import ImageTk, Image
from sys import argv
            
if __name__ == '__main__':
    filename = argv[1]
    Map_path = '../../INPUT/MAP/'
    asset_path = '../../ASSET'
    
    map_size, maze = handlein.read_file(Map_path + filename)

    for each in maze:
        print(each)
    
    root = Tk()
    canvas = Canvas(root, width='600p', height='550p')
    canvas.pack(expand=YES, fill=BOTH)
    root.title("WUMPUS WORLD AI")
    icon = ImageTk.PhotoImage(Image.open(asset_path + '/Wumpus-Icon.png'))
    root.iconphoto(None, icon)
    
    # Draw Background
    background = {
        '-'     : ImageTk.PhotoImage(file=asset_path + '/terrain.png'),
        'P'     : ImageTk.PhotoImage(file=asset_path + '/pit.png'),
        'B'     : ImageTk.PhotoImage(file=asset_path + '/terrain_breeze.png'),
        'S'     : ImageTk.PhotoImage(file=asset_path + '/terrain_stench.png'),
        'BS'    : ImageTk.PhotoImage(file=asset_path + '/terrain_BS.png'),
        'A'     : ImageTk.PhotoImage(file=asset_path + '/terrain.png'),
        'W'     : ImageTk.PhotoImage(file=asset_path + '/terrain.png'),
        'G'     : ImageTk.PhotoImage(file=asset_path + '/terrain.png'),
        'BG'    : ImageTk.PhotoImage(file=asset_path + '/terrain_breeze.png'),
        'GS'    : ImageTk.PhotoImage(file=asset_path + '/terrain_stench.png'),
        'BGS'   : ImageTk.PhotoImage(file=asset_path + '/terrain_BS.png')
    }

    # Game object
    game_object = {
        'G'     : ImageTk.PhotoImage(file=asset_path + '/gold.png'),
        'W'     : ImageTk.PhotoImage(file=asset_path + '/wumpus.png'),
        'A'     : ImageTk.PhotoImage(file=asset_path + '/agent_right.png')
    }

    # Agent Direction
    agent_direction = {
        'UP'    : ImageTk.PhotoImage(file=asset_path + '/agent_up.png'),
        'RIGHT' : ImageTk.PhotoImage(file=asset_path + '/agent_right.png'),
        'DOWN'  : ImageTk.PhotoImage(file=asset_path + '/agent_down.png'),
        'LEFT'  : ImageTk.PhotoImage(file=asset_path + '/agent_right.png'),
    }
    
    # Use to cover unvistited position
    hidden = ImageTk.PhotoImage(file=asset_path + '/hidden.png')

    # Draw Maze
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            canvas.create_image((x * background[tile].width(), y * background[tile].height()), anchor = 'nw', image=background[tile])

    # Put Object
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'G' in tile:
                canvas.create_image((x * game_object['G'].width(), y * game_object['G'].height()), anchor = 'nw', image=game_object['G'])
            elif 'W' in tile:
                canvas.create_image((x * game_object['W'].width(), y * game_object['W'].height()), anchor = 'nw', image=game_object['W'])
            else:
                continue

    #######################################################################################################################################       

    # Initialize the game
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'A' not in tile:
                canvas.create_image((x * hidden.width(), y * hidden.height()), anchor = 'nw', image=hidden)
            else:
                canvas.create_image((x * game_object['A'].width(), y * game_object['A'].height()), anchor = 'nw', image=game_object['A'])
            
    # Game
    score = 0
    starting_position = tuple() # A position to escape
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'A' in tile:
                starting_position = (x, y)
                break

    





    
            
    root.mainloop()
