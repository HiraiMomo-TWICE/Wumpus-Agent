import tkinter
import os
import handle_input as handlein

if __name__ == '__main__':
    file = 'Map2.txt'

    maze_size, maze = handlein.read_file(file)

    print(f'Size: {map_size}')
    print(maze)
