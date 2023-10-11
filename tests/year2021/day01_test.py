import aoc.common.process_input
import aoc.year2021.day01
from ..common_test import read_file

year = "2021"
day = "01"
testname = "example.txt"

def test_calculate_part1():
    input_content = aoc.common.process_input.to_function_list(read_file(year, day, testname), int)
    result = aoc.year2021.day01.calculate_part1(input_content)
    assert result == 7

def test_calculate_part2():
    input_content = aoc.common.process_input.to_function_list(read_file(year, day, testname), int)
    result = aoc.year2021.day01.calculate_part2(input_content)
    assert result == 5
