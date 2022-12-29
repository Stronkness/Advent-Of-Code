import re

board = {}
row_EOL = {} # Where in the map the column ends, for wrap around
col_EOL = {} # Where in the map the row ends, for wrap around
current = None # Current placement used for calculation in the end
facing = 0 # For use later when calculating answer

input = open('input').read().split("\n\n")
map = input[0].split('\n')
directions = input[1]

row = 0
for map_row in map: # True/False based on if you can move here or not, walls basiclly
    row += 1
    for col, value in enumerate(map_row, 1):
        if value == ' ':
            continue
        else:
            if value == '.':
                board[row, col] = True
            else:
                board[row, col] = False


            if board.get((row - 1, col)) == None:
                col_EOL[col] = (row, None)
            else:
                col_EOL[col] = (col_EOL[col][0], row)


            if not current and row == 1: # First time a part of the actual map iterates
                current = (1, col)

            row_EOL[row] = (row_EOL.get(row, (col,))[0], col)

directions_split = []
directions_numbers = re.findall('\d+', directions)
directions_letters = re.findall('[LR]', directions)
for i in range(len(directions_letters)):
    directions_split.append(directions_numbers[i])
    directions_split.append(directions_letters[i])
directions_split.append(directions_numbers[len(directions_numbers)-1])
path = directions_split # just rename for clarification

for action in path:
    if action.isdigit():
        steps = int(action)
        delta_p, delta_i = not facing in (1, 3), (1, -1)[facing in (2, 3)]

        for i in range(steps):
            new = current[delta_p] + delta_i
            ends = (col_EOL, row_EOL)[delta_p][current[(-delta_p)-1]]

            if new < ends[0] or new > ends[1]:
                if delta_i == 1:
                    new = ends[0]
                else:
                    new = ends[1]
            
            if delta_p:
                new_pos = (current[(-delta_p)-1], new)
            else:
                new_pos = (new, current[(-delta_p)-1])
            valid = board[new_pos]

            if not valid:
                break

            current = new_pos

    elif action == 'L': # 90 degree conditions
        if facing == 0:
            facing = 3
        elif facing == 1:
            facing = 0
        elif facing == 2:
            facing = 1
        else:
            facing = 2
    elif action == 'R':
        if facing == 0:
            facing = 1
        elif facing == 1:
            facing = 2
        elif facing == 2:
            facing = 3
        else:
            facing = 0

print(1000*current[0] + 4*current[1] + facing)
