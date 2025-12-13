import math
import itertools

points = [tuple(map(int, line.split(","))) for line in open('test.in').read().strip().splitlines()]
n = len(points)

# Build all edges
edges = []
for i, j in itertools.combinations(range(n), 2):
    x1, y1, z1 = points[i]
    x2, y2, z2 = points[j]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    edges.append((dist, i, j))

edges.sort(key=lambda e: e[0])

# Union-Find (DSU)
parent = list(range(n))
rank = [0]*n
components = n

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    global components
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    components -= 1
    return True

# Process edges until fully connected
for _, i, j in edges:
    if union(i, j):
        if components == 1:
            x1 = points[i][0]
            x2 = points[j][0]
            print(x1 * x2)
            break
