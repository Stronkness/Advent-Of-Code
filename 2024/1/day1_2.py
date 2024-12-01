file = open("large.in").read().split()
list_length = int(len(file) / 2)
list_1, list_2 = [], []
sum = 0
for i in range(list_length):
    idx = i*2
    list_1.append(int(file[idx]))
    list_2.append(int(file[idx + 1]))

for i in range(list_length):
    num = list_1[i]
    sum += list_2.count(num)*num

print(sum)
