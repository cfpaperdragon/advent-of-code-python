import sys
sys.path.insert(0, '../')

import aoc.common.process_input
from aoc.year2021.day23_map import build_map


def test_build_map():
    map = build_map()
    exit_map = map[0]
    room_content = map[1]
    assert len(exit_map.keys()) == 19
    assert len(room_content.keys()) == 19
    assert len(exit_map['HA']) == 3
    assert room_content['A1'] == "."