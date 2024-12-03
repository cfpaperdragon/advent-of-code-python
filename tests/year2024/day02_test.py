import aoc.common.process_input
import aoc.year2024.day01
import aoc.year2024.day02
from ..common_test import read_file

year = "2024"
day = "02"
testname = "example.txt"

def test_calculate_part1():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day02.calculate_part1(input_content)
    assert result == 2


def test_is_report_safe():
    result = aoc.year2024.day02.is_report_safe([7, 6, 4, 2, 1])
    assert result
    result = aoc.year2024.day02.is_report_safe([1, 2, 7, 8, 9])
    assert not result


def test_read_input():
    fileContent = read_file(year, day, "input.txt") 
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day02.calculate_part1(input_content)
    assert result != 1

def test_calculate_part2():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2024.day02.calculate_part2(input_content)
    assert result != 1


