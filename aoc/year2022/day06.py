# aoc.year2022.day06

def find_marker(message, num_chars):
    unique_chars = []
    for i in range(len(message)):
        c = message[i]
        if c not in unique_chars:
            unique_chars.append(c)
        else:
            index = unique_chars.index(c)
            # slice to remove the repeated
            unique_chars = unique_chars[index+1:]
            unique_chars.append(c)
        if len(unique_chars) == num_chars:
            break
    return i+1


def calculate_part1(input_list):
    return find_marker(input_list[0], 4)


def calculate_part2(input_list):
    return find_marker(input_list[0], 14)
