input = open("test.in").read().splitlines()
rows = [line[::-1] for line in input] # reverse as their math works that way lol
ans = 0
cur_vals = []
for col in zip(*rows): # column wise as their math works that way too
    num_str = "".join(col[:-1]).strip()
    if not num_str.isdigit():
        continue

    value = int(num_str)
    cur_vals.append(value)
    op = col[-1]
    res = 0
    if op == "+":
        for num in cur_vals:
            res += num
        ans += res
        cur_vals = []
    elif op == "*":
        res = 1
        for num in cur_vals:
            res *= num
        ans += res
        cur_vals = []

print(ans)
