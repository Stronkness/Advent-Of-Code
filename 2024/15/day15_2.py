DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def check_movable(grid, row, col, delta_row, delta_col, visited):
    if (row, col) in visited:
        return True

    visited.add((row, col))
    next_row, next_col = row + delta_row, col + delta_col

    if grid[next_row][next_col] == "#":
        return False
    elif grid[next_row][next_col] == "[":
        return check_movable(grid, next_row, next_col, delta_row, delta_col, visited) and check_movable(grid, next_row, next_col + 1, delta_row, delta_col, visited)
    elif grid[next_row][next_col] == "]":
        return check_movable(grid, next_row, next_col, delta_row, delta_col, visited) and check_movable(grid, next_row, next_col - 1, delta_row, delta_col, visited)
        
    return True

input = open("small.in").read().split("\n\n")
original_grid = [[char for char in line] for line in input[0].split("\n")]
moves = [move for row in input[1].split("\n") for move in row]

expanded_grid = []
char_transform = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}
for line in input[0].split("\n"):
    expanded_line = "".join(char_transform[char] for char in line)
    expanded_grid.append(list(expanded_line))
grid = expanded_grid

robot_position = (0, 0)
for i, row in enumerate(grid):
    for j, r in enumerate(row):
        if r == '@':
            robot_position = (i,j)

for move in moves:
    delta_row, delta_col = DIRECTIONS[move]
    next_row, next_col = robot_position[0] + delta_row, robot_position[1] + delta_col

    if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != "#"):
        continue

    if grid[next_row][next_col] in ["[", "]"]:
        visited = set()

        if not check_movable(grid, robot_position[0], robot_position[1], delta_row, delta_col, visited):
            continue

        while visited:
            for obj_row, obj_col in visited.copy():
                new_obj_row, new_obj_col = obj_row + delta_row, obj_col + delta_col
                if (new_obj_row, new_obj_col) not in visited:
                    if grid[new_obj_row][new_obj_col] != "@" and grid[obj_row][obj_col] != "@":
                        grid[new_obj_row][new_obj_col] = grid[obj_row][obj_col]
                        grid[obj_row][obj_col] = "."

                    visited.remove((obj_row, obj_col))

        grid[robot_position[0]][robot_position[1]] = grid[next_row][next_col]
        grid[next_row][next_col] = grid[robot_position[0]][robot_position[1]]
        robot_position = (next_row, next_col)
        continue

    grid[robot_position[0]][robot_position[1]] = grid[next_row][next_col]
    grid[next_row][next_col] = grid[robot_position[0]][robot_position[1]]
    robot_position = (next_row, next_col)

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            result += 100 * i + j

print_grid(grid)
print(result)
