# aoc.year2021.day23

from aoc.year2021.day23_map import build_map
from aoc.year2021.day23_move_grid import calculate_move_grid

def prepare_game(start_positions):
    maps = build_map()
    exit_maps = maps[0]
    content_map = maps[1]
    amphipods = {}
    amphipods['A'] = []
    amphipods['B'] = []
    amphipods['C'] = []
    amphipods['D'] = []

    for sp in start_positions:
        content_map[sp[0]] = sp[1]
        amphipods[sp[1]] = sp[0]
    return content_map, amphipods

def is_end_state(content_map):
    return content_map['A1'] == 'A' and content_map['A2'] == 'A' and \
        content_map['B1'] == 'B' and content_map['B2'] == 'B' and \
        content_map['C1'] == 'C' and content_map['C2'] == 'C' and \
        content_map['D1'] == 'D' and content_map['D2'] == 'D'


def calculate_part1(start_positions):
    content_map, amphipods = prepare_game(start_positions)


    return 0


def calculate_part2(input_list):
    return 0