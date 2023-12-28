import sys

# Increase recursion limit to avoid stack overflow
sys.setrecursionlimit(10000)

def get_neighbors(position, map_data, height, width):
    i,j = position
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    # Filter out walls ('#') for empty spots ('.')
    empty_neighbors = []
    for (i, j) in neighbors:
        if 0 <= i < height and 0 <= j < width and map_data[i][j] != '#':
            empty_neighbors.append((i, j))

    return empty_neighbors


def prepare_data():
    file = open('input', 'r').read().splitlines()
    return [[x for x in line] for line in file]


def DFS(current, destination, initial_distance, visited, map_data, contracted_graph):
    results = []

    if current == destination:
        results.append(initial_distance)

    for neighbor, distance in contracted_graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            # Recursively explore the neighbors and append the distances to the list
            results.extend(DFS(neighbor, destination, initial_distance + distance, visited, map_data, contracted_graph))
            visited.remove(neighbor)

    return results

"""
A contracted graph is a representation of a larger graph in which certain nodes and edges have been combined or contracted to form a simpler, 
condensed version of the original graph. This contraction process aims to reduce the complexity of the graph while preserving certain properties, 
such as connectivity or distances between nodes.

The idea behind a contracted graph is often used in graph algorithms and optimization problems. By simplifying the graph, 
algorithms can be more efficient while still providing solutions that are valid in the context of the original, larger graph.

The specific criteria for contraction depend on the problem at hand. This contraction is based on bifurcation points, which are 
locations in the grid with more than two neighbors. The algorithm contracts paths between bifurcation points, resulting in a simplified 
representation of the graph.

The benefits of using a contracted graph include faster algorithmic computations and reduced memory requirements. However, the challenge 
lies in designing a contraction strategy that preserves the relevant properties of the original graph for the specific problem being solved.
"""

# Sadly borrowed from a Reddit user
def build_contracted_graph(map_data, start_position, end_position, height, width):
    # Identify bifurcation points
    bifurcations = [start_position] + [(i, j) for i in range(height) for j in range(width) if len(get_neighbors((i, j), map_data, height, width)) > 2] + [end_position]

    # Build the contracted graph
    from collections import defaultdict
    contracted_graph = defaultdict(list)

    for bifurcation in bifurcations:
        for neighbor in get_neighbors(bifurcation, map_data, height, width):
            previous, current = bifurcation, neighbor
            distance = 1
            while current not in bifurcations:
                previous, current = current, [p for p in get_neighbors(current, map_data, height, width) if p != previous][0]
                distance += 1
            contracted_graph[bifurcation].append((current, distance))
    
    return contracted_graph


def main():
    map_data = prepare_data()

    # Dimensions of the map
    height, width = len(map_data), len(map_data[0])

    # Start and end positions
    start_position = (0, 1)
    end_position = (height - 1, width - 2)

    # Build the contracted graph
    contracted_graph = build_contracted_graph(map_data, start_position, end_position, height, width)

    # Find the maximum distance using DFS
    visited = set()
    visited.add(start_position)
    max_distance = max(DFS(start_position, end_position, 0, visited, map_data, contracted_graph))

    print(max_distance)

if __name__ == '__main__': 
    main()
