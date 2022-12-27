from collections import defaultdict

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

elfs = open('input').read().split('\n')
grid = defaultdict(lambda: 0)

for x, elf in enumerate(elfs):
    for y, char in enumerate(elf):
        if char == '#':
            grid.update({(y, x): 1})

prev_pos = []
for itr in range(100000000):
    curr_pos = []
    for pos, elf in grid.items():
        if elf:
            curr_pos.append(pos)
    new_pos = defaultdict(list)

    # Check if curr_pos is same as prev_pos, as then new positions doesn't exist and amount of rounds are done
    if curr_pos == prev_pos:
        print(itr)
        exit()

    # If there is a square around the elf that is free to move to, if not then iterate to next elf
    for elf in curr_pos:
        temp = []
        for y in (-1,0,1):
            for x in (-1,0,1):
                if x != 0 or y != 0:
                   temp.append(grid[elf[0] + y, elf[1] + x])
        if all(not element for element in temp):
            continue

        for i in range(4):
            curr_dir = (itr + i) % 4

            if curr_dir == NORTH:
                temp = []
                for y in (-1,0,1):
                    temp.append(grid[elf[0] + y, elf[1] - 1])
                if all(not element for element in temp):
                    new_pos[elf[0], elf[1] - 1].append(elf)
                    break
            elif curr_dir == SOUTH:
                temp = []
                for y in (-1,0,1):
                    temp.append(grid[elf[0] + y, elf[1] + 1])
                if all(not element for element in temp):
                    new_pos[elf[0], elf[1] + 1].append(elf)
                    break
            elif curr_dir == WEST:
                temp = []
                for x in (-1,0,1):
                    temp.append(grid[elf[0] - 1, elf[1] + x])
                if all(not element for element in temp):
                    new_pos[elf[0] - 1, elf[1]].append(elf)
                    break
            elif curr_dir == EAST:
                temp = []
                for y in (-1,0,1):
                    temp.append(grid[elf[0] + 1, elf[1] + y])
                if all(not element for element in temp):
                    new_pos[elf[0] + 1, elf[1]].append(elf)
                    break

    for pos, elf in new_pos.items(): # Update positions 
        if len(elf) == 1: # if one elf is supposed to use this position, then its ok, otherwise skip as more than one wants to move here
            grid[elf[0]] = 0 # index zero as its a list containing one element
            grid[pos] = 1

    prev_pos = curr_pos
