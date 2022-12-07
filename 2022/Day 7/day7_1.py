lines = open('testinput').read().splitlines()

path = []
directories = {}

for line in lines:
    line = line.split(' ')
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] != '..':
                if line[2] == '/':
                    path.append('~/')
                else:
                    path.append(line[2] + '/')
            else: 
                path.pop()
        elif line[1] == 'ls':
            continue
    elif line[0] == 'dir':
        continue
    else:
        for i in range(len(path)):
            if i == 0:
                # End of path
                curr_path = ''.join(path)
            else:
                # Backtrack to / and add size to all subdirs
                curr_path = ''.join(path[:-i])

            if curr_path not in directories:
                directories[curr_path] = int(line[0])
            else:
                directories[curr_path] += int(line[0])

print(sum(value for value in directories.values() if value <= 100000))
