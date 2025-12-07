input = open("test.in").read().split("\n")
size = len(input)
rows = [list(map(int, line.split())) for line in input[:size-1]]
operator = [x for x in input[size-1].split()]
ans = 0
for idx, op in enumerate(operator):
    if op == "*":
        res = 1
        for row in rows:
            res *= row[idx]
    else: # +
        res = 0
        for row in rows:
            res += row[idx]

    ans += res

print(ans)