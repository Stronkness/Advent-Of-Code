"""
This solution highly depend on recursion, as we don't then have to keep track 
on which lightbeams are active or how many they are left, need to define a function
"""

import sys
# set recursion limit as we get maximum recursion depth exceeded error
sys.setrecursionlimit(10000)

map = open('input', 'r').read().splitlines()
map = [[x for x in row] for row in map]

directions = {  # directions and their x, y changes
    "N": (0, -1),
    "S": (0, 1),
    "E": (1, 0),
    "W": (-1, 0)
}

mirror_directions = {  # mirrors and the directions they can reflect to
    ".": {"N": ["N"], "S": ["S"], "E": ["E"], "W": ["W"]},
    "-": {"N": ["E", "W"], "S": ["E", "W"], "E": ["E"], "W": ["W"]},
    "|": {"N": ["N"], "S": ["S"], "E": ["N", "S"], "W": ["N", "S"]},
    "/": {"N": ["E"], "S": ["W"], "E": ["N"], "W": ["S"]},
    "\\": {"N": ["W"], "S": ["E"], "E": ["S"], "W": ["N"]}
}


def check_lightbeams(edge_x, edge_y, edge_direction):
    visited = set()  # set of visited coordinates

    def check_lightbeams_recursion(x, y, direction):
        if (x, y, direction) in visited:  # if we have already visited this coordinate
            return

        visited.add((x, y, direction))  # add this coordinate to visited

        current_mirror = map[y][x]  # get the current mirror
        # get the possible directions we can go to, mostly cares about the splitters
        possible_next_directions = mirror_directions[current_mirror][direction]

        for next_direction in possible_next_directions:
            dx, dy = directions[next_direction]
            next_x, next_y = x + dx, y + dy

            # if we are still in the map
            if 0 <= next_x < len(map[0]) and 0 <= next_y < len(map):
                # check the next coordinate
                check_lightbeams_recursion(next_x, next_y, next_direction)

    check_lightbeams_recursion(edge_x, edge_y, edge_direction)
    unique_positions = set((x, y) for x, y, _ in visited)
    energized_tiles = len(unique_positions)
    return energized_tiles


visited = set()  # set of visited coordinates
edges = []
for y in range(len(map)):  # left most column
    edges.append((0, y, "E"))
for y in range(len(map)):  # right most column
    edges.append((len(map[0]) - 1, y, "W"))
for x in range(len(map[0])):  # top most row
    edges.append((x, 0, "S"))
for x in range(len(map[0])):  # bottom most row
    edges.append((x, len(map) - 1, "N"))


e_tiles = []
for edge in edges:
    e_tiles.append(check_lightbeams(edge[0], edge[1], edge[2]))

print(max(e_tiles))
