# aoc.year2023.day01

def process_line(line):
    l = list()
    for ch in line:
        if ch.isdigit():
            l.append(ch)
    return l[0], l[-1]

def calculate_part1(input_list):
    result = 0
    for line in input_list:
        first, last = process_line(line)
        value_str = "" + first + last
        value = int(value_str)
        result += value
    return result


def calculate_part2(input_list):
    
    return 0

