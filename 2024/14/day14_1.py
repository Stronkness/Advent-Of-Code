import re, math

input = open("large.in").read().split("\n")
width = 101
length = 103

robots = []
for row in input:
    nums = re.findall("-?\d+", row)
    robots.append([int(x) for x in nums])

grid = [[0 for _ in range(width)] for _ in range(length)]

quadrants = [0,0,0,0]
for robot in robots:
    px, py, vx, vy = robot
    nx = (px + 100 * vx) % width
    ny = (py + 100 * vy) % length
    grid[ny][nx] += 1

    if nx < width // 2 and ny < length // 2: # upper left quadrant
        quadrants[0] += 1
    if nx > width // 2 and ny < length // 2: # upper left quadrant
        quadrants[1] += 1
    if nx < width // 2 and ny > length // 2: # lower left quadrant
        quadrants[2] += 1
    if nx > width // 2 and ny > length // 2: # lower right quadrant
        quadrants[3] += 1

safety_factor = math.prod(quadrants)
print(safety_factor)
