import collections


def change_dir(curr_dirr):
    return DIRECTIONS[(DIRECTIONS.index(curr_dirr) + 1) % 4]


def get_start_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return (i, j)


def get_walls(grid):
    walls = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                walls.append((i, j))
    return walls


input = open("large.in").read().split("\n")
grid = [pos for pos in input]

curr_dir = (-1, 0)
curr_pos = get_start_pos(grid)

WALLS = get_walls(grid)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
HISTORY = set()

# Prepare all locations of visited places, to be used later with obstacle calculations
while True:
    HISTORY.add(curr_pos)

    next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])

    if next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]) or next_pos[0] < 0 or next_pos[1] < 0:
        break

    if next_pos not in WALLS:
        curr_pos = next_pos
    else:
        curr_dir = change_dir(curr_dir)

OBSTACLE_COORDINATES = HISTORY - {get_start_pos(grid)}
inf_loop_counter = 0
for obstacle in OBSTACLE_COORDINATES:
    curr_pos = get_start_pos(grid) # Restart position
    curr_dir = (-1, 0) # Restart direction
    walked_path = collections.defaultdict(int)
    walked_path[(curr_pos, curr_dir)] = 1
    test_obstacle = WALLS + [obstacle] # not ... = WALLS and then append as it will add to original WALLS list

    while True:
        next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])

        if next_pos not in test_obstacle:
            curr_pos = next_pos
        else:
            curr_dir = change_dir(curr_dir)

        if walked_path[(curr_pos, curr_dir)] > 0: # infinite loop detected
            inf_loop_counter += 1
            break
        else:
            walked_path[(curr_pos, curr_dir)] += 1

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            break

print(inf_loop_counter)
