from collections import defaultdict

def handle_data():
    global path_count, instructions_length, paths, instructions
    data = open('input', 'r').read().splitlines()
    instructions = data[0]
    pathways = data[2:]

    path_count = 0
    instructions_length = len(instructions)
    paths = defaultdict(list)
    [paths[path.split()[0]].extend(path[path.find("(") + 1:path.find(")")].split(', ')) for path in pathways]

def compute_paths():
    global path_count
    current_path = 'AAA'
    inst_count = 0
    while current_path != 'ZZZ':
        dir = instructions[inst_count]
        if dir == "R":
            current_path = paths[current_path][1]
        else:
            current_path = paths[current_path][0]
        
        path_count += 1
        inst_count += 1

        if inst_count == instructions_length:
            inst_count = 0

handle_data()
compute_paths()
print(path_count)
