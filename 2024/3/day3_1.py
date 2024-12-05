import re

input = open("large.in").read()
regex = re.findall("mul\(\d+,\d+\)", input)
sum = 0
for mul in regex:
    mult = re.findall(r'\D+|\d+', mul)
    tmp_sum = 1
    for num in mult:
        if num.isdigit():
            tmp_sum *= int(num)
    sum += tmp_sum
print(sum)