import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2021.day23


def test_calculate_part1_example1():
    # file_content = aoc.common.process_input.read_file("input\\year2021\\day23\\example.txt")
    start_positions = []
    start_positions.append(('A2','B'))
    start_positions.append(('A1','A'))
    start_positions.append(('B2','C'))
    start_positions.append(('B1','D'))
    start_positions.append(('C2','B'))
    start_positions.append(('C1','C'))
    start_positions.append(('D2','D'))
    start_positions.append(('D1','A'))
    result = aoc.year2021.day23.calculate_part1(start_positions)
    assert result == 12521