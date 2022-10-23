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

