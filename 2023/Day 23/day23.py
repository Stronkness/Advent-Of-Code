import sys

# Increase recursion limit to avoid stack overflow
sys.setrecursionlimit(10000)

def prepare_data():
    file = open('input', 'r').read().splitlines()
    return [[x for x in line] for line in file]

# Define the possible movements based on the current direction
def get_neighbors(position, map_data):
    i, j = position
    if map_data[i][j] == '>':
        return [(i, j + 1)]
    elif map_data[i][j] == '<':
        return [(i, j - 1)]
    elif map_data[i][j] == '^':
        return [(i - 1, j)]
    elif map_data[i][j] == 'v':
        return [(i + 1, j)]
    else:
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        # Filter out walls ('#') for empty spots ('.')
        empty_neighbors = []
        for (i, j) in neighbors:
            if 0 <= i < height and 0 <= j < width and map_data[i][j] != '#':
                empty_neighbors.append((i, j))
        return empty_neighbors

# Depth First Search algorithm to find the maximum distance between two points
def DFS(current, destination, initial_distance, visited, map_data):
    distances = []
    if current == destination:
        distances.append(initial_distance)
    else:
        for neighbor in get_neighbors(current, map_data):
            if neighbor not in visited:
                visited.add(neighbor)
                # Recursively explore the neighbors and append the distances to the list
                distances.extend(DFS(neighbor, destination, initial_distance + 1, visited, map_data))
                visited.remove(neighbor)

    return distances

start_point = (0, 1)
map_data = prepare_data()
height, width = len(map_data), len(map_data[0])
end_point = (height - 1, width - 2)
visited = set()
visited.add(start_point)

max_distance = max(DFS(start_point, end_point, 0, visited, map_data))
print(max_distance)
