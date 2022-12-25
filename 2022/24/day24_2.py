# For easier visualization the coordinates here are (y,x).
# For this solution we use a BFS algorthm to traverse through the blizzards

"""
So for part 2 it is basiclly just to send in a time variable to BFS
and save the time of that iteration. This time is sent in to BFS when
doing the reverse (back to start) and the same when returning with the
snacks for the elf to increment the total time. We send in a flag to BFS
to know if we are going through the start to end or end to start.

Basiclly the only difference is the result calculation furthest down in
the code. But also the flag conditions inside BFS for the start position
and to check if you have reached your destination.
"""

directions = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]

def BFS_blizzard_mayhem(curr_time, flag):
    if flag: # right path
        q = [(-1, 0)]
    else: # end to start
        q = [(h, w - 1)] # End position, see input for the dot in the furthest down wall

    while q:
        upd_q = set() # used for future iterations, removes duplicates and infinite loops (yes a list caused this)
        curr_time += 1 # 1 minute passes for this step
        
        # Build grid
        blizzard_grid = []
        for i in range(h): 
            blizzard_grid.append(['.']*w) # no explanation needed here
        for blizzard in blizzards:
            y = (blizzard[0] + blizzard[2] * curr_time) % h
            x = (blizzard[1] + blizzard[3] * curr_time) % w
            blizzard_grid[y][x] = '#'

        # Basiclly BFS
        for (y,x) in q:
            if flag and x == w - 1 and y == h - 1: # end coordinates, "end"
                return curr_time
            elif not flag and x == 0 and y == 0: # end coordinates, "start"
                return curr_time

            for dir_y, dir_x in directions:
                if dir_x != 0 or dir_y != 0:
                    if x + dir_x >= w or y + dir_y >= h: # out of bounds (walls rightmost and downmost)
                        continue

                    if x + dir_x < 0 or y + dir_y < 0: # out of bounds (leftmost and uppmost walls)
                        continue
                
                if y == h or y == -1 or blizzard_grid[y + dir_y][x + dir_x] == '.':
                    upd_q.add((y + dir_y, x + dir_x))
        q = upd_q

def get_direction(direction): # Works opposite in y and x axis. We want to get closer to the end, hence +1 if we traverse down in the graph and -1 if we go up (closer to the start)
    if direction == '^':
        return directions[0]
    elif direction == 'v':
        return directions[4]
    elif direction == '<':
        return directions[1]
    elif direction == '>':
        return directions[3]
    else:
        return directions[2] # This shouldn't happen though ...

windy = open('input').read().split('\n')
blizzards = []
for y, blizzard in enumerate(windy, -1): # start wall
    if y == len(windy)-1: # end wall
        continue
    h, w = y, len(blizzard) - 2 # -2 for no walls included in blizzard
    for x, direction in enumerate(blizzard, -1): # starting blizzard directions in x-axis
        if direction == '#' or direction == '.':
            continue
        dir_y, dir_x = get_direction(direction)
        blizzards.append((y, x, dir_y, dir_x))

res = 0
original_path = [True, False, True]
for path in original_path:
    res = BFS_blizzard_mayhem(res, path)

print(res)
