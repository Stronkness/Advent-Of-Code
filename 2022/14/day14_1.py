rocks = open('input').read().split('\n')
blocked = set()

# Prepare rock blockage
for rock in rocks:
    rock = rock.split(' -> ')
    for i in range(len(rock) - 1):
        x0,y0 = rock[i].split(',') # curr
        x1,y1 = rock[i+1].split(',') # prev

        x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)

        for j in range(min((x0),x1), max(x0,x1)+1):
            blocked.add((j,y0))
        for k in range(min(y0,y1), max(y0,y1)+1):
            blocked.add((x0,k))

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

    if (x,y) == start: # well this doesn't work in this part...
        break
    print(units_of_sand)

# Goes into a infinite loop, hence the print of units_of_sand inside the while-loop, prints out the right answer but doesnt stop.
# Could be the infinite dark void beneath that does this as P2 can execute properly, maybe find a maximum y which needs to be bigger than current y to not go into endless loop?
print(units_of_sand)
