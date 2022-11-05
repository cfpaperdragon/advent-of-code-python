# aoc.common.process_input

def read_file(file_path):
    fileContent = ""
    with open(file_path) as file:
        line = file.readline()
        while line:
            fileContent += line
            line = file.readline()
    return fileContent


def to_function_list(file, function):
    result = []
    file_lines = file.splitlines()
    for line in file_lines:
        value = function(line.strip())
        result.append(value)
    return result

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
