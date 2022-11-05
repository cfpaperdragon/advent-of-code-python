# aoc.year2021.day22
from aoc.year2021.cuboid import Cuboid

def set_and_expand_cuboid(c, min_x, max_x, min_y, max_y, min_z, max_z, state):
    # this is the brute force approach, there may be optimization if approaching one axis at a time
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                c.set_and_expand(x, y, z, 0, state)
    return c

def calculate_part1(input_list):
    first = input_list.pop(0) # get first instruction
    first_state = 1
    if first['status'] == "off":
        first_state = 0
    processor = Cuboid(first['x'][0], first['x'][1], first['y'][0], first['y'][1], first['z'][0], first['z'][1], first_state)
    # processor.print()
    for i in input_list:
        i_state = 1
        if i['status'] == "off":
            i_state = 0
        # check if within the limits
        if i['x'][0] > 50 or i['x'][0] < -50: 
            continue # skip
        processor = set_and_expand_cuboid(processor, i['x'][0], i['x'][1], i['y'][0], i['y'][1], i['z'][0], i['z'][1], i_state)
        # print(i)
        # processor.print()
    result = processor.count_state()
    return result


def calculate_part2(input_list):
    
    return 0
