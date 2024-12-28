input = open("large.in").read().strip().split('\n\n')
locks = []
keys = []

for schematic in input:
    column_counts = [column.count('#') for column in zip(*schematic.split('\n'))]

    if schematic.startswith('#'):
        locks.append(column_counts)
    else:
        keys.append(column_counts)

compatible_count = 0
for lock in locks:
    for key in keys:
        if all(sum(pair) <= 7 for pair in zip(lock, key)):
            compatible_count += 1

print(compatible_count)
