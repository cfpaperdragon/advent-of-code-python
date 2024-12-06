import aoc.common.process_input
import aoc.year2024.day06
from ..common_test import read_file

year = "2024"
day = "06"
testname = "example.txt"

def test_calculate_part1():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day06.calculate_part1(input_content)
    assert result == 41

def test_read_input():
    fileContent = read_file(year, day, "input.txt") 
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day06.calculate_part1(input_content)
    assert result != 1

def test_calculate_part2():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day06.calculate_part2(input_content)
    assert result == 0
