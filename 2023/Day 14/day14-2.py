import copy

maps = open('input', 'r').read().strip().splitlines()
grid = {(r,c): x for r, row in enumerate(maps) for c, x in enumerate(row)}

def move_rocks_north(): # DONE
    moved = True
    while moved:
        moved = False
        for row in range(1, len(maps)):
            for col in range(len(maps[0])):
                if not grid[(row, col)] == 'O':  # no rocky
                    continue
                if grid[(row-1,col)] == '.':
                    grid[(row-1, col)] = 'O'
                    grid[(row, col)] = '.'
                    moved = True

def move_rocks_west():
    moved = True
    while moved:
        moved = False
        for row in range(len(maps)):
            for col in range(1,len(maps[0])):
                if not grid[(row, col)] == 'O':  # no rocky
                    continue
                if grid[(row,col-1)] == '.':
                    grid[(row, col-1)] = 'O'
                    grid[(row, col)] = '.'
                    moved = True

def move_rocks_south():
    moved = True
    while moved:
        moved = False
        for row in range(len(maps)-1):
            for col in range(len(maps[0])):
                if not grid[(row, col)] == 'O':  # no rocky
                    continue
                if grid[(row+1,col)] == '.':
                    grid[(row+1, col)] = 'O'
                    grid[(row, col)] = '.'
                    moved = True

def move_rocks_east():
    moved = True
    while moved:
        moved = False
        for row in range(len(maps)):
            for col in range(len(maps[0])-1):
                if not grid[(row, col)] == 'O':  # no rocky
                    continue
                if grid[(row,col+1)] == '.':
                    grid[(row, col+1)] = 'O'
                    grid[(row, col)] = '.'
                    moved = True


cycle = 0
visited_grids = []
load_cycles = []
cycle_cache = {}
cycles = 1000000000
while cycle < cycles:
    move_rocks_north()
    move_rocks_west()
    move_rocks_south()
    move_rocks_east()
    cycle += 1

    if grid in visited_grids: # To easily determine a cycle has appeared
        grid_pattern = ''
        for x in grid:
            grid_pattern += grid[x]
        # Cycle detection
        cycle_length = cycle - cycle_cache[grid_pattern]
        cycle += cycle_length * ((cycles - cycle) // cycle_length) # Formula found on Reddit
        """
        ChatGPT states:
        cycle += cycle_length * ((cycles - cycle) // cycle_length): This adjusts the cycle number based on the length of the cycle. 
        It effectively jumps forward by a multiple of the cycle length to skip redundant iterations. 
        This is a common optimization when dealing with repeating patterns.
        """
        last_cycle_length = cycle - cycle_length

    visited_grids.append(copy.deepcopy(grid))
    depth = len(maps[0])
    tmp = 0
    for object_loc in grid:
        if grid[object_loc] == 'O':
            row,col = object_loc
            tmp += depth - row
    load_cycles.append(tmp)
    
    grid_pattern = ''
    for x in grid:
        grid_pattern += grid[x]
    cycle_cache[grid_pattern] = cycle
    


print(load_cycles[last_cycle_length-1])
# 96105
