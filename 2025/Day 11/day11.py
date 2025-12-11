input = open('test.in').read().split('\n')
graph = {}
for line in input:
    start, conn = line.split(': ')
    graph[start] = conn.split(' ')

queue = ['you']
paths = 0
for path in queue:
    if path == 'out':
        paths += 1
    else:
        for p in graph[path]:
            queue.append(p)

print(paths)
