X = 1
signal_strength = 0
cycle = 0

instructions = open('input').read().split('\n')

for _, execution in enumerate(instructions, 1):
    if execution == 'noop':
        cycle += 1
        if cycle % 40 == 20: # Thresholds for signal_strength
            signal_strength += X*cycle

    else: # addx
        _, V = execution.split(" ")

        # Two clock cycles for this instruction
        cycle += 1
        if cycle % 40 == 20: # Thresholds for signal_strength
            signal_strength += X*cycle

        cycle += 1
        if cycle % 40 == 20: # Thresholds for signal_strength
            signal_strength += X*cycle

        X += int(V)

print(signal_strength)
