"""
Had to rewrite the entire code for part 2 and check hints on Reddit. My part 1 code is not that good...
This part still uses DFS but we use it iteratively and not functions in functions wise. Makes it more readable.
It is a bit chaotic ...
"""
from collections import defaultdict

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
grid = [list(line) for line in open("large.in").read().splitlines()]
rows, cols = len(grid), len(grid[0])
visited = {}
result = 0

def iterative_dfs(start_x, start_y, region_id):
    stack = [(start_x, start_y)]
    visited[start_x, start_y] = region_id

    while stack:
        x, y = stack.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == grid[x][y]:
                visited[nx, ny] = region_id
                stack.append((nx, ny))

region_id = 0
for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            iterative_dfs(i, j, region_id)
            region_id += 1

regions = defaultdict(set)
for coord, region in visited.items():
    regions[region].add(coord)

for region_nodes in regions.values():
    area = len(region_nodes)
    perimeter = set()

    for x, y in region_nodes:
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols and (nx, ny) in region_nodes):
                perimeter.add(((x, y), (nx, ny)))

    reduced_perimeter = set()
    for edge1, edge2 in perimeter:
        is_valid = True
        for dx, dy in [(1, 0), (0, 1)]:
            neighbor1 = (edge1[0] + dx, edge1[1] + dy)
            neighbor2 = (edge2[0] + dx, edge2[1] + dy)
            if (neighbor1, neighbor2) in perimeter:
                is_valid = False
                break
        if is_valid:
            reduced_perimeter.add((edge1, edge2))

    result += area * len(reduced_perimeter)

print(result)
