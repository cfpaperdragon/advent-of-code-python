import aoc.common.process_input
import aoc.year2022.day05

from ..common_test import read_file

year = "2022"
day = "05"
testname = "example.txt"


def test_calculate_part1():
    fileContent = read_file(year, day, testname)      
    input_content = aoc.common.process_input.to_str_list_no_strip(fileContent)
    print(input_content)
    result = aoc.year2022.day05.calculate_part1(input_content)
    assert result == 'CMZ'

def test_calculate_part2():
    fileContent = read_file(year, day, testname)      
    input_content = aoc.common.process_input.to_str_list_no_strip(fileContent)
    print(input_content)
    result = aoc.year2022.day05.calculate_part2(input_content)
    assert result == 'MCD'