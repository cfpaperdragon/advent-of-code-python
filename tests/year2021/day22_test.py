import sys
sys.path.insert(0, '../')

import aoc.common.process_input
import aoc.year2021.day22

def test_process_reboot_steps():
    file = "on x=10..12,y=10..12,z=10..12\noff x=9..11,y=9..11,z=9..11"
    result = aoc.year2021.day22.process_reboot_steps(file)
    expected = "[{'status':'on','x':(10,12),'y':(10,12),'z':(10,12)},{'status':'off','x':(9,11),'y':(9,11),'z':(9,11)}]"
    assert result == eval(expected)

def test_calculate_part1_example1():
    file_content = aoc.common.process_input.read_file("input\\year2021\\day22\\example1.txt")
    result = aoc.year2021.day22.calculate_part1(file_content)
    assert result == 39

def test_calculate_part1_example2():
    result = aoc.year2021.day22.calculate_part1([])
    assert result == 590784