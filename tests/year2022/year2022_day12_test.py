import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2022.day12

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day12\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day12.calculate_part1(input_content)
    assert result == 31

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day12\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day12.calculate_part2(input_content)
    assert result == 29