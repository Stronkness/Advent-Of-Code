disk_map = open("large.in").read() # Part 2 takes around 30 seconds to run

# Step 1: Represent blocks
block_scheme = []
free_space = False
id = 0
for digit in disk_map:
    if free_space:
        block_scheme.extend(['.'] * int(digit))
        free_space = False
    else:
        block_scheme.extend([str(id)] * int(digit))
        id += 1
        free_space = True

# Step 2: Move files in descending order of file ID
file_sizes = {}
for idx, block in enumerate(block_scheme):
    if block != '.':
        file_sizes[block] = file_sizes.get(block, 0) + 1

# Descending order from highest id to lowest
file_ids = sorted(file_sizes.keys(), key=int, reverse=True)

for file_id in file_ids:
    file_size = file_sizes[file_id]
    file_positions = []
    for pos, block in enumerate(block_scheme):
        if block == file_id:
            file_positions.append(pos)

    free_start = -1
    free_count = 0
    for idx, block in enumerate(block_scheme):
        if block == '.':
            if free_start == -1:
                free_start = idx
            free_count += 1

            if free_count == file_size:
                if all(pos >= free_start + file_size for pos in file_positions):
                    for pos in file_positions:
                        block_scheme[pos] = '.'
                    for i in range(free_start, free_start + file_size):
                        block_scheme[i] = file_id

                break
        else: # Restart free position
            free_start = -1
            free_count = 0

# Step 3: Calculate the checksum
checksum = 0
for idx, block in enumerate(block_scheme):
    if block == '.': continue
    checksum += idx * int(block)

print(checksum)
