import os

def read_file(mapfile):
    file = os.sys.path(open('../MAP/' + mapfile , 'r'))

    map_size = int(file.readline().split(' '))

    maze = [[string(attr) for attr in file.readline().split('.')] for _ in range(map_size)]

    f.close()

    return map_size, maze
