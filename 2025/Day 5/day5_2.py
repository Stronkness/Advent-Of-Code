input = open("test.in").read().split("\n\n")
ranges = sorted([tuple(map(int, r.split("-"))) for r in input[0].split("\n")])

fresh = 0
start, end = ranges[0]
for r1, r2 in ranges[1:]:
    if r1 > end + 1: # Starts after prev merge, add total and start on new range loc
        fresh += end - start + 1
        start, end = r1, r2
    else: # Overlapping ranges, merge
        end = max(end, r2)

# If a final merge happened we skip it in the for-loop, therefore calculate total
fresh += end - start + 1

print(fresh)
