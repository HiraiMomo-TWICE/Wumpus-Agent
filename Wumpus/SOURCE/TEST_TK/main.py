import handle_input as handlein
from tkinter import *
from PIL import ImageTk, Image
from sys import agv

# Path Settings
os.chdir('../')
PATH = os.getcwd()

if __name__ == '__main__':
    filename = os.path.join(PATH, 'INPUT/MAP', arg[1])

    map_size, maze = handlein.read_file(filename)

    print(map_size)
    for each in maze:
        print(each)
