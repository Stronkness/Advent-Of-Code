import collections

input = open("small.in").read().split("\n")
antennas = collections.defaultdict(list)
for y, row in enumerate(input):
    for x, freq in enumerate(row):
        if freq != '.':
            antennas[freq].append({"x": x, "y": y})

antinodes = set()
for antenna, positions in antennas.items():
    for i, pos_1 in enumerate(positions):
        for j, pos_2 in enumerate(positions):
            if i == j: # Same antenna == no no
                continue

            d_x = pos_2["x"] - pos_1["x"]
            d_y = pos_2["y"] - pos_1["y"]

            antinode_x = pos_1["x"] + d_x * 2 # Twice the X-value, current antenna (i) which we are checking
            antinode_y = pos_1["y"] + d_y * 2 # Twice the Y-value, -||-

            if 0 <= antinode_x <= len(input[0]) - 1 and 0 <= antinode_y <= len(input[1]) - 1: # Within grid
                antinodes.add((antinode_x, antinode_y))

print(len(antinodes))
