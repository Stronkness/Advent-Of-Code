input = open("large.in").read().split("\n")
safe = 0
yay = []
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
                
            else:
                exit = True
        
        # brute force and check every number if it creates a safe path, copy pasta code
        skip = False
        passed_level = False
        if exit:

            for id, _ in enumerate(levels):
                exit = False
                increase, decrease = False, False
                if passed_level:
                    skip = True
                    break

                temp_levels = list(levels)
                temp_levels.pop(id)

                for check_idx, check_level in enumerate(temp_levels):
                    if check_idx == len(temp_levels)-1 and exit == False:
                        passed_level = True
                        break

                    if exit: break

                    current_level = int(check_level)
                    next_level = int(temp_levels[check_idx+1])

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
        if skip:
            safe += 1
            break

print(safe)
