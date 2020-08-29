import handle_input as handlein
import wumpus as wp
from sys import argv
            
if __name__ == '__main__':
    filename = argv[1]
    Map_path = '../../INPUT/MAP/'
    asset_path = '../../ASSET'
    
    map_size, maze = handlein.read_file(Map_path + filename)
    for each in maze:
        print(each)
        
    wp.play(maze, map_size, asset_path)
