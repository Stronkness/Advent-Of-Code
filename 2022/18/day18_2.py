def find_max(droplets, max):
    for i in droplets:
        if int(i) > max:
            max = int(i)
    return max

def find_min(droplets, min):
    for i in droplets:
        if int(i) < min:
            min = int(i)
    return min

droplets = open('input').read().split('\n')
cubes = []
sum = 0
neighbors = [[1, 0, 0], 
             [-1, 0, 0], 
             [0, 1, 0], 
             [0, -1, 0], 
             [0, 0, 1], 
             [0, 0, -1]]

for droplet in droplets:
    droplet = droplet.split(',')
    cubes.append([int(droplet[0]), int(droplet[1]), int(droplet[2])])

x_values, y_values, z_values = [], [], []
for droplet in droplets:
    droplet = droplet.split(',')
    x_values.extend([droplet[0]])
    y_values.extend([droplet[1]])
    z_values.extend([droplet[2]])

min_x = find_min(x_values, float("inf"))
min_y = find_min(y_values, float("inf"))
min_z = find_min(z_values, float("inf"))
max_x = find_max(x_values, -float("inf"))
max_y = find_max(y_values, -float("inf"))
max_z = find_max(z_values, -float("inf"))

# + 2 is for the maximum range of droplets + air cube
x_range = range(min_x - 1, max_x + 2)
y_range = range(min_y - 1, max_y + 2)
z_range = range(min_z - 1, max_z + 2)
q = [[min_x-1, min_y-1, min_z-1]] # aircube outside the droplets, 
visited = cubes

new_cubes = []
for elem in cubes:
    if elem not in new_cubes:
        new_cubes.append(elem)
cubes = new_cubes

while q:
    temp = q.pop(0)
    x, y, z = temp[0], temp[1], temp[2]
    if [x, y, z] in visited:
        continue

    visited.append([x, y, z])
    neighbor_droplets = [[x + dx, y + dy, z + dz] for dx, dy, dz in neighbors]
    sum += len([1 for nd in neighbor_droplets if nd in cubes])
    for nd in neighbor_droplets:
        if nd not in visited and nd[0] in x_range and nd[1] in y_range and nd[2] in z_range:
            q.append(nd)

print(sum)
