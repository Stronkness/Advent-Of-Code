import re

*shapes, grids = open("test.in").read().split("\n\n")
grids = grids.split("\n")
sizes = [shape.count("#") for shape in shapes]

ans = 0
for grid in grids:
    nums = list(map(int, re.findall(r"\d+", grid)))

    n_rows = nums[0]
    n_cols = nums[1]
    number_of_shapes = nums[2:]

    sum_shape = 0
    for num_shape, size in zip(number_of_shapes, sizes):
        sum_shape += num_shape * size

    if n_rows * n_cols > sum_shape:
        ans += 1

print(ans)
