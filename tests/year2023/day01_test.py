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

# replacing may not be the way
def test_replace_string_with_digit():
    input_str = "two1nine"
    result = aoc.year2023.day01.replace_string_with_digit(input_str)
    assert result == "219"
    input_str = "xtwone3four"
    result = aoc.year2023.day01.replace_string_with_digit(input_str)
    assert result == "x234"

def test_calculate_part2():
    fileContent = read_file(year, day, "example2.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2023.day01.calculate_part2(input_content)
    assert result == 281

