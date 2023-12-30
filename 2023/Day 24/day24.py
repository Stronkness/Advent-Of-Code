UPPER_LIMIT = 400000000000000
LOWER_LIMIT = 200000000000000


def prepare_data():
    data = []
    with open('input', 'r') as file:
        for line in file:
            pos, speed = line.strip().split('@')
            pos = [int(pos) for pos in pos.split(',')]
            speed = [int(speed) for speed  in speed.split(',')]
            data.append((pos, speed))
    return data

def process_interception(data):
    lines = []
    for pos, speed in data:
        slope_y_per_x = speed[1] / speed[0]
        intercept_y_at_x0 = pos[1] - slope_y_per_x * pos[0]
        lines.append((slope_y_per_x, intercept_y_at_x0, speed[1], pos[1]))
    return lines

def do_lines_intersect(line1, line2):
    slope1, intercept1, speed1, pos1 = line1
    slope2, intercept2, speed2, pos2 = line2

    if slope1 == slope2:
        return False
    
    x_val = (intercept1 - intercept2) / (slope2 - slope1)
    y_val = x_val * slope1 + intercept1

    x_within_limits = LOWER_LIMIT <= x_val <= UPPER_LIMIT
    y_within_limits = LOWER_LIMIT <= y_val <= UPPER_LIMIT

    cond1 = (speed1 > 0 and y_val > pos1) or (speed1 < 0 and y_val < pos1)
    cond2 = (speed2 > 0 and y_val > pos2) or (speed2 < 0 and y_val < pos2)

    return x_within_limits and y_within_limits and cond1 and cond2

def main():
    data = prepare_data()
    lines = process_interception(data)
    intersection_count = 0
    for index, line1 in enumerate(lines):
        for line2 in lines[index+1:]:
            if do_lines_intersect(line1, line2):
                intersection_count += 1

    print("Number of intersections:", intersection_count)


if __name__ == "__main__":
    main()
