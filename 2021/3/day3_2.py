binaries = open('input').read().split('\n')

curr_len = 0
copy_binaries = binaries
while True:
    if len(copy_binaries) == 1:
        oxygen_rating = copy_binaries[0]
        curr_len = 0
        copy_binaries = binaries
        break

    ones = 0
    zeros = 0
    for i, binary in enumerate(copy_binaries):
        if binary[curr_len] == '0':
            zeros += 1
        else:
            ones += 1
    if ones > zeros or ones == zeros:
        co2_flag = True
    else:
        co2_flag = False

    temp = []
    for binary in copy_binaries:
        if co2_flag and binary[curr_len] == '1':
            temp.append(binary)
        elif not co2_flag and binary[curr_len] == '0':
            temp.append(binary)

    copy_binaries = temp
    curr_len += 1


while True:
    if len(copy_binaries) == 1:
        co2_rating = copy_binaries[0]
        break

    ones = 0
    zeros = 0
    for i, binary in enumerate(copy_binaries):
        if binary[curr_len] == '0':
            zeros += 1
        else:
            ones += 1
    if ones > zeros or ones == zeros:
        co2_flag = True
    else:
        co2_flag = False

    temp = []
    for binary in copy_binaries:
        if co2_flag and binary[curr_len] == '0':
            temp.append(binary)
        elif not co2_flag and binary[curr_len] == '1':
            temp.append(binary)

    copy_binaries = temp
    curr_len += 1

oxygen_rating = int(oxygen_rating, 2)
co2_rating = int(co2_rating, 2)
print(oxygen_rating*co2_rating)
