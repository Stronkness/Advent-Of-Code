from collections import defaultdict
import math

def handle_data():
    global instructions_length, paths, instructions
    data = open('input', 'r').read().splitlines()
    instructions = data[0]
    pathways = data[2:]

    instructions_length = len(instructions)
    paths = defaultdict(list)
    [paths[path.split()[0]].extend(path[path.find("(") + 1:path.find(")")].split(', ')) for path in pathways]

def compute_paths(start):
    path_count = 0
    current_path = start
    inst_count = 0
    while not current_path.endswith('Z'):
        dir = instructions[inst_count]
        if dir == "R":
            current_path = paths[current_path][1]
        else:
            current_path = paths[current_path][0]
        
        path_count += 1
        inst_count += 1

        if inst_count == instructions_length:
            inst_count = 0

    return path_count

handle_data()
print(compute_paths('AAA')) # Part 1
steps = 1 # Neede for doing LCM maths
for path in paths:
    if path.endswith('A'):
        steps = math.lcm(steps, compute_paths(path))
print(steps) # Part 2
