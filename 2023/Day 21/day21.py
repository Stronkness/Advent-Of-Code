def prepare_data():
	file = open("input","r").read().splitlines()
	matrix = [[x for x in row] for row in file]
	for i, row in enumerate(matrix):
		for j, c in enumerate(row):
			if c == 'S':
				row[j] = '.' # Treat it as a garden plot and save the S coordinates
				start = (j,i)
	return matrix, start

def calculate_garden_plots(matrix, start, steps):
	visited = set()
	visited.add(start)
	directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, left, down, right

	for _ in range(steps):
		current_visited = set()
		for coordinates in visited:
			x, y = coordinates

			# Check the neighbors (up, left, down, right) of the current coordinate
			for check_x, check_y in directions:
				new_x, new_y = x + check_x, y + check_y

				# Probably unnecessary, but just in case
				if 0 <= new_y < len(matrix) and 0 <= new_x < len(matrix[0]) and matrix[new_y][new_x] == '.':
					current_visited.add((new_x, new_y))

		visited = current_visited

	return len(visited)

def main():
	matrix, start = prepare_data()
	steps = 64
	print(calculate_garden_plots(matrix, start, steps))


if __name__ == "__main__":
	main()