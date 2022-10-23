import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2021.day01

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2021\\day01\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, int)
    result = aoc.year2021.day01.calculate_part1(input_content)
    assert result == 7

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2021\\day01\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, int)
    result = aoc.year2021.day01.calculate_part2(input_content)
    assert result == 5
