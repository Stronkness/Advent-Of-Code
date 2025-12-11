from functools import cache

@cache
def dfs(cur, found_dac, found_fft):
    if cur == 'out':
        if found_dac and found_fft:
            return 1
        return 0

    if cur == 'dac':
        found_dac = True
    elif cur == 'fft':
        found_fft = True

    total = sum(map(lambda edge: dfs(edge, found_dac, found_fft), graph[cur]))
    return total


input = open('test.in').read().split('\n')
graph = {}
for line in input:
    start, conn = line.split(': ')
    graph[start] = conn.split(' ')

ans = dfs('svr', False, False)
print(ans)
