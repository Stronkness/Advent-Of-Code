rocks = open('input').read().split('\n')
y_max = 0
blocked = set()

# Prepare rock blockage
for rock in rocks:
    rock = rock.split(' -> ')
    for i in range(len(rock) - 1):
        x0,y0 = rock[i].split(',')
        x1,y1 = rock[i+1].split(',')

        x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)

        for j in range(min((x0),x1), max(x0,x1)+1):
            blocked.add((j,y0))
        for k in range(min(y0,y1), max(y0,y1)+1):
            blocked.add((x0,k))
        y_max = max(y_max, y1)

# Prepare rock blockage floor
for i in range(5000): # random number, i dont know how long you're supposed to draw this, the problem states that it's infinite...
    blocked.add((i,y_max+2)) # plus 2 is as stated in the problem information, y = 2 + max(y)

# I don't like sand. It's course and rough and irritating. And it gets everywhere
start = (500, 0)
units_of_sand = 0
while True:
    x,y = start
    while True:
        if (x, y+1) not in blocked:
            y += 1
            continue
        elif (x-1, y+1) not in blocked:
            x -= 1
            y += 1
            continue
        elif (x+1, y+1) not in blocked:
            x += 1
            y += 1
            continue
        else:
            blocked.add((x,y))
            units_of_sand += 1
            break # blockage, can't move, save position and add one unit

    if (x,y) == start:
        break

print(units_of_sand)
