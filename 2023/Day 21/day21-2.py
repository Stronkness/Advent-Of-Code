from collections import defaultdict

"""
We're running our step counter until we hit a point where our count of steps mod the board size equals out target number of steps 
modulus the board size. This gives us one term for the polynomial that will give the solution. 
Do that until we have the 3 terms we need to work with a quadratic equation.

Using those 3 terms, we can then solve for the number of possible garden tiles.

Cyclical basis. Which means it's some sort of series, which means a quadratic equation. 

The key points in the cycle are step 65 (which is our goal modulo our map size. 
It's also the number of steps needed to move out of the initial garden). 
And then 65 + 131 (131 being the width or height of our input) and again at 65 + 131 + 131.
"""

def prepare_data():
	file = open("input","r").read().splitlines()
	matrix = [[x for x in row] for row in file]
	for i, row in enumerate(matrix):
		for j, c in enumerate(row):
			if c == 'S':
				row[j] = '.' # Treat it as a garden plot and save the S coordinates
				start = (j,i)
	return matrix, start


def calculate_garden_plots(matrix, start, total_steps, width, height):
    visited = defaultdict(set)
    visited[0].add(start) 
    step_counts = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for step in range(total_steps): 
        for coordinates in visited[step]: 
            x, y = coordinates
            for direction in directions:
                dx, dy = direction
                new_x, new_y = x + dx, y + dy

                # Check if the new position is valid
                if matrix[new_y % height][new_x % width] == '.': 
                    visited[step + 1].add((new_x, new_y))

        # Check if we've hit the end of the cycle
        if step % width == total_steps % width:
            step_counts.append(len(visited[step]))

        # Check if we have all the terms we need to calculate the formula
        if len(step_counts) == 3:
            break

    return step_counts


def calculate_formula(steps, step_counts): # Quadratic formula
    b0 = step_counts[0]
    b1 = step_counts[1] - step_counts[0]
    b2 = step_counts[2] - step_counts[1]

    step_term = b1 * steps
    quadratic_term = (steps - 1) * steps * (b2 - b1) // 2

    result = b0 + step_term + quadratic_term
    return result


def main():
    matrix, start = prepare_data()
    height, width = len(matrix), len(matrix[0])
    total_steps = 26501365
    
    step_counts = calculate_garden_plots(matrix, start, total_steps, width, height)

    result = calculate_formula(total_steps // width, step_counts)
    print(result - 617565692567199)


if __name__ == "__main__":
    main()