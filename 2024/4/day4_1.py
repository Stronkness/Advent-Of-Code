input = open("large.in").read().strip()

graph = input.split('\n')
row_size = len(graph) # NOTE: 1 larger R further down
col_size = len(graph[0]) # NOTE: 1 larger C further down
sum = 0

for R in range(row_size):
    for C in range(col_size):
        if C+3 < col_size and graph[R][C] == 'X' and graph[R][C+1] == 'M' and graph[R][C+2] == 'A' and graph[R][C+3] == 'S': # Left to Right
            sum += 1
        if C+3 < col_size and graph[R][C] == 'S' and graph[R][C+1] == 'A' and graph[R][C+2] == 'M' and graph[R][C+3] == 'X': # Right to Left
            sum += 1
        if R+3 < row_size and graph[R][C] == 'X' and graph[R+1][C] == 'M' and graph[R+2][C] == 'A' and graph[R+3][C] == 'S': # Up to Down
            sum += 1
        if R+3 < row_size and graph[R][C] == 'S' and graph[R+1][C] == 'A' and graph[R+2][C] == 'M' and graph[R+3][C] == 'X': # Down to up
            sum += 1
        if R+3 < row_size and C+3 < col_size and graph[R][C] == 'X' and graph[R+1][C+1] == 'M' and graph[R+2][C+2] == 'A' and graph[R+3][C+3] == 'S': # Up to Down \
            sum += 1
        if R+3 < row_size and C+3 < col_size and graph[R][C] == 'S' and graph[R+1][C+1] == 'A' and graph[R+2][C+2] == 'M' and graph[R+3][C+3] == 'X': # Up to Down \
            sum += 1
        if R-3 >= 0 and C+3 < col_size and graph[R][C] == 'S' and graph[R-1][C+1] == 'A' and graph[R-2][C+2] == 'M' and graph[R-3][C+3] == 'X': # Down to Up /
            sum += 1
        if R-3 >= 0 and C+3 < col_size and graph[R][C] == 'X' and graph[R-1][C+1] == 'M' and graph[R-2][C+2] == 'A' and graph[R-3][C+3] == 'S': # Down to Up /
            sum += 1
print(sum)