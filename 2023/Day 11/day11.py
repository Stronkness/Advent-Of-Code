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

# Expand the universe
for i in reversed(empty_rows):
    galaxies.insert(i+1, ['.' for _ in range(c_len)])

for index in reversed(empty_cols):
    adjusted_index = index
    for row in galaxies:
        row.insert(adjusted_index, '.')
#####

# Assign every galaxy to a set
galaxy_idxs = set()
for i, row in enumerate(galaxies):
    for j, c in enumerate(row):
        if c == '#':
            galaxy_idxs.add((i,j))
#####

# Assign pairs (combinations)
pairs = set()
for galaxy1 in galaxy_idxs:
    for galaxy2 in galaxy_idxs:
        if galaxy1 > galaxy2:
            pairs.add(tuple(sorted([galaxy1, galaxy2])))
#####

# Find shortest path
total = 0
for pair in pairs:
    galaxy1, galaxy2 = pair
    path_len = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    total += path_len
#####

# 9686930
print(total)