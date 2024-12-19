from heapq import heappop, heappush
# With some help from Reddit

def dijkstra_revamped(start, end, grid):
    distances = {(start, 1, 0): 0}
    heap = [(0, [start], 1, 0)]
    best_end_cost = 0
    best_path = set()

    while heap:
        current_cost, current_path, delta_x, delta_y = heappop(heap)
        current_row, current_col = current_path[-1]

        if (current_row, current_col) == end:
            best_path.update(current_path)
            best_end_cost = current_cost

        elif not best_end_cost or current_cost < best_end_cost:
            possible_moves = [
                (current_cost + 1, current_row + delta_x, current_col + delta_y, delta_x, delta_y),  # Move forward
                (current_cost + 1000, current_row, current_col, delta_y, -delta_x),  # Turn right
                (current_cost + 1000, current_row, current_col, -delta_y, delta_x)  # Turn left
            ]

            for next_cost, next_row, next_col, next_delta_x, next_delta_y in possible_moves:
                next_position = (next_row, next_col, next_delta_x, next_delta_y)
                if grid[next_col][next_row] != '#' and distances.get(next_position, float('inf')) >= next_cost:
                    distances[next_position] = next_cost
                    heappush(heap, (next_cost, current_path + [(next_row, next_col)], next_delta_x, next_delta_y))

    return len(best_path)

input_data = open("small.in").read().split("\n")
grid = [list(row) for row in input_data]

start, end = (0, 0), (0, 0)
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        if grid[row_index][col_index] == "S":
            start = (row_index, col_index)
        if grid[row_index][col_index] == "E":
            end = (row_index, col_index)

print(dijkstra_revamped(start, end, grid))
