data = open('input', 'r').read().splitlines()
galaxies = [[x for x in row] for row in data]
r_len = len(galaxies)
c_len = len(galaxies[0])

# Empty row and cols
empty_rows = []
empty_cols = [0 for _ in range(c_len)]

for i,row in enumerate(galaxies):
    if row.count('.') == len(row):
        empty_rows.append(i)

    for j,c in enumerate(row):
        if c == '.':
            empty_cols[j] += 1
tmp = []
for idx, c in enumerate(empty_cols):
    if c == c_len:
        tmp.append(idx)
empty_cols = tmp
#####

# Assign every galaxy to a set
galaxy_idxs = set()
for i, row in enumerate(galaxies):
    for j, c in enumerate(row):
        if c == '#':
            galaxy_idxs.add((i,j))
print(galaxy_idxs)
#####

# Assign pairs (combinations) and apply expanding universe
pairs = set()
for galaxy1 in galaxy_idxs:
    for galaxy2 in galaxy_idxs:
        g1_x, g1_y = galaxy1
        g2_x, g2_y = galaxy2

        expanded_universe_rows_1 = 0
        expanded_universe_rows_2 = 0
        expanded_universe_cols_1 = 0
        expanded_universe_cols_2 = 0

        for r in empty_rows:
            horizontal_dist = range(min(g1_x, g2_x), max(g1_x, g2_x))
            if r in horizontal_dist:
                if g2_x > r:
                    expanded_universe_rows_2 += 999999
                else:
                    expanded_universe_rows_1 += 999999

        for c in empty_cols:
            vertical_dist = range(min(g1_y, g2_y), max(g1_y, g2_y))
            if c in vertical_dist:
                if g2_y > c:
                    expanded_universe_cols_2 += 999999
                else:
                    expanded_universe_cols_1 += 999999

        pairs.add(tuple(sorted([(g1_x + expanded_universe_rows_1, g1_y + expanded_universe_cols_1),
                                (g2_x + expanded_universe_rows_2, g2_y + expanded_universe_cols_2)])))


#####


"""
Part 2

You one galaxy x1;y1, then take another x2;y2, then trace from
y = y1 to y2, x = x1 to x2 and increase length by 1, but then
check if point x;y is expandable (no galaxies vertical OR horisontal)
increase path by 999_999 (part2), thats all, no really need to expand array
or something else
"""
# Find shortest path and apply expanding universe
total = 0
for pair in pairs:
    galaxy1, galaxy2 = pair
    path_len = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    expanded_universe_rows = 0
    expanded_universe_cols = 0
    total += path_len + expanded_universe_cols + expanded_universe_rows
#####



# 630728425490
print(total)