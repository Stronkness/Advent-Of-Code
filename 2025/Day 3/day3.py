input = open("test.in").read().split('\n')
ans = 0

for banks in input:
    batteries = list(map(int, banks))
    max_battery = max(batteries)
    idx_of_max = batteries.index(max_battery)

    if idx_of_max == len(batteries) - 1:
        max_battery, next_max_battery = max(batteries[:-1][::-1]), max_battery
    else:
        next_max_battery = max(batteries[idx_of_max+1:])

    ans += int(str(max_battery) + str(next_max_battery))

print(ans)
