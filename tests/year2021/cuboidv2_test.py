import sys
sys.path.insert(0, '../')

from aoc.year2021.cuboidv2 import Cuboid
from aoc.year2021.cuboidv2 import cuboid_intersect
from aoc.year2021.cuboidv2 import cuboid_intersect_and_split

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


def test_split_cuboid():
    c = Cuboid(0, 2, 0, 2, 0, 2, 1)
    # split over x=1
    result = c.split('x', 1)
    assert len(result) == 2
    assert result[0].max_x == 1
    assert result[1].min_x == 2
    # split over y=1
    result = c.split('y', 1)
    assert len(result) == 2
    assert result[0].max_y == 1
    assert result[1].min_y == 2
    # split over z=1
    result = c.split('z', 1)
    assert len(result) == 2
    assert result[0].max_z == 1
    assert result[1].min_z == 2


def test_intersect_and_split():
    c1 = Cuboid(0, 2, 0, 2, 0, 2, 1)
    c2 = Cuboid(1, 3, 1, 3, 1, 3, 1)
    # keep c1 the same, chop up c2 and return the parts don't intersect
    
    cuboid_final_list = [c1]

    result = cuboid_intersect(c1, c2)
    next_split = []
    print(result)
    if len(result['x']) == 1:
        # means that in the x axis, c2 is partially inside c1
        # i want to split c2 by the value closer to the edge outside c1
        x_value = result['x'][0]
        if x_value == c2.min_x:
            x_value_to_split = c1.max_x
        else:
            x_value_to_split = c1.min_x

        split_result = c2.split('x', x_value_to_split)    
        next_split = []
        for c in split_result:
            intersect = cuboid_intersect(c1, c)
            if len(intersect) == 3:
                y_value = result['y'][0]
                if y_value == c.min_x:
                    y_value_to_split = c1.max_y
                else:
                    y_value_to_split = c1.min_y
                split_result_y = c.split('y', y_value_to_split)
                for c_y in split_result_y:
                    intersect = cuboid_intersect(c1, c_y)
                    if len(intersect) == 3:
                        z_value = result['z'][0]
                        if z_value == c.min_z:
                            z_value_to_split = c1.max_z
                        else:
                            z_value_to_split = c1.min_z
                        split_result_z = c.split('z', z_value_to_split)
                        for c_z in split_result_z:
                            intersect = cuboid_intersect(c1, c_z)
                            if len(intersect) != 3:
                                cuboid_final_list.append(c_z)
                    else:
                        cuboid_final_list.append(c_y)
            else:
                cuboid_final_list.append(c)
    for c in cuboid_final_list:
        c.print()
    assert len(cuboid_final_list) == 4