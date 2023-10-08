import aoc.common.process_input
import aoc.year2021.day22
import pytest

def test_process_reboot_steps():
    file = "on x=10..12,y=10..12,z=10..12\noff x=9..11,y=9..11,z=9..11"
    result = aoc.common.process_input.to_function_list(file, aoc.common.process_input.process_reboot_steps_line)
    expected = "[{'status':'on','x':(10,12),'y':(10,12),'z':(10,12)},{'status':'off','x':(9,11),'y':(9,11),'z':(9,11)}]"
    assert result == eval(expected)

def test_process_input_example1():
    file_content = aoc.common.process_input.read_file("input\\year2021\\day22\\example1.txt")
    input_list = aoc.common.process_input.to_function_list(file_content, aoc.common.process_input.process_reboot_steps_line)
    result = len(input_list)
    assert result == 4

def test_calculate_part1_example1():
    file_content = aoc.common.process_input.read_file("input\\year2021\\day22\\example1.txt")
    input_list = aoc.common.process_input.to_function_list(file_content, aoc.common.process_input.process_reboot_steps_line)
    result = aoc.year2021.day22.calculate_part1(input_list)
    assert result == 39

@pytest.mark.skip("Current version is too slow")
def test_calculate_part1_example2():
    file_content = aoc.common.process_input.read_file("input\\year2021\\day22\\example2.txt")
    input_list = aoc.common.process_input.to_function_list(file_content, aoc.common.process_input.process_reboot_steps_line)
    result = aoc.year2021.day22.calculate_part1(input_list)
    assert result == 590784