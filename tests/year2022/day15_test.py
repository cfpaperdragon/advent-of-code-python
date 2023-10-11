import aoc.common.process_input
import aoc.year2022.day15
from ..common_test import read_file

year = "2022"
day = "15"
testname = "example.txt"


def test_calculate_part1():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day15.calculate_part1(input_content, 10)
    assert result == 26

