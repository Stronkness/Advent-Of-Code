sequence = open('input').read()

index = 0
for i in range(len(sequence)):
    if len(set(sequence[i:i+14])) == 14: # four letters for sequence
        index = i+14
        break

print(index)