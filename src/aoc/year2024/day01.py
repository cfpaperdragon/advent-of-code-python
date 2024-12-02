# aoc.year2024.day01

def process_input_list(input_list):
    left_list = []
    right_list = []
    for line in input_list:
        # input has 3 spaces, example has 4
        # split_result = line.strip().split("   ") 
        line = line.strip()
        last_space_index = line.rindex(" ")
        left_id = int(line[:last_space_index].strip())
        left_list.append(left_id)
        right_id = int(line[last_space_index+1:].strip())
        right_list.append(right_id)

    return left_list, right_list


def calculate_distance(left_value, right_value):
    return abs(left_value - right_value)


def calculate_part1(input_list):
    left, right = process_input_list(input_list)
    left.sort()
    right.sort()    
    sum = 0
    for i in range(0, len(left)):
        sum += calculate_distance(left[i], right[i])
    return sum


def calculate_part2(input_list):   
    return 0