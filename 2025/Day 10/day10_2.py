from scipy.optimize import linprog

ans = 0
lines = open("test.in").read().splitlines()

for line in lines:
    parts = line.split()

    buttons_raw = parts[1:-1]
    jolts_raw = parts[-1][1:-1]

    buttons = []
    for btn in buttons_raw:
        buttons.append(eval(btn[:-1] + ",)"))

    jolts = eval(jolts_raw)

    costs = []
    for _ in buttons:
        costs.append(1)

    eqs = []
    for i in range(len(jolts)):
        row = []
        for bset in buttons:
            row.append(i in bset)
        eqs.append(row)

    result = linprog(costs, A_eq=eqs, b_eq=jolts, integrality=1)
    ans += result.fun

print(int(ans))
