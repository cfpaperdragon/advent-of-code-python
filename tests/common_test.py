import aoc.common.process_input

def read_file(year, day, filename):
    complete_filename = aoc.common.process_input.get_filename(f"../input/year{year}/day{day}/{filename}")
    file_content = aoc.common.process_input.read_file(complete_filename)        
    return file_content