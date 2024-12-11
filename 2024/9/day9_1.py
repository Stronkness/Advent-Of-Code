disk_map = open("large.in").read()

# Step 1: Represent blocks
block_scheme = list()
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

# Step 2: Rearrange blocks
last_digit = len(block_scheme) - 1
for idx, space in enumerate(block_scheme):
    if idx > last_digit:
        break
    if space == '.':
        while block_scheme[last_digit] == '.':
            last_digit -= 1
        block_scheme[idx] = block_scheme[last_digit]
        block_scheme[last_digit] = '.'
        last_digit -= 1

sequence = [block for block in block_scheme if block != '.']

# Step 3: Checksum calculation
checksum = 0
for id, seq in enumerate(sequence):
    checksum += id * int(seq)

print(checksum)
