# aoc.year2024.day06
from aoc.year2024.grid import Grid2d as Grid2d

def process_input_list(input_list):
    len_x = len(input_list[0].strip())
    len_y = len(input_list)
    map = Grid2d(input_list, len_x, len_y, find_character = True, character = "^")
    return map


def map_mark_position(map, x, y, character):
    map.set(x, y, character)


def is_position_out_of_map(map, x, y):
    return x < map.min_x or x > map.max_x or y < map.min_y or y > map.max_y


def map_calculate_next_position(map, x, y, direction):
    if direction == UP:
        new_x = x
        new_y = y - 1
    elif direction == RIGHT:
        new_x = x + 1
        new_y = y
    elif direction == DOWN:
        new_x = x
        new_y = y + 1
    elif direction == LEFT:
        new_x = x - 1
        new_y = y
    else:
        raise Exception("Invalid direction!")
    return (new_x, new_y)


UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def next_direction(direction):
    index = DIRECTIONS.index(direction)
    next_index = (index + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_index]


def calculate_patrol(map, start_x, start_y, start_direction):
    x = start_x
    y = start_y
    direction = start_direction
    map_mark_position(map, x, y, "X")
    while not is_position_out_of_map(map, x, y):
        next_x, next_y = map_calculate_next_position(map, x, y, direction)
        if is_position_out_of_map(map, next_x, next_y):
            break
        map_value  = map.get(next_x, next_y)
        if map_value == "#": # obstacle
            direction = next_direction(direction)
            continue
        x = next_x
        y = next_y
        map_mark_position(map, x, y, "X")
    return map


def calculate_part1(input_list):
    X = 0
    Y = 1
    map = process_input_list(input_list)
    start_pos = map.character_pos
    map = calculate_patrol(map, start_pos[X], start_pos[Y], UP)
    visited = map.count_value("X")
    return visited


def calculate_part2(input_list):  
    return 0
