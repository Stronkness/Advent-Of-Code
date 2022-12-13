from string import ascii_lowercase
import heapq

routes = open('input').read().split('\n')
grid = [list(route) for route in routes]
length = len(grid)
height = len(grid[0])
visited = [[False]*height for i in range(length)] # all coordinates in grid must be False, for visited nodes durther down

def check_allowed_climb_height(letter):
    if letter == "S":
        return 0 # elevatiion of a
    elif letter == "E":
        return 25 # elevation of z
    elif letter in ascii_lowercase:
        return ascii_lowercase.index(letter)
    else:
        return None # this shouldn't happen

def check_neighbours(pos_x, pos_y):
    directions = [[1,0], [0,1], [-1,0], [0,-1]] # can either go one step to left, right, up or down from current pos_x, pos_y
    for dir in directions:
        x, y = dir[0], dir[1]

        neighbour_x = x + pos_x
        neighbour_y = y + pos_y

        if not(length > neighbour_x >= 0 and height > neighbour_y >= 0): # outside of grid to right-most, left-most, upper or furthest down part of the grid
            continue # is outside with current coordinates, just continue to avoid indexing problems
        if check_allowed_climb_height(grid[neighbour_x][neighbour_y]) - check_allowed_climb_height(grid[pos_x][pos_y]) <= 1: # check if index of ascii_lowercase is at most one higher than current elevation
            yield neighbour_x, neighbour_y # to check all four directions

for i in range(length):
    for j in range(height):
        if grid[i][j] == "S": # start
            start = i,j
        if grid[i][j] == "E": # end
            end = i,j


"""
Part 1 consists of building up a graph and iterate through the different neighbours of current position
to find the shortest path to the end point E. This is done in my case with Dijkstras algorithm. If the closest neighbour
which is returned by the check_neighbour function is not visited yet we set it to True and iterate through the new points
closests neighbours to fins the shortest path towards the goal. check_neighbours returns all instances of
the neighbours if the difference condition is fullfiled which is pushed to the heapqueue. heappop takes out the smallest value
which is why the four neighbours of the point is inserted to the heap queue to basiclly fins the closest neighbour.
"""
curr = [(0, start[0], start[1])]
minimum_steps = 0
while True:
    steps, x, y = heapq.heappop(curr)

    if visited[x][y] != False:
        continue

    if (x,y) == end: # iteration done through Dijkstras algorithm, minimum_steps found
        minimum_steps = steps
        break

    visited[x][y] = True

    for neighbour_x, neighbour_y in check_neighbours(x, y): # returns all possible neighbours and adds them to heap, picks the smallest further up
        heapq.heappush(curr, (steps + 1, neighbour_x, neighbour_y))

print(minimum_steps)
