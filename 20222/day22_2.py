from collections import defaultdict, deque

input = list(map(int,open("large.in").read().strip().split("\n")))
secret_numbers = defaultdict(int)
for num in input:
    window = deque()
    seen = set()
    for _ in range(2000):
        start = num % 10
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216

        window.append((num % 10, (num % 10) - start))

        if len(window) > 4:
            window.popleft()
        
        sequence = tuple([x[1] for x in window])
        if sequence in seen:
            continue
        seen.add(sequence)
        if len(sequence) == 4:
            secret_numbers[sequence] += window[-1][0]
    
print(max(secret_numbers.values()))

# Wrong on sample... correct on large ...