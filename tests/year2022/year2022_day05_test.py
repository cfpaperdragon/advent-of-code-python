import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2022.day05

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day05\\example.txt")      
    input_content = aoc.common.process_input.to_str_list_no_strip(fileContent)
    print(input_content)
    result = aoc.year2022.day05.calculate_part1(input_content)
    assert result == 'CMZ'

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day05\\example.txt")      
    input_content = aoc.common.process_input.to_str_list_no_strip(fileContent)
    print(input_content)
    result = aoc.year2022.day05.calculate_part2(input_content)
    assert result == 'MCD'