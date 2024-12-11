def DFS(loc_x, loc_y):
    if grid[loc_x][loc_y] == 9:
        return 1
    
    score = 0
    for (dx,dy) in DIRECTIONS:
        new_x, new_y = loc_x + dx, loc_y + dy
        if 0 <= new_x < length and 0 <= new_y < width:
            if grid[new_x][new_y] == 1 + grid[loc_x][loc_y]:
                score += DFS(new_x, new_y)
    
    return score

input = open("large.in").read().split("\n")
grid = [[int(x) for x in row] for row in input]
width, length = len(grid[0]), len(grid)

DIRECTIONS = ((1,0), (-1,0), (0,1), (0,-1))

trailhead_score = 0
for i in range(width):
    for j in range(length):
        if grid[i][j] == 0:
            trailhead_score += DFS(i,j)

print(trailhead_score)