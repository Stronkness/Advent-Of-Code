def manhattan_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def remove_overlaps(limitations):
    for i in range(len(limitations) - 1):
        if limitations[i][1] + 1 >= limitations[i + 1][0]:
            limitations[i] = (min(limitations[i][0], limitations[i + 1][0]), max(limitations[i][1], limitations[i + 1][1]))
            limitations.pop(i + 1)
            remove_overlaps(limitations)
            break
    return limitations

from collections import defaultdict

positions = open('input').read().split('\n')
sensors = []
beacons = []
limit = 4000000
result = 0
distances = []
locations = defaultdict(set)

for position in positions:
    position = position.split(' ')
    s_x, s_y = int(position[2].split(',')[0][2:]), int(position[3].split(':')[0][2:])
    b_x, b_y = int(position[8].split(',')[0][2:]), int(position[9][2:])
    sensors.append((s_x, s_y))
    beacons.append((b_x, b_y))

    distances.append(manhattan_distance((s_x, s_y), (b_x, b_y))) # this works as indexing follow through sensors, beacons and distances list

for x in range(limit):
    limitations = []
    for i,s in enumerate(sensors):
        dist = distances[i] - abs(s[1] - x)
        if dist <= 0: # distance failed...
            continue
        min_x = max(0, s[0] - dist)
        max_x = min(s[0] + dist, limit)
        limitations.append((min_x, max_x))
    limitations.sort()
    limitations = remove_overlaps(limitations)
    if len(limitations) == 2:
        result = (limitations[0][1] + 1) * 4000000 + x
        break

print(result)