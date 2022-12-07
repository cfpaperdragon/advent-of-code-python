# main
import sys
import time

import aoc.common.process_input
from aoc.common.import_utils import import_module

n = len(sys.argv)
if n != 4:
    print("Missing parameters - needs 3 parameters: year day part")
    exit(-1)

year = sys.argv[1]
day = sys.argv[2]
part = sys.argv[3]

module_name = "aoc.year" + year + ".day" + day 
module = import_module(module_name)

# record start time
start = time.time()

file_content = aoc.common.process_input.read_file("input\\year" + year + "\\day" + day + "\\input.txt")  
process_function = int
if year == "2021" and day == "22":
    process_function = aoc.common.process_input.process_reboot_steps_line
elif year == "2022" and day == "01":
    process_function = str      
elif year == "2022" and day == "02":
    process_function = str   
elif year == "2022" and day == "03":
    process_function = str   
elif year == "2022" and day == "04":
    process_function = str  
elif year == "2022" and day == "06":
    process_function = str  
elif year == "2022" and day == "07":
    process_function = str  
    
if year == "2022" and day == "05":
    input_content = aoc.common.process_input.to_str_list_no_strip(file_content)   
else:     
    input_content = aoc.common.process_input.to_function_list(file_content, process_function)
if part == "1":
    result = module.calculate_part1(input_content)
else:
    result = module.calculate_part2(input_content)

# record end time
end = time.time()

print("Result:", result, "in", (end-start) * 10**3, "ms")