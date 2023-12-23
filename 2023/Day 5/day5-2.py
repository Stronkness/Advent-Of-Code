file = open("input").read().strip().split("\n\n")

seeds_str = file[0].replace("seeds: ", "").split(" ")
seeds = [int(x) for x in seeds_str]
ranges = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = start + seeds[i + 1]
    ranges.append((start, end))

# Map format: [[destination_range_start, source_range_start, range_length], ...]
maps = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
][::-1]  # Reverse the map, as go from the end point seed towards the beginning is easier than going from start to end, lower time complexity

location = 0
while True:
    seed = location
    for m in maps:
        for destination_range_start, source_range_start, range_length in m:
            interval = range(source_range_start,
                             source_range_start + range_length)
            if seed in interval:
                seed = destination_range_start + (seed - source_range_start)
                break

    for start, end in ranges:
        if end > seed and seed >= start:
            print(location)
            break

    location += 1

    # Print progress due to brute force method
    if location % 500_000 == 0:
        print(location)
