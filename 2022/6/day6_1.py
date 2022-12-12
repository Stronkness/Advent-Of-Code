sequence = open('input').read()

index = 0
for i in range(len(sequence)):
    if len(set(sequence[i:i+4])) == 4: # four letters for sequence
        index = i+4
        break

print(index)