binaries = open('input').read().split('\n')
gamma_rate = ''
bin_len = len(binaries[0])
curr_len = 0
for _ in range(bin_len):
    ones = 0
    zeros = 0
    for i, binary in enumerate(binaries):
        if binary[curr_len] == '0':
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gamma_rate += '1'
    else:
        gamma_rate += '0'
    curr_len += 1

epilson_rate = int(''.join('0' if i == '1' else '1' for i in gamma_rate), 2)
gamma_rate = int(gamma_rate, 2)
print(gamma_rate*epilson_rate)