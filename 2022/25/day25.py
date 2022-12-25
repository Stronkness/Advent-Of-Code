console_input = open('input').read().split('\n')
res_number = 0
for weird_math_line in console_input:
    temp = 0
    for char in weird_math_line:
        temp *= 5
        if char == '=':
            temp += -2
        elif char == '-':
            temp += -1
        elif char == '1':
            temp += 1
        elif char == '2':
            temp += 2
        else:
            continue # '0'
    res_number += temp

value = []
decimals = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2'
}
while res_number > 0:
    remainder = res_number % 5
    if remainder > 2:
        res_number += remainder
        value.append(decimals[remainder - 5])
    else:
        value.append(str(remainder))

    res_number //= 5
    
print(''.join(reversed(value)))
