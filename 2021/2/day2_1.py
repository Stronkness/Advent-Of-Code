commands = open('input').read().split('\n')
x,y = 0,0

for command in commands:
    nbr = int(command[-1]) # exploit that its single digits
    if command.startswith("forward"):
        x += nbr
    elif command.startswith("up"):
        y -= nbr
    else: # down
        y += nbr

print(x*y)