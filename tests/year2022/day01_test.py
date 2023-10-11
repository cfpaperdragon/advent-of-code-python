import aoc.common.process_input
import aoc.year2022.day01
from ..common_test import read_file

year = "2022"
day = "01"
testname = "example.txt"

def test_calculate_part1():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day01.calculate_part1(input_content)
    assert result == 24000

def test_calculate_part2():
    fileContent = read_file(year, day, testname)
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day01.calculate_part2(input_content)
    assert result == 45000

