import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2021.day23


def test_calculate_part1_example1():
    file_content = aoc.common.process_input.read_file("input\\year2021\\day23\\example.txt")
    input_list = []
    result = aoc.year2021.day23.calculate_part1(input_list)
    assert result == 39