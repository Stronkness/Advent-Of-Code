# For easier visualization the coordinates here are (y,x).
# For this solution we use a BFS algorthm to traverse through the blizzards

directions = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]

def BFS_blizzard_mayhem():
    q = [(-1, 0)]
    curr_time = 0
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
            if x == w - 1 and y == h - 1: # end coordinates
                return curr_time
            for dir_y, dir_x in directions:
                if dir_x != 0 or dir_y != 0:
                    if x + dir_x >= w or y + dir_y >= h: # out of bounds (walls rightmost and downmost)
                        continue
                    if x + dir_x < 0 or y + dir_y < 0: # out of bounds (leftmost and uppmost walls)
                        continue
                
                if y == -1 or blizzard_grid[y + dir_y][x + dir_x] == '.' or y == h:
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

print(BFS_blizzard_mayhem())
