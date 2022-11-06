import sys
sys.path.insert(0, '../')

from aoc.year2021.cuboidv2 import Cuboid
from aoc.year2021.cuboidv2 import cuboid_intersect

def test_create():
    new_cuboid = Cuboid(1, 2, 3, 4, 5, 6, 1)
    assert new_cuboid.min_x == 1
    assert new_cuboid.max_x == 2
    assert new_cuboid.min_y == 3
    assert new_cuboid.max_y == 4
    assert new_cuboid.min_z == 5
    assert new_cuboid.max_z == 6
    assert new_cuboid.state == 1

def test_count_state():
    c = Cuboid(1, 3, 1, 3, 1, 3, 1)
    result = c.count_state()
    assert result == 27

# different ways to intersect:
# ???
# if cuboid intersect on only one axis - they share an edge (a bit of an edge)
# -> in this case, I should only count the edge once | or remove the edge from one of them
# if cuboid intersect on two axis - they share a surface (a bit of a surface)
# -> in this case, I should only cound the shared surface once | or reduce one so that the surface doesn't share anymore
# if cuboid intersect on three axis
# - one cuboid is partly inside the other, depending on the state, I should ignore or negate the shared space
# - one cuboid is completely inside the other, depending on the state, I should ignore or negate the space
# spliting the cuboids so that there is no shared spaces seems good

def test_intersect():
    # intersect on x
    c1 = Cuboid(0, 1, 0, 1, 0, 1, 1)
    c2 = Cuboid(0, 2, 2, 3, 2, 3, 1)
    result = cuboid_intersect(c1, c2)
    assert len(result) == 1 and 'x' in result
    c3 = Cuboid(2, 3, 2, 0, 2, 3, 1)
    result = cuboid_intersect(c1, c3)
    assert len(result) == 1 and 'y' in result
    c4 = Cuboid(2, 3, 2, 3, 0, 3, 1)
    result = cuboid_intersect(c1, c4)
    assert len(result) == 1 and 'z' in result
    c5 = Cuboid(0, 2, 0, 2, 0, 2, 1)
    result = cuboid_intersect(c1, c5)
    assert len(result) == 3