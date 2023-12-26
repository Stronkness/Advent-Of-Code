
def move_tiles(direction, tiles, coordinates):
  if direction in ['R']: 
    return (coordinates[0] , coordinates[1] + tiles)
  
  elif direction in ['D']: 
    return (coordinates[0] + tiles, coordinates[1])
  
  elif direction in ['L']:
    return (coordinates[0], coordinates[1] - tiles)
  
  else: # Up
    return (coordinates[0] - tiles, coordinates[1])
  
"""
This calculation is based on the shoelace formula, which is a method for finding the area of a polygon when
the coordinates of its edges are known. In this case, the function computes the absolute difference between two sums 
of products, each corresponding to a different traversal of the edges. The result divided by 2 gives the area of the polygon 
formed by the edges. 
"""
def calc_cubic_meters_of_lava(edges):
    summation_1, summation_2 = 0,0
    for k in range(len(edges)-1):
        (x1,y1), (x2,y2) = edges[k], edges[k+1]
        summation_1, summation_2 = summation_1 + x1*y2, summation_2 + y1*x2
    area = abs(summation_1 - summation_2) / 2
    return area

dig_plan = open("input").read().splitlines()

coordinates = (0,0)
edges = []
total_tiles = 0
for instruction in dig_plan:
    parts = instruction.split()
    direction = parts[0]
    tiles = int(parts[1])

    total_tiles += tiles
    coordinates = move_tiles(direction,tiles,coordinates)
    edges.append(coordinates)

print(int(calc_cubic_meters_of_lava(edges) + (total_tiles / 2) + 1))