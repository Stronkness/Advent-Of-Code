import heapq

def dijkstra(start, end, grid):
    distance = {(start[0], start[1], 1): 0}
    heap = [(0, start[0], start[1], 1)]
    
    while heap:
        current_distance, row, col, facing = heapq.heappop(heap)
        if (row, col) == end:
            return current_distance
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []

        for direction_index, (dr, dc) in enumerate(directions):
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#":
                neighbors.append((new_row, new_col, direction_index))

        for rotation in [-1, 1]:
            neighbors.append((row, col, (facing + rotation) % 4))
        
        for new_row, new_col, new_facing in neighbors:
            if new_facing == facing:
                cost = current_distance + 1
            else:
                cost = current_distance + 1000 + 1
            
            if (new_row, new_col, new_facing) not in distance or cost < distance[(new_row, new_col, new_facing)]:
                distance[(new_row, new_col, new_facing)] = cost
                heapq.heappush(heap, (cost, new_row, new_col, new_facing))

input_data = open("large.in").read().split("\n")
grid = [list(row) for row in input_data]

start, end = (0, 0), (0, 0)
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        if grid[row_index][col_index] == "S":
            start = (row_index, col_index)
        if grid[row_index][col_index] == "E":
            end = (row_index, col_index)

print(dijkstra(start, end, grid))
