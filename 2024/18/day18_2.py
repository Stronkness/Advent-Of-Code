# large.in = 70x70, 1024 bytes
# small.in = 6x6, 12 bytes

import heapq

def dijkstra(start, end, grid): # Reuse dijkstras code from day 16??? :O
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
            cost = current_distance + 1
            
            if (new_row, new_col, new_facing) not in distance or cost < distance[(new_row, new_col, new_facing)]:
                distance[(new_row, new_col, new_facing)] = cost
                heapq.heappush(heap, (cost, new_row, new_col, new_facing))


input = open("large.in").read().split("\n")
byte_positions = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in input]
grid = [['.' for _ in range(71)] for _ in range(71)]
start = (0,0)
end = (70,70)

# Check each byte, this runs really slow though
for byte in byte_positions:
    x, y = byte
    grid[x][y] = '#' # Add one byte at a time
    if dijkstra(start, end, grid) is None:
        print(byte)
        break
