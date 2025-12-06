input = open("test.in").read().split(',')
answer = []

for pattern in input:
    low, high = pattern.split('-')  
    for num in range(int(low), int(high)+1):
        str_num = str(num)
        if len(str_num) % 2 == 0:
            if str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]:
                answer.append(num)

print(sum(answer))