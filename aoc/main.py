# main
import sys
import time

import common.process_input
from common.import_utils import import_module

n = len(sys.argv)
if n != 4:
    print("Missing parameters - needs 3 parameters: year day part")
    exit(-1)

year = sys.argv[1]
day = sys.argv[2]
part = sys.argv[3]

module_name = "year" + year + ".day" + day 
module = import_module(module_name)

# record start time
start = time.time()

file_content = common.process_input.read_file("input\\year" + year + "\\day" + day + "\\input.txt")        
input_content = common.process_input.to_function_list(file_content, int)
if part == "1":
    result = module.calculate_part1(input_content)
else:
    result = module.calculate_part2(input_content)

# record end time
end = time.time()

print("Result:", result, "in", (end-start) * 10**3, "ms")