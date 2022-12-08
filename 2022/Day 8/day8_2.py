tree_heights = open('input').read().split('\n')

grid = []
visible_trees = 0

def get_max(list):
    maximum = 0
    for item in list:
        if item > maximum:
            maximum = item
    return maximum

for tree in tree_heights:
    grid.append([int(x) for x in tree])

# Count edges
for i in range(len(grid)):
    if i == 0 or i == len(grid)-1:
        for tree in grid[i]:
            visible_trees += 1
    else:
        visible_trees += 2

width = len(grid[0])
height = len(grid)

# Count inside edges
for y in range(height):
    for x in range(width):
        # This is to remove the effect of double increment "Count edges"
        if y == 0 or x == 0 or y == height-1 or x == width-1:
            continue
        else:
            row = grid[y]
            col = [yeet[x] for yeet in grid]
            current_tree = grid[y][x]
            
            top = col[:y]
            bottom = col[y+1:]
            left = row[:x]
            right = row[x+1:]

            top = get_max(top)
            bottom = get_max(bottom)
            left = get_max(left)
            right = get_max(right)

            if top < current_tree or bottom < current_tree or left < current_tree or right < current_tree:
                visible_trees += 1

print(visible_trees)
