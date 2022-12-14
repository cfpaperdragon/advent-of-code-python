# aoc.year2022.day14

from aoc.year2022.map import Map2d as Map2d

# parse input
# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
def parse_input(input_list):
    count = 1
    rocks_dict = {}
    for input in input_list:
        rocks_dict[count] = []
        points = input.strip().split(" -> ")
        for point in points:
            coordenates = point.strip().split(',')
            actual_point = (int(coordenates[0]), int(coordenates[1]))
            rocks_dict[count].append(actual_point)
        count += 1
    return rocks_dict

def move_grain_of_sand(grid, min_x, max_x, max_y, sand_source):
    x = sand_source[0]
    y = sand_source[1]

    found_rest_position = False

    while (x > min_x and x < max_x and y < max_y):
        # print(x, y)
        # down one step
        if grid.get(x, y+1) == '.':
            # print("down")
            y += 1
        # one step down and to the left
        elif grid.get(x-1, y+1) == '.':
            # print("down + left")
            y += 1
            x -= 1
        # one step down and to the right
        elif grid.get(x+1, y+1) == '.':
            # print("down + right")
            y += 1
            x += 1
        else: # can't move any longer
            # print("rest")
            found_rest_position = True
            grid.set(x, y, '.', 'o')
            break

    return found_rest_position

def find_min_and_max(rocks_dict):

    min_x = 9000
    max_x = 0
    min_y = 0
    max_y = 0

    for key in rocks_dict.keys():
        points = rocks_dict[key]
        points_x = [a[0] for a in points]
        points_y = [a[1] for a in points]
        min_x = min(min_x, min(points_x))
        max_x = max(max_x, max(points_x))
        max_y = max(max_y, max(points_y))

    return min_x, max_x, min_y, max_y

def fill_grid_with_rocks(grid, rocks_dict):
    for key in rocks_dict.keys():
        points = rocks_dict[key]
        for i in range(1, len(points)):
            # draw the rock line from i-1 to i
            source = points[i-1]
            target = points[i]
            if source[0] == target[0]: # y changes, draw vertical line 
                for j in range(min(source[1], target[1]), max(source[1], target[1])+1):
                    grid.set(source[0], j, '.', '#')
            else: # x changes, draw horizontal line
                for j in range(min(source[0], target[0]), max(source[0], target[0])+1):
                    grid.set(j, source[1], '.', '#')

def calculate_part1(input_list):

    rocks_dict = parse_input(input_list)

    min_x, max_x, min_y, max_y = find_min_and_max(rocks_dict)

    grid = Map2d(min_x-1, max_x+1, min_y-1, max_y+1, '.')
    
    fill_grid_with_rocks(grid, rocks_dict)

    sand_source = (500,0)
    count_sand = 0

    found_rest_position = True

    while found_rest_position:
        found_rest_position = move_grain_of_sand(grid, min_x, max_x, max_y, sand_source)
        if found_rest_position:
            count_sand += 1

    # grid.print_asc()
    # print(count_sand)
    return count_sand

def move_grain_of_sand_part2(grid, sand_source):
    x = sand_source[0]
    y = sand_source[1]

    # min_x, max_x can shift
    keys = grid.map.get_keys('all', True)
    min_x = keys[0][0]
    max_x = keys[0][-1]
    # max_y is fixed
    max_y = keys[1][-1]

    while (True):
        if x == min_x:
            min_x -= 1
            # expand grid to x-1
            grid.set(min_x , max_y, '.', '#')
        elif x == max_x:
            max_x += 1
            # expand grid to x+1
            grid.set(max_x , max_y, '.', '#')
        
        # down one step
        if grid.get(x, y+1) == '.':
            # print("down")
            y += 1
        # one step down and to the left
        elif grid.get(x-1, y+1) == '.':
            # print("down + left")
            y += 1
            x -= 1
        # one step down and to the right
        elif grid.get(x+1, y+1) == '.':
            # print("down + right")
            y += 1
            x += 1
        else: # can't move any longer
            # print("rest")
            found_rest_position = True
            grid.set(x, y, '.', 'o')
            break

    return (x, y)

def calculate_part2(input_list):

    rocks_dict = parse_input(input_list)
    min_x, max_x, min_y, max_y = find_min_and_max(rocks_dict)
    grid = Map2d(min_x-1, max_x+1, min_y-1, max_y+1, '.')
    fill_grid_with_rocks(grid, rocks_dict)
    grid.set(max_x, max_y+2, '#', '#')

    sand_source = (500,0)
    count_sand = 0

    while True:
        last_sand_position = move_grain_of_sand_part2(grid, sand_source)
        count_sand += 1
        if last_sand_position == sand_source:
            break

    return count_sand
