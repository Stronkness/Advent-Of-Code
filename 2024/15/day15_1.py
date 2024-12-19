import copy

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

input = open("large.in").read().split("\n\n")
grid = [[p for p in mappiece] for mappiece in input[0].split("\n")]
moves = [move for x in input[1].split("\n") for move in x]
robot_position = 0, 0
for i, row in enumerate(grid):
    for j, r in enumerate(row):
        if r == '@':
            robot_position = i, j

for move in moves:
    tmp_grid = copy.deepcopy(grid)
    dir = 0, 0
    if move == '<':
        dir = 0, -1
    elif move == '>':
        dir = 0, 1
    elif move == '^':
        dir = -1, 0
    elif move == 'v':
        dir = 1, 0
    else:
        print("Invalid input, unexpected move:", move)
        continue
    
    r_new_pos = tuple(map(sum, zip(robot_position, dir)))

    if not (0 <= r_new_pos[0] < len(grid) and 0 <= r_new_pos[1] < len(grid[0])):
        continue

    map_element = tmp_grid[r_new_pos[0]][r_new_pos[1]]

    if map_element == '#':
        continue

    elif map_element == '.':
        tmp_grid[r_new_pos[0]][r_new_pos[1]] = '@'
        tmp_grid[robot_position[0]][robot_position[1]] = '.'
        robot_position = r_new_pos

    elif map_element == 'O':
        chain_positions = [r_new_pos]
        current_pos = r_new_pos

        while True:
            next_pos = tuple(map(sum, zip(current_pos, dir)))

            if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
                break

            if tmp_grid[next_pos[0]][next_pos[1]] == 'O':
                chain_positions.append(next_pos)
                current_pos = next_pos
            elif tmp_grid[next_pos[0]][next_pos[1]] == '.':
                for pos in reversed(chain_positions):
                    push_pos = tuple(map(sum, zip(pos, dir)))
                    tmp_grid[push_pos[0]][push_pos[1]] = 'O'

                tmp_grid[r_new_pos[0]][r_new_pos[1]] = '@'
                tmp_grid[robot_position[0]][robot_position[1]] = '.'
                robot_position = r_new_pos
                break
            else:
                break

    grid = tmp_grid

coordinates = 0
for i, row in enumerate(grid):
    for j, r in enumerate(row):
        if r == 'O':
            coordinates += 100 * i + j

print_grid(grid)
print(coordinates)
