# aoc.year2022.day08

from aoc.year2022.map import Map2d as Map2d

def load_map(input_list):
    x_size = len(input_list[0])
    y_size = len(input_list)
    map = Map2d(0, x_size-1, 0, y_size-1, 0)
    for y in range(y_size):
        input = input_list[y]
        for x in range(x_size):
            map.set(x, y, 0, int(input[x]))
    return map
    
def check_any_direction(direction, map, vis, x, y, value):
    if direction == 'left':
        lambda_x = lambda a: a-1
        lambda_y = lambda b: b
    elif direction == 'right':
        lambda_x = lambda a: a+1
        lambda_y = lambda b: b
    elif direction == 'up':
        lambda_x = lambda a: a
        lambda_y = lambda b: b-1
    elif direction == 'down':
        lambda_x = lambda a: a
        lambda_y = lambda b: b+1
    else:
        raise Exception("invalid direction: " + direction)

    checked_value = map.get(lambda_x(x), lambda_y(y))
    if checked_value < value:
        if vis.get(lambda_x(x), lambda_y(y)) in ['e']:
            return True
        else:
            return check_any_direction(direction, map, vis, lambda_x(x), lambda_y(y), value)
    return False

def calculate_part1(input_list):
    x_size = len(input_list[0])
    y_size = len(input_list)
    map = load_map(input_list)
    visibility_map = Map2d(0, x_size-1, 0, y_size-1, '.')
    
    # set with edge
    for y in range(y_size):
        for x in range(x_size):
            if x in [0, x_size-1] or y in [0, y_size-1]:
                visibility_map.set(x, y, '.', 'e')

    for y in range(1, y_size - 1):
        for x in range(1, x_size - 1):
            # print(x,y)
            if visibility_map.get(x, y) in ['e','v','h']:
                continue
            else:
                value = map.get(x, y)
                if check_any_direction("left", map, visibility_map, x, y, value):
                    # print("visible on left")
                    visibility_map.set(x, y, '.', 'v')
                    continue
                elif check_any_direction("right", map, visibility_map, x, y, value):
                    # print("visible on right")
                    visibility_map.set(x, y, '.', 'v')
                    continue
                elif check_any_direction("up", map, visibility_map, x, y, value):
                    # print("visible on up")
                    visibility_map.set(x, y, '.', 'v')
                    continue
                elif check_any_direction("down", map, visibility_map, x, y, value):
                    # print("visible on down")
                    visibility_map.set(x, y, '.', 'v')
                    continue
                else:
                    # print("hidden")
                    visibility_map.set(x, y, '.', 'h')

    visibility_map.print_asc()

    count_lambda = lambda x: x in ['e','v']
    result = visibility_map.count(count_lambda)
    return result

def calculate_part2(input_list):
    return 0
