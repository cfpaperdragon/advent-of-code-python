# aoc.year2021.day23_move_grid

from aoc.year2021.day23_map import build_map

def calculate_move_grid():
    maps = build_map()
    exit_maps = maps[0]
    
    # setup
    grid = {}
    for room_i in exit_maps.keys():
        grid[room_i] = {}
        for room_j in exit_maps.keys():
            grid[room_i][room_j] = (0, [])
    
    return grid

def build_move_grid():
    grid = {}

    grid['H1'] = {}
    grid['H1']['H1'] = (0, [])
    grid['H1']['H2'] = (1, ['H2'])
    grid['H1']['HA'] = (2, ['H2', 'HA'])
    grid['H1']['H3'] = (3, ['H2', 'HA', 'H3'])
    grid['H1']['HB'] = (4, ['H2', 'HA', 'H3', 'HB'])
    grid['H1']['H4'] = (5, ['H2', 'HA', 'H3', 'HB', 'H4'])
    grid['H1']['HC'] = (6, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC'])
    grid['H1']['H5'] = (7, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5'])
    grid['H1']['HD'] = (8, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD'])
    grid['H1']['H6'] = (9, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'H6'])
    grid['H1']['H7'] = (10, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'H6', 'H7'])
    grid['H1']['A2'] = (3, ['H2', 'HA', 'A2'])
    grid['H1']['A1'] = (4, ['H2', 'HA', 'A2', 'A1'])
    grid['H1']['B2'] = (5, ['H2', 'HA', 'H3', 'HB', 'B2'])
    grid['H1']['B1'] = (6, ['H2', 'HA', 'H3', 'HB', 'B2', 'B1'])
    grid['H1']['C2'] = (7, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'C2'])
    grid['H1']['C1'] = (8, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'C2', 'C1'])
    grid['H1']['D2'] = (9, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'D2'])
    grid['H1']['D1'] = (10, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'D2', 'D1'])

    # does it make sense to build this by hand or just program it? maybe programming will be faster?
    # I think programming it will be faster.

    return grid
