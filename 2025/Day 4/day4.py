input = open("test.in").read().split("\n")
grid = [[x for x in row] for row in input]
cols, rows = len(grid[0]), len(grid)
rolls_of_paper = [(r,c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "@"]
answer = 0

for (roll_x, roll_y) in rolls_of_paper:
    neighbour = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            
            pos_row, pos_col = roll_x + i, roll_y + j
            if 0 <= pos_row < rows and 0 <= pos_col < cols:
                if grid[pos_row][pos_col] == "@":
                    neighbour += 1
    
    if neighbour <= 3:
        answer += 1

print(answer)           
