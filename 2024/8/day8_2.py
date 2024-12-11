import collections

input = open("large.in").read().split("\n")
antennas = collections.defaultdict(list)
for y, row in enumerate(input):
    for x, freq in enumerate(row):
        if freq != '.':
            antennas[freq].append({"x": x, "y": y})

antinodes = set()
for antenna, positions in antennas.items():
    for i, pos_1 in enumerate(positions):
        for j, pos_2 in enumerate(positions):
            d_x = pos_2["x"] - pos_1["x"]
            d_y = pos_2["y"] - pos_1["y"]


            # As the grid is 50x50, we iterate from the antenna and a total of 100 units (50, -50) from the location to simulate the harmonics
            for i in range(-50,50):
                antinode_x = pos_1["x"] + d_x * 2 * i # Twice the X-value, current antenna (i) which we are checking
                antinode_y = pos_1["y"] + d_y * 2 * i # Twice the Y-value, -||-
                if 0 <= antinode_x <= len(input[0]) - 1 and 0 <= antinode_y <= len(input[1]) - 1: # Within grid
                    antinodes.add((antinode_x, antinode_y))

print(len(antinodes))
