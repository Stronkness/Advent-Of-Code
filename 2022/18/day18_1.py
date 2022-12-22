droplets = open('input').read().split('\n')
cubes = []

for droplet in droplets:
    droplet = droplet.split(',')
    cubes.append([int(droplet[0]), int(droplet[1]), int(droplet[2])])

sum = 0
for x,y,z in cubes:
    if [x+1, y, z] not in cubes:
        sum += 1
    if [x-1, y, z] not in cubes:
        sum += 1
    if [x, y+1, z] not in cubes:
        sum += 1
    if [x, y-1, z] not in cubes:
        sum += 1
    if [x, y, z+1] not in cubes:
        sum += 1
    if [x, y, z-1] not in cubes:
        sum += 1

print(sum)
# This code is a bit embarassing :P
