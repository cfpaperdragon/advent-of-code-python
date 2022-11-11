# aoc.year2021.day23_map

def build_map():
    exit_map = {}
    room_content = {}
    # H1
    exit_map['H1'] = ['H2']
    room_content['H1'] = "."
    # H2
    exit_map['H2'] = ['H1','HA']
    room_content['H2'] = "."
    # HA
    exit_map['HA'] = ['H2','H3','A2']
    room_content['HA'] = "."
    # H3
    exit_map['H3'] = ['HA','HB']
    room_content['H3'] = "."
    # HB
    exit_map['HB'] = ['H3','H4','B2']
    room_content['HB'] = "."
    # H4
    exit_map['H4'] = ['HC','HB']
    room_content['H4'] = "."
    # HC
    exit_map['HC'] = ['H4','H5','C2']
    room_content['HC'] = "."
    # H5
    exit_map['H5'] = ['HC','HD']
    room_content['H5'] = "."
    # HD
    exit_map['HD'] = ['H6','H5','D2']
    room_content['HD'] = "."
    # H6
    exit_map['H6'] = ['HD','H7']
    room_content['H6'] = "."
    # H7
    exit_map['H7'] = ['H6']
    room_content['H7'] = "."
    # A2
    exit_map['A2'] = ['A1','HA']
    room_content['A2'] = "."
    # A1
    exit_map['A1'] = ['A2']
    room_content['A1'] = "."
   # B2
    exit_map['B2'] = ['B1','HB']
    room_content['B2'] = "."
    # B1
    exit_map['B1'] = ['B2']
    room_content['B1'] = "."
    # C2
    exit_map['C2'] = ['C1','HC']
    room_content['C2'] = "."
    # C1
    exit_map['C1'] = ['C2']
    room_content['C1'] = "."
    # D2
    exit_map['D2'] = ['D1','HD']
    room_content['D2'] = "."
    # D1
    exit_map['D1'] = ['D2']
    room_content['D1'] = "."

    return exit_map, room_content