from typing import List

file = open("test").read().strip().split("\n\n")

seeds_str = file[0].replace("seeds: ", "").split(" ")
seeds = [int(x) for x in seeds_str]
ranges = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = start + seeds[i + 1]
    ranges.append((start, end))

# Map format: [[destination_range_start, source_range_start, range_length], ...]
# Reverse the map, as go from the end point seed towards the beginning is easier than going from start to end, lower time complexity
maps = []
for i in range(7, 0, -1):
    inner_list = []
    lines = file[i].splitlines()[1::]
    for line in lines:
        start, end, range_length = [int(x) for x in line.split(" ")]
        inner_list.append((end, start, range_length))
    maps.append(inner_list)


location = 0
while True:
    seed = location
    for map in maps:
        for destination_range_start, source_range_start, range_length in map:
            interval = range(source_range_start,
                             source_range_start + range_length)
            if seed in interval:
                seed = destination_range_start + (seed - source_range_start)
                break

    done = False
    for start, end in ranges:
        if end > seed and seed >= start:
            print(location)
            done = True
            break

    if done:
        break

    location += 1

    # Print progress due to brute force method
    if location % 500_000 == 0:
        print(location)
