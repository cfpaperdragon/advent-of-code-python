import aoc.common.process_input
import aoc.year2022.day04


def test_check_contains():
    pair1 = (2, 4)
    pair2 = (6, 8)
    result = aoc.year2022.day04.check_contains(pair1, pair2)
    assert not result # doesn't contain 
    pair1 = (2, 8)
    pair2 = (3, 7)
    result = aoc.year2022.day04.check_contains(pair1, pair2)
    assert result # contain 
    pair1 = (2, 8)
    pair2 = (3, 7)
    result = aoc.year2022.day04.check_contains(pair2, pair1)
    assert not result # doesn't contain 

def test_check_overlaps():
    pair1 = (2, 4)
    pair2 = (6, 8)
    result = aoc.year2022.day04.check_overlap(pair1, pair2)
    assert not result # doesn't
    pair1 = (2, 8)
    pair2 = (3, 7)
    result = aoc.year2022.day04.check_overlap(pair1, pair2)
    assert result # overlap 
    result = aoc.year2022.day04.check_overlap(pair2, pair1)
    assert not result # overlap  
    pair1 = (5, 7)
    pair2 = (7, 9)
    result = aoc.year2022.day04.check_overlap(pair1, pair2)
    assert result # overlap 
    result = aoc.year2022.day04.check_overlap(pair2, pair1)
    assert result # overlap 

def test_calculate_part1():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day04\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day04.calculate_part1(input_content)
    assert result == 2

def test_calculate_part2():
    fileContent = aoc.common.process_input.read_file("input\\year2022\\day04\\example.txt")        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    result = aoc.year2022.day04.calculate_part2(input_content)
    assert result == 4

