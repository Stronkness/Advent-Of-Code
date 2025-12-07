from collections import defaultdict

grid = open("test.in").read().split("\n")
beams = defaultdict(bool)
beams[grid[0].index("S")] = True
splits = 0

for y in range(len(grid)-1):
    for x, _ in list(beams.items()):
        tile = grid[y+1][x]

        if tile == "^":
            beams[x-1] = True
            beams[x+1] = True
            beams.pop(x)
            splits += 1

print(splits)
