sweeps = open('input').read().split('\n')

increases = 0
for i in range(len(sweeps)):
    current = sum((int(x) for x in sweeps[i:i+3]))

    if i == 0:
        previous = current
        continue

    if current > previous:
        increases += 1
    previous = current

print(increases)