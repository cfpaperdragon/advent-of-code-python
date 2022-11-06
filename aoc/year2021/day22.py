# aoc.year2021.day22
from aoc.year2021.cuboidv2 import Cuboid
from aoc.year2021.cuboidv2 import cuboid_intersect

def calculate_part1(input_list):
    first = input_list.pop(0) # get first instruction
    first_state = 1
    if first['status'] == "off":
        first_state = 0
    c = Cuboid(first['x'][0], first['x'][1], first['y'][0], first['y'][1], first['z'][0], first['z'][1], first_state)

    for i in input_list:
        i_state = 1
        if i['status'] == "off":
            i_state = 0
        # check if within the limits
        if i['x'][0] > 50 or i['x'][0] < -50: 
            continue # skip
        i_cuboid = Cuboid(i['x'][0], i['x'][1], i['y'][0], i['y'][1], i['z'][0], i['z'][1], i_state)
        intersect_result = cuboid_intersect(c, i_cuboid)
        i_cuboid.print()
        print(intersect_result)    
    
    return 0


def calculate_part2(input_list):
    
    return 0
