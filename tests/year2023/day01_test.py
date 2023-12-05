import aoc.common.process_input
import aoc.year2023.day01
from ..common_test import read_file

year = "2023"
day = "01"
testname = "example.txt"

def test_calculate_part1():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2023.day01.calculate_part1(input_content)
    assert result == 142

# def test_calculate_part2():


