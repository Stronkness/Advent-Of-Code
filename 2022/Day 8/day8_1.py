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
for i in range(height):
    for j in range(width):
        # This is to remove the effect of double increment "Count edges"
        if i == 0 or j == 0 or i == height-1 or j == width-1:
            continue
        else:
            row = grid[i]
            col = [x[j] for x in grid]
            current_tree = grid[i][j]
            
            top = col[:i]
            bottom = col[i+1:]
            left = row[:j]
            right = row[j+1:]

            top = get_max(top)
            bottom = get_max(bottom)
            left = get_max(left)
            right = get_max(right)

            if top < current_tree or bottom < current_tree or left < current_tree or right < current_tree:
                visible_trees += 1

print(visible_trees)
