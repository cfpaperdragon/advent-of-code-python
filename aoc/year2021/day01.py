# aoc.year2021.day01

def count_increases(integer_list):
    count = 0
    for i in range(1, len(integer_list)):
        if integer_list[i] > integer_list[i-1]:
            count += 1
    return count


def count_increases_groups(integer_list):
    count = 0
    previous = 1000000 # very large number, the first is never an increase
    for i in range(2, len(integer_list)):
        sum_measurement = integer_list[i-2] + integer_list[i-1] + integer_list[i]
        if sum_measurement > previous:
            count += 1
        previous = sum_measurement
    return count


def calculate_part1(input_list):
    number_increases = count_increases(input_list)
    return number_increases


def calculate_part2(input_list):
    number_increases = count_increases_groups(input_list)
    return number_increases


# execute
# calculate_part1()
# calculate_part2()