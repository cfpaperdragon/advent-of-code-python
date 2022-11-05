import sys
sys.path.insert(0, '../')

from aoc.year2021.cuboid import Cuboid

def test_create():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    result = new_cuboid.count_state()
    assert result == 27

def test_get_valid():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    result = new_cuboid.get(1, 1, 1)
    assert result == 1

def test_get_invalid():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    result = new_cuboid.get(0, 1, 1)
    assert result == 0

def test_get_keys():
    new_cuboid = Cuboid(1, 2, 3, 4, 5, 6, 1)
    result_x = new_cuboid.get_keys('x', True)
    assert result_x == [[1, 2]]
    result_y = new_cuboid.get_keys('y', True)
    assert result_y == [[3, 4]]
    result_z = new_cuboid.get_keys('z', True)
    assert result_z == [[5, 6]]
    result_all = new_cuboid.get_keys('all', True)
    assert result_all == [[1, 2], [3, 4], [5, 6]]

def test_expand_z():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    new_cuboid.extend_z(4, 1)
    result = max(new_cuboid.get_keys('z', False)[0])
    assert result == 4
    new_cuboid.extend_z(0, 1)
    result = min(new_cuboid.get_keys('z', False)[0])
    assert result == 0

def test_expand_y():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    new_cuboid.extend_y(4, 1)
    result = max(new_cuboid.get_keys('y', False)[0])
    assert result == 4
    new_cuboid.extend_y(0, 1)
    result = min(new_cuboid.get_keys('y', False)[0])
    assert result == 0

def test_expand_x():
    new_cuboid = Cuboid(1, 3, 1, 3, 1, 3, 1)
    new_cuboid.extend_x(4, 1)
    result = max(new_cuboid.get_keys('x', False)[0])
    assert result == 4
    new_cuboid.extend_x(0, 1)
    result = min(new_cuboid.get_keys('x', False)[0])
    assert result == 0

def test_set_and_expand():
    new_cuboid = Cuboid(1, 2, 1, 2, 1, 2, 0)
    new_cuboid.set_and_expand(3, 3, 3, 0, 1)
    result = new_cuboid.count_state()
    assert result == 1
    