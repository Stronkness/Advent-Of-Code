import re
from PIL import Image

def save_grid_as_image(grid, filename="grid_image.png"):
    # Normalize grid values to 0-255 for image representation
    max_value = max(max(row) for row in grid)
    normalized_grid = [[int((cell / max_value) * 255) if max_value > 0 else 0 for cell in row] for row in grid]

    # Create image from normalized grid
    img = Image.new("L", (len(grid[0]), len(grid)))  # "L" mode for grayscale
    img.putdata([pixel for row in normalized_grid for pixel in row])  # Flatten grid
    img.save(filename)

input = open("large.in").read().split("\n")
width = 101
length = 103

robots = []
for row in input:
    nums = re.findall("-?\d+", row)
    robots.append([int(x) for x in nums])

grid = [[0 for _ in range(width)] for _ in range(length)]
check_dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

seconds = 1
while True: # Cancel iteration when having some pictures
    temp_grid = [[0 for _ in range(width)] for _ in range(length)]
    for idx, robot in enumerate(robots):
        px, py, vx, vy = robot
        nx = (px + vx) % width
        ny = (py + vy) % length
        robots[idx] = [nx,ny,vx,vy]
        temp_grid[ny][nx] += 1

    grid = [row[:] for row in temp_grid]
    
    # Detect christmas tree, all 8 neighbours of a robot should have a robot, i.e potential filled tree
    for r in robots:
        px,py,_,_ = r
        filled_neighbours = True
        for dir in check_dirs:
            x,y = dir
            if 0 <= (px+x) < width and 0 <= (py+y) < length:
                if grid[py+y][px+x] > 0:
                    continue
                else:
                    filled_neighbours = False
                    break
        
        if filled_neighbours: # Save image hint from Reddit
            save_grid_as_image(grid, filename=f"potential_trees/{seconds}.png")
    
    seconds += 1
