# aoc.year2021.day23_move_grid

from aoc.year2021.day23_map import build_map

def calculate_steps_from_room(start_room, this_room, visited, steps, path, grid, exit_maps):
    # print("start_room:", start_room, "this_room:", this_room, "visited:", visited, "steps:", steps, "path:", path)
    if this_room in visited:
        return grid
    
    visited.append(this_room)
    exits = exit_maps[this_room]
    for exit in exits:
        if exit in visited:
            continue
        exit_steps = steps + 1
        exit_path = path.copy()
        exit_path.append(exit)
        grid[start_room][exit] = (exit_steps, exit_path)    
        calculate_steps_from_room(start_room, exit, visited, exit_steps, exit_path, grid, exit_maps) 

    return grid


def calculate_move_grid():
    maps = build_map()
    exit_maps = maps[0]
    
    # setup
    grid = {}
    for room_i in exit_maps.keys():
        grid[room_i] = {}
        for room_j in exit_maps.keys():
            grid[room_i][room_j] = (0, [])

    rooms = list(exit_maps.keys())
    for room in rooms: 
        grid = calculate_steps_from_room(room, room, [], 0, [], grid, exit_maps) 
    
    return grid
