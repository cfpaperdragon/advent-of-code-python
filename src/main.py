#!/usr/bin/env python3
"""Call a particular problem of Advent of Code.

Usage:

   python3 main.py <year> <day> <part>
"""
import sys
import time

import aoc.common.process_input
from aoc.common.import_utils import import_module


def run_aoc(year, day, part):
    """Run a specific problem of Advent of Code.

      Args:
          year: the year of the problem 
          day: the day of the problem (2 digits)
          part: 1 or 2

      Returns:
          Result of executing the problem if implemented.
    """
    module_name = "aoc.year" + year + ".day" + day 
    module = import_module(module_name)

    filename = aoc.common.process_input.get_filename_for_day(year, day, "input.txt")
    file_content = aoc.common.process_input.read_file(filename)  
    process_function = int
    if year == "2021" and day == "22":
        process_function = aoc.common.process_input.process_reboot_steps_line
    elif year == "2022":
        process_function = str      
    if year == "2022" and day == "05":
        input_content = aoc.common.process_input.to_str_list_no_strip(file_content)   
    else:     
        input_content = aoc.common.process_input.to_function_list(file_content, process_function)

    if part == "1":
        if year == "2022" and day == "15":
            result = module.calculate_part1(input_content, 2000000)
        else:
            result = module.calculate_part1(input_content)
    else:
        result = module.calculate_part2(input_content)

    return result


if __name__ == '__main__':

    try:
        year = sys.argv[1]
        day = sys.argv[2]
        part = sys.argv[3]

        # record start time
        start = time.time()
        result = run_aoc(year, day, part)
        # record end time
        end = time.time()
        print("Result:", result, "in", (end-start) * 10**3, "ms")
    except IndexError:
        print("Missing parameter: needs to be called with 3 parameters: year day part")
    
    except ModuleNotFoundError as e: 
        print(f"{e!r}", file=sys.stderr)

    finally:
        print("End.")
