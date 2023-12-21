grids = open('input', 'r').read().strip().split("\n\n")
grids = [g.splitlines() for g in grids]

total = 0
smudges = 0  # Change for the different parts, 0 for Part 1 and 1 for Part 2
for grid in grids:
    rows = 0
    for r in range(1, len(grid)):
        above = list(reversed(grid[:r]))
        below = grid[r:]

        differences_count = 0
        for row_above, row_below in zip(above, below):
            for a, b in zip(row_above, row_below):
                if a != b:  # Check if the elements are different, indicating reflection
                    differences_count += 1

        if differences_count == smudges:  # Success for finding a reflection
            rows = r
    total += rows * 100

    # Transpose the grid to check the columns as we switch rows with the columns
    grid = list(zip(*grid))

    cols = 0
    for c in range(1, len(grid)):
        above = list(reversed(grid[:c]))
        below = grid[c:]

        differences_count = 0
        for row_above, row_below in zip(above, below):
            for a, b in zip(row_above, row_below):
                if a != b:  # Check if the elements are different, indicating reflection
                    differences_count += 1

        if differences_count == smudges:  # Success for finding a reflection
            cols = c

    total += cols

print(total)
