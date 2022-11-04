# aoc.year2021.cuboid

# using 2020-17 3d map as inspiration
# a cuboid is a 3 level dictionary
# cuboid[z][y][x] will give us the point (x, y, z)
# inside we will save a state 1 for on, 0 for off

def create_cuboid(min_x, max_x, min_y, max_y, min_z, max_z, start_state):
    dict_z = dict()
    for z in range(min_z, max_z+1):
        dict_y = dict()
        for y in range(min_y, max_y+1):
            dict_x = dict()
            for x in range(min_x, max_x+1):
                dict_x[x] = start_state
            dict_y[y] = dict_x
        dict_z[z] = dict_y
    return dict_z

def print_cuboid(cuboid):
    zkeys = list(cuboid.keys())
    zkeys.sort()
    ykeys = list(cuboid[zkeys[0]].keys())
    ykeys.sort()
    xkeys = list(cuboid[zkeys[0]][ykeys[0]].keys())
    xkeys.sort()
    
    for k in zkeys:
        print("z = {}".format(k))
        map_dict = cuboid[k]
        for ykey in ykeys:
            line_string = ""
            for xkey in xkeys:
                line_string += str(map_dict[ykey][xkey])
            print(line_string)


def count_cuboid(cuboid):
    count = 0
    zkeys = list(cuboid.keys())
    ykeys = list(cuboid[zkeys[0]].keys())
    xkeys = list(cuboid[zkeys[0]][ykeys[0]].keys())
    for zkey in zkeys:
        for ykey in ykeys:
            for xkey in xkeys:
                count += cuboid[zkey][ykey][xkey]
    return count