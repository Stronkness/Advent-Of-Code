input = open("large.in").read().strip()

graph = input.split('\n')
row_size = len(graph) # NOTE: 1 larger R further down
col_size = len(graph[0]) # NOTE: 1 larger C further down
sum = 0

""" The Pattern to be found to create X-MAS where the X is from the X form shape of letters
M.S
.A.
M.S
"""

for R in range(row_size):
    for C in range(col_size):
        if C+2 < col_size and R+2 < row_size and graph[R][C] == 'M' and graph[R][C+2] == 'S' and graph[R+1][C+1] == 'A' and graph[R+2][C] == 'M' and graph[R+2][C+2] == 'S': # Start top left and go to right and down
            sum += 1
        if C+2 < col_size and R+2 < row_size and graph[R][C] == 'S' and graph[R][C+2] == 'M' and graph[R+1][C+1] == 'A' and graph[R+2][C] == 'S' and graph[R+2][C+2] == 'M': # Start top right and go to left and down
            sum += 1
        if C+2 < col_size and R+2 < row_size and graph[R][C] == 'S' and graph[R][C+2] == 'S' and graph[R+1][C+1] == 'A' and graph[R+2][C] == 'M' and graph[R+2][C+2] == 'M': # Start bottom left and go to right and up
            sum += 1
        if C+2 < col_size and R+2 < row_size and graph[R][C] == 'M' and graph[R][C+2] == 'M' and graph[R+1][C+1] == 'A' and graph[R+2][C] == 'S' and graph[R+2][C+2] == 'S': # Start bottom right and go to left and up
            sum += 1
print(sum)