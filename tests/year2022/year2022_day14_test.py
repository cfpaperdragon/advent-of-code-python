import aoc.common.process_input
import aoc.year2022.day14

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day14\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day14.calculate_part1(input_content)
    assert result == 24

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day14\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day14.calculate_part2(input_content)
    assert result == 93
