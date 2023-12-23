input = open('input', 'r').read().split('\n\n')
seeds = [int(x) for x in input[0].replace('seeds: ', '').split(' ')]
maps = []  # [[destination_range_start, source_range_start, range_length], ...]
for i in range(1, 8):
    maps.append([[int(y) for y in x.split(' ')]
                for x in input[i].splitlines()[1::]])

r = 100000000  # Just a big number
for seed in seeds:
    for map in maps:
        for destination_range_start, source_range_start, range_length in map:
            interval = range(source_range_start,
                             source_range_start + range_length)
            if seed in interval:
                seed = destination_range_start + \
                    (seed - source_range_start)
                break
    r = min(r, seed)

print(r)
