import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2022.day09
from aoc.year2021.cuboid import Cuboid

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day09\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day09.calculate_part1(input_content)
    map = Cuboid(0, 5, 0, 5, 0, 0, ".")
    map.print()
    assert result == 13

