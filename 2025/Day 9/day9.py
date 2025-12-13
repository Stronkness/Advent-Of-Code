coords = [tuple(map(int, cord.split(','))) for cord in open('test.in').read().split("\n")]

area = []
for i in range(len(coords)):
    x1, y1 = coords[i]
    for j in range(i+1, len(coords)):
        x2, y2 = coords[j]

        n_x = abs(x1 - x2) + 1
        n_y = abs(y1 - y2) + 1
        area.append(n_x * n_y)

print(max(area))
