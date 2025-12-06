input = open("test.in").read().split('\n')
ans = 0

for banks in input:
    batteries = list(map(int, banks))
    jolts = 0
    start = 0
    for remaining in range(12, 0, -1):
        end = len(batteries) - remaining + 1
        max_idx = start
        for i in range(start + 1, end):
            if batteries[i] > batteries[max_idx]:
                max_idx = i

        jolts += batteries[max_idx] * (10 ** (remaining - 1))
        start = max_idx + 1

    ans += jolts
    
print(ans)
