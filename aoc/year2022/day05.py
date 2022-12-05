# aoc.year2022.day05

def get_initial_stack_state(input_list):
    temp_stack = []
    for input in input_list:
        if len(input.strip()) == 0:
            break
        else:
            temp_stack.insert(0, input)
    str_num_stacks = temp_stack.pop(0)
    arr_num_stacks = str_num_stacks.strip().split('   ')
    num_stacks = len(arr_num_stacks)
    
    stack_dict = {}
    for i in range(1, num_stacks+1):
        stack_dict[i] = []
    
    while len(temp_stack)>0:
        stack_line = temp_stack.pop(0)
        for i in range(1, num_stacks+1):
            index = 1 + 4*(i-1)
            container = stack_line[index]
            if container != ' ':
                stack_dict[i].append(container)
    return stack_dict

def process_instruction(instruction):
    parts = instruction.strip().split(' ')
    processed_instruction = (int(parts[1]), int(parts[3]), int(parts[5]))
    return processed_instruction

def move_one_container(stacks, origin, target):
    # get last position from origin stack
    container = stacks[origin].pop(len(stacks[origin])-1)
    stacks[target].append(container)
    return stacks

def move_amount_containers(stacks, amount, origin, target):
    all_containers_in_stack = stacks[origin]
    containers_to_move = all_containers_in_stack[-amount:]
    stacks[origin] = all_containers_in_stack[:-amount]
    for c in containers_to_move:
        stacks[target].append(c)
    return stacks

def get_top_container_from_all_stacks(stacks):
    result = ''
    stack_list = list(stacks.keys())
    stack_list.sort()
    for key in stack_list:
        result += stacks[key][-1]
    return result    

def get_index_for_instructions(input_list):
    index = 0
    for i in range(0, len(input_list)):
        if len(input_list[i].strip()) == 0:
            index = i+1
            break
    return index

def calculate_part1(input_list):
    stack_dict = get_initial_stack_state(input_list)

    # skip stack definition
    index = get_index_for_instructions(input_list)
    
    for i in range(index, len(input_list)):
        instruction = process_instruction(input_list[i])
        # (amount, origin, target)
        for n in range(0, instruction[0]):
            stack_dict = move_one_container(stack_dict, instruction[1], instruction[2])

    return get_top_container_from_all_stacks(stack_dict)


def calculate_part2(input_list):
    stack_dict = get_initial_stack_state(input_list)

    # skip stack definition
    index = get_index_for_instructions(input_list)
    
    # print(stack_dict)
    for i in range(index, len(input_list)):
        instruction = process_instruction(input_list[i])
        # (amount, origin, target)
        stack_dict = move_amount_containers(stack_dict, instruction[0], instruction[1], instruction[2])

    return get_top_container_from_all_stacks(stack_dict)
