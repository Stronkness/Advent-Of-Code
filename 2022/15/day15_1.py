def manhattan_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

from collections import defaultdict

positions = open('input').read().split('\n')
sensors = []
beacons = []
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

beacons_at_target = []
sensors_at_target = []
for i,sensor in enumerate(sensors):
    beacon = beacons[i]

    if beacons[1] == 2000000:
        beacons_at_target.append(beacon[0])
    if sensors[1] == 2000000:
        sensors_at_target.append(sensor)
    dist = distances[i] - abs(sensor[1] - 2000000)
    if dist >= 0:
        sensors_at_target.append((sensor[0] - dist, sensor[0] + dist))

spots = []
for a, b in sensors_at_target:
    spots.extend([x for x in range(a,b) if x not in spots])
res_spots = spots
[res_spots.append(x) for x in spots if x not in res_spots]

print(len(res_spots) - len(beacons_at_target)) # 5125700
# This solution is embarassing, it legits take several hours to compute...
