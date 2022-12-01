#!/usr/bin/env python3

supplies = open('input.txt').read().split("\n\n")

sum_array = []
for index, item in enumerate(supplies):
    splitter = item.split("\n")
    temp = [int(x) for x in splitter]
    sum_array.append(sum(temp))

print(max(sum_array))
sum_array.sort()
print(sum(sum_array[-3:]))
