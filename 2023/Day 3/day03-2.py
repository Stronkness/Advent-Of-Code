from collections import defaultdict

def valid_move(y,x):
    if x < 0 or y < 0:
        return False

    if not (0 <= x < grid_length and 0 <= y < grid_length):
        return False
    
    if grid[y][x] == "*":
        return True

    return False

moves = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, 1),   # down-right
    (1, -1),  # down-left
]

def check_matrix(row,idx,number):
    num_length = len(number)
    for i in range(num_length):
        for (y,x) in moves:
            new_x, new_y = idx + x - i, row + y
            valid = valid_move(new_y, new_x)
            if valid:
                gears[(new_y, new_x)].append(number)

def main():
    global grid, grid_length, gears
    map_data = open('input', 'r').read().splitlines()
    grid = [list(row) for row in map_data]
    grid_length = len(grid[0])
    gears = defaultdict(list)
    S = 0

    for row, path in enumerate(grid):
        number = ""
        for idx, tile in enumerate(path):
            if tile.isnumeric():
                number += tile
            else:
                number = ""

            if idx != grid_length - 1 and (number and not path[idx + 1].isnumeric()):
                check_matrix(row, idx, number)
            elif idx == grid_length - 1 and number:  # Edge case of numbers at the end of the row
                check_matrix(row, idx, number)
    
    for gear in gears:
        gear = set(gears[gear])
        if len(gear) == 2:
            part1, part2 = gear
            S += int(part1)*int(part2)

    print(S)

if __name__ == "__main__":
    main()
