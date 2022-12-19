# aoc.year2022.day18

def parse_line(line):
    parts = line.split(',')
    x = int(parts[0].strip())
    y = int(parts[1].strip())
    z = int(parts[2].strip())
    return x, y, z

# can join 2 cubes if they share 2 coordinates and are consective in the third coordinate
def join_cube(cubes, c1, c2):
    cube1 = cubes[c1]
    cube2 = cubes[c2]
    can_join = False
    if cube1['x'] == cube2['x'] and cube1['y'] == cube2['y'] and abs(cube1['z'] - cube2['z']) == 1:
        if cube1['z'] > cube2['z']:
            if cube1['lz'] is None and cube2['uz'] is None:
                can_join = True
                connection = (c1, 'lz', c2, 'uz')
                cube1['lz'] = connection
                cube2['uz'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over z')
        else:
            if cube1['uz'] is None and cube2['lz'] is None:
                can_join = True
                connection = (c1, 'uz', c2, 'lz')
                cube1['uz'] = connection
                cube2['lz'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over z')
    elif cube1['y'] == cube2['y'] and cube1['z'] == cube2['z'] and abs(cube1['x'] - cube2['x']) == 1:
        if cube1['x'] > cube2['x']:
            if cube1['lx'] is None and cube2['ux'] is None:
                can_join = True
                connection = (c1, 'lx', c2, 'ux')
                cube1['lx'] = connection
                cube2['ux'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over x')
        else:
            if cube1['ux'] is None and cube2['lx'] is None:
                can_join = True
                connection = (c1, 'ux', c2, 'lx')
                cube1['ux'] = connection
                cube2['lx'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over x')
    elif cube1['z'] == cube2['z'] and cube1['x'] == cube2['x'] and abs(cube1['y'] - cube2['y']) == 1:
        if cube1['y'] > cube2['y']:
            if cube1['ly'] is None and cube2['uy'] is None:
                can_join = True
                connection = (c1, 'ly', c2, 'uy')
                cube1['ly'] = connection
                cube2['uy'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over y')
        else:
            if cube1['uy'] is None and cube2['ly'] is None:
                can_join = True
                connection = (c1, 'uy', c2, 'ly')
                cube1['uy'] = connection
                cube2['ly'] = connection
            else:
                print('cannot join', c1, 'and', c2, 'over y')
    # print("cube1", cube1)
    # print("cube2", cube2)
    # print("can_join", can_join)
    return can_join

def calculate_part1(input_list):
    # 1 cube
    # x, y, z e.g. 1,1,1
    # it has 6 sides
    # upper_x, lower_x
    # upper_y, lower_y
    # upper_z, lower_z

    # 1 = Cube(1,1,1)
    # 2 = Cube(2,1,1)
    # 1's upper_x side is connected to 2's lower_x side

    cubes = {}
    cube_counter = 0

    # a connection is a tuple (cube1_index, cube1_side, cube2_index, cube2_side)
    cube1_index = 0
    cube1_side = 1
    cube2_index = 2
    cube2_side = 3

    cube_list = []

    for line in input_list:
        x, y, z = parse_line(line)

        cube = {}
        cube['x'] = x
        cube['y'] = y
        cube['z'] = z
        cube['ux'] = None
        cube['lx'] = None
        cube['uy'] = None
        cube['ly'] = None
        cube['uz'] = None
        cube['lz'] = None

        cubes[cube_counter] = cube
        cube_list.append(cube_counter)

        cube_counter += 1

    connected_cubes = []
    first_cube = cube_list.pop(0)
    connected_cubes.append(first_cube)

    while len(cube_list) > 0:
        # print("list", cube_list)
        # print("connected", connected_cubes)
        cube_to_connect = cube_list.pop(0)
        for cube in connected_cubes:
            result = join_cube(cubes, cube, cube_to_connect)
            # print(cube_to_connect, "connects to", cube, result)
        connected_cubes.append(cube_to_connect)

    count_empty_sides = 0
    for key in cubes:
        if cubes[key]['ux'] is None:
            count_empty_sides += 1
        if cubes[key]['lx'] is None:
            count_empty_sides += 1
        if cubes[key]['uy'] is None:
            count_empty_sides += 1
        if cubes[key]['ly'] is None:
            count_empty_sides += 1
        if cubes[key]['uz'] is None:
            count_empty_sides += 1
        if cubes[key]['lz'] is None:
            count_empty_sides += 1
            
    return count_empty_sides
    

def calculate_part2(input_list):
    return 0