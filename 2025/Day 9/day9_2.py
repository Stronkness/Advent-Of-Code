polygon = [tuple(map(int, cord.split(','))) for cord in open('test.in').read().split("\n")]

def is_inside_polygon(c1, c2, polygon):
    if c1[0] < c2[0]:
        xmin = c1[0]
        xmax = c2[0]
    else:
        xmin = c2[0]
        xmax = c1[0]

    if c1[1] < c2[1]:
        ymin = c1[1]
        ymax = c2[1]
    else:
        ymin = c2[1]
        ymax = c1[1]

    i = 0
    while i < len(polygon):

        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if y1 == y2:
            if y1 > ymin and y1 < ymax:
                left  = min(x1, x2)
                right = max(x1, x2)
                if (xmin >= left and xmin < right) or \
                   (xmax > left and xmax <= right):
                    return False
        elif x1 == x2:
            if x1 > xmin and x1 < xmax:
                bottom = min(y1, y2)
                top    = max(y1, y2)
                if (ymin >= bottom and ymin < top) or \
                   (ymax > bottom and ymax <= top):
                    return False

        i += 1

    return True

area = []
for i in range(len(polygon)):
    x1, y1 = polygon[i]
    for j in range(i+1, len(polygon)):
        x2, y2 = polygon[j]

        if is_inside_polygon((x1, y1), (x2, y2), polygon):
            n_x = abs(x1 - x2) + 1
            n_y = abs(y1 - y2) + 1
            area.append(n_x * n_y)

print(max(area))
