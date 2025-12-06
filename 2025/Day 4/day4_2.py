input = open("test.in").read().split("\n")
grid = [[x for x in row] for row in input]
cols, rows = len(grid[0]), len(grid)
rolls_of_paper = [(r,c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "@"]
answer = 0

while True:
    remove_paper_rolls = []
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
            remove_paper_rolls.append((roll_x, roll_y))
    
    if len(remove_paper_rolls) == 0:
        break

    answer += len(remove_paper_rolls)
    for (x, y) in remove_paper_rolls:
        if (x, y) in rolls_of_paper:
            rolls_of_paper.remove((x, y))
            grid[x][y] = "."

    remove_paper_rolls = []

print(answer)           
