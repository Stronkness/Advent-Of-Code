sequence = open('input', 'r').read().split(',')

hash_values = []
for seq in sequence:
    current_value = 0
    for ch in seq:
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256
    hash_values.append(current_value)

print(sum(hash_values))