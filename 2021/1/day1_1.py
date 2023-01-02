sweeps = open('input').read().split('\n')

increases = 0
for i,sonar in enumerate(sweeps[1:], 1):
    if int(sonar) > int(sweeps[i-1]):
        increases += 1
print(increases)