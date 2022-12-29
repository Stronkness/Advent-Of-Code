import re

def facing_direction(facing, dir, times):
    directions = (0, 1, 2, 3)

    if dir == 'L':
        idx = (facing + times *(-1)) % 4 # Basiclly reverse R
    else: # R
        idx = (facing + times) % 4

    facing_dir = directions[idx]
    return facing_dir

board = {}
row_EOL = {} # Where in the map the column ends, for wrap around
col_EOL = {} # Where in the map the row ends, for wrap around
current = None # Current placement used for calculation in the end
facing = 0 # For use later when calculating answer
sections = set() # This time we split up in different sections to visualise the cube format

input = open('input').read().split("\n\n")
map = input[0].split('\n')
directions = input[1]

row = 0
for map_row in map:
    row_section = (row // 50) + 1
    row += 1
    for col, value in enumerate(map_row, 1):
        col_section = ((col - 1) // 50) + 1
        
        if value == ' ':
            continue
        else:
            sections.add((row_section, col_section))
            if value == '.': # This time we use tuples for storing the values of the board
                board[row, col] = (True, (row_section, col_section))
            else:
                board[row, col] = (False, (row_section, col_section))


            if board.get((row - 1, col)) == None:
                col_EOL[col] = (row, None)
            else:
                col_EOL[col] = (col_EOL[col][0], row)


            if not current and row == 1:
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
        for _ in range(steps):
            delta_p, delta_i = not facing in (1, 3), (1, -1)[facing in (2, 3)]
            new = current[delta_p] + delta_i

            if delta_p:
                section_1, section_2 = board.get(current)[1][:: -1]
            else:
                section_1, section_2 = board.get(current)[1][:: 1]

            ends = (col_EOL, row_EOL)[delta_p][current[(-delta_p)-1]]

            if new < ends[0] or new > ends[1]:
                if delta_i == -1:
                    changed_section_position = 1
                else:
                    changed_section_position = 50

                constant_section_position = current[(-delta_p)-1] - 50*(section_2 - 1)

                # This puzzle is just too much ...
                hard_code_mappings = []
                hard_code_mappings.append(((section_1 + delta_i, section_2 - delta_i), (facing_direction(facing, ("R", "L")[delta_p], 1), constant_section_position, changed_section_position)))
                hard_code_mappings.append(((section_1 - 3*delta_i, section_2 + 2*delta_i), (facing, 51 - changed_section_position, constant_section_position)))
                hard_code_mappings.append(((section_1 - delta_i, section_2 + 3*delta_i), (facing_direction(facing, ("L"), 1), constant_section_position, changed_section_position)))
                hard_code_mappings.append(((section_1 - delta_i, section_2 + 2*delta_i), (facing_direction(facing, ("L"), 2), changed_section_position, 51 - constant_section_position)))
                hard_code_mappings.append(((section_1 - 3*delta_i, section_2 + delta_i), (facing_direction(facing, ("R"), 1), constant_section_position, changed_section_position)))
                hard_code_mappings.append(((section_1 + delta_i, section_2 - 2*delta_i), (facing_direction(facing, ("R"), 2), changed_section_position, 51 - constant_section_position)))
                hard_code_mappings.append(((section_1 - delta_i, section_2 - 2*delta_i), (facing_direction(facing, ("L"), 2), changed_section_position, 51 - constant_section_position)))

                for section, value in hard_code_mappings:
                    if delta_p:
                        temp = reversed(section)
                        temp_section = tuple(temp)
                    else:
                        temp_section = section

                    if temp_section in sections:
                        new_facing = value[0]
                        new_pos = (value[1] + 50*(section[0] - 1),value[2] + 50*(section[1] - 1))
                        
                        if delta_p:
                            temp = reversed(new_pos)
                            new_pos = tuple(temp)

                        break

            else:
                if delta_p:
                    new_pos = (current[(-delta_p)-1], new)
                else:
                    new_pos = (new, current[(-delta_p)-1])

                new_facing = facing

            if not board[new_pos][0]:
                break

            current = new_pos
            facing = new_facing
    else:
        facing = facing_direction(facing, action, 1)

print(1000*current[0] + 4*current[1] + facing)
