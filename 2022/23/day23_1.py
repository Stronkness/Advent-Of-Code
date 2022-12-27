from collections import defaultdict

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

elfs = open('input').read().split('\n')
grid = defaultdict(lambda: 0) # 0 for no elf, 1 for elf

for x, elf in enumerate(elfs):
    for y, char in enumerate(elf):
        if char == '#':
            grid.update({(y, x): 1})

for itr in range(11):
    curr_pos = []
    for pos, elf in grid.items():
        if elf:
            curr_pos.append(pos)
    new_pos = defaultdict(list)

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


res = 0
x,y = [],[]
for elf in curr_pos: # last positions after ten iterations
    x.append(elf[0])
    y.append(elf[1])

min_x, min_y = min(x), min(y)
max_x, max_y = max(x), max(y)

# # This is basiclly get the difference between the highest and lowest positions
# # to determine the amount of positions between the max and min (+1 for 0). Then
# # multiply x and y positions with eachother to gain the totalt amount
# # of points in the grid. Then subtract with the length of curr_pos as the last
# # iteration of this is how many elves are in correct positions. So the formula
# # is basiclly: Points - Elfes_on_field = Empty points
res = (max_x - min_x + 1) * (max_y - min_y + 1) - len(curr_pos)
print(res)
