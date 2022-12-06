import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2022.day06

def test_calculate_part1():
    input_content = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']
    result = aoc.year2022.day06.calculate_part1(input_content)
    assert result == 7

    input_content = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    result = aoc.year2022.day06.calculate_part1(input_content)
    assert result == 5

    input_content = ['nppdvjthqldpwncqszvftbrmjlhg']
    result = aoc.year2022.day06.calculate_part1(input_content)
    assert result == 6

    input_content = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
    result = aoc.year2022.day06.calculate_part1(input_content)
    assert result == 10

    input_content = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
    result = aoc.year2022.day06.calculate_part1(input_content)
    assert result == 11

def test_calculate_part2():
    input_content = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb']
    result = aoc.year2022.day06.calculate_part2(input_content)
    assert result == 19

    input_content = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    result = aoc.year2022.day06.calculate_part2(input_content)
    assert result == 23

    input_content = ['nppdvjthqldpwncqszvftbrmjlhg']
    result = aoc.year2022.day06.calculate_part2(input_content)
    assert result == 23

    input_content = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
    result = aoc.year2022.day06.calculate_part2(input_content)
    assert result == 29

    input_content = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
    result = aoc.year2022.day06.calculate_part2(input_content)
    assert result == 26
