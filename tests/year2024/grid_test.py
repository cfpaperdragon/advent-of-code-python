
import aoc.common.process_input
from aoc.year2024.grid import Grid2d as Grid2d
from ..common_test import read_file

year = "2024"
day = "04"
testname = "example.txt"

def test_something():
    assert 0 == aoc.year2024.grid.this_is_a_method()

def test_grid_create():
    fileContent = read_file(year, day, testname)        
    input_content = aoc.common.process_input.to_function_list(fileContent, str)
    grid = Grid2d(input_content, len(input_content[0].strip()), len(input_content))
    pos_0_0 = grid.get(0, 0)
    pos_0_9 = grid.get(0, 9)
    pos_9_0 = grid.get(9, 0)
    pos_9_9 = grid.get(9, 9)
    pos_10_10 = grid.get(10, 10)
    assert "M" == pos_0_0
    assert "M"  == pos_0_9
    assert "M"  == pos_9_0
    assert "X"  == pos_9_9
    assert "."  == pos_10_10

