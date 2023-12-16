maps = open('input', 'r').read().strip().splitlines()
grid = {(r,c): x for r, row in enumerate(maps) for c, x in enumerate(row)}

def move_up(row, col):
    if grid[(row-1,col)] == '.':
        grid[(row-1, col)] = 'O'
        grid[(row, col)] = '.'
        return True
    return False

def move_rocks():
    moved = True
    while moved:
        moved = False
        for row in range(1, len(maps)):
            for col in range(len(maps[0])):
                if not grid[(row, col)] == 'O':  # no rocky
                    continue
                moved = move_up(row, col) or moved

move_rocks()

load = 0
depth = len(maps[0])
for object_loc in grid:
    if grid[object_loc] == 'O':
        row,col = object_loc
        load += depth - row

print(load)
# 109596