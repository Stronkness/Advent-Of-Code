from collections import defaultdict

grid = open("test.in").read().split("\n")
beams = defaultdict(int)
beams[grid[0].index("S")] = 1

for y in range(len(grid)-1):
    new_beams = defaultdict(int)
    for x, count in beams.items():
        tile = grid[y+1][x]

        # Counting how many timelines we go through this specific beam
        if tile == "^":
            new_beams[x-1] += count
            new_beams[x+1] += count
        else:
            new_beams[x] += count

    beams = new_beams

print(sum(beams.values()))
