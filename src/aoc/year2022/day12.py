# aoc.year2022.day12
from aoc.year2022.map import Map2d as Map2d

def load_map(input_list, function_value):
    x_size = len(input_list[0])
    y_size = len(input_list)
    map = Map2d(0, x_size-1, 0, y_size-1, 0)
    for y in range(y_size):
        input = input_list[y]
        for x in range(x_size):
            map.set(x, y, 0, function_value(input[x]))
    return map

def get_adjacents(point, max_x, max_y):
    adjacents = []
    x = point[0]
    y = point[1]
    # left
    if x != 0:
        adjacents.append((x-1, y))
    # right
    if x != max_x:
        adjacents.append((x+1, y))
    # up
    if y != 0:
        adjacents.append((x, y-1))
    # down
    if y != max_y:
        adjacents.append((x, y+1))
    return adjacents

def find_shorter_path(mountain_map, start_position, end_position, size_x, size_y):
    
    count_steps = Map2d(0, size_x -1, 0, size_y -1, -1)
    count_steps.set(start_position[0], start_position[1], -1, 0)

    nodes = [start_position]
    while len(nodes) > 0:
        # print(nodes)
        current = nodes.pop(0)
        
        steps_value = count_steps.get(current[0], current[1])
        letter = mountain_map.get(current[0], current[1])

        # check adjacents
        adjacents = get_adjacents(current, size_x -1, size_y -1)
        # print(current, adjacents)
        for adj in adjacents:
            adj_letter = mountain_map.get(adj[0], adj[1])
            # print(adj, adj_letter)
            if ord(adj_letter) - ord(letter) > 1: # not same letter or one above
                continue

            adj_value = count_steps.get(adj[0], adj[1])
            # print(adj, adj_value)
            if adj_value == -1:
                # not visited yet
                nodes.append(adj)
                count_steps.set(adj[0], adj[1], -1, 1 + steps_value)

            elif adj_value > steps_value + 1:
                # visited but from another path
                # visit again?
                nodes.append(adj)
                count_steps.set(adj[0], adj[1], -1, 1 + steps_value)

            # else: 
                # visited from another path but shorter
                # do nothing

    # count_steps.print_asc()
    
    return count_steps.get(end_position[0],end_position[1])

def calculate_part1(input_list):
    mountain_map = load_map(input_list, str)
   
    size_x = len(input_list[0])
    size_y = len(input_list)

    start = mountain_map.find_in_map(lambda a: a == 'S')
    end = mountain_map.find_in_map(lambda a: a == 'E')

    mountain_map.set(start[0],start[1], '', 'a')
    mountain_map.set(end[0],end[1], '', 'z')
    
    return find_shorter_path(mountain_map, start, end, size_x, size_y)

def calculate_part2(input_list):
    mountain_map = load_map(input_list, str)
   
    size_x = len(input_list[0])
    size_y = len(input_list)

    start = mountain_map.find_in_map(lambda a: a == 'S')
    end = mountain_map.find_in_map(lambda a: a == 'E')

    mountain_map.set(start[0],start[1], '', 'a')
    mountain_map.set(end[0],end[1], '', 'z')

    start_list = mountain_map.find_all_in_map(lambda a: a == 'a')
    results = {}
    for start_pos in start_list:
        result = find_shorter_path(mountain_map, start_pos, end, size_x, size_y)
        # print(start_pos, result)
        if result != -1:
            results[start_pos] = result

    shortest_paths = list(results.values())
    shortest_paths.sort()
    the_shortest = shortest_paths[0]
    return the_shortest

