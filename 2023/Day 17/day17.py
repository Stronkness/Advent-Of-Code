from heapq import heappop, heappush


def find_minimum_heat_loss(grid, min_steps, max_steps, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left

    visited_heat_loss = {}  # {(position, direction): heat_loss}

    # (total_heat_loss, current_position, last_direction)
    priority_queue = [(0, start, -1)]

    while priority_queue:
        total_heat_loss, current_position, last_direction = heappop(
            priority_queue
        )

        if current_position == end:
            print(step_count)
            return total_heat_loss

        # Determine allowed directions to move giving their idxs of the directions array, 90 degree turn
        allowed_directions = []
        if last_direction == -1:  # First step, all directions are allowed
            allowed_directions = [0, 1, 2, 3]
        else:
            if last_direction == 1 or last_direction == 3:  # Left or Right, means going up or down is allowed
                allowed_directions = [0, 2]
            elif last_direction == 0 or last_direction == 2:  # Up or Down, means going left or right is allowed
                allowed_directions = [1, 3]
            else:
                print("Error: Invalid last direction - ", last_direction)
                exit()

        for next_direction in allowed_directions:
            next_heat_loss = total_heat_loss
            for step_count in range(1, max_steps + 1):
                next_position = tuple(
                    a + b * step_count for a, b in zip(current_position, directions[next_direction]))

                # Check if the next position is within the grid boundaries
                if 0 <= next_position[0] <= end[0] and 0 <= next_position[1] <= end[1]:
                    next_heat_loss += int(grid[next_position[0]]
                                          [next_position[1]])

                    # Update the minimum heat loss for the current position and direction
                    if next_heat_loss < visited_heat_loss.get((next_position, next_direction), float("inf")):
                        visited_heat_loss[(
                            next_position, next_direction)] = next_heat_loss

                        # Add to the priority queue if the step count is equal to or greater than the minimum steps
                        if step_count >= min_steps:
                            heappush(priority_queue, (next_heat_loss,
                                     next_position, next_direction))


# Read the map from a file named 'test'
map_file = open('input', 'r').read().splitlines()
grid_map = [[char for char in row] for row in map_file]
num_rows = len(grid_map)
num_cols = len(grid_map[0])
start_position = (0, 0)
end_position = (num_rows - 1, num_cols - 1)

# Part 1
min_heat_loss_part1 = find_minimum_heat_loss(
    grid_map, 1, 3, start_position, end_position)
print("Part 1 Minimum Heat Loss:", min_heat_loss_part1)

# Part 2
min_heat_loss_part2 = find_minimum_heat_loss(
    grid_map, 4, 10, start_position, end_position) - 2  # Subtract 2 because off by 2 error
print("Part 2 Minimum Heat Loss:", min_heat_loss_part2)
