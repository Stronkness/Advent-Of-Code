from functools import cache

input = open("large.in").read().strip().split("\n")
towels = []
designs = []
for i,x in enumerate(input):
    if i == 0:
        towels = x.split(", ")
    elif i == 1:
        continue
    else:
        designs.append(x)

@cache
def arrangements(pattern):
    if len(pattern) == 0:
        return 1
    
    pattern_arrangements = 0
    for towel in towels:
        if pattern.startswith(towel):
            pattern_arrangements += arrangements(pattern[len(towel):])

    return pattern_arrangements


result = 0
for pattern in designs:
    result += arrangements(pattern)

print(result)