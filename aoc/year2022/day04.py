# aoc.year2022.day04

def process_line(input_line):
    """
    2-4,6-8 -> ((2,4),(6,8))
    """
    pairs = input_line.split(',')
    limits_pair1 = pairs[0].split("-")
    sections_pair1 = (int(limits_pair1[0]), int(limits_pair1[1]))
    limits_pair2 = pairs[1].split("-")
    sections_pair2 = (int(limits_pair2[0]), int(limits_pair2[1]))
    return (sections_pair1, sections_pair2)

def process_input_list(input_list):
    result = []
    for input_line in input_list:
        sections = process_line(input_line)
        result.append(sections)
    return result

def check_contains(pair1, pair2):
    """
    returns true if pair1 sections contain section2 
    """
    return pair1[0] <= pair2[0] and pair1[1] >= pair2[1]
    

def calculate_part1(input_list):
    sections_list = process_input_list(input_list)
    # print(sections_list)
    count = 0
    for sections in sections_list:
        if check_contains(sections[0], sections[1]) or check_contains(sections[1], sections[0]):
            count += 1
    return count

def check_overlap(pair1, pair2):
    """
    returns true if pair1 sections overlap with section2 
    """
    return (pair1[0] <= pair2[0] and pair1[1] >= pair2[0]) or (pair1[0] <= pair2[1] and pair1[1] >= pair2[1])

def calculate_part2(input_list):
    sections_list = process_input_list(input_list)
    # print(sections_list)
    count = 0
    for sections in sections_list:
        if check_overlap(sections[0], sections[1]) or check_overlap(sections[1], sections[0]):
            count += 1
    return count