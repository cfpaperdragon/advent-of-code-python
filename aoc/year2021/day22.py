# aoc.year2021.day22

def process_reboot_steps_line(file_line):
    '''
    transform this: 
    on x=10..12,y=10..12,z=10..12
    into:
    {
        "status": "on",
        "x": (10, 12),
        "y": (10, 12),
        "z": (10, 12)
    }
    '''
    result_dict = dict()

    first_split_result = file_line.split(" ") # split on x=10..12,y=10..12,z=10..12
    result_dict["status"] = first_split_result[0]

    second_split_result = first_split_result[1].split(",") # split each coordinate
    for split_result in second_split_result:
        third_split_result = split_result.split("=") # split coordenate from values
        coordenate = third_split_result[0]
        fourth_split_result = third_split_result[1].split("..") # split min and max values
        min_value = int(fourth_split_result[0])
        max_value = int(fourth_split_result[1])
        result_dict[coordenate] = (min_value, max_value)

    return result_dict

def process_reboot_steps(file_content):
    '''
    transform this: 
    on x=10..12,y=10..12,z=10..12
    off x=9..11,y=9..11,z=9..11
    into:
    [
        {
            "status": "on",
            "x": (10, 12),
            "y": (10, 12),
            "z": (10, 12)
        },
        {
            "status": "off",
            "x": (9, 11),
            "y": (9, 11),
            "z": (9, 11)
        }
    ]
    '''
    result = []
    file_lines = file_content.splitlines()
    for line in file_lines:
        value = process_reboot_steps_line(line.strip())
        result.append(value)
    return result

def calculate_part1(input_list):
    
    return 0


def calculate_part2(input_list):
    
    return 0
