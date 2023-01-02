import re

input = open('testinput').read().split('\n\n')
bingo_numbers = input[0].split(',')
boards = []
for rows in input[1:]:
    rows = re.findall('[0-9]+', rows)
    board = []
    idx = 0
    for i in range(5):
        board.append((rows[i*5:i*5+5]))
    boards.append(board)

for nbr in bingo_numbers:
    for board in boards:
        for row in board:
            for i, row_nbr in enumerate(row):
                if row_nbr == nbr:
                    # Change rob_nbr to for example 'X', 
                    row[i] = 'X'
    print(boards)
    exit()
    # Check for bingo yes