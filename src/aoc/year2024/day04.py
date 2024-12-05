# aoc.year2024.day04
from aoc.year2024.grid import Grid2d as Grid2d

def process_input_list(input_list):
    len_x = len(input_list[0].strip())
    len_y = len(input_list)
    word_search = Grid2d(input_list, len_x, len_y)
    return word_search


def calculate_part1(input_list):
    word_search = process_input_list(input_list)
    return 0


def calculate_part2(input_list):  
    return 0
