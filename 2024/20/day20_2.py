"""The idea is to find the shortest path from the start to the end, 
and then find all the points that are 2 steps away from the end. Then we 
check if we can reach those points from the start in a way that is at 
least 100 steps shorter than the shortest path. If we can,
we add 0 <= manhattan distance <= 20 to the answer."""

input = open("large.in").read().strip().split("\n")
grid = [list(x) for x in input]
start, end = (0,0), (0,0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (j,i)
        elif grid[i][j] == "E":
            end = (j, i)


start_distance = {start: 0}
frontier = [start]
while frontier:
    next_node = frontier.pop(0)
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nbr = (next_node[0]+dx, next_node[1]+dy)
        if not (0 <= nbr[0] < len(grid[0]) and 0 <= nbr[1] < len(grid)):
            continue
        if grid[nbr[1]][nbr[0]] == "#":
            continue

        if nbr in start_distance:
            if start_distance[nbr] > start_distance[next_node] + 1:
                start_distance[nbr] = min(start_distance[nbr], start_distance[next_node] + 1)
                frontier.append(nbr)
        else:
            start_distance[nbr] = start_distance[next_node] + 1
            frontier.append(nbr)


end_distance = {end: 0}
curr = [end]
while curr:
    next_node = curr.pop(0)
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nbr = (next_node[0]+dx, next_node[1]+dy)
        if not (0 <= nbr[0] < len(grid[0]) and 0 <= nbr[1] < len(grid)):
            continue
        if grid[nbr[1]][nbr[0]] == "#":
            continue

        if nbr in end_distance:
            if end_distance[nbr] > end_distance[next_node] + 1:
                end_distance[nbr] = min(end_distance[nbr], end_distance[next_node] + 1)
                curr.append(nbr)
        else:
            end_distance[nbr] = end_distance[next_node] + 1
            curr.append(nbr)


best_dist = start_distance[end]
cheat_numbers = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        position = (j,i)
        if grid[i][j] == "#":
            continue
        for cheat in end_distance:
            m_d = abs(cheat[0] - position[0]) + abs(cheat[1]-position[1])
            if not (m_d <= 20):
                continue

            if 0 <= position[0] < len(grid[0]) and 0 <= position[1] < len(grid):
                if grid[position[1]][position[0]] == "#":
                    continue

            new_dist = start_distance[position] + end_distance[cheat] + m_d
            if new_dist <= best_dist - 100:
                cheat_numbers += 1


print(cheat_numbers)
