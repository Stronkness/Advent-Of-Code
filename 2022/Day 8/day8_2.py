tree_heights = open('input').read().split('\n')

grid = []
scenic_score = 0

def scenic(direction, tree):
    count = 0
    for ele in direction:
        if tree > ele:
            count += 1
        elif tree == ele or tree < ele:
            count += 1
            break
    return count 

for tree in tree_heights:
    grid.append([int(x) for x in tree])

width = len(grid[0])
height = len(grid)

# Count inside edges
for i in range(height):
    for j in range(width):
        row = grid[i]
        col = [x[j] for x in grid]
        current_tree = grid[i][j]
            
        top = col[:i][::-1] # Reverse it
        bottom = col[i+1:]
        left = row[:j][::-1] # Reverse it
        right = row[j+1:]

        top = scenic(top, current_tree)
        bottom = scenic(bottom, current_tree)
        left = scenic(left, current_tree)
        right = scenic(right, current_tree)

        new_scenic_score = top*bottom*left*right
        if new_scenic_score > scenic_score:
            scenic_score = new_scenic_score

print(scenic_score)
