# aoc.year2021.day01

def process_input_list(input_list):
    elf_dict = {}
    count = 0
    for input in input_list:
        if len(input) == 0:
            count += 1
            continue
        else:
            int_input = int(input)
            if count in elf_dict:
                elf_dict[count].append(int_input)
            else:
                elf_dict[count] = [int_input]
    return elf_dict

def calculate_part1(input_list):
    elf_dict = process_input_list(input_list)
    # print(elf_dict)
    sum_list = []
    for key in elf_dict.keys():
        sum_list.append(sum(elf_dict[key]))

    return max(sum_list)


def calculate_part2(input_list):
    elf_dict = process_input_list(input_list)
    # print(elf_dict)
    sum_list = []
    for key in elf_dict.keys():
        sum_list.append(sum(elf_dict[key]))

    value1 = max(sum_list)
    sum_list.remove(value1)
    value2 = max(sum_list)
    sum_list.remove(value2)
    value3 = max(sum_list)
    sum_list.remove(value3)
    
    return value1 + value2 + value3


# execute
# calculate_part1()
# calculate_part2()