# aoc.year2022.day10

def calculate_part1(input_list):

    inst = {
        'noop': 1,
        'addx': 2
    }

    reg = {
        'X': 1
    }

    cycle = 0
    save = [20, 60, 100, 140, 180, 220]
    save_value = {}

    current_instruction = 'noop'
    num_cycles = 0

    while len(input_list) > 0 or num_cycles > 0:
        # if cycle > 180:
        #    print(cycle, current_instruction, num_cycles, reg['X'])
        # if previous operation ended, get a new one
        if num_cycles == 0:
            current_instruction = input_list.pop(0) 
        
            if 'noop' in current_instruction:
                # does nothing
                num_cycles = inst['noop']
            elif 'addx' in current_instruction:
                num_cycles = inst['addx']
            else: 
                raise Exception('Invalid instruction')

        cycle += 1
        num_cycles -= 1

        if cycle in save:
            save_value[cycle] = reg['X']

        # at the end of the cycle, do the operation
        if num_cycles == 0:
            if 'addx' in current_instruction:
                parts = current_instruction.split(' ')
                add_value = int(parts[1])
                reg['X'] += add_value

    result = 0
    for key,value in save_value.items():
        result += key*value

    return result

def calculate_part2(input_list):
    return 0

