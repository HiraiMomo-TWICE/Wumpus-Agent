import tkinter as tk
from PIL import ImageTk, Image

def play(maze, map_size, asset_path):
    root = tk.Tk()
    canvas = tk.Canvas(root, width='600p', height='550p')
    canvas.pack(expand='YES', fill='both')
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
        'A'     : {
            'UP'    : ImageTk.PhotoImage(file=asset_path + '/agent_up.png'),
            'RIGHT' : ImageTk.PhotoImage(file=asset_path + '/agent_right.png'),
            'DOWN'  : ImageTk.PhotoImage(file=asset_path + '/agent_down.png'),
            'LEFT'  : ImageTk.PhotoImage(file=asset_path + '/agent_right.png'),
        }
    }

    
    # Use to cover unvistited position
    hidden = ImageTk.PhotoImage(file=asset_path + '/hidden.png')

    count_Gold = 0
    count_Wumpus = 0
    # Draw Maze
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            canvas.create_image((x * background[tile].width(), y * background[tile].height()), anchor = 'nw', image=background[tile])
        scoreDisplay_pos = y

    # Put Object
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'G' in tile:
                canvas.create_image((x * game_object['G'].width(), y * game_object['G'].height()), anchor = 'nw', image=game_object['G'])
                count_Gold = count_Gold + 1
            elif 'W' in tile:
                canvas.create_image((x * game_object['W'].width(), y * game_object['W'].height()), anchor = 'nw', image=game_object['W'])
                count_Wumpus = count_Wumpus + 1
            else:
                continue

    print(count_Gold, count_Wumpus)
    #######################################################################################################################################       

    # Initialize the game
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'A' not in tile:
                canvas.create_image((x * hidden.width(), y * hidden.height()), anchor = 'nw', image=hidden)
            else:
                canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])

    # Game
    score = 0
    gold = 100
    climb_out = 10
    shoot_arrow = 100
    each_step = 10
    
    Wall = ''
    starting_position = tuple() # A position to escape
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'A' in tile:
                starting_position = (x, y)
                break


    # MOVE (IF not Wall)
        # If direction not LEFT -> change to LEFT -> Move to left
        # elif LEFT -> MOVE to left
        # If direction not UP -> change to UP -> Move up
        # elif UP -> MOVE up
        # If direction not RIGHT -> change to RIGHT -> Move to RIGHT
        # elif RIGHT -> MOVE to RIGHT
        # If direction not DOWN -> change to DOWN -> Move to DOWN
        # elif DOWN -> MOVE down

    # Move right
    for y, item in enumerate(maze):
        for x, tile in enumerate(item):
            if 'A' in tile:
                if not game_object['A']['RIGHT']: # and next tile is not Wall:
                    canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    score -= each_step
                elif game_object['A']['RIGHT']: # and next tile is not Wall:
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    score -= each_step
                    pass
                elif not game_object['A']['LEFT']: # and next tile is not Wall:
                    canvas.create_image((x * game_object['A']['LEFT'].width(), y * game_object['A']['LEFT'].height()), anchor = 'nw', image=game_object['A']['LEFT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    score -= each_step
                elif game_object['A']['LEFT']: # and next tile is not Wall:
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    score -= each_step
                    pass
                elif not game_object['A']['UP']: # and next tile is not Wall:
                    canvas.create_image((x * game_object['A']['UP'].width(), y * game_object['A']['UP'].height()), anchor = 'nw', image=game_object['A']['UP'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    score -= each_step
                elif game_object['A']['UP']: # and next tile is not Wall:
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    score -= each_step
                    pass
                elif not game_object['A']['DOWN']: # and next tile is not Wall:
                    canvas.create_image((x * game_object['A']['DOWN'].width(), y * game_object['A']['DOWN'].height()), anchor = 'nw', image=game_object['A']['DOWN'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    score -= each_step
                elif game_object['A']['DOWN']: # and next tile is not Wall:
                    # canvas.create_image((x * game_object['A']['RIGHT'].width(), y * game_object['A']['RIGHT'].height()), anchor = 'nw', image=game_object['A']['RIGHT'])
                    # canvas.delete(game_object['A']['RIGHT'])
                    score -= each_step
                    pass
                if 'S' in tile:
                    # look directions NOT WALL and shoot arrows
                    pass

    # IF Shoot Arrow
        # 1. Face Direction, shoot arrow
        # 2. You can shoot arrow step
    # print('ARROW SHOT')
    
    # 
           
    root.mainloop()
