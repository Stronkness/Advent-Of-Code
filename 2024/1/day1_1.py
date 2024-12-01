file = open("large.in").read().split()
list_length = int(len(file) / 2)
list_1, list_2 = [], []
sum = 0
for i in range(list_length):
    idx = i*2
    list_1.append(int(file[idx]))
    list_2.append(int(file[idx + 1]))

for i in range(list_length):
    smallest, smallest_2 = min(list_1), min(list_2)
    list_1.remove(smallest)
    list_2.remove(smallest_2)

    sum += abs(smallest_2 - smallest)

print(sum)
