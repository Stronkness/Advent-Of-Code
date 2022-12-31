def find_zero_indexes(l):
    temp = []
    for e in l:
        temp.append(e[0])
    zero = temp.index(0)
    result = 0
    result += temp[(zero+1000) % (len(l))]
    result += temp[(zero+2000) % (len(l))]
    result += temp[(zero+3000) % (len(l))]
    return result

numbers = open('input').read().split('\n')
encrypted = []
zero_index = 0
for i,e in enumerate(numbers):
    encrypted.append((int(e), i))
    if int(e) == 0:
        zero_index = i

sum = 0
for i in range(len(encrypted)):
    if i == zero_index:
        continue
    idx = 0
    for j, (a,b) in enumerate(encrypted):
        if b == i:
            idx = j # index found for the next number to be moved
            break
    new = (idx + a) % (len(encrypted) - 1)
    encrypted.pop(idx)
    encrypted.insert(new, (a,b))

sum = find_zero_indexes(encrypted)
print(sum)
