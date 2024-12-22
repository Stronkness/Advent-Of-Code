input = list(map(int,open("large.in").read().strip().split("\n")))
secret_numbers = []
for num in input:

    for _ in range(2000):
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
    
    secret_numbers.append(num)

print(sum(secret_numbers))