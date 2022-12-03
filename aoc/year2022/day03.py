# aoc.year2022.day03

def get_priority_dict():
    items = 'abcdefghijklmnopqrstuvwxyz'
    count = 1
    priorities = {}
    for c in items:
        priorities[c] = count
        count += 1
    for c in items:
        priorities[c.capitalize()] = count
        count += 1
    return priorities


def calculate_part1(input_list):
    total_match_list = []
    for input in input_list:
        full_length = len(input)
        half = int(full_length/2)
        compartment1 = input[:half]
        compartment2 = input[half:]
        match_list = []
        for c in compartment1:
            if c in compartment2:
                if c not in match_list:
                    match_list.append(c)
        total_match_list += match_list
    priorities = get_priority_dict()
    total = 0
    for c in total_match_list:
        total += priorities[c]
    return total

def calculate_part2(input_list):
    total_rucksacks = len(input_list)
    total_groups = int(total_rucksacks/3)
    badge_list = []
    for i in range(total_groups):
        rucksack1 = input_list[i*3]
        rucksack2 = input_list[i*3+1]
        rucksack3 = input_list[i*3+2]
        for c in rucksack1:
            if c in rucksack2:
                if c in rucksack3:
                    badge_list.append(c)
                    break
    priorities = get_priority_dict()
    total = 0
    for c in badge_list:
        total += priorities[c]
    return total

