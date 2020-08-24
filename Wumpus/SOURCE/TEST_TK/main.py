import handle_input as handlein

if __name__ == '__main__':
    filename = 'Map1.txt'

    map_size, maze = handlein.read_file(filename)

    print(map_size)
    for each in maze:
        print(each)
