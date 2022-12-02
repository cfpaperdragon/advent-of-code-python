import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2022.day02

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day02\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    # print(input_content)
    result = aoc.year2022.day02.calculate_part1(input_content)
    assert result == 15

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day02\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    # print(input_content)
    result = aoc.year2022.day02.calculate_part2(input_content)
    assert result == 12