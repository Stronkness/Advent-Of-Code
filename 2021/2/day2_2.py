commands = open('input').read().split('\n')
x,y,aim = 0,0,0

for command in commands:
    nbr = int(command[-1]) # exploit that its single digits
    if command.startswith("forward"):
        x += nbr
        y += aim * nbr
    elif command.startswith("up"):
        aim -= nbr
    else: # down
        aim += nbr

print(x*y)