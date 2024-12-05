import re

input = open("large.in").read()
regex = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", input)
sum = 0
multiply = True
for mul in regex:
    mult = re.findall(r'\D+|\d+', mul)
    if len(mult) == 1: # do dont
        if mult[0] == "don't()":
            multiply = False
        elif mult[0] == "do()":
            multiply = True
    if multiply:
        tmp_sum = 1
        for num in mult:
            if num.isdigit():
                tmp_sum *= int(num)
        if tmp_sum != 1:
            sum += tmp_sum
print(sum)