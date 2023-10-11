import aoc.common.process_input
import aoc.year2021.day01
import ..day01_test

year = "2021"
day = "01"
testname = "example.txt"

def read_file():
    filename = aoc.common.process_input.get_filename(f"../input/year{year}/day{day}/{testname}")
    file_content = aoc.common.process_input.read_file(filename)        
    return file_content

def test_calculate_part1():
    input_content = aoc.common.process_input.to_function_list(read_file(), int)
    result = aoc.year2021.day01.calculate_part1(input_content)
    assert result == 7

def test_calculate_part2():
    input_content = aoc.common.process_input.to_function_list(read_file(), int)
    result = aoc.year2021.day01.calculate_part2(input_content)
    assert result == 5
