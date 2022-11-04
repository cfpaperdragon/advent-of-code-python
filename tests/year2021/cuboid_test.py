import sys
sys.path.insert(0, '../')

import aoc.year2021.cuboid

def test_create_cuboid():
    new_cuboid = aoc.year2021.cuboid.create_cuboid(1, 3, 1, 3, 1, 3, 1)
    # aoc.year2021.cuboid.print_cuboid(new_cuboid)
    result = aoc.year2021.cuboid.count_cuboid(new_cuboid)
    assert result == 27