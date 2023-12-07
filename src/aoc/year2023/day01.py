# aoc.year2023.day01

# chatgpt provided this function
# original version doesn't work, I'll try my idea
def replace_string_with_digit(input_string):
    # Define a dictionary mapping string representations of digits to their actual values
    digit_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    modified_string = input_string
    for k,v in digit_map.items():
        modified_string = modified_string.replace(k, v)

    return modified_string


def process_line(line):
    l = list()
    for ch in line:
        if ch.isdigit():
            l.append(ch)
    return l[0], l[-1]

def compose_processing(preprocess, process):
    def composed_processing(line):
        processed_line = preprocess(line)
        processed_line = process(processed_line)
        return processed_line
    return composed_processing


def process_all_lines(input_list, process_function):
    result = 0
    for line in input_list:
        first, last = process_function(line)
        value_str = "" + first + last
        value = int(value_str)
        result += value
    return result

def calculate_part1(input_list):
    result = process_all_lines(input_list, process_line)
    return result


def calculate_part2(input_list):
    result = process_all_lines(input_list, compose_processing(replace_string_with_digit,process_line))
    return result

