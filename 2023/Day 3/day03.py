def valid_move(y,x):
    if x < 0 or y < 0:
        return False

    if not (0 <= x < grid_length and 0 <= y < grid_length):
        return False
    
    if grid[y][x].isnumeric():
        return False

    return True

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
    print("---------")
    print(number)
    for i in range(num_length):
        for (y,x) in moves:
            new_x, new_y = idx + x - i, row + y - i
            valid = valid_move(new_y, new_x)
            print(new_y, new_x)

    print("---------")    
    return True       



map = open('test', 'r').read().splitlines()

grid = [list(row) for row in map]
grid_length = len(grid[0])
used_numbers = set()
S = 0

for row, path in enumerate(grid):
    number = ""
    for idx, tile in enumerate(path):
        if tile.isnumeric():
            number += tile
        else:
            number = ""
                
        if idx != grid_length - 1:
            if number and not path[idx+1].isnumeric():
                if check_matrix(row,idx,number):
                    S += int(number)
                    number = ""
                    break
                
    
    
