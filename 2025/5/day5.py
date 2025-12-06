input = open("test.in").read().split("\n\n")
ranges = [tuple(map(int, r.split("-"))) for r in input[0].split("\n")]
ingredients = list(map(int, input[1].split("\n")))

fresh = 0
for ingredient in ingredients:
    for start, end in ranges:
        if start <= ingredient <= end:
            fresh += 1
            break

print(fresh)