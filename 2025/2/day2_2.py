import re
regex = r'^(\d+)\1+$'

input = open("test.in").read().split(',')
answer = []

for pattern in input:
    low, high = pattern.split('-')  
    for num in range(int(low), int(high)+1):
        match = re.match(regex, str(num))
        if match is not None:
            answer.append(int(match.group(0)))

print(sum(answer))