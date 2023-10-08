import aoc.common.process_input
import aoc.year2022.day08

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day08\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day08.calculate_part1(input_content)
    assert result == 21

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day08\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day08.calculate_part2(input_content)
    assert result == 8
