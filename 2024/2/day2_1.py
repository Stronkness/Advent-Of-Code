input = open("large.in").read().split("\n")
safe = 0
for row in input:
    levels = row.split(" ")
    exit = False
    increase, decrease = False, False
    for idx, level in enumerate(levels):
        if idx == len(levels)-1 and exit == False:
            safe += 1
            break

        if exit: break

        current_level = int(level)
        next_level = int(levels[idx+1])

        if current_level == next_level:
            exit = True
            continue
        
        if current_level > next_level:
            if 1 <= abs(current_level - next_level) <= 3:
                if increase:
                    exit = True
                decrease = True
            else:
                exit = True

        
        if current_level < next_level:
            if 1 <= abs(current_level - next_level) <= 3:
                if decrease:
                    exit = True
                increase = True
                continue
            else:
                exit = True

print(safe)
