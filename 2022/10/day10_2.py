X = 1
cycle = 0

X_progress = [X]

instructions = open('input').read().split('\n')

for _, execution in enumerate(instructions, 1):
    if execution == 'noop':
        X_progress.append(X)

    else: # addx
        _, V = execution.split(" ")

        X_progress.extend([X,X]) # add two X's because of two clock cycles
        X += int(V)

for y in range(6): # rows
    crt = ''
    for x in range(40): # cols
        cycle = x + y * 40 # current index in cols but the row in y*40 indicated the rows divisble by 40. For e.g y*2 = 80 which means row 2
        if abs(X_progress[cycle + 1] - x) <= 1:
            crt += '#'
        else:
            crt += '.'
    print(crt)
