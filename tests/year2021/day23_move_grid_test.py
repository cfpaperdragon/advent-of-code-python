import sys
sys.path.insert(0, '../')

from aoc.year2021.day23_move_grid import calculate_move_grid

def test_calculate_move_grid():
    grid = calculate_move_grid()
    assert grid['H1']['H1'] == (0, [])
    assert grid['H1']['H7'] == (10, ['H2', 'HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'H6', 'H7'])
    assert grid['H2']['H2'] == (0, [])
    assert grid['H2']['H7'] == (9, ['HA', 'H3', 'HB', 'H4', 'HC', 'H5', 'HD', 'H6', 'H7'])
    assert grid['H3']['H3'] == (0, [])
    assert grid['H3']['H7'] == (7, ['HB', 'H4', 'HC', 'H5', 'HD', 'H6', 'H7'])