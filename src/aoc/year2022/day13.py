# aoc.year2022.day13
import functools

def compare_pair(left, right):
    """
    return 0 if the same
    return 1 if left is smaller
    return -1 if right is smaller
    """
    value = 0
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if i > len(left)-1:
                # no more lefts
                value = 1
            elif i > len(right)-1:
                value = -1
            else:
                value = compare_pair(left[i], right[i])
            
            # if reached decision, end
            if value != 0:
                return value
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    # one is a list and the other is a int
    elif isinstance(left, int):
        left = [left]
        value = compare_pair(left, right)

    elif isinstance(right, int):
        right = [right]
        value = compare_pair(left, right)

    return value

def calculate_part1(input_list):
    count = 0
    result = {}

    while len(input_list) > 0:
        count += 1
        # get a pair
        left_str = input_list.pop(0)
        right_str = input_list.pop(0)
        if len(input_list) > 0:
            empty_str = input_list.pop(0)

        left = eval(left_str)
        right = eval(right_str)
        # (left, right)
        value = compare_pair(left, right)
        result[count] = value

    total = 0
    for key in result.keys():
        if result[key] == 1:
            total += key

    return total


def calculate_part2(input_list):
    message_list = []

    while len(input_list) > 0:
        # get a pair
        left_str = input_list.pop(0)
        right_str = input_list.pop(0)
        if len(input_list) > 0:
            empty_str = input_list.pop(0)

        message_list.append(eval(left_str))
        message_list.append(eval(right_str))

    message_list.append([[2]])
    message_list.append([[6]])


    sorted_message_list = sorted(message_list, key=functools.cmp_to_key(compare_pair), reverse=True)
    # for m in sorted_message_list:
    #     print(m)

    position1 = sorted_message_list.index([[2]]) +1
    position2 = sorted_message_list.index([[6]]) +1

    return position1*position2
