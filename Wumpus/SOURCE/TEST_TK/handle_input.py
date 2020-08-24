def read_file(filename):
    f = open('../../INPUT/MAP/' + filename, 'r')

    content = f.read().splitlines()

    maze_size, maze = content[0], content[1:]
    room = []
    for each in maze:
        room.append(each.split('.'))
    return maze_size, room

    f.close()
